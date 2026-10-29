"""Keep the mod's low-memory code alive across the game's IOP reboots.

Right after the game reboots the IOP (with cdrom0:\\MODULES\\DNAS300.IMG) the EE memory
0x84000-0x100000 gets zeroed, and that is where the mod's own code lives (0xE0100-0x100000).
PCSX2 hides this because it re-applies the pnach every frame; a baked ISO on a PS2/PS3 runs
into the zeroed code and crashes. So the game's two `jal` calls that lead to a reboot are
hooked:

* the hook copies the mod area to a stash (at boot a fixed spot in memory the game hasn't
  started using yet; later, the highest 132 KB run of zero pages it can find) and, the first
  time, adds a vblank interrupt handler, then makes the original call;
* each vblank the handler checks a few words of the mod area. If they all read zero, it copies
  the stash back (after checking the stash still holds the mod) and flushes the caches.
* A second after the last restore (or 20 s after the hook if no wipe came) the handler
  zeroes the stash again, unless the game has written to it, and goes idle until the next hook.

The handler and its state live at 0x80180-0x81000, which the wipe leaves alone; the hooks'
code lives just below the mod at 0xDF000, inside the area that gets wiped and restored.
"""

import struct

LO, HI = 0xDF000, 0x100000          # the area kept alive: keeper code + mod code
STATE = 0x80180                     # 0 installed, 4 active, 8 idle frames, C restores (total),
                                    # 10 restores this round, 14 stash address, 18 call
HANDLER = 0x80200
BOOT_STASH = 0x1F40000              # zero at boot, first used by the game ~2 s after the wipe
SCAN_LO, SCAN_HI = 0x780000, 0x1FFB000
SETTLE = 60                         # frames without a wipe after a restore before going idle
GIVE_UP = 1200                      # frames without any wipe before going idle
VBLANK_START = 2                    # INTC cause; the game itself only uses 0 and 3

# per game version: [(address of a `jal call` that leads to an IOP reboot, call)]
SITES = {
    0xFB2F4502: [(0x2BCDF0, 0x2BCCA8), (0x10079C, 0x575408)],     # USA
    0xE0F96C7D: [(0x2BCDF0, 0x2BCCA8), (0x10079C, 0x5754C8)],     # Europe
}

ZERO, V0, V1, A0, A1, A2 = 0, 2, 3, 4, 5, 6
T0, T1, T2, T3, T4, T5, T6 = 8, 9, 10, 11, 12, 13, 14
RA = 31
SYSCALL = 0x0C


def _i(op, rs, rt, imm):
    return (op << 26) | (rs << 21) | (rt << 16) | (imm & 0xFFFF)


def jal(addr):
    return (0x03 << 26) | ((addr >> 2) & 0x3FFFFFF)


class _Asm:
    """Just enough MIPS for the keeper. Every loop is kept longer than six instructions with
    empty delay slots (the PS2 CPU can run very short loops wrongly)."""

    def __init__(self, base):
        self.base, self.w, self.labels, self.fix = base, [], {}, []

    def label(self, name):
        self.labels[name] = len(self.w)

    def addr(self, name):
        return self.base + self.labels[name] * 4

    def li(self, rt, value):
        self.w += [_i(0x0F, 0, rt, value >> 16), _i(0x0D, rt, rt, value)]       # lui, ori

    def lw(self, rt, off, base):
        self.w += [_i(0x23, base, rt, off), 0]

    def sw(self, rt, off, base):
        self.w.append(_i(0x2B, base, rt, off))

    def addiu(self, rt, rs, imm):
        self.w.append(_i(0x09, rs, rt, imm))

    def sltu(self, rd, rs, rt):
        self.w.append((rs << 21) | (rt << 16) | (rd << 11) | 0x2B)

    def jr(self, rs):
        self.w += [(rs << 21) | 0x08, 0]

    def _br(self, op, rs, rt, name):
        self.fix.append((len(self.w), op, rs, rt, name))
        self.w += [0, 0]

    def beq(self, rs, rt, name):
        self._br(0x04, rs, rt, name)

    def bne(self, rs, rt, name):
        self._br(0x05, rs, rt, name)

    def b(self, name):
        self._br(0x04, ZERO, ZERO, name)

    def syscall(self, number, a0=None):
        if a0 is not None:
            self.addiu(A0, ZERO, a0)
        self.addiu(V1, ZERO, number)
        self.w.append(SYSCALL)

    def flush(self, interrupt=False):
        n = -0x64 if interrupt else 0x64              # (i)FlushCache: write back data, drop instructions
        self.syscall(n, 0)
        self.syscall(n, 2)

    def copy(self, src_reg, dst_reg, n, tag):
        """copy n bytes from (src_reg) to (dst_reg); uses t0-t3"""
        self.w += [_i(0x09, src_reg, T0, 0), _i(0x09, dst_reg, T1, 0)]
        self.li(T2, n)
        self.w.append((T1 << 21) | (T2 << 16) | (T2 << 11) | 0x21)               # addu t2,t1,t2
        self.label(tag)
        self.w += [_i(0x23, T0, T3, 0), _i(0x09, T0, T0, 4), _i(0x2B, T1, T3, 0), _i(0x09, T1, T1, 4), 0, 0]
        self.bne(T1, T2, tag)

    def zero(self, dst_reg, n, tag):
        """zero n bytes at (dst_reg); uses t1, t2"""
        self.w.append(_i(0x09, dst_reg, T1, 0))
        self.li(T2, n)
        self.w.append((T1 << 21) | (T2 << 16) | (T2 << 11) | 0x21)
        self.label(tag)
        self.w += [_i(0x2B, T1, ZERO, 0), _i(0x09, T1, T1, 4), 0, 0, 0, 0]
        self.bne(T1, T2, tag)

    def check_stash(self, sentinels, bad):
        """branch to `bad` unless the stash (address in state+0x14) still holds the mod"""
        self.li(T4, STATE)
        self.lw(T5, 0x14, T4)
        for a, v in sentinels:
            self.li(T1, a - LO)
            self.w.append((T5 << 21) | (T1 << 16) | (T0 << 11) | 0x21)          # addu t0,t5,t1
            self.lw(T3, 0, T0)
            self.li(T1, v)
            self.bne(T3, T1, bad)

    def done(self):
        for at, op, rs, rt, name in self.fix:
            self.w[at] = _i(op, rs, rt, self.labels[name] - at - 1)
        return struct.pack("<%dI" % len(self.w), *self.w)


def _handler(sentinels):
    n = HI - LO
    h = _Asm(HANDLER)
    h.label("handler")
    h.li(T4, STATE)
    h.lw(T0, 4, T4)
    h.beq(T0, ZERO, "ret")                                  # idle
    for a, _v in sentinels:
        h.li(T0, a)
        h.lw(T3, 0, T0)
        h.bne(T3, ZERO, "intact")
    h.b("restore")                                          # all of them read zero: wiped
    # not wiped this frame: count, and go idle once settled
    h.label("intact")
    h.lw(T0, 8, T4)
    h.addiu(T0, T0, 1)
    h.sw(T0, 8, T4)
    h.lw(T1, 0x10, T4)
    h.beq(T1, ZERO, "no_restore_yet")
    h.addiu(T1, ZERO, SETTLE)
    h.b("limit")
    h.label("no_restore_yet")
    h.addiu(T1, ZERO, GIVE_UP)
    h.label("limit")
    h.sltu(T2, T0, T1)
    h.bne(T2, ZERO, "ret")
    h.check_stash(sentinels, "deactivate")                  # the game took the stash over: leave it
    h.zero(T5, n, "clear")                                  # it was zero before the hook
    h.label("deactivate")
    h.li(T4, STATE)
    h.sw(ZERO, 4, T4)
    h.b("ret")
    h.label("restore")
    h.check_stash(sentinels, "deactivate")
    h.li(T6, LO)
    h.copy(T5, T6, n, "put_back")
    h.flush(interrupt=True)
    h.li(T4, STATE)
    for off in (0xC, 0x10):
        h.lw(T0, off, T4)
        h.addiu(T0, T0, 1)
        h.sw(T0, off, T4)
    h.sw(ZERO, 8, T4)
    h.label("ret")
    h.addiu(V0, ZERO, 1)
    h.jr(RA)
    return h


def _hook(sites):
    n = HI - LO
    k = _Asm(LO)
    for i, (_site, call) in enumerate(sites):
        k.label("entry%d" % i)
        k.li(T4, STATE)
        k.li(T0, call)
        k.sw(T0, 0x18, T4)
        k.b("common")
    k.label("common")
    k.lw(T0, 4, T4)
    k.bne(T0, ZERO, "go")                                   # already watching
    k.lw(T0, 0, T4)
    k.li(T5, BOOT_STASH)
    k.beq(T0, ZERO, "stash")                                # first time (boot): fixed stash
    # later: find the highest run of n bytes of zero pages, top down
    k.li(T5, SCAN_HI)
    k.addiu(T6, ZERO, 0)                                    # zero pages in a row
    k.label("page")
    k.li(T0, SCAN_LO)
    k.sltu(T2, T0, T5)
    k.beq(T2, ZERO, "go")                                   # nothing free: go on unprotected
    k.addiu(T5, T5, -0x1000)
    k.w += [_i(0x09, T5, T1, 0), _i(0x09, T5, T2, 0x1000)]  # t1 = page, t2 = page end
    k.label("word")
    k.lw(T3, 0, T1)
    k.bne(T3, ZERO, "used")
    k.addiu(T1, T1, 4)
    k.w += [0, 0]
    k.bne(T1, T2, "word")
    k.addiu(T6, T6, 1)
    k.addiu(T0, ZERO, n // 0x1000 + (1 if n % 0x1000 else 0))
    k.bne(T6, T0, "page")
    k.b("stash")
    k.label("used")
    k.addiu(T6, ZERO, 0)
    k.b("page")
    k.label("stash")
    k.li(T4, STATE)
    k.sw(T5, 0x14, T4)
    k.li(T6, LO)
    k.copy(T6, T5, n, "save")
    k.li(T4, STATE)
    k.addiu(T0, ZERO, 1)
    k.sw(T0, 4, T4)
    k.sw(ZERO, 8, T4)
    k.sw(ZERO, 0x10, T4)
    k.lw(T1, 0, T4)
    k.sw(T0, 0, T4)
    k.bne(T1, ZERO, "flush")
    k.addiu(A0, ZERO, VBLANK_START)                         # AddIntcHandler(vblank start, handler, 0)
    k.li(A1, HANDLER)
    k.addiu(A2, ZERO, 0)
    k.syscall(0x10)
    k.syscall(0x14, VBLANK_START)                           # EnableIntc(vblank start)
    k.label("flush")
    k.flush()
    k.label("go")
    k.li(T4, STATE)
    k.lw(T0, 0x18, T4)
    k.jr(T0)                                                # the original call (ra = site + 8)
    return k


def keeper_writes(crc, writes, elf_word):
    """Extra (address, bytes) writes that keep the mod area alive, or [] when not needed.
    `writes` are the pnach's writes; elf_word(addr) reads a word of the original ELF."""
    if not any(0x84000 <= a < HI for a, _d in writes):
        return []
    sites = SITES.get(crc)
    if sites is None:
        raise ValueError("no IOP-reboot hooks known for this game version")
    for site, call in sites:
        if elf_word(site) != jal(call):
            raise ValueError("unexpected code at %08X" % site)
    image = {}
    for a, d in writes:
        for i, b in enumerate(d):
            image[a + i] = b
    for a in image:
        if LO <= a < 0xE0100 or STATE <= a < 0x81000:
            raise ValueError("the pnach writes to memory the keeper needs (%08X)" % a)
        if a >> 2 in ((s >> 2) for s, _c in sites):
            raise ValueError("the pnach changes a call the keeper hooks (%08X)" % a)
    # sentinels: function prologues (addiu sp,sp,-n: code the mod never changes) spread over the area
    word = lambda a: int.from_bytes(bytes(image.get(a + i, 0) for i in range(4)), "little")
    cand = sorted(a for a in image if a % 4 == 0 and 0xE0100 <= a < HI and word(a) >> 16 == 0x27BD
                  and word(a) & 0x8000)
    if len(cand) < 6:
        raise ValueError("can't find enough of the mod's code to watch")
    sentinels = [(cand[len(cand) * i // 6], word(cand[len(cand) * i // 6])) for i in range(6)]
    k, h = _hook(sites), _handler(sentinels)
    code, handler = k.done(), h.done()
    assert LO + len(code) <= 0xE0100 and HANDLER + len(handler) <= 0x81000, (len(code), len(handler))
    out = [(LO, code), (STATE, bytes(HANDLER - STATE)), (HANDLER, handler)]
    # The mod keeps its variables in parts of its area the pnach doesn't write (they start at zero
    # under PCSX2). On a console that memory still holds whatever the loader left there, so the
    # boot copier zeroes those parts too.
    gap = None
    for a in range(LO + len(code), HI + 1):
        if a < HI and a not in image:
            gap = a if gap is None else gap
        elif gap is not None:
            out.append((gap, bytes(a - gap)))
            gap = None
    for i, (site, _call) in enumerate(sites):
        out.append((site, struct.pack("<I", jal(k.addr("entry%d" % i)))))
    return out

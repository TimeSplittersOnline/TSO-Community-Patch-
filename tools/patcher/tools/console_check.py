"""Look through a pnach's code for things PCSX2 lets slide but a real PS2/PS3 doesn't.

Usage: python3 tools/console_check.py <game ELF> <pnach> [--all]

Checks the mod's own code (everything reachable from the pnach's hooks into 0x000DF000-0x00100000)
and every game instruction the pnach changes, plus their neighbours:

  errors (crash or misbehave on a console):
    null-load      a load/store in the delay slot of the branch that checks its pointer for zero,
                   so it runs on the NULL path too (PCSX2 logs a TLB miss and carries on)
    bad-opcode     an instruction the EE doesn't have (reserved instruction exception)
    branch-in-slot a branch or jump in another branch's delay slot
    bad-target     a jump/branch to memory the pnach doesn't write and that isn't game code
    misaligned     a load/store at a fixed address that isn't aligned for its size
    bad-address    a load/store at a fixed address with nothing behind it
  warnings (worth a look):
    use-then-check a pointer used and then checked for zero a few instructions later
    short-loop     a loop of 6 instructions or fewer (with its delay slot) whose only branch is the one at
                   the end and whose delay slot isn't a nop: the R5900 can run it only once or twice
    code-write     a store into code (needs FlushCache on a console; PCSX2 doesn't cache)
    forced-write   a store into a word the pnach writes: PCSX2 puts the pnach's value back every
                   frame, a console (and the ISO/xdelta build) keeps whatever the code stored

Exit status 1 if there are errors. --all also lists every warning instead of the first 20 per kind.
"""
import collections
import os
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pmd import ps2patch as p

MOD_LO, MOD_HI = 0x000DF000, 0x00100000
s16 = lambda x: x - 0x10000 if x & 0x8000 else x

SPECIAL_OK = {0, 2, 3, 4, 6, 7, 8, 9, 0xA, 0xB, 0xC, 0xD, 0xF, 0x10, 0x11, 0x12, 0x13, 0x14, 0x16, 0x17,
              0x18, 0x19, 0x1A, 0x1B, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A,
              0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33, 0x34, 0x36, 0x38, 0x3A, 0x3B, 0x3C,
              0x3E, 0x3F}
REGIMM_OK = {0, 1, 2, 3, 8, 9, 0xA, 0xB, 0xC, 0xE, 0x10, 0x11, 0x12, 0x13, 0x18, 0x19}
PRIMARY_OK = set(range(0x00, 0x13)) | set(range(0x14, 0x1D)) | {0x1E, 0x1F} | set(range(0x20, 0x30)) \
    | {0x31, 0x33, 0x36, 0x37, 0x39, 0x3E, 0x3F}
COP1_S_OK = {0, 1, 2, 3, 4, 5, 6, 7, 0x16, 0x18, 0x19, 0x1A, 0x1C, 0x1D, 0x1E, 0x1F, 0x24, 0x28, 0x29,
             0x30, 0x32, 0x34, 0x36}
# primary opcode -> (size, is_store) for loads/stores
MEM = {0x1A: (8, 0), 0x1B: (8, 0), 0x1E: (16, 0), 0x1F: (16, 1), 0x20: (1, 0), 0x21: (2, 0), 0x22: (4, 0),
       0x23: (4, 0), 0x24: (1, 0), 0x25: (2, 0), 0x26: (4, 0), 0x27: (4, 0), 0x28: (1, 1), 0x29: (2, 1),
       0x2A: (4, 1), 0x2B: (4, 1), 0x2C: (8, 1), 0x2D: (8, 1), 0x2E: (4, 1), 0x31: (4, 0), 0x36: (16, 0),
       0x37: (8, 0), 0x39: (4, 1), 0x3E: (16, 1), 0x3F: (8, 1)}
UNALIGNED_OK = {0x1A, 0x1B, 0x22, 0x26, 0x2A, 0x2C, 0x2D, 0x2E}       # ldl/ldr/lwl/lwr/swl/sdl/sdr/swr
REGIONS = [(0x00080000, 0x02000000), (0x20000000, 0x22000000), (0x30000000, 0x32000000),
           (0x70000000, 0x70004000), (0x10000000, 0x10010000), (0x11000000, 0x11010000),
           (0x12000000, 0x12002000), (0x80000000, 0x82000000), (0xA0000000, 0xA2000000)]


def branch(w):
    """(kind, tested reg or None, likely, target fn) for branches/jumps, else None.
    kind: 'b' conditional, 'j' j/jal, 'jr' register jump."""
    op, rs, rt = w >> 26, (w >> 21) & 31, (w >> 16) & 31
    rel = lambda pc: pc + 4 + s16(w & 0xFFFF) * 4
    if op in (2, 3):
        return "j", None, False, lambda pc: (pc & 0xF0000000) | ((w & 0x3FFFFFF) << 2), op == 3
    if op == 0 and w & 0x3F in (8, 9):
        return "jr", None, False, None, w & 0x3F == 9
    if op in (4, 5, 0x14, 0x15):
        reg = rs if rt == 0 else rt if rs == 0 else None
        return "b", (op & 1, reg), op >= 0x14, rel, False
    if op in (6, 7, 0x16, 0x17):
        return "b", (op & 1 | 2 << (op & 1), rs), op >= 0x14, rel, False          # 2 blez, 5 bgtz
    if op == 1 and rt in (0, 1, 2, 3, 0x10, 0x11, 0x12, 0x13):
        return "b", (8 | rt & 1, rs), bool(rt & 2), rel, rt >= 0x10                # 8 bltz, 9 bgez
    if op in (0x10, 0x11, 0x12) and rs == 8:
        return "b", None, bool(rt & 2), rel, False
    return None


def zero_path_runs_slot(cond, likely):
    """Does the delay slot run when the tested register is zero?"""
    if not likely:
        return True
    kind = cond[0]
    return kind in (0, 2, 9)        # beql, blezl, bgezl run their slot when the register is 0


def valid(w):
    op = w >> 26
    if op not in PRIMARY_OK:
        return False
    if op == 0:
        return w & 0x3F in SPECIAL_OK
    if op == 1:
        return (w >> 16) & 31 in REGIMM_OK
    if op == 0x11:
        fmt = (w >> 21) & 31
        if fmt in (0, 2, 4, 6, 8):
            return True
        if fmt == 0x10:
            return w & 0x3F in COP1_S_OK
        if fmt == 0x14:
            return w & 0x3F == 0x20
        return False                 # no doubles (or anything else) on the EE's FPU
    return True


def dest(w):
    """General register an instruction writes, if any (approximate, enough for constant tracking)."""
    op = w >> 26
    if op == 0:
        f = w & 0x3F
        if f in (8, 0xC, 0xD, 0xF, 0x11, 0x13, 0x18, 0x19, 0x1A, 0x1B, 0x29) or 0x30 <= f <= 0x36:
            return None if f not in (0x18, 0x19) else (w >> 11) & 31
        return (w >> 11) & 31
    if op == 3:
        return 31
    if op == 1:
        return 31 if (w >> 16) & 31 >= 0x10 else None
    if op in (2, 4, 5, 6, 7, 0x14, 0x15, 0x16, 0x17, 0x2F, 0x33) or op in MEM and MEM[op][1] or op in (0x31, 0x36):
        return None
    if op in (0x10, 0x11, 0x12):
        rs = (w >> 21) & 31
        return (w >> 16) & 31 if rs in (0, 1, 2) else None
    if op == 0x1C:
        return (w >> 11) & 31
    return (w >> 16) & 31


class Check:
    def __init__(self, elf, pnach):
        self.elf = elf
        self.pn = pnach
        self.img = {}
        for a, d in pnach.writes:
            for i, b in enumerate(d):
                self.img[a + i] = b
        self.written = {a & ~3 for a in self.img}
        _o, _e, ph = p._phdrs(elf)
        self.loads = [x for x in ph if x[0] == p.PT_LOAD]
        self.text = self._exec_ranges()
        self.found = collections.defaultdict(list)

    def _exec_ranges(self):
        e = self.elf
        shoff, = struct.unpack_from("<I", e, 32)
        shentsize, shnum, shstrndx = struct.unpack_from("<HHH", e, 46)
        out = []
        strtab = struct.unpack_from("<10I", e, shoff + shstrndx * shentsize)[4]
        for i in range(shnum):
            name, _t, flags, addr, _off, size = struct.unpack_from("<6I", e, shoff + i * shentsize)
            nm = e[strtab + name:e.index(b"\0", strtab + name)]
            if flags & 4 and size and nm != b".vutext":
                out.append((addr, addr + size))
        if not out:
            out = [(x[2], x[2] + x[4]) for x in self.loads if x[6] & 1]
        return out

    def word(self, a):
        if a in self.written:
            return int.from_bytes(bytes(self.img.get(a + i, self._orig_byte(a + i)) for i in range(4)), "little")
        return self._orig(a)

    def _orig_byte(self, a):
        w = self._orig(a & ~3)
        return 0 if w is None else (w >> 8 * (a & 3)) & 0xFF

    def _orig(self, a):
        for x in self.loads:
            if x[2] <= a < x[2] + x[4]:
                return struct.unpack_from("<I", self.elf, x[1] + a - x[2])[0]
            if x[2] <= a < x[2] + x[5]:
                return 0
        return None

    def is_text(self, a):
        return any(lo <= a < hi for lo, hi in self.text)

    def is_code(self, a):
        return self.is_text(a) or MOD_LO <= a < MOD_HI and a in self.written

    def add(self, kind, addr, text):
        self.found[kind].append((addr, text))

    # --- which mod words are code --------------------------------------------------------
    def mod_code(self):
        entries = set()
        for a in self.written:
            w = self.word(a)
            b = branch(w)
            if b and b[3] and (self.is_text(a) or MOD_LO <= a < MOD_HI):
                t = b[3](a)
                if MOD_LO <= t < MOD_HI and not MOD_LO <= a < MOD_HI:
                    entries.add(t)
        # function pointers: written data words, and lui/addiu pairs, that point at a function start
        def looks_like_start(t):
            return t in self.written and t % 4 == 0 and self.word(t) >> 16 == 0x27BD      # addiu sp,sp,-n
        for a in self.written:
            v = self.word(a)
            if MOD_LO <= v < MOD_HI and looks_like_start(v):
                entries.add(v)
        code, todo = set(), list(entries)
        while todo:
            a = todo.pop()
            while MOD_LO <= a < MOD_HI and a not in code:
                code.add(a)
                w = self.word(a)
                b = branch(w)
                if b:
                    slot = a + 4
                    code.add(slot)
                    if b[3]:
                        t = b[3](a)
                        if MOD_LO <= t < MOD_HI:
                            todo.append(t)
                    if b[0] == "jr" and not b[4] or b[0] == "j" and not b[4] or \
                            b[0] == "b" and w >> 16 == 0x1000:                          # b / j / jr: no fall-through
                        break
                    a = slot + 4
                    continue
                if a not in self.written:
                    break
                a += 4
        # lui/addiu pointers found inside the code we know about
        more = set()
        for a in sorted(code):
            w = self.word(a)
            if w >> 26 == 0xF:
                hi, r = (w & 0xFFFF) << 16, (w >> 16) & 31
                for k in range(1, 6):
                    n = self.word(a + 4 * k)
                    if n is None:
                        break
                    if n >> 26 in (9, 0xD) and (n >> 21) & 31 == r:
                        v = (hi + s16(n & 0xFFFF)) & 0xFFFFFFFF if n >> 26 == 9 else hi | n & 0xFFFF
                        if MOD_LO <= v < MOD_HI and v not in code and looks_like_start(v):
                            more.add(v)
                        break
        if more:
            todo = list(more)
            while todo:
                a = todo.pop()
                while MOD_LO <= a < MOD_HI and a not in code and a in self.written:
                    code.add(a)
                    w = self.word(a)
                    b = branch(w)
                    if b:
                        code.add(a + 4)
                        if b[3] and MOD_LO <= b[3](a) < MOD_HI:
                            todo.append(b[3](a))
                        if b[0] in ("j", "jr") and not b[4] or b[0] == "b" and w >> 16 == 0x1000:
                            break
                        a += 8
                        continue
                    a += 4
        return code

    # --- checks on a run of instructions ------------------------------------------------------
    def scan(self, addrs, report_if):
        """Check each instruction in addrs (sorted, code). Only findings for which report_if(addresses
        involved) is true are kept."""
        targets = set()
        for a in addrs:
            b = branch(self.word(a))
            if b and b[3]:
                targets.add(b[3](a))
        known = {}
        prev = None
        aset = set(addrs)
        for a in addrs:
            w = self.word(a)
            if a in targets or prev is None or a != prev + 4:
                known = {}
            prev = a
            known[0] = 0
            if not valid(w):
                if report_if((a,)):
                    self.add("bad-opcode", a, "%08X is not an EE instruction" % w)
                continue
            b = branch(w)
            op, rs, rt = w >> 26, (w >> 21) & 31, (w >> 16) & 31
            if b:
                slot = self.word(a + 4)
                sb = branch(slot) if slot is not None else None
                if sb and report_if((a, a + 4)):
                    self.add("branch-in-slot", a + 4, "%08X sits in the delay slot of %08X at %08X" % (slot, w, a))
                if b[3]:
                    t = b[3](a)
                    if not self.is_code(t) and not (b[0] == "j" and t == 0) and report_if((a,)):
                        what = "unwritten mod memory (zero)" if MOD_LO <= t < MOD_HI else "no code there"
                        self.add("bad-target", a, "%08X goes to %08X: %s" % (w, t, what))
                    # R5900 erratum: <= 6 instructions with the delay slot, one conditional branch at
                    # the end and no other branch or jump in the loop, delay slot not a nop
                    if b[0] == "b" and w >> 16 != 0x1000 and t <= a and (a - t) // 4 + 2 <= 6 and slot != 0 \
                            and not any(branch(self.word(x) or 0) for x in range(t, a, 4)) and report_if((a, a + 4)):
                        self.add("short-loop", a, "loop %08X-%08X has %08X in its delay slot" % (t, a + 4, slot))
                if b[0] == "b" and b[1] and b[1][1] and slot is not None and slot >> 26 in MEM:
                    if (slot >> 21) & 31 == b[1][1] and zero_path_runs_slot(b[1], b[2]) and report_if((a, a + 4)):
                        self.add("null-load", a, "%08X checks r%d for zero but %08X in its delay slot uses it anyway"
                                 % (w, b[1][1], slot))
            if op in MEM:
                size, store = MEM[op]
                base, off = rs, s16(w & 0xFFFF)
                if base in known and base != 0 or base == 0:
                    ea = (known.get(base, 0) + off) & 0xFFFFFFFF
                    if report_if((a,)):
                        if op not in UNALIGNED_OK and size <= 8 and ea % size:
                            self.add("misaligned", a, "%08X: %d-byte access at %08X" % (w, size, ea))
                        if not any(lo <= ea < hi for lo, hi in REGIONS):
                            self.add("bad-address", a, "%08X accesses %08X" % (w, ea))
                        if store:
                            phys = ea & 0x1FFFFFFF
                            if self.is_code(phys):
                                self.add("code-write", a, "%08X stores into code at %08X" % (w, ea))
                            elif any(phys + i in self.img for i in range(size)) and True:
                                self.add("forced-write", a, "%08X stores into %08X, which the pnach also writes"
                                         % (w, ea))
                # pointer used, then checked for zero shortly after
                if base not in (0, 29, 28) and (store or rt != base) and not (b or (prev and branch(self.word(a - 4) or 0))):
                    for k in range(1, 7):
                        n = self.word(a + 4 * k)
                        if n is None or dest(n) == base:
                            break
                        nb = branch(n)
                        if nb:
                            if nb[0] == "b" and nb[1] and nb[1][1] == base and report_if((a, a + 4 * k)):
                                self.add("use-then-check", a, "%08X uses r%d, then %08X at %08X checks it for zero"
                                         % (w, base, n, a + 4 * k))
                            break
            d = dest(w)
            if op == 0xF:
                known[rt] = (w & 0xFFFF) << 16
            elif op == 9 and rs in known:
                known[rt] = (known[rs] + s16(w & 0xFFFF)) & 0xFFFFFFFF
            elif op == 0xD and rs in known:
                known[rt] = known[rs] | w & 0xFFFF
            elif op == 0 and w & 0x3F in (0x21, 0x2D, 0x25) and rt == 0 and rs in known:
                known[(w >> 11) & 31] = known[rs]
            elif d is not None:
                known.pop(d, None)
            if b and b[0] != "b" or b and w >> 16 == 0x1000:
                known = {}

    def run(self):
        code = self.mod_code()
        self.code = code
        mod_words = {a for a in self.written if MOD_LO <= a < MOD_HI}
        self.scan(sorted(code), lambda addrs: True)
        # game code the pnach changes, with 16 words either side
        near = set()
        for a in self.written:
            if self.is_text(a):
                for k in range(-16, 17):
                    if self.is_text(a + 4 * k):
                        near.add(a + 4 * k)
        touched = self.written
        self.scan(sorted(near), lambda addrs: any(x in touched for x in addrs))
        # stores anywhere in the game's code to words the pnach writes (data, not code)
        data_words = {a for a in self.written if not self.is_code(a) or MOD_LO <= a < MOD_HI and a not in code}
        self.data_words = data_words
        for lo, hi in self.text:
            self._scan_forced(lo, hi, data_words)
        self.unreached = sorted(mod_words - code)
        return self.found

    def _scan_forced(self, lo, hi, data_words):
        """lui/addiu-addressed stores in the game's own code that land on a word the pnach writes."""
        lui = {}
        for a in range(lo, hi, 4):
            w = self.word(a)
            if w is None:
                continue
            op, rs, rt = w >> 26, (w >> 21) & 31, (w >> 16) & 31
            if branch(w):
                lui = {}
                continue
            if op == 0xF:
                lui[rt] = ((w & 0xFFFF) << 16, a)
                continue
            if op in MEM and MEM[op][1] and rs in lui and a - lui[rs][1] <= 64:
                ea = (lui[rs][0] + s16(w & 0xFFFF)) & 0x1FFFFFFF
                size = MEM[op][0]
                if any((ea + i) & ~3 in data_words for i in range(size)) and a not in self.code:
                    self.add("forced-write", a, "%08X stores into %08X, which the pnach also writes" % (w, ea))
            d = dest(w)
            if d is not None and op != 9:
                lui.pop(d, None)


ERRORS = ["null-load", "bad-opcode", "branch-in-slot", "bad-target", "misaligned", "bad-address"]
WARNINGS = ["use-then-check", "short-loop", "code-write", "forced-write"]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    every = "--all" in sys.argv
    if len(args) != 2:
        sys.exit(__doc__)
    elf = open(args[0], "rb").read()
    c = Check(elf, p.Pnach(args[1]))
    found = c.run()
    mod = [a for a in c.written if MOD_LO <= a < MOD_HI]
    game = [a for a in c.written if a >= MOD_HI]
    print("%s: %d words in the mod area (%d traced as code), %d game words changed"
          % (os.path.basename(args[1]), len(mod), len(c.code), len(game)))
    errors = 0
    for kind in ERRORS + WARNINGS:
        items = sorted(set(found.get(kind, [])))
        if kind in ERRORS:
            errors += len(items)
        label = "ERROR" if kind in ERRORS else "warning"
        print("%-8s %-15s %d" % (label, kind, len(items)))
        for a, t in items if every or kind in ERRORS else items[:20]:
            print("           %08X  %s" % (a, t))
        if not every and kind not in ERRORS and len(items) > 20:
            print("           ... %d more (--all)" % (len(items) - 20))
    # mod words that aren't traced code, as ranges: data, or code reached some way the check can't see
    rng, start, last = [], None, None
    for a in c.unreached:
        if start is None or a != last + 4:
            if start is not None:
                rng.append((start, last + 4))
            start = a
        last = a
    if start is not None:
        rng.append((start, last + 4))
    print("not traced as code (data, or code only reached through a register): %d words in %d ranges"
          % (len(c.unreached), len(rng)))
    if every:
        for lo, hi in rng:
            print("           %08X-%08X" % (lo, hi))
    print("errors: %d" % errors)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()

"""Run the keeper (pmd/ps2keeper.py) of a patched ELF through boot, the IOP-reboot wipes and vblanks.

Usage: python3 tests/ps2_keeper_sim.py <dir with SLUS_211.48 and SLES_529.93> <NTSC pnach> <PAL pnach>
Boots the patched ELF (ps2_boot_sim), clears the game's bss like crt0 does, then for each hooked
call: runs the hook, zeroes 0x84000-0x100000 like the reboot does, runs the vblank handler and checks
the mod area is back, the stash is cleared again once things settle and the handler goes idle."""
import os, struct, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pmd import ps2patch as p, ps2keeper as k
import ps2_boot_sim as sim

STOP = 0xDEAD0000
N = k.HI - k.LO


def run(mem, pc, stop, regs=None):
    """Interpret from pc until pc == stop; returns (registers, syscalls as (v1, a0, a1, a2))."""
    r = list(regs) if regs else [0] * 32
    r[31] = r[31] or STOP
    delay, calls = None, []
    for _ in range(10 ** 9):
        if pc == stop and delay is None:
            return r, calls
        w, = struct.unpack_from("<I", mem, pc)
        op, rs, rt, imm = w >> 26, (w >> 21) & 31, (w >> 16) & 31, w & 0xFFFF
        t = None
        if w == 0:
            pass
        elif w == 0x0C:
            calls.append((r[3], r[4], r[5], r[6]))
        elif op == 0 and w & 0x3F == 0x08:
            t = r[rs]
        elif op == 0 and w & 0x3F == 0x21:
            r[(w >> 11) & 31] = (r[rs] + r[rt]) & 0xFFFFFFFF
        elif op == 0 and w & 0x3F == 0x2D:
            r[(w >> 11) & 31] = (r[rs] + r[rt]) & 0xFFFFFFFF
        elif op == 0 and w & 0x3F == 0x2B:
            r[(w >> 11) & 31] = int(r[rs] < r[rt])
        elif op == 3:
            r[31], t = pc + 8, (pc & 0xF0000000) | ((w & 0x3FFFFFF) << 2)
        elif op == 0x0F:
            r[rt] = imm << 16
        elif op == 0x0D:
            r[rt] = r[rs] | imm
        elif op == 0x09:
            r[rt] = (r[rs] + sim.s16(imm)) & 0xFFFFFFFF
        elif op == 0x23:
            r[rt], = struct.unpack_from("<I", mem, (r[rs] + sim.s16(imm)) & 0xFFFFFFFF)
        elif op == 0x2B:
            struct.pack_into("<I", mem, (r[rs] + sim.s16(imm)) & 0xFFFFFFFF, r[rt])
        elif op in (0x04, 0x05):
            if (r[rs] == r[rt]) == (op == 0x04):
                t = pc + 4 + sim.s16(imm) * 4
        else:
            raise AssertionError("keeper uses an instruction the test can't run: %08X at %08X" % (w, pc))
        r[0] = 0
        pc, delay = (delay, None) if delay is not None else (pc + 4, None)
        if t is not None:
            delay = t
    raise AssertionError("never got to %08X" % stop)


def state(mem):
    return struct.unpack_from("<7I", mem, k.STATE)


def check(orig, pnach):
    pn = p.Pnach(pnach)
    new, rep = p.patch_elf(orig, pn)
    assert rep["keeper"]
    crc = p.elf_crc(orig)
    (site1, call1), (site2, call2) = k.SITES[crc]
    word = lambda m, a: struct.unpack_from("<I", m, a)[0]
    o = lambda a: struct.unpack_from("<I", orig, a - 0x100000 + 0x1000)[0]
    mem, _sc = sim.boot(new, struct.unpack_from("<I", orig, 24)[0])
    mod = bytes(mem[k.LO:k.HI])
    want = {}
    for a, d in pn.writes:                                        # later lines win, as in PCSX2
        for i, b in enumerate(d):
            want[a + i] = b
    assert all(mem[a] == b for a, b in want.items())
    _t, _off, va, _pa, fs, ms, _f, _a = p._phdrs(orig)[2][0]
    mem[0x774B00:va + ms] = bytes(va + ms - 0x774B00)        # crt0 clears the bss
    assert word(mem, site1) != o(site1) and word(mem, site2) != o(site2)

    def vblank():
        r, c = run(mem, k.HANDLER, STOP, [0] * 32)
        assert r[2] == 1, r[2]
        return c

    def wipe():
        mem[0x84000:0x100000] = bytes(0x100000 - 0x84000)

    # boot: the first hooked call stashes at the fixed spot and adds the handler
    r, c = run(mem, site1, call1)
    assert r[31] == site1 + 8
    assert [x[0] for x in c] == [0x10, 0x14, 0x64, 0x64], c
    assert c[0][1:] == (k.VBLANK_START, k.HANDLER, 0) and c[1][1] == k.VBLANK_START
    assert mem[k.BOOT_STASH:k.BOOT_STASH + N] == mod
    assert state(mem)[:2] == (1, 1)
    assert vblank() == []
    # a mod word that legitimately becomes zero must not trigger a restore
    first = next(a for a in range(0xE0100, k.HI, 4) if word(mem, a))
    struct.pack_into("<I", mem, first, 0)
    vblank()
    assert word(mem, first) == 0
    struct.pack_into("<I", mem, first, word(memoryview(mod), first - k.LO))
    wipe()
    c = vblank()
    assert [(x[0], x[1]) for x in c] == [(0xFFFFFF9C, 0), (0xFFFFFF9C, 2)], c
    assert mem[k.LO:k.HI] == mod and state(mem)[3] == 1
    for _ in range(k.SETTLE - 1):
        vblank()
    assert state(mem)[1] == 1 and mem[k.BOOT_STASH:k.BOOT_STASH + N] == mod
    vblank()
    assert state(mem)[1] == 0 and mem[k.BOOT_STASH:k.BOOT_STASH + N] == bytes(N), "stash not cleared"
    wipe()
    assert vblank() == []                                         # idle: leaves memory alone
    mem[k.LO:k.HI] = mod

    # in game: the other hooked call (network shutdown) stashes in the highest free run
    junk = 0x1F00000                                              # the game is using the top
    mem[junk:va + ms] = b"\x11" * (va + ms - junk)
    r, c = run(mem, site2, call2)
    assert r[31] == site2 + 8 and [x[0] for x in c] == [0x64, 0x64], c
    stash = state(mem)[5]
    assert stash + N <= junk and stash % 0x1000 == 0 and stash > junk - N - 0x1000, hex(stash)
    assert mem[stash:stash + N] == mod
    wipe()
    vblank()
    assert mem[k.LO:k.HI] == mod
    for _ in range(k.SETTLE):
        vblank()
    assert state(mem)[1] == 0 and mem[stash:stash + N] == bytes(N)

    # the game writes into the stash before a wipe: no restore from it, and it isn't cleared
    run(mem, site2, call2)
    stash = state(mem)[5]
    mem[stash:stash + N] = b"\x22" * N
    wipe()
    vblank()
    assert mem[k.LO:k.HI] == bytes(N) and state(mem)[1] == 0 and mem[stash:stash + N] == b"\x22" * N
    mem[k.LO:k.HI] = mod

    # no wipe at all: gives up after GIVE_UP frames and clears the stash
    mem[stash:stash + N] = bytes(N)
    run(mem, site2, call2)
    stash = state(mem)[5]
    for _ in range(k.GIVE_UP - 1):
        vblank()
    assert state(mem)[1] == 1
    vblank()
    assert state(mem)[1] == 0 and mem[stash:stash + N] == bytes(N)
    # the hooks stay in place for the next reboot
    assert word(mem, site1) != o(site1) and word(mem, site2) != o(site2)
    return rep


if __name__ == "__main__":
    d, ntsc, pal = sys.argv[1:4]
    for name, pn in (("SLUS_211.48", ntsc), ("SLES_529.93", pal)):
        check(open(os.path.join(d, name), "rb").read(), pn)
        print("%s: keeper survives the boot wipe, an in-game wipe, a reused stash and no wipe" % name)
    print("ok")

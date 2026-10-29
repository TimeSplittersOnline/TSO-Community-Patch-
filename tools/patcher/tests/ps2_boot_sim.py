"""Load a patched PS2 ELF the way the console does and run its boot copier up to the game's entry.

Usage: python3 tests/ps2_boot_sim.py <dir with SLUS_211.48 and SLES_529.93> <NTSC pnach> <PAL pnach>
Checks that memory at the game's entry holds the original ELF image plus every pnach write, that the
mod code area is fully rewritten (stale RAM there is overwritten) and that both caches get flushed."""
import os, struct, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pmd import ps2patch as p

JUNK = 0xA5


def s16(x):
    return x - 0x10000 if x & 0x8000 else x


def boot(elf, stop):
    """Memory (32 MB) after loading every PT_LOAD and running from e_entry until pc == stop."""
    mem = bytearray([JUNK]) * 0x2000000
    for t, off, va, _pa, fs, ms, _f, _a in p._phdrs(elf)[2]:
        if t == p.PT_LOAD:
            mem[va:va + ms] = bytes(ms)
            mem[va:va + fs] = elf[off:off + fs]
    pc, = struct.unpack_from("<I", elf, 24)
    r = [0] * 32
    delay = None
    syscalls = []
    for _ in range(10 ** 8):
        if pc == stop and delay is None:
            return mem, syscalls
        w, = struct.unpack_from("<I", mem, pc)
        op, rs, rt, imm = w >> 26, (w >> 21) & 31, (w >> 16) & 31, w & 0xFFFF
        target = None
        if w == 0:
            pass
        elif w == 0x0C:
            syscalls.append((r[3], r[4]))
        elif op == 0 and w & 0x3F == 8:
            target = r[rs]
        elif op == 0x0F:
            r[rt] = imm << 16
        elif op == 0x0D:
            r[rt] = r[rs] | imm
        elif op == 0x09:
            r[rt] = (r[rs] + s16(imm)) & 0xFFFFFFFF
        elif op == 0x23:
            r[rt], = struct.unpack_from("<I", mem, (r[rs] + s16(imm)) & 0xFFFFFFFF)
        elif op == 0x2B:
            struct.pack_into("<I", mem, (r[rs] + s16(imm)) & 0xFFFFFFFF, r[rt])
        elif op in (0x04, 0x05):
            if (r[rs] == r[rt]) == (op == 0x04):
                target = pc + 4 + s16(imm) * 4
        else:
            raise AssertionError("copier uses an instruction the test can't run: %08X at %08X" % (w, pc))
        r[0] = 0
        pc, delay = (delay, None) if delay is not None else (pc + 4, None)
        if target is not None:
            delay = target
    raise AssertionError("copier never reached the game's entry")


def check(orig, pnach):
    pn = p.Pnach(pnach)
    new, rep = p.patch_elf(orig, pn)
    phdrs = p._phdrs(new)[2]
    assert sum(1 for h in phdrs if h[0] == p.PT_LOAD) == 1, "patched ELF must keep a single segment"
    entry, = struct.unpack_from("<I", orig, 24)
    mem, sc = boot(new, entry)
    assert sc == [(0x64, 0), (0x64, 2)], sc
    _t, off, va, _pa, fs, ms, _f, _a = p._phdrs(orig)[2][0]
    exp = bytearray([JUNK]) * 0x2000000
    exp[va:va + ms] = bytes(ms)
    exp[va:va + fs] = orig[off:off + fs]
    for lo, hi in rep["segments"]:
        exp[lo:hi] = bytes(hi - lo)
    for a, d in pn.writes:
        exp[a:a + len(d)] = d
    copier, = struct.unpack_from("<I", new, 24)
    assert mem[:copier] == exp[:copier], "memory at the game's entry differs from the pnach result"
    assert new[off + fs:len(orig)] == orig[off + fs:], "file data after the segment (overlays) moved"
    return rep, copier


if __name__ == "__main__":
    d, ntsc, pal = sys.argv[1:4]
    for name, pn in (("SLUS_211.48", ntsc), ("SLES_529.93", pal)):
        rep, copier = check(open(os.path.join(d, name), "rb").read(), pn)
        print("%s: copier at %08X; memory at entry = original + all pnach writes (%d), code areas %s"
              % (name, copier, rep["in_elf"] + rep["new_segment"], ", ".join("%08X-%08X" % r for r in rep["segments"])))
    print("ok")

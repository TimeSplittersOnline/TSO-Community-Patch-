"""Write a copy of a TSFP pnach with the code fixed that PCSX2 runs fine but a real PS2/PS3 doesn't.

Usage: python3 tools/consolefix.py <game ELF> <in.pnach> <out.pnach>

The copy is the original file with lines added at the end (later lines win), using free memory from
0x000F4000. Run tools/console_check.py on the result: it should report no errors and no short loops.

  null loads   `beq reg,zero,skip` with a load through reg in its delay slot loads from a NULL pointer
               (PCSX2 only logs a TLB miss; a console takes an exception). Each pair becomes `j T; nop`;
               T does the check first and the load only when reg isn't NULL.
  short loops  the R5900 can run a loop of 6 instructions or fewer, whose only branch is the one at the
               end and whose delay slot isn't a nop, only once or twice. Each such loop is moved to T
               with nops added so it's 7 instructions long (same instructions, same order), and its
               first two words become `j T; nop`.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import console_check as cc
from console_check import branch, s16

FREE_LO, FREE_HI = 0x000F4000, 0x000F8E00
J = lambda t: (2 << 26) | ((t >> 2) & 0x3FFFFFF)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    elf_path, src, dst = sys.argv[1:4]
    c = cc.Check(open(elf_path, "rb").read(), cc.p.Pnach(src))
    found = c.run()
    code = sorted(c.code)
    W = c.word
    targets = set()
    for a in c.written:
        b = branch(W(a))
        if b and b[3]:
            targets.add(b[3](a))
    patches = []                        # (address, word)
    T = FREE_LO
    used = []

    def place(words):
        nonlocal T
        at = T
        for i, x in enumerate(words):
            patches.append((T + 4 * i, x))
        T += 4 * len(words)
        T = (T + 31) & ~31
        used.append((at, T))
        return at

    # null loads
    nulls = sorted(a for a, _t in set(found.get("null-load", [])))
    for s in nulls:
        w, d = W(s), W(s + 4)
        assert s + 4 not in targets, "a branch lands in the delay slot at %08X" % (s + 4)
        assert w >> 26 == 4, "%08X: only beq/beqz null loads are handled" % s
        rs = (w >> 21) & 31 or (w >> 16) & 31
        skip = s + 4 + s16(w & 0xFFFF) * 4
        at = place([(5 << 26) | (rs << 21) | 3, 0, J(skip), 0, d, J(s + 8), 0, 0])
        patches += [(s, J(at)), (s + 4, 0)]

    # short loops
    loops = sorted(a for a, _t in set(found.get("short-loop", [])))
    for a in loops:
        w = W(a)
        t = a + 4 + s16(w & 0xFFFF) * 4
        body = [W(x) for x in range(t, a, 4)]
        slot = W(a + 4)
        assert not any(t < x <= a + 4 for x in targets), "something jumps into the loop at %08X" % t
        assert not branch(W(t - 4) or 0), "the loop at %08X starts in a delay slot" % t
        pad = max(0, 7 - (len(body) + 2))
        new_t = T
        n = len(body) + pad                                  # the branch's index in the moved loop
        moved_branch = (w & 0xFFFF0000) | ((-(n + 1)) & 0xFFFF)
        at = place(body + [0] * pad + [moved_branch, slot, J(a + 8), 0])
        assert at == new_t
        patches += [(t, J(at)), (t + 4, 0)]

    hit = [x for x, _w in patches if not FREE_LO <= x < FREE_HI]
    assert len(hit) == len(set(hit)), "two fixes touch the same word"
    for x, _w in patches:
        if FREE_LO <= x < FREE_HI:
            assert x not in c.written, "%08X is in use by this pnach" % x
    assert T <= FREE_HI, "out of free memory"
    refs = [a for a in c.written if FREE_LO <= (W(a) & 0x1FFFFFFF) < T and not FREE_LO <= a < T
            and W(a) >> 26 not in (2, 3)]
    assert not refs, "the pnach refers to the free area at %s" % ", ".join("%08X" % r for r in refs)

    lines = ["", "// console fixes (tools/consolefix.py). PCSX2 runs the code above fine, a PS2/PS3 doesn't:"]
    if nulls:
        lines.append("// - %d null checks had their load in the branch delay slot, so it ran for a NULL pointer too; "
                     "the check now comes first" % len(nulls))
    if loops:
        lines.append("// - %d loops were short enough to hit the R5900 short-loop bug (a console can run them only "
                     "once or twice); they now run 7+ instructions from 0x%08X" % (len(loops), FREE_LO))
    lines += ["patch=1,EE,%08X,word,%08X" % (x, v) for x, v in patches]
    text = open(src, "r", encoding="utf-8", errors="surrogateescape").read()
    nl = "\r\n" if "\r\n" in text else "\n"
    open(dst, "w", encoding="utf-8", errors="surrogateescape", newline="").write(
        text.rstrip("\r\n") + nl + nl.join(lines) + nl)
    print("%s: %d null loads (%s), %d short loops (%s), code at %08X-%08X"
          % (dst, len(nulls), " ".join("%08X" % s for s in nulls), len(loops),
             " ".join("%08X" % s for s in loops), FREE_LO, T))


if __name__ == "__main__":
    main()

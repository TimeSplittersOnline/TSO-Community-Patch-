"""Write a copy of a TSFP pnach with its delay-slot null loads fixed.

Usage: python3 tools/nullfix.py <in.pnach> <out.pnach>
A `beq reg,zero,skip` with `lw x,off(reg)` in its delay slot loads from address off when reg is
NULL. PCSX2 only logs a TLB miss; a PS2/PS3 takes an exception. Each such pair becomes `j T; nop`,
and T (from 0x000F4000) does the check first and the load only when reg isn't NULL."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pmd import ps2patch as p

s16 = lambda x: x - 0x10000 if x & 0x8000 else x
src, dst = sys.argv[1:3]
pn = p.Pnach(src)
img = {}
for a, d in pn.writes:
    for i, b in enumerate(d):
        img[a + i] = b
W = lambda a: int.from_bytes(bytes(img.get(a + i, 0) for i in range(4)), "little")
words = sorted(set(a & ~3 for a in img))
sites = []
for a in words:
    w = W(a)
    op, rs, rt = w >> 26, (w >> 21) & 31, (w >> 16) & 31
    if op == 4 and rs and rt == 0 and (a + 4) in img:
        d = W(a + 4)
        if d >> 26 in (0x20, 0x21, 0x23, 0x24, 0x25, 0x27, 0x37) and (d >> 21) & 31 == rs:
            sites.append(a)
targets = set()
for a in words:
    w = W(a)
    op = w >> 26
    if op in (1, 4, 5, 6, 7, 0x14, 0x15, 0x16, 0x17):
        targets.add(a + 4 + s16(w & 0xFFFF) * 4)
    if op in (2, 3):
        targets.add((w & 0x3FFFFFF) << 2)
assert not any(s + 4 in targets for s in sites), "a branch lands on a delay slot"
T0 = T = 0x000F4000
lines = ["", "// fix: a null check had its load in the branch delay slot, so the load ran even for a NULL "
         "pointer (address 0xC / 0xC8). PCSX2 only logs a TLB miss; a PS2/PS3 crashes. The check now "
         "comes first (code at 0x000F4000)."]
for s in sites:
    w, d = W(s), W(s + 4)
    rs = (w >> 21) & 31
    skip = s + 4 + s16(w & 0xFFFF) * 4
    tramp = [(5 << 26) | (rs << 21) | 3, 0, (2 << 26) | (skip >> 2), 0, d, (2 << 26) | ((s + 8) >> 2), 0, 0]
    lines.append("patch=1,EE,%08X,word,%08X" % (s, (2 << 26) | (T >> 2)))
    lines.append("patch=1,EE,%08X,word,%08X" % (s + 4, 0))
    for i, x in enumerate(tramp):
        lines.append("patch=1,EE,%08X,word,%08X" % (T + 4 * i, x))
    T += 32
assert not any(a in img for a in range(T0, T)), "0x000F4000 is in use by this pnach"
text = open(src, "r", encoding="utf-8", errors="replace").read()
nl = "\r\n" if "\r\n" in text else "\n"
open(dst, "w", encoding="utf-8", newline="").write(text.rstrip("\r\n") + nl + nl.join(lines) + nl)
print("%s: %d sites fixed: %s" % (dst, len(sites), ", ".join("%08X" % s for s in sites)))

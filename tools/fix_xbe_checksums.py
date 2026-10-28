"""Recompute every section's SHA-1 in an XBE's section headers (after editing bytes by hand), in place.
Usage: python fix_xbe_checksums.py "TSO Community Patch.xbe""""
import sys,struct,hashlib
p=sys.argv[1]; d=bytearray(open(p,'rb').read())
base=struct.unpack_from('<I',d,0x104)[0]; n,sh=struct.unpack_from('<II',d,0x11c); sh-=base; fixed=0
for i in range(n):
    o=sh+i*56; fl,va,vs,ra,rs=struct.unpack_from('<5I',d,o)
    h=hashlib.sha1(struct.pack('<I',rs)+bytes(d[ra:ra+rs])).digest()
    if d[o+36:o+56]!=h: d[o+36:o+56]=h; fixed+=1
open(p,'wb').write(d); print('%d section%s, %d checksum%s updated'%(n,'' if n==1 else 's',fixed,'' if fixed==1 else 's'))

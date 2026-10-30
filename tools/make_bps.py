"""Make a BPS patch (original file -> modded file) and apply one. Usage:
  python make_bps.py make <original.xbe> <modded.xbe> <out.bps>
  python make_bps.py apply <original.xbe> <patch.bps> <out.xbe>
BPS: Floating IPS, beat and most patchers apply it. Only bytes the player's own file lacks are stored (the title
update's changes and TSO's); everything else is copied from that file.
Make the release patch from the USA retail disc default.xbe (no title update; 6270976 bytes, CRC32 05BF2120,
MD5 4aeb1a1fded674575759b681f2125966) -> TSO Community Patch.bps. Not originals/xbox_default_supplied.xbe:
that one has extra private changes, so no player's file matches it."""
import sys,zlib,struct
def vint(n):
    b=bytearray()
    while True:
        x=n&0x7f; n>>=7
        if n==0: b.append(0x80|x); return bytes(b)
        b.append(x); n-=1
def rint(d,i):
    n,s=0,1
    while True:
        x=d[i]; i+=1; n+=(x&0x7f)*s
        if x&0x80: return n,i
        s<<=7; n+=s
def make(src,tgt):   # src = original file, tgt = modded file
    # Copies from the same offset where the files line up, from anywhere else in the original where code has moved
    # (found by 12-byte keys at every 4th original offset), the rest as new bytes.
    K=12; idx={}
    for p in range(0,len(src)-K+1,4): idx.setdefault(src[p:p+K],p)
    out=bytearray(b'BPS1'+vint(len(src))+vint(len(tgt))+vint(0))
    lit=bytearray(); srel=0; n=len(tgt); i=0
    def flush():
        if lit: out.extend(vint(((len(lit)-1)<<2)|1)+lit); lit.clear()
    while i<n:
        s=i if i<len(src) and tgt[i:i+K]==src[i:i+K] else idx.get(tgt[i:i+K])
        if s is None: lit.append(tgt[i]); i+=1; continue
        j,e=i,s
        while j<n and e<len(src) and tgt[j]==src[e]: j+=1; e+=1
        b=0                                             # take back new bytes that match just before the copy
        while b<len(lit) and s-b>0 and src[s-b-1]==tgt[i-b-1]: b+=1
        if b: del lit[len(lit)-b:]
        s-=b; l=j-(i-b); flush()
        if s==i-b: out+=vint(((l-1)<<2)|0)              # copy from the same offset of the original
        else:                                           # copy from elsewhere in the original
            o=s-srel; out+=vint(((l-1)<<2)|2)+vint((abs(o)<<1)|(o<0)); srel=s+l
        i=j
    flush()
    out+=struct.pack('<II',zlib.crc32(src),zlib.crc32(tgt))
    out+=struct.pack('<I',zlib.crc32(out)); return bytes(out)
def apply(src,p):
    assert p[:4]==b'BPS1','not a BPS patch'
    assert zlib.crc32(p[:-4])==struct.unpack('<I',p[-4:])[0],'patch damaged'
    sc,tc=struct.unpack('<II',p[-12:-4])
    assert zlib.crc32(src)==sc,'this is not the XBE the patch was made for (wrong version?)'
    i=4; ss,i=rint(p,i); ts,i=rint(p,i); ms,i=rint(p,i); i+=ms
    out=bytearray(); so=to=0; end=len(p)-12
    while i<end:
        d,i=rint(p,i); a=d&3; l=(d>>2)+1
        if a==0: out+=src[len(out):len(out)+l]
        elif a==1: out+=p[i:i+l]; i+=l
        else:
            o,i=rint(p,i); o=(-1 if o&1 else 1)*(o>>1)
            if a==2: so+=o; out+=src[so:so+l]; so+=l
            else:
                to+=o
                for _ in range(l): out.append(out[to]); to+=1
    assert len(out)==ts and zlib.crc32(out)==tc,'result check failed'
    return bytes(out)
RETAIL_USA_CRC=0x05BF2120   # USA retail disc default.xbe, the file players have
if __name__=='__main__':
    if sys.argv[1]=='make':
        src=open(sys.argv[2],'rb').read()
        if sys.argv[4].endswith('TSO Community Patch.bps') and zlib.crc32(src)!=RETAIL_USA_CRC:
            sys.exit('the release patch must be made from the USA retail disc default.xbe (CRC32 05BF2120); '
                     'this file is CRC32 %08X, so no player could apply the patch' % zlib.crc32(src))
        open(sys.argv[4],'wb').write(make(src,open(sys.argv[3],'rb').read()))
    else: open(sys.argv[4],'wb').write(apply(open(sys.argv[2],'rb').read(),open(sys.argv[3],'rb').read()))

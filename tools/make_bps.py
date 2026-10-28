"""Make a BPS patch (original file -> modded file) and apply one. Usage:
  python make_bps.py make <original.xbe> <modded.xbe> <out.bps>
  python make_bps.py apply <original.xbe> <patch.bps> <out.xbe>
BPS: Floating IPS, beat and most patchers apply it. Only the changed bytes are stored; unchanged ones are copied from the
player's own file, so the patch holds none of the game's code."""
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
    out=bytearray(b'BPS1'+vint(len(src))+vint(len(tgt))+vint(0))
    i=0; n=len(tgt)
    while i<n:
        if i<len(src) and src[i]==tgt[i]:
            j=i
            while j<n and j<len(src) and src[j]==tgt[j]: j+=1
            out+=vint(((j-i-1)<<2)|0)                  # copy from the original
        else:
            j=i
            while j<n and not (j<len(src) and src[j]==tgt[j] and j+8<=min(n,len(src)) and src[j:j+8]==tgt[j:j+8]): j+=1
            out+=vint(((j-i-1)<<2)|1)+tgt[i:j]          # new bytes
        i=j
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
if __name__=='__main__':
    if sys.argv[1]=='make': open(sys.argv[4],'wb').write(make(open(sys.argv[2],'rb').read(),open(sys.argv[3],'rb').read()))
    else: open(sys.argv[4],'wb').write(apply(open(sys.argv[2],'rb').read(),open(sys.argv[3],'rb').read()))

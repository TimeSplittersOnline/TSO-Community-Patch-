"""Make an xdelta (VCDIFF, RFC 3284) patch from an original file to the modded one, and check it. Usage:
  python make_xdelta.py <original> <modded> <out.xdelta>
xdelta3, xdelta UI and Delta Patcher apply it. Only bytes the original lacks are stored; everything else is copied from
the player's own file. Code that moved is found too (12-byte keys at every 4th original offset), so an XBE patch stays
about 1.8 MB. After writing, the patch is decoded again and must rebuild the modded file exactly.
Release XBE patches are made from the stock disc default.xbe of each region: USA MD5 4aeb1a1fded674575759b681f2125966,
Europe MD5 a048c094f604559e870fe14f33f784b3. An xdelta does not check its base, so a wrong file gives a broken result."""
import io,sys
K=12; WINDOW=4<<20
def vint(n):
    b=[n&0x7f]; n>>=7
    while n: b.append(0x80|(n&0x7f)); n>>=7
    return bytes(reversed(b))
def rint(f):
    n=0
    while True:
        x=f.read(1)[0]; n=(n<<7)|(x&0x7f)
        if not x&0x80: return n
def window(src,idx,tgt,t0):    # one window: the whole original as source, ADD (code 1) and COPY mode 0 (code 19) only
    data,inst,addr,lit=bytearray(),bytearray(),bytearray(),bytearray()
    def flush():
        if lit: inst.append(1); inst.extend(vint(len(lit))); data.extend(lit); lit.clear()
    i=0; n=len(tgt)
    while i<n:
        g=t0+i
        s=g if g<len(src) and tgt[i:i+K]==src[g:g+K] else idx.get(tgt[i:i+K])
        if s is None: lit.append(tgt[i]); i+=1; continue
        j,e=i,s
        while j<n and e<len(src) and tgt[j]==src[e]: j+=1; e+=1
        b=0                                             # take back new bytes that match just before the copy
        while b<len(lit) and s-b>0 and src[s-b-1]==tgt[i-b-1]: b+=1
        if b: del lit[len(lit)-b:]
        s-=b; l=j-(i-b); flush()
        inst.append(19); inst.extend(vint(l)); addr.extend(vint(s)); i=j
    flush()
    body=vint(n)+b'\x00'+vint(len(data))+vint(len(inst))+vint(len(addr))+bytes(data)+bytes(inst)+bytes(addr)
    return b'\x01'+vint(len(src))+vint(0)+vint(len(body))+body
def make(src,tgt):
    idx={}
    for p in range(0,len(src)-K+1,4): idx.setdefault(src[p:p+K],p)
    out=bytearray(b'\xD6\xC3\xC4\x00\x00')
    for t0 in range(0,len(tgt),WINDOW): out+=window(src,idx,tgt[t0:t0+WINDOW],t0)
    return bytes(out)
def apply(src,p):              # decodes what make() writes
    f=io.BytesIO(p); assert f.read(5)==b'\xD6\xC3\xC4\x00\x00','not a patch from make_xdelta'
    out=bytearray()
    while f.tell()<len(p):
        assert f.read(1)==b'\x01'
        sl,sp=rint(f),rint(f); s=src[sp:sp+sl]
        body=io.BytesIO(f.read(rint(f))); tl=rint(body); body.read(1)
        ld,li,la=rint(body),rint(body),rint(body)
        d,ins,a=io.BytesIO(body.read(ld)),io.BytesIO(body.read(li)),io.BytesIO(body.read(la))
        w=bytearray()
        while ins.tell()<li:
            code=ins.read(1)[0]; size=rint(ins)
            if code==1: w+=d.read(size)
            else: x=rint(a); w+=s[x:x+size]
        assert len(w)==tl; out+=w
    return bytes(out)
if __name__=='__main__':
    src,tgt=open(sys.argv[1],'rb').read(),open(sys.argv[2],'rb').read()
    p=make(src,tgt)
    if apply(src,p)!=tgt: sys.exit('check FAILED: the patch does not rebuild the modded file')
    open(sys.argv[3],'wb').write(p)
    print('wrote %s (%d bytes); checked: it rebuilds the modded file exactly' % (sys.argv[3],len(p)))

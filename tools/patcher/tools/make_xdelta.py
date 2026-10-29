"""Make an xdelta (VCDIFF, RFC 3284) patch from an original ISO to a patched one.

Usage: python3 tools/make_xdelta.py <original.iso> <patched.iso> <out.xdelta> [--hint OFFSET]

Plain Python, so it runs anywhere the patcher does; apply the result with xdelta3 / Delta Patcher /
xdelta UI. The patched ISO is the original plus a few changed sectors and the patched game file added
at the end, so each 1 MB target window is compared with the same spot of the original (and, past the
original's end, with the original game file, which the patched one mostly matches; found from
SYSTEM.CNF for a PS2 ISO, or given with --hint):
equal runs become COPYs, the rest ADDs.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

WINDOW = 1 << 20
MIN_COPY = 32          # shorter equal runs are cheaper as part of an ADD


def varint(n):
    out = [n & 0x7F]
    n >>= 7
    while n:
        out.append(0x80 | (n & 0x7F))
        n >>= 7
    return bytes(reversed(out))


def encode_window(src, src_pos, tgt):
    """One VCDIFF window for target bytes `tgt`, using source bytes `src` (from src_pos) as dictionary."""
    data, inst, addr = bytearray(), bytearray(), bytearray()
    n = len(tgt)
    m = min(len(src), n)
    i = 0
    pending = bytearray()

    def flush_add():
        if pending:
            inst.append(1)                      # ADD, size follows
            inst.extend(varint(len(pending)))
            data.extend(pending)
            pending.clear()

    while i < n:
        if i < m and src[i] == tgt[i]:
            j = i
            # find the end of the equal run quickly in blocks
            while j < m:
                blk = min(4096, m - j)
                if src[j:j + blk] == tgt[j:j + blk]:
                    j += blk
                    continue
                while src[j] == tgt[j]:
                    j += 1
                break
            if j - i >= MIN_COPY:
                flush_add()
                inst.append(19)                 # COPY mode 0 (address as is), size follows
                inst.extend(varint(j - i))
                addr.extend(varint(i))
            else:
                pending.extend(tgt[i:j])
            i = j
        else:
            j = i + 1
            while j < n and not (j < m and src[j] == tgt[j]):
                j += 1
            pending.extend(tgt[i:j])
            i = j
    flush_add()
    body = (varint(n) + b"\x00" + varint(len(data)) + varint(len(inst)) + varint(len(addr))
            + bytes(data) + bytes(inst) + bytes(addr))
    if src:
        head = b"\x01" + varint(len(src)) + varint(src_pos)          # VCD_SOURCE
    else:
        head = b"\x00"
    return head + varint(len(body)) + body


def make(orig_path, new_path, out_path, hint=None, log=print):
    olen, nlen = os.path.getsize(orig_path), os.path.getsize(new_path)
    with open(orig_path, "rb") as fo, open(new_path, "rb") as fn, open(out_path, "wb") as out:
        out.write(b"\xD6\xC3\xC4\x00\x00")
        pos = 0
        while pos < nlen:
            fn.seek(pos)
            tgt = fn.read(WINDOW)
            if pos < olen:
                sp = pos
            elif hint is not None:
                sp = hint + (pos - olen)
            else:
                sp = None
            if sp is not None and sp < olen:
                fo.seek(sp)
                src = fo.read(min(WINDOW, olen - sp))
            else:
                src, sp = b"", 0
            out.write(encode_window(src, sp, tgt))
            pos += len(tgt)
    log("wrote %s (%d bytes) for a %d-byte target" % (out_path, os.path.getsize(out_path), nlen))


def _read_varint(f):
    n = 0
    while True:
        b = f.read(1)[0]
        n = (n << 7) | (b & 0x7F)
        if not b & 0x80:
            return n


def verify(orig_path, delta_path, new_path):
    """Decode the patch (the subset make() writes) against the original and compare with the patched ISO."""
    import hashlib
    import io
    h_out, h_new = hashlib.sha1(), hashlib.sha1()
    with open(orig_path, "rb") as fo, open(delta_path, "rb") as fd, open(new_path, "rb") as fn:
        if fd.read(5) != b"\xD6\xC3\xC4\x00\x00":
            raise ValueError("not a patch from make_xdelta")
        while True:
            ind = fd.read(1)
            if not ind:
                break
            src = b""
            if ind[0] & 1:
                slen, spos = _read_varint(fd), _read_varint(fd)
                fo.seek(spos)
                src = fo.read(slen)
            body = io.BytesIO(fd.read(_read_varint(fd)))
            tlen = _read_varint(body)
            body.read(1)
            ld, li, la = _read_varint(body), _read_varint(body), _read_varint(body)
            data, inst, addr = io.BytesIO(body.read(ld)), io.BytesIO(body.read(li)), io.BytesIO(body.read(la))
            out = bytearray()
            while inst.tell() < li:
                code = inst.read(1)[0]
                size = _read_varint(inst)
                if code == 1:
                    out += data.read(size)
                elif code == 19:
                    a = _read_varint(addr)
                    out += src[a:a + size]
                else:
                    raise ValueError("unexpected instruction %d" % code)
            if len(out) != tlen:
                raise ValueError("window decodes to the wrong size")
            h_out.update(out)
            h_new.update(fn.read(tlen))
        if fn.read(1):
            raise ValueError("the patch makes a shorter file")
    return h_out.hexdigest() == h_new.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("original")
    ap.add_argument("patched")
    ap.add_argument("out")
    ap.add_argument("--hint", type=lambda s: int(s, 0), default=None,
                    help="offset in the original that the part past its end resembles (the original game file)")
    a = ap.parse_args()
    hint = a.hint
    if hint is None:
        try:
            from pmd import ps2patch
            with ps2patch.Ps2Iso(a.original) as iso:
                hint = iso.find(iso.boot_file())["extent"] * ps2patch.SECTOR
        except Exception:
            hint = None
    make(a.original, a.patched, a.out, hint)
    if not verify(a.original, a.out, a.patched):
        sys.exit("check FAILED: the patch does not rebuild %s" % a.patched)
    print("checked: applying it to the original rebuilds the patched ISO exactly")


if __name__ == "__main__":
    main()

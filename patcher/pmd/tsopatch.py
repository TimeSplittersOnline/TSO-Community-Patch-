"""Turn a player's own TimeSplitters: Future Perfect default.xbe into the TSO Community Patch XBE.

The patch file (tso_patch.dat) holds, for every default.xbe it knows (by hash), the
differences between that file and the TSO build, never a whole XBE. Applying it gives
exactly the delivered build: the result is checked against the build's own hash.

File layout: b"TSOPATCH" + u32 format + lzma( u32 header length + JSON header + delta streams ).
Delta stream: ops until the end, each op one byte:
  0 COPY  u32 source offset, u32 length   (bytes from the player's XBE)
  1 ADD   u32 length, then that many bytes
"""

import hashlib
import json
import lzma
import os
import struct
import sys

MAGIC = b"TSOPATCH"
FORMAT = 1
OP_COPY, OP_ADD = 0, 1
PATCH_NAME = "tso_patch.dat"


class PatchError(Exception):
    pass


def md5(data):
    return hashlib.md5(data).hexdigest()


def sha1(data):
    return hashlib.sha1(data).hexdigest()


# -- reading / applying -----------------------------------------------------------

def patch_path():
    """tso_patch.dat next to the program (or inside the PyInstaller bundle)."""
    here = getattr(sys, "_MEIPASS", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    return os.path.join(here, PATCH_NAME)


class TsoPatch:
    def __init__(self, path=None):
        path = path or patch_path()
        try:
            with open(path, "rb") as f:
                raw = f.read()
        except OSError:
            raise PatchError("The patch data (%s) is missing. Download the patcher again." % PATCH_NAME)
        if raw[:8] != MAGIC:
            raise PatchError("%s is not TSO patch data." % os.path.basename(path))
        fmt, = struct.unpack_from("<I", raw, 8)
        if fmt != FORMAT:
            raise PatchError("This patch data needs a newer patcher (format %d)." % fmt)
        body = lzma.decompress(raw[12:])
        hlen, = struct.unpack_from("<I", body, 0)
        self.header = json.loads(body[4:4 + hlen].decode("utf-8"))
        self.blob = body[4 + hlen:]
        self.version = self.header["version"]
        self.out = self.header["output"]
        self.inputs = {i["md5"]: i for i in self.header["inputs"]}
        self.known = {i["md5"]: i for i in self.header.get("known", [])}  # recognised, but no delta shipped

    def identify(self, data):
        """What this XBE is: ("input", entry), ("done", None) when it already is this build, or (None, None)."""
        h = md5(data)
        if h == self.out["md5"] and len(data) == self.out["size"]:
            return "done", None
        e = self.inputs.get(h)
        if e and len(data) == e["size"] and sha1(data) == e["sha1"]:
            return "input", e
        k = self.known.get(h)
        if k and len(data) == k["size"] and sha1(data) == k["sha1"]:
            return "known", k
        return None, None

    def apply(self, data):
        kind, e = self.identify(data)
        if kind == "done":
            return bytes(data)
        if kind == "known":
            raise PatchError("%s can't be patched by this patcher: %s" % (e["name"], e["why"]))
        if kind is None:
            raise PatchError("This default.xbe isn't one the patcher knows, so it can't be patched safely.")
        out = apply_delta(data, self.blob[e["ofs"]:e["ofs"] + e["len"]])
        if len(out) != self.out["size"] or sha1(out) != self.out["sha1"]:
            raise PatchError("The patched XBE didn't come out right (checksum mismatch), so nothing was written.")
        return out


def apply_delta(src, delta):
    out = bytearray()
    i, n = 0, len(delta)
    while i < n:
        op = delta[i]
        if op == OP_COPY:
            s, ln = struct.unpack_from("<II", delta, i + 1)
            i += 9
            if s + ln > len(src):
                raise PatchError("Damaged patch data.")
            out += src[s:s + ln]
        elif op == OP_ADD:
            ln, = struct.unpack_from("<I", delta, i + 1)
            i += 5
            out += delta[i:i + ln]
            i += ln
        else:
            raise PatchError("Damaged patch data.")
    return bytes(out)


# -- making (build time only) ----------------------------------------------------------

def make_delta(src, dst, key=16, step=4, min_match=32):
    """Copy/add ops that turn src into dst. Same-offset copies first, then any offset."""
    index = {}
    for i in range(0, len(src) - key + 1, step):
        index.setdefault(src[i:i + key], i)
    ops = []
    add_start = 0
    i = 0
    n = len(dst)

    def extend(s, d):
        ln = 0
        while d + ln < n and s + ln < len(src):
            blk = 4096
            if src[s + ln:s + ln + blk] == dst[d + ln:d + ln + blk] and d + ln + blk <= n and s + ln + blk <= len(src):
                ln += blk
                continue
            if src[s + ln] != dst[d + ln]:
                break
            ln += 1
        return ln

    while i < n:
        s = None
        if i + min_match <= len(src) and src[i:i + min_match] == dst[i:i + min_match]:
            s = i
        else:
            s = index.get(dst[i:i + key])
        ln = extend(s, i) if s is not None else 0
        if ln >= min_match:
            # grow backwards into the pending add
            while i > add_start and s > 0 and src[s - 1] == dst[i - 1]:
                i, s, ln = i - 1, s - 1, ln + 1
            if i > add_start:
                ops.append((OP_ADD, dst[add_start:i]))
            ops.append((OP_COPY, s, ln))
            i += ln
            add_start = i
        else:
            i += 1
    if add_start < n:
        ops.append((OP_ADD, dst[add_start:n]))
    out = bytearray()
    for op in ops:
        if op[0] == OP_COPY:
            out += struct.pack("<BII", OP_COPY, op[1], op[2])
        else:
            out += struct.pack("<BI", OP_ADD, len(op[1])) + op[1]
    assert apply_delta(src, bytes(out)) == bytes(dst)
    return bytes(out)


def make_patch(version, output_xbe, inputs, path, known=()):
    """inputs: list of (name, xbe bytes). known: list of (name, xbe bytes, why) recognised without a delta.
    Writes the patch file and returns its header."""
    out = bytes(output_xbe)
    header = {"version": version,
              "output": {"md5": md5(out), "sha1": sha1(out), "size": len(out)},
              "inputs": [],
              "known": [{"name": n, "md5": md5(d), "sha1": sha1(d), "size": len(d), "why": w} for n, d, w in known]}
    blob = bytearray()
    for name, data in inputs:
        d = make_delta(data, out)
        header["inputs"].append({"name": name, "md5": md5(data), "sha1": sha1(data), "size": len(data),
                                 "ofs": len(blob), "len": len(d)})
        blob += d
    hj = json.dumps(header, indent=1).encode("utf-8")
    body = struct.pack("<I", len(hj)) + hj + bytes(blob)
    raw = MAGIC + struct.pack("<I", FORMAT) + lzma.compress(body, preset=9 | lzma.PRESET_EXTREME)
    with open(path, "wb") as f:
        f.write(raw)
    return header

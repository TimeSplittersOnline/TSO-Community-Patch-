"""Bake a PCSX2 .pnach into a TimeSplitters: Future Perfect PS2 ISO.

The pnach's EE writes are applied to the game's ELF. Writes inside the ELF's
loaded file data change those bytes; writes below/above every segment (the
mod's own code area, e.g. 0xFA800-0x100000) go into a new loadable segment.
The patched ELF is appended to the end of the ISO and the ISO's directory
entry is pointed at it, so the original ELF bytes are never touched and
undoing is just pointing back and trimming the ISO to its old length.

PS2 DVDs carry a second file listing (UDF) next to the ISO9660 one, and
some loaders (a PS3 running the ISO through webMAN) read that one, so the
UDF file entry is pointed at the patched ELF as well (class Udf).
"""

import os
import re
import struct

SECTOR = 2048

# The only games this works on: (serial, ELF CRC as PCSX2 computes it, label)
TSFP_VERSIONS = {
    0xFB2F4502: ("SLUS-21148", "USA", "NTSC"),
    0xE0F96C7D: ("SLES-52993", "Europe", "PAL"),
}

PT_LOAD = 1


class Ps2PatchError(Exception):
    pass


# -- pnach --------------------------------------------------------------------

class Pnach:
    def __init__(self, path):
        self.path = path
        text = open(path, "r", encoding="utf-8", errors="replace").read()
        self.title = ""
        m = re.search(r"^\s*gametitle\s*=\s*(.*)$", text, re.M | re.I)
        if m:
            self.title = m.group(1).strip()
        self.crc = None
        m = re.search(r"([0-9A-Fa-f]{8})\.pnach$", os.path.basename(path))
        if m:
            self.crc = int(m.group(1), 16)
        else:
            m = re.search(r"\(([0-9A-Fa-f]{8})\)", self.title)
            if m:
                self.crc = int(m.group(1), 16)
        self.writes = []      # (address, bytes)
        self.skipped = []     # lines we can't bake in
        for n, line in enumerate(text.splitlines(), 1):
            s = line.split("//")[0].strip()
            if not s.lower().startswith("patch"):
                continue
            m = re.match(r"patch\s*=\s*(\d+)\s*,\s*(\w+)\s*,\s*([0-9A-Fa-f]+)\s*,\s*(\w+)\s*,\s*([0-9A-Fa-f]+)", s, re.I)
            if not m:
                self.skipped.append((n, line.strip(), "not understood"))
                continue
            cpu, addr, kind, val = m.group(2).upper(), int(m.group(3), 16), m.group(4).lower(), int(m.group(5), 16)
            if cpu != "EE":
                self.skipped.append((n, line.strip(), "not an EE (main CPU) patch"))
                continue
            if kind == "extended":
                code = addr >> 28
                addr &= 0x01FFFFFF
                if code == 0:
                    kind, val = "byte", val & 0xFF
                elif code == 1:
                    kind, val = "short", val & 0xFFFF
                elif code == 2:
                    kind = "word"
                else:
                    self.skipped.append((n, line.strip(), "conditional/extended code can't be baked in"))
                    continue
            addr &= 0x01FFFFFF
            if kind == "byte":
                data = struct.pack("<B", val & 0xFF)
            elif kind == "short":
                data = struct.pack("<H", val & 0xFFFF)
            elif kind == "word":
                data = struct.pack("<I", val & 0xFFFFFFFF)
            elif kind == "double":
                data = struct.pack("<Q", val)
            else:
                self.skipped.append((n, line.strip(), "unknown write type"))
                continue
            self.writes.append((addr, data))
        if not self.writes:
            raise Ps2PatchError("No patch lines found in %s" % os.path.basename(path))


# -- ELF ----------------------------------------------------------------------

def elf_crc(data):
    """PCSX2's game CRC: XOR of every 32-bit word of the ELF."""
    c = 0
    n = len(data) // 4
    for (w,) in struct.iter_unpack("<I", data[:n * 4]):
        c ^= w
    return c


def _phdrs(elf):
    if elf[:4] != b"\x7fELF" or elf[4] != 1 or elf[5] != 1:
        raise Ps2PatchError("The game's main file is not a 32-bit little-endian ELF")
    phoff, = struct.unpack_from("<I", elf, 28)
    phentsize, phnum = struct.unpack_from("<HH", elf, 42)
    out = []
    for i in range(phnum):
        out.append(list(struct.unpack_from("<8I", elf, phoff + i * phentsize)))
    return phoff, phentsize, out


def patch_elf(elf, pnach):
    """Return (new_elf, report) with every pnach write baked in."""
    phoff, phentsize, phdrs = _phdrs(elf)
    loads = [p for p in phdrs if p[0] == PT_LOAD]
    out = bytearray(elf)
    outside = {}
    report = {"in_elf": 0, "new_segment": 0, "bss": []}
    for addr, data in pnach.writes:
        for i, b in enumerate(data):
            a = addr + i
            placed = False
            for p in loads:
                _t, off, va, _pa, filesz, memsz, _f, _al = p
                if va <= a < va + filesz:
                    out[off + a - va] = b
                    placed = True
                    break
                if va + filesz <= a < va + memsz:
                    report["bss"].append(a)
                    placed = True
                    break
            if not placed:
                outside[a] = b
        if not any(p[2] <= addr < p[2] + p[4] for p in loads):
            if not any(p[2] + p[4] <= addr < p[2] + p[5] for p in loads):
                report["new_segment"] += 1
                continue
        report["in_elf"] += 1
    if report["bss"]:
        first = min(report["bss"])
        raise Ps2PatchError("%d patch bytes land in memory the game clears when it starts (first at %08X), "
                            "so they can't be baked into the ISO." % (len(report["bss"]), first))
    if outside:
        # group into ranges, merging gaps smaller than 4 KB
        addrs = sorted(outside)
        ranges = []
        start = prev = addrs[0]
        for a in addrs[1:]:
            if a - prev > 0x1000:
                ranges.append((start, prev + 1))
                start = a
            prev = a
        ranges.append((start, prev + 1))
        for lo, hi in ranges:
            for p in loads:
                if lo < p[2] + p[5] and hi > p[2]:
                    raise Ps2PatchError("Patch range %08X-%08X overlaps the game's memory" % (lo, hi))
        first_data = min(p[1] for p in phdrs if p[4]) if phdrs else len(out)
        need = phoff + (len(phdrs) + len(ranges)) * phentsize
        if need > first_data or any(out[phoff + len(phdrs) * phentsize:need]):
            raise Ps2PatchError("No room in the ELF header for the extra code segment")
        new_ph = []
        for lo, hi in ranges:
            lo &= ~3
            hi = (hi + 3) & ~3
            seg = bytearray(hi - lo)
            for a in range(lo, hi):
                if a in outside:
                    seg[a - lo] = outside[a]
            while len(out) % 16:
                out.append(0)
            # keep file offset and address congruent modulo the alignment
            while len(out) % 16 != lo % 16:
                out.append(0)
            off = len(out)
            out += seg
            new_ph.append((PT_LOAD, off, lo, lo, len(seg), len(seg), 7, 16))
        for i, p in enumerate(new_ph):
            struct.pack_into("<8I", out, phoff + (len(phdrs) + i) * phentsize, *p)
        struct.pack_into("<H", out, 44, len(phdrs) + len(new_ph))
        report["segments"] = [(p[2], p[2] + p[4]) for p in new_ph]
    return bytes(out), report


# -- ISO9660 ------------------------------------------------------------------

class Ps2Iso:
    def __init__(self, path, writable=False):
        self.path = path
        self.f = open(path, "r+b" if writable else "rb")
        self.f.seek(16 * SECTOR)
        pvd = self.f.read(SECTOR)
        if pvd[1:6] != b"CD001" or pvd[0] != 1:
            self.close()
            raise Ps2PatchError("%s is not a PS2 DVD/CD image (.iso)" % os.path.basename(path))
        self.pvd = pvd
        self.root = self._record(pvd, 156)

    def close(self):
        if self.f:
            self.f.close()
            self.f = None

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()

    @staticmethod
    def _record(buf, pos):
        ln = buf[pos]
        extent, = struct.unpack_from("<I", buf, pos + 2)
        size, = struct.unpack_from("<I", buf, pos + 10)
        flags = buf[pos + 25]
        nlen = buf[pos + 32]
        name = buf[pos + 33:pos + 33 + nlen].decode("latin-1")
        return {"len": ln, "extent": extent, "size": size, "flags": flags, "name": name}

    def listdir(self, rec):
        self.f.seek(rec["extent"] * SECTOR)
        data = self.f.read(rec["size"])
        out = []
        pos = 0
        while pos < len(data):
            ln = data[pos]
            if ln == 0:
                pos = (pos // SECTOR + 1) * SECTOR
                continue
            r = self._record(data, pos)
            r["record_offset"] = rec["extent"] * SECTOR + pos
            if r["name"] not in ("\x00", "\x01"):
                out.append(r)
            pos += ln
        return out

    def find(self, path):
        parts = [p for p in path.replace("\\", "/").split("/") if p]
        cur = self.root
        for i, part in enumerate(parts):
            want = part.upper().split(";")[0]
            for r in self.listdir(cur):
                if r["name"].upper().split(";")[0] == want:
                    cur = r
                    break
            else:
                raise Ps2PatchError("%s not found in the ISO" % path)
        return cur

    def read(self, rec):
        self.f.seek(rec["extent"] * SECTOR)
        return self.f.read(rec["size"])

    def boot_file(self):
        cnf = self.read(self.find("SYSTEM.CNF")).decode("latin-1", "replace")
        m = re.search(r"BOOT2\s*=\s*cdrom0:\\?\\?([^\s;]+)", cnf, re.I)
        if not m:
            raise Ps2PatchError("SYSTEM.CNF has no BOOT2 line; is this a PS2 game?")
        return m.group(1).replace("\\", "/")

    def set_record(self, rec, extent, size):
        o = rec["record_offset"]
        self.f.seek(o + 2)
        self.f.write(struct.pack("<I", extent) + struct.pack(">I", extent))
        self.f.seek(o + 10)
        self.f.write(struct.pack("<I", size) + struct.pack(">I", size))

    def set_volume_size(self, sectors):
        self.f.seek(16 * SECTOR + 80)
        self.f.write(struct.pack("<I", sectors) + struct.pack(">I", sectors))


# -- UDF (the DVD's second file listing) --------------------------------------

def _crc16(b):
    c = 0
    for x in b:
        c ^= x << 8
        for _ in range(8):
            c = ((c << 1) ^ 0x1021) & 0xFFFF if c & 0x8000 else (c << 1) & 0xFFFF
    return c


def _retag(sec, loc=None):
    """Fix a UDF descriptor's tag (location, CRC, checksum) after changing it."""
    if loc is not None:
        struct.pack_into("<I", sec, 12, loc)
    ln, = struct.unpack_from("<H", sec, 10)
    struct.pack_into("<H", sec, 8, _crc16(bytes(sec[16:16 + ln])))
    sec[4] = (sum(sec[0:4]) + sum(sec[5:16])) & 0xFF


def _dstring(b, comp):
    if comp == 16:
        return b.decode("utf-16-be", "replace")
    return b.decode("latin-1")


class Udf:
    """Just enough UDF 1.02 to find a file's entry and re-point it."""

    def __init__(self, f):
        self.f = f
        avdp = self.sector(256)
        if struct.unpack_from("<H", avdp, 0)[0] != 2:
            raise Ps2PatchError("no UDF")
        self.avdp = avdp
        mlen, mloc, rlen, rloc = struct.unpack_from("<IIII", avdp, 16)
        self.pds = []
        lvd = None
        for s in list(range(mloc, mloc + mlen // SECTOR)) + list(range(rloc, rloc + rlen // SECTOR)):
            t, = struct.unpack_from("<H", self.sector(s), 0)
            if t == 5:
                self.pds.append(s)
            elif t == 6 and lvd is None:
                lvd = self.sector(s)
            elif t == 8:
                if s >= rloc:
                    break
        if not self.pds or lvd is None:
            raise Ps2PatchError("UDF volume descriptors not found")
        pd = self.sector(self.pds[0])
        self.pstart, self.plen = struct.unpack_from("<II", pd, 188)
        fsd_blk, = struct.unpack_from("<I", lvd, 252)
        fsd = self.sector(self.pstart + fsd_blk)
        if struct.unpack_from("<H", fsd, 0)[0] != 256:
            raise Ps2PatchError("UDF file set descriptor not found")
        self.root = struct.unpack_from("<I", fsd, 404)[0]

    def sector(self, s):
        self.f.seek(s * SECTOR)
        return bytearray(self.f.read(SECTOR))

    def _fe(self, blk):
        sec = self.sector(self.pstart + blk)
        if struct.unpack_from("<H", sec, 0)[0] != 261:
            raise Ps2PatchError("UDF file entry not found")
        if struct.unpack_from("<H", sec, 34)[0] & 7 != 0:
            raise Ps2PatchError("UDF file entry uses an unsupported layout")
        lea, lad = struct.unpack_from("<II", sec, 168)
        ads = [(a & 0x3FFFFFFF, b) for a, b in struct.iter_unpack("<II", bytes(sec[176 + lea:176 + lea + lad]))]
        return sec, ads, lea

    def find(self, path):
        """Return (FE sector number, [(length, partition block)], file length)."""
        blk = self.root
        parts = [p for p in path.replace("\\", "/").split("/") if p]
        for part in parts:
            sec, ads, _ = self._fe(blk)
            ln, = struct.unpack_from("<Q", sec, 56)
            data = b"".join(self.sector(self.pstart + b + i)
                            for alen, b in ads for i in range((alen + SECTOR - 1) // SECTOR))[:ln]
            want = part.upper().split(";")[0]
            p = 0
            found = None
            while p + 38 <= len(data) and struct.unpack_from("<H", data, p)[0] == 257:
                lfi = data[p + 19]
                icb, = struct.unpack_from("<I", data, p + 24)
                liu, = struct.unpack_from("<H", data, p + 36)
                raw = data[p + 38 + liu:p + 38 + liu + lfi]
                if raw and _dstring(raw[1:], raw[0]).upper().split(";")[0] == want:
                    found = icb
                    break
                p += (38 + liu + lfi + 3) & ~3
            if found is None:
                raise Ps2PatchError("%s not found in the UDF listing" % path)
            blk = found
        sec, ads, _ = self._fe(blk)
        return self.pstart + blk, ads, struct.unpack_from("<Q", sec, 56)[0]

    def read(self, path):
        _s, ads, ln = self.find(path)
        out = b""
        for alen, b in ads:
            self.f.seek((self.pstart + b) * SECTOR)
            out += self.f.read(alen)
        return out[:ln]

    def repoint(self, path, sector, size, volume_sectors):
        """Point the file at `size` bytes from ISO sector `sector`, growing the partition to
        cover `volume_sectors` (the image's new length) and adding an anchor at its last sector.
        touched() lists the sectors this changes inside the old image, for undo."""
        fes, ads, _ln = self.find(path)

        def put(s, sec):
            self.f.seek(s * SECTOR)
            self.f.write(bytes(sec))

        end = volume_sectors - 1          # last sector holds a new anchor
        if self.pstart + self.plen < end:
            for s in self.pds:
                pd = self.sector(s)
                struct.pack_into("<I", pd, 192, end - self.pstart)
                _retag(pd)
                put(s, pd)
            self.plen = end - self.pstart
        sec, _ads, lea = self._fe(fes - self.pstart)
        blocks = (size + SECTOR - 1) // SECTOR
        struct.pack_into("<QQ", sec, 56, size, blocks)
        struct.pack_into("<I", sec, 172, 8)
        struct.pack_into("<II", sec, 176 + lea, size, sector - self.pstart)
        ln = 176 + lea + 8 - 16
        struct.pack_into("<H", sec, 10, ln)
        _retag(sec)
        put(fes, sec)
        anchor = bytearray(self.avdp)
        _retag(anchor, end)
        self.f.seek(end * SECTOR)
        self.f.write(bytes(anchor))

    def touched(self, path):
        return self.pds + [self.find(path)[0]]


def open_udf(f):
    """The disc's UDF listing, or None if it has none."""
    try:
        return Udf(f)
    except (Ps2PatchError, struct.error):
        return None


def inspect_iso(path):
    """Return dict about the TSFP ISO: boot file, record, ELF crc, version."""
    with Ps2Iso(path) as iso:
        boot = iso.boot_file()
        rec = iso.find(boot)
        elf = iso.read(rec)
        iso.f.seek(0, os.SEEK_END)
        length = iso.f.tell()
    crc = elf_crc(elf)
    return {"boot": boot, "record": rec, "elf": elf, "crc": crc, "length": length,
            "version": TSFP_VERSIONS.get(crc)}


def pnach_version(pn):
    """The game CRC a pnach is for: from its name/title, or a TSFP serial in either."""
    if pn.crc is not None:
        return pn.crc
    text = (os.path.basename(pn.path) + " " + pn.title).upper().replace("_", "-").replace(".", "")
    for crc, (serial, _r, _t) in TSFP_VERSIONS.items():
        if serial in text or serial.replace("-", "") in text:
            return crc
    return None


def describe_crc(crc):
    v = TSFP_VERSIONS.get(crc)
    return "%s (%s, %s)" % (v[1], v[2], v[0]) if v else "unknown version (CRC %08X)" % (crc or 0)

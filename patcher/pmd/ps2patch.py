"""Bake a PCSX2 .pnach into a TimeSplitters: Future Perfect PS2 ISO.

The pnach's EE writes are applied to the game's ELF. Writes inside the ELF's
loaded file data change those bytes; writes below/above every segment (the
mod's own code area, e.g. 0xFA800-0x100000) go into a new loadable segment.
The patched ELF is appended to the end of the ISO and the ISO's directory
entry is pointed at it, so the original ELF bytes are never touched and
undoing is just pointing back and trimming the ISO to its old length.
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

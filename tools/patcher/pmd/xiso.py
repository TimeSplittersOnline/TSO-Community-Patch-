"""Xbox game disc images (XISO / redump .iso): find and replace files in place.

A file is only replaced when the new data fits in the space the old file had
before the next thing on the disc, so nothing else in the image moves.
"""

import os
import struct

SECTOR = 2048
MAGIC = b"MICROSOFT*XBOX*MEDIA"
# where the game partition starts: extract-xiso images, redump XGD1/2/3
PARTITION_OFFSETS = (0, 0x18300000, 0x0FD90000, 0x02080000)
ATTR_DIRECTORY = 0x10


class XisoError(Exception):
    pass


class XisoEntry:
    __slots__ = ("name", "attr", "sector", "size", "entry_offset")

    @property
    def is_dir(self):
        return bool(self.attr & ATTR_DIRECTORY)


class Xiso:
    def __init__(self, path, writable=False):
        self.path = path
        self.f = open(path, "r+b" if writable else "rb")
        self.base = None
        for off in PARTITION_OFFSETS:
            self.f.seek(off + 32 * SECTOR)
            if self.f.read(20) == MAGIC:
                self.base = off
                break
        if self.base is None:
            self.f.close()
            raise XisoError("%s is not an Xbox game disc image" % os.path.basename(path))
        self.f.seek(self.base + 32 * SECTOR + 20)
        self.root_sector, self.root_size = struct.unpack("<II", self.f.read(8))

    def close(self):
        if self.f:
            self.f.close()
            self.f = None

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()

    def _read(self, off, n):
        self.f.seek(off)
        return self.f.read(n)

    def listdir(self, sector, size):
        """Entries of the directory table at sector (in-order tree walk)."""
        table_off = self.base + sector * SECTOR
        data = self._read(table_off, size)
        out, seen = [], set()
        stack, node = [], 0
        # iterative in-order walk of the binary tree (offsets are in dwords)
        while stack or node is not None:
            while node is not None:
                pos = node * 4
                if pos in seen or pos + 14 > len(data):
                    node = None
                    break
                seen.add(pos)
                stack.append(pos)
                left = struct.unpack_from("<H", data, pos)[0]
                node = left if left not in (0, 0xFFFF) else None
            if not stack:
                break
            pos = stack.pop()
            left, right, start, fsize, attr, nlen = struct.unpack_from("<HHIIBB", data, pos)
            e = XisoEntry()
            e.name = data[pos + 14:pos + 14 + nlen].decode("latin-1")
            e.attr, e.sector, e.size = attr, start, fsize
            e.entry_offset = table_off + pos
            out.append(e)
            node = right if right not in (0, 0xFFFF) else None
        return out

    def walk(self, sector=None, size=None, prefix=""):
        """Yield (path, entry) for everything on the disc."""
        if sector is None:
            sector, size = self.root_sector, self.root_size
        for e in self.listdir(sector, size):
            p = (prefix + "/" + e.name).strip("/")
            yield p, e
            if e.is_dir and e.size:
                yield from self.walk(e.sector, e.size, p)

    def lookup(self, path):
        want = path.replace("\\", "/").strip("/").lower()
        for p, e in self.walk():
            if p.lower() == want:
                return e
        raise FileNotFoundError(path)

    def read_file(self, path):
        e = self.lookup(path)
        return self._read(self.base + e.sector * SECTOR, e.size)

    def room_for(self, e):
        """Bytes available for e without touching the next file or table."""
        starts = [self.root_sector]
        for _p, o in self.walk():
            if o.size:
                starts.append(o.sector)
        after = [s for s in starts if s > e.sector]
        if after:
            return (min(after) - e.sector) * SECTOR
        self.f.seek(0, os.SEEK_END)
        return self.f.tell() - (self.base + e.sector * SECTOR)

    def replace_file(self, path, data):
        e = self.lookup(path)
        if e.is_dir:
            raise XisoError("%s is a folder" % path)
        room = self.room_for(e)
        if len(data) > room:
            # Too big for its slot: put it at the end of the image instead and
            # point the directory entry there. The old copy is left in place.
            self.f.seek(0, os.SEEK_END)
            end = self.f.tell()
            start = (end - self.base + SECTOR - 1) // SECTOR
            alloc = ((len(data) + SECTOR - 1) // SECTOR) * SECTOR
            self.f.seek(self.base + start * SECTOR)
            self.f.write(data + b"\0" * (alloc - len(data)))
            self.f.seek(e.entry_offset + 4)
            self.f.write(struct.pack("<II", start, len(data)))
            self.f.flush()
            os.fsync(self.f.fileno())
            return
        old_alloc = ((e.size + SECTOR - 1) // SECTOR) * SECTOR
        new_alloc = ((len(data) + SECTOR - 1) // SECTOR) * SECTOR
        pad = max(old_alloc, new_alloc) - len(data)
        self.f.seek(self.base + e.sector * SECTOR)
        self.f.write(data + b"\0" * pad)
        self.f.seek(e.entry_offset + 8)
        self.f.write(struct.pack("<I", len(data)))
        self.f.flush()
        os.fsync(self.f.fileno())

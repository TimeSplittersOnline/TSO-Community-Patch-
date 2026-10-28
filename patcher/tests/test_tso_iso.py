"""Patch a hand-made disc image whose default.xbe is a known XBE, update it again, and put the original back.
Usage: python tests/test_tso_iso.py <TSO xbe> <known default.xbe>
"""
import hashlib
import os
import struct
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from pmd import core  # noqa: E402
from pmd.xiso import MAGIC, SECTOR  # noqa: E402


def make_iso(path, xbe):
    """default.xbe followed straight away by another file, like a real disc (no room to grow in place)."""
    other = b"pak data" * 1000
    xs = (len(xbe) + SECTOR - 1) // SECTOR
    e1 = bytearray(struct.pack("<HHIIBB", 0, 0, 34, len(xbe), 0x20, 11) + b"default.xbe")
    e1 += b"\0" * (-len(e1) % 4)
    e2 = struct.pack("<HHIIBB", 0, 0, 34 + xs, len(other), 0x20, 3) + b"zzz"
    struct.pack_into("<H", e1, 2, len(e1) // 4)  # right child: the second entry
    ent = bytes(e1) + e2
    hdr = MAGIC + struct.pack("<II", 33, SECTOR) + b"\0" * 8 + b"\0" * 0x7C8 + MAGIC
    with open(path, "wb") as f:
        f.write(b"\0" * (32 * SECTOR) + hdr.ljust(SECTOR, b"\0") + ent.ljust(SECTOR, b"\xff"))
        f.write(xbe + b"\0" * (-len(xbe) % SECTOR) + other + b"\0" * (-len(other) % SECTOR))


tso = open(sys.argv[1], "rb").read()
orig = open(sys.argv[2], "rb").read()
work = tempfile.mkdtemp(prefix="tso_iso_")
iso, bdir = os.path.join(work, "game.iso"), os.path.join(work, "backups")
make_iso(iso, orig)
before = hashlib.sha1(open(iso, "rb").read()).hexdigest()
from pmd.xiso import Xiso  # noqa: E402
with Xiso(iso) as x:
    other = x.read_file("zzz")
t = core.find_iso_game(iso)
assert t.info.is_tsfp
data = core.original_iso_xbe(bdir, t)
assert data == orig
core.patch_iso(iso, t, core.make_tso_xbe(data), bdir, log=lambda m: print("  " + m))
assert core.read_iso_xbe(t) == tso
with Xiso(iso) as x:
    assert x.read_file("zzz") == other, "patching damaged the next file"
# once patched, the disc image's own XBE is still the saved original
assert core.original_iso_xbe(bdir, t) == orig
core.patch_iso(iso, t, core.make_tso_xbe(core.original_iso_xbe(bdir, t)), bdir, log=lambda m: print("  " + m))
core.restore_original(t, bdir, log=lambda m: print("  " + m))
with Xiso(iso) as x:
    assert x.read_file("default.xbe") == orig and x.read_file("zzz") == other
if len(tso) <= len(orig):
    assert hashlib.sha1(open(iso, "rb").read()).hexdigest() == before, "image not back to the original"
print("disc image: patch, re-patch and restore OK")

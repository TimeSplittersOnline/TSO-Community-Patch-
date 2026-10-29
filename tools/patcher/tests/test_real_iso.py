"""Patch and restore a COPY of a real disc image, end to end, the way the buttons do.
Usage:
  python tests/test_real_iso.py ps2 <PS2 ISO> <pnach> [work folder]
  python tests/test_real_iso.py xbox <Xbox ISO> [work folder]
The image is copied into the work folder (default: the system temp folder) and the copy is deleted after.
"""
import hashlib
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pmd import core, ps2patch  # noqa: E402


def sha1(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def log(m):
    print("  " + m)


def ps2(iso, bdir, pnach):
    before = sha1(iso)
    orig = ps2patch.inspect_iso(iso)
    core.patch_ps2_iso(pnach, iso, bdir, log=log)
    new = ps2patch.inspect_iso(iso)
    assert new["elf"] != orig["elf"], "the game file didn't change"
    with open(iso, "rb") as f:
        udf = ps2patch.open_udf(f)
        if udf:
            assert udf.read(orig["boot"]) == new["elf"], "UDF listing doesn't point at the patched game file"
    print("patched: ISO9660%s point at the patched game file" % (" and UDF" if udf else ""))
    core.patch_ps2_iso(pnach, iso, bdir, log=log)  # patching again undoes the first one, then patches
    assert ps2patch.inspect_iso(iso)["elf"] == new["elf"]
    print("patched again: same result")
    rec = core.ps2_patched_record(bdir, iso)
    assert rec is not None
    core.restore_ps2_iso(rec, log=log)
    assert sha1(iso) == before, "the ISO isn't byte for byte the original after restoring"
    print("restored: byte for byte the original ISO")


def xbox(iso, bdir):
    t = core.find_iso_game(iso)
    assert t.info and t.info.is_tsfp, "not TimeSplitters: Future Perfect"
    orig = core.read_iso_xbe(t)
    want = core.make_tso_xbe(core.original_iso_xbe(bdir, t))
    core.patch_iso(iso, t, want, bdir, log=log)
    t = core.find_iso_game(iso)
    assert core.read_iso_xbe(t) == want
    print("patched: the disc image starts the TSO Community Patch %s" % core.tso_patch().version)
    core.restore_original(t, bdir, log=log)
    assert core.read_iso_xbe(core.find_iso_game(iso)) == orig
    print("restored: the original default.xbe is back")


kind, src = sys.argv[1], sys.argv[2]
rest = sys.argv[3:]
pnach = rest.pop(0) if kind == "ps2" else None
work = tempfile.mkdtemp(prefix="tso_real_", dir=rest[0] if rest else None)
try:
    iso = os.path.join(work, os.path.basename(src))
    shutil.copyfile(src, iso)
    bdir = os.path.join(work, "backups")
    ps2(iso, bdir, pnach) if kind == "ps2" else xbox(iso, bdir)
    print("OK: %s" % os.path.basename(src))
finally:
    shutil.rmtree(work, ignore_errors=True)

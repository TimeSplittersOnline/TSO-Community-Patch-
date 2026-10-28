"""Xbox disc image test: swap default.xbe in images built by extract-xiso (plain and
redump layout), check extract-xiso agrees, then patch and restore through core.
Usage: python tests/test_iso.py path/to/extract-xiso
"""

import hashlib
import os
import random
import shutil
import struct
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from pmd import core  # noqa: E402

def fake_xbe(title, size, seed):
    rnd = random.Random(seed)
    body = bytearray(rnd.getrandbits(8) for _ in range(size))
    body[0:4] = b"XBEH"
    base = 0x10000
    struct.pack_into("<I", body, 0x104, base)
    struct.pack_into("<I", body, 0x118, base + 0x200)
    struct.pack_into("<III", body, 0x200, 0x1D0, 0, 0x4541000D)
    name = title.encode("utf-16-le")[:78]
    body[0x20C:0x20C + 80] = name.ljust(80, b"\0")
    return bytes(body)


def xiso_test(extract_xiso):
    """Replace default.xbe inside a disc image built by extract-xiso, then extract it back."""
    from pmd.xiso import Xiso, XisoError
    work = tempfile.mkdtemp(prefix="pmd_xiso_")
    game = os.path.join(work, "TSFP")
    os.makedirs(os.path.join(game, "media", "sub"))
    orig = fake_xbe("TimeSplitters FP", 6_344_704, 21)
    open(os.path.join(game, "default.xbe"), "wb").write(orig)
    others = {}
    for i in range(40):
        p = os.path.join("media", "sub" if i % 2 else "", "file%02d.bin" % i)
        b = os.urandom(random.randint(1, 300000))
        open(os.path.join(game, p), "wb").write(b)
        others[p.replace(os.sep, "/")] = b
    subprocess.check_call([extract_xiso, "-c", game, os.path.join(work, "g.iso")], stdout=subprocess.DEVNULL)
    iso = os.path.join(work, "g.iso")
    # a redump-style image has the game partition at 0x18300000
    redump = os.path.join(work, "redump.iso")
    with open(redump, "wb") as f:
        f.seek(0x18300000)
        f.write(open(iso, "rb").read())
    for img in (iso, redump):
        with Xiso(img) as x:
            assert x.read_file("default.xbe") == orig
            assert x.read_file("media/sub/file01.bin") == others["media/sub/file01.bin"]
        mod = bytearray(orig)
        mod[0x5000:0x5000 + 64] = os.urandom(64)
        for new in (bytes(mod), bytes(mod[:6_000_000]), bytes(mod) + b"\x90" * 1000):
            with Xiso(img, writable=True) as x:
                x.replace_file("default.xbe", new)
            with Xiso(img) as x:
                assert x.read_file("default.xbe") == new
                for p, b in others.items():
                    assert x.read_file(p) == b, p
        if img == iso:
            out = os.path.join(work, "x")
            os.makedirs(out)
            subprocess.check_call([extract_xiso, "-x", img, "-d", out], stdout=subprocess.DEVNULL)
            got = open(os.path.join(out, "default.xbe"), "rb").read()
            assert got == bytes(mod) + b"\x90" * 1000, "extract-xiso disagrees"
            for p, b in others.items():
                assert open(os.path.join(out, p), "rb").read() == b, p
    # core flow: patch, then restore the original
    bdir = os.path.join(work, "b")
    t = core.find_iso_game(iso)
    with open(os.path.join(work, "mod.xbe"), "wb") as f:
        f.write(bytes(mod))
    with Xiso(iso) as x:
        before = x.read_file("default.xbe")
    core.patch_iso(iso, t, os.path.join(work, "mod.xbe"), bdir)
    with Xiso(iso) as x:
        assert x.read_file("default.xbe") == bytes(mod)
    core.restore_original(t, bdir)
    with Xiso(iso) as x:
        cur = x.read_file("default.xbe")
    assert cur == before
    assert core.load_backups(bdir)[0]["note"] == "ORIGINAL"
    shutil.rmtree(work)
    print("XISO TESTS PASSED", len(cur))


if __name__ == "__main__":
    xiso_test(sys.argv[1])

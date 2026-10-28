"""TSO patch test: every known default.xbe becomes the delivered TSO build, and anything else is refused.
Usage: python tests/test_tso.py <TSO Community Patch.xbe> <known default.xbe> ...
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from pmd import core, tsopatch  # noqa: E402


def main():
    tso = open(sys.argv[1], "rb").read()
    p = core.tso_patch()
    assert tsopatch.md5(tso) == p.out["md5"], "tso_patch.dat is not for this TSO build"
    for path in sys.argv[2:]:
        data = open(path, "rb").read()
        ok, text = core.describe_xbe(data)
        assert ok, text
        assert core.make_tso_xbe(data) == tso
        print("OK  %s: %s" % (os.path.basename(path), text))
    ok, text = core.describe_xbe(tso)
    assert ok and "already" in text, text
    assert core.make_tso_xbe(tso) == tso
    # one changed byte, a truncated file, a loader-sized file and a non-XBE are refused
    bad = bytearray(open(sys.argv[2], "rb").read())
    bad[0x200000] ^= 1
    for name, d in (("one byte changed", bytes(bad)), ("truncated", bytes(bad[:-1])), ("loader", bytes(bad[:126976])),
                    ("not an xbe", b"hello" * 1000)):
        ok, text = core.describe_xbe(d)
        assert not ok, name
        try:
            core.make_tso_xbe(d)
            raise AssertionError("patched " + name)
        except tsopatch.PatchError:
            pass
        print("OK  refused %s: %s" % (name, text))
    print("all good")


if __name__ == "__main__":
    main()

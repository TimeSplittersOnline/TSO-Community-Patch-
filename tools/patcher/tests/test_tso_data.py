"""Quick check that tso_patch.dat loads (run before building the exe)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from pmd import tsopatch  # noqa: E402

p = tsopatch.TsoPatch()
print("tso_patch.dat: TSO Community Patch %s, %d known default.xbe files" % (p.version, len(p.inputs)))
for e in p.header["inputs"]:
    print("  %s (%s)" % (e["name"], e["md5"]))

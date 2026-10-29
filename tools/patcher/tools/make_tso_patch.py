#!/usr/bin/env python3
"""Make tso_patch.dat for a new TSO build (run once per delivered build).

  make_tso_patch.py <version> <TSO Community Patch.xbe> <out tso_patch.dat> "<name>=<input default.xbe>" ...

Each input is a default.xbe players may have (title update, MapMaker title update, disc ...).
"!<name>=<default.xbe>" only recognises that file (no delta is shipped for it) and shows NO_DELTA_WHY.
"@<builds folder>" adds every earlier TSO build in it (one "v<X.Y> <date>" folder per build, holding its .xbe), so
players can update an old TSO XBE straight to this one.
The patch is checked by applying it to every input before it is written.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pmd import tsopatch  # noqa: E402

NO_DELTA_WHY = ("Install the title update first, then pick the title update's default.xbe "
                "(TDATA\\45410066\\$u\\default.xbe).")


def old_builds(folder, out):
    """(name, xbe) for every earlier TSO build in folder, oldest first; the current build itself is skipped."""
    found = []
    for d in os.listdir(folder):
        m = re.match(r"v(\d+)\.(\d+)\b", d)
        xbes = [f for f in os.listdir(os.path.join(folder, d)) if f.lower().endswith(".xbe")] if m else []
        if len(xbes) != 1:
            continue
        with open(os.path.join(folder, d, xbes[0]), "rb") as f:
            data = f.read()
        if data != out:
            found.append(((int(m.group(1)), int(m.group(2))), "TSO Community Patch v%s.%s" % m.groups(), data))
    seen = set()
    builds = []
    for _, name, data in sorted(found):
        if tsopatch.md5(data) not in seen:  # a build identical to the one before it needs no entry of its own
            seen.add(tsopatch.md5(data))
            builds.append((name, data))
    return builds


def main():
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    version, out_xbe, dat = sys.argv[1:4]
    with open(out_xbe, "rb") as f:
        out = f.read()
    inputs, known = [], []
    for arg in sys.argv[4:]:
        if arg.startswith("@"):
            inputs += old_builds(arg[1:], out)
            continue
        name, _, p = arg.partition("=")
        with open(p, "rb") as f:
            data = f.read()
        if name.startswith("!"):
            known.append((name[1:], data, NO_DELTA_WHY))
        else:
            inputs.append((name, data))
    h = tsopatch.make_patch(version, out, inputs, dat, known)
    p = tsopatch.TsoPatch(dat)
    for name, data in inputs:
        assert p.apply(data) == out, name
    assert p.apply(out) == out
    for name, data, _ in known:
        assert p.identify(data)[0] == "known", name
    print("%s: %s, %d bytes" % (dat, version, os.path.getsize(dat)))
    for e in h["inputs"]:
        print("  %-40s %s  delta %d bytes  OK" % (e["name"], e["md5"], e["len"]))


if __name__ == "__main__":
    main()

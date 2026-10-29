"""Keep the patch data current: fetch the newest tso_patch.dat from the TSO Community Patch repository.

The exe carries the patch data of the build it was made with. A newer tso_patch.dat (downloaded here, or put
next to the exe by hand) is used instead when it is for a later TSO version, so one exe keeps working for
every new version. A download is only kept after it loads as valid patch data.
"""

import os
import re
import sys
import tempfile
import urllib.request

from . import tsopatch

URL = "https://raw.githubusercontent.com/TimeSplittersOnline/TSO-Community-Patch-/main/tools/patcher/tso_patch.dat"
MAX_SIZE = 64 * 1024 * 1024


def data_dir():
    base = os.environ.get("APPDATA") or os.path.expanduser("~")
    return os.path.join(base, "TSO Community Patcher")


def cached_path():
    return os.path.join(data_dir(), tsopatch.PATCH_NAME)


def version_key(version):
    """(5, 102) for "v5.102"; () when it can't be read."""
    m = re.match(r"v?(\d+)\.(\d+)", version or "")
    return (int(m.group(1)), int(m.group(2))) if m else ()


def candidates():
    """Every place patch data can come from: built in, next to the exe, downloaded."""
    out = [tsopatch.patch_path()]
    if getattr(sys, "frozen", False):
        out.append(os.path.join(os.path.dirname(sys.executable), tsopatch.PATCH_NAME))
    out.append(cached_path())
    return out


def best_patch():
    """The patch data for the latest TSO version found (raises PatchError when there is none)."""
    best, err = None, None
    for p in candidates():
        if not os.path.isfile(p):
            continue
        try:
            t = tsopatch.TsoPatch(p)
        except tsopatch.PatchError as e:  # a damaged or too-new file is skipped, not fatal
            err = e
            continue
        if best is None or version_key(t.version) > version_key(best.version):
            best = t
    if best is None:
        raise err or tsopatch.PatchError("The patch data (%s) is missing. Download the patcher again."
                                         % tsopatch.PATCH_NAME)
    return best


def pending_path():
    return os.path.join(data_dir(), "tso_patch.pending.dat")


def install_pending():
    """Start using the newer patch data that check() found."""
    os.replace(pending_path(), cached_path())


def check(current_version, timeout=20):
    """Download the newest patch data. When it is newer than current_version it is kept aside (not used until
    install_pending()) and its version returned, else None. Raises OSError when it can't be reached."""
    with urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "TSO Community Patcher"}),
                                timeout=timeout) as r:
        raw = r.read(MAX_SIZE + 1)
    if len(raw) > MAX_SIZE:
        raise OSError("The downloaded patch data is too big.")
    os.makedirs(data_dir(), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=data_dir(), suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(raw)
        t = tsopatch.TsoPatch(tmp)  # only valid patch data is kept
        if version_key(t.version) <= version_key(current_version):
            return None
        os.replace(tmp, pending_path())
        return t.version
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)

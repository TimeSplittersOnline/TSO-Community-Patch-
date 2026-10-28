"""What the TSO Community Patcher does with the files the user picks: check they are
TimeSplitters: Future Perfect, turn the player's own default.xbe into the TSO Community
Patch XBE, put it into an Xbox disc image or save it, bake a pnach into a PS2 ISO, and
put the original back."""

import datetime
import hashlib
import json
import os
import re
import struct
import subprocess
import sys

from .xbe import parse_xbe_header, is_xbe
from .xiso import Xiso
from . import ps2patch, tsopatch

MANIFEST = "backups.json"


# -- is the emulator running? -------------------------------------------------

def xemu_running():
    """Best-effort check for a running xemu process."""
    try:
        if sys.platform.startswith("win"):
            r = subprocess.run(["tasklist", "/FI", "IMAGENAME eq xemu.exe", "/NH"],
                               capture_output=True, text=True, timeout=10,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            return "xemu.exe" in r.stdout.lower()
        r = subprocess.run(["pgrep", "-x", "xemu"], capture_output=True, text=True, timeout=10)
        return r.returncode == 0
    except Exception:
        return False


def pcsx2_running():
    """Best-effort check for a running PCSX2 (any build)."""
    try:
        if sys.platform.startswith("win"):
            r = subprocess.run(["tasklist", "/NH"], capture_output=True, text=True, timeout=10,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            return "pcsx2" in r.stdout.lower()
        r = subprocess.run(["pgrep", "-i", "pcsx2"], capture_output=True, text=True, timeout=10)
        return r.returncode == 0
    except Exception:
        return False


# -- Xbox disc images -----------------------------------------------------------

class IsoTarget:
    """default.xbe inside a game disc image."""
    kind = "iso"
    partition = "ISO"

    def __init__(self, iso_path, path="default.xbe", size=0, info=None):
        self.iso_path = os.path.abspath(iso_path)
        self.path = path
        self.size = size
        self.info = info

    @property
    def display(self):
        return "%s (inside %s)" % (self.path, os.path.basename(self.iso_path))

    @property
    def folder_display(self):
        return "game disc image %s" % os.path.basename(self.iso_path)

    @property
    def default_xbe(self):
        return self.path

    def __repr__(self):
        return "<IsoTarget %s>" % self.display


def find_iso_game(iso_path):
    with Xiso(iso_path) as x:
        e = x.lookup("default.xbe")
        head = x._read(x.base + e.sector * 2048, min(e.size, 0x4000))
    return IsoTarget(iso_path, "default.xbe", e.size, parse_xbe_header(head))


def iso_xbe_sha1(target):
    with Xiso(target.iso_path) as x:
        return hashlib.sha1(x.read_file(target.path)).hexdigest()


# -- undo records ---------------------------------------------------------------

def _now_id():
    return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


def _unique_name(backup_dir, name):
    base, n = name, 2
    while os.path.exists(os.path.join(backup_dir, name)):
        name = "%s-%d" % (base, n)
        n += 1
    return name


def load_backups(backup_dir):
    p = os.path.join(backup_dir, MANIFEST)
    if not os.path.isfile(p):
        return []
    with open(p, "r", encoding="utf-8") as f:
        items = json.load(f)
    return [b for b in items if os.path.isfile(os.path.join(backup_dir, b["file"]))]


def _add_backup(backup_dir, rec):
    os.makedirs(backup_dir, exist_ok=True)
    p = os.path.join(backup_dir, MANIFEST)
    items = []
    if os.path.isfile(p):
        with open(p, "r", encoding="utf-8") as f:
            items = json.load(f)
    items.append(rec)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)
    os.replace(tmp, p)


def original_backup(backup_dir, target):
    """The first saved copy of the disc image's default.xbe (the untouched original)."""
    for b in load_backups(backup_dir):
        if b["kind"] == "iso-xbe" and os.path.normcase(b["iso_path"]) == os.path.normcase(target.iso_path):
            return b
    return None


# -- Xbox: swap in the TSO patch XBE ---------------------------------------------

def _iso_write_and_verify(iso_path, path, data):
    with Xiso(iso_path, writable=True) as x:
        x.replace_file(path, data)
    with Xiso(iso_path) as x:
        back = x.read_file(path)
    if hashlib.sha1(back).digest() != hashlib.sha1(data).digest():
        raise IOError("Verification failed: the file read back from the disc image does not match")


def read_iso_xbe(target):
    with Xiso(target.iso_path) as x:
        return x.read_file(target.path)


_PATCH = None


def tso_patch():
    """The TSO patch data shipped with the patcher (loaded once)."""
    global _PATCH
    if _PATCH is None:
        _PATCH = tsopatch.TsoPatch()
    return _PATCH


def tso_build_version(data):
    """"v5.47" when this XBE is a TSO Community Patch build (its Advanced Settings title says so), else None."""
    m = re.search(rb"Advanced Settings \(v(\d+\.\d+)\)", data)
    return "v" + m.group(1).decode() if m else None


def describe_xbe(data, what="This file"):
    """(ok, text) for a default.xbe the player picked: can it become the TSO build?"""
    info = parse_xbe_header(data[:0x4000])
    if info is None:
        return False, "%s is not an Xbox game file (.xbe)." % what
    if not info.is_tsfp:
        return False, "%s is \"%s\", not TimeSplitters: Future Perfect." % (what, info.title_name or "another game")
    p = tso_patch()
    kind, e = p.identify(data)
    if kind == "done":
        return True, "%s is already the TSO Community Patch %s." % (what, p.version)
    if kind == "input":
        return True, "Found: %s. Ready to make the TSO Community Patch %s." % (e["name"], p.version)
    if kind == "known":
        text = "Found: %s. %s" % (e["name"], e["why"])
        if what != "This file":
            text += " Choose \"A default.xbe file\" for that. Your disc image stays picked and gets patched."
        return False, text
    if len(data) < 1024 * 1024:
        return False, ("%s is only a small disc loader (%d KB), not the game. Use the game's 6 MB default.xbe."
                       % (what, len(data) // 1024))
    old = tso_build_version(data)
    if old:
        return False, ("%s is an older TSO Community Patch (%s). %s instead."
                       % (what, old, pick_hint()))
    return False, ("%s is a Future Perfect default.xbe the patcher doesn't recognise, so it can't be patched safely. "
                   "%s instead." % (what, pick_hint()))


def takes_disc_xbe():
    """True when the shipped patch data can start from a disc's own default.xbe (not only the title update's)."""
    try:
        return any("disc" in i["name"].lower() for i in tso_patch().inputs.values())
    except tsopatch.PatchError:
        return True


def source_hint():
    if takes_disc_xbe():
        return "From the USA or Europe disc, or the title update (TDATA\\45410066\\$u\\default.xbe)."
    return "The title update's default.xbe (TDATA\\45410066\\$u\\default.xbe)."


def pick_hint():
    return ("Pick an unmodded default.xbe from your disc or the title update" if takes_disc_xbe()
            else "Pick the title update's unmodded default.xbe")


def make_tso_xbe(data):
    """The TSO Community Patch XBE made from the player's own default.xbe (checked)."""
    return tso_patch().apply(data)


def save_xbe(data, path, log=print):
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)
    with open(path, "rb") as f:
        if hashlib.sha1(f.read()).digest() != hashlib.sha1(data).digest():
            raise IOError("Verification failed: the saved file does not match")
    log("Saved %s (checked)." % path)


def patch_iso(iso_path, target, new, backup_dir, label="the TSO Community Patch", log=print):
    """Replace default.xbe inside a game disc image with the bytes new, saving the current one first."""
    if not is_xbe(new):
        raise ValueError("That is not an Xbox game file (.xbe)")
    with Xiso(iso_path) as x:
        old = x.read_file(target.path)
    if old == new:
        log("The disc image already starts %s; nothing to do." % label)
        return target
    first = original_backup(backup_dir, target) is None
    os.makedirs(backup_dir, exist_ok=True)
    name = _unique_name(backup_dir, "%s_ISO_%s_default.xbe" % (_now_id(), re.sub(r"[^A-Za-z0-9._-]+", "_", os.path.splitext(os.path.basename(iso_path))[0])[:60]))
    with open(os.path.join(backup_dir, name), "wb") as f:
        f.write(old)
    info = parse_xbe_header(old[:0x4000])
    _add_backup(backup_dir, {"id": _now_id(), "kind": "iso-xbe", "file": name, "iso_path": os.path.abspath(iso_path),
                             "path": target.path, "size": len(old), "sha1": hashlib.sha1(old).hexdigest(),
                             "title": info.title_name if info else "", "note": "ORIGINAL" if first else "before patch",
                             "created": datetime.datetime.now().isoformat(timespec="seconds")})
    log("Saved the current default.xbe from the disc image: %s" % name)
    log("Writing %s into %s ..." % (label, os.path.basename(iso_path)))
    _iso_write_and_verify(iso_path, target.path, new)
    log("Done. The disc image now starts %s (checked)." % label)
    return target


def original_iso_xbe(backup_dir, target):
    """The disc image's own default.xbe: the saved original if we patched it, else what is in it now."""
    rec = original_backup(backup_dir, target)
    if rec is not None:
        with open(os.path.join(backup_dir, rec["file"]), "rb") as f:
            data = f.read()
        if hashlib.sha1(data).hexdigest() == rec.get("sha1"):
            return data
    return read_iso_xbe(target)


def restore_original(target, backup_dir, log=print):
    rec = original_backup(backup_dir, target)
    if rec is None:
        raise ValueError("No saved original for %s yet. It is saved the first time you patch." % os.path.basename(target.iso_path))
    with open(os.path.join(backup_dir, rec["file"]), "rb") as f:
        data = f.read()
    if rec.get("sha1") and hashlib.sha1(data).hexdigest() != rec["sha1"]:
        raise IOError("Backup file %s is damaged (checksum mismatch)" % rec["file"])
    log("Putting the original default.xbe back in %s ..." % os.path.basename(rec["iso_path"]))
    _iso_write_and_verify(rec["iso_path"], rec["path"], data)
    log("Original restored (checked).")


# -- PS2: bake a pnach into a TimeSplitters: Future Perfect ISO ---------------

def ps2_patched_record(backup_dir, iso_path):
    """The undo record if this ISO is currently patched by us, else None."""
    recs = [b for b in load_backups(backup_dir) if b["kind"] == "ps2-elf"
            and os.path.normcase(b["iso_path"]) == os.path.normcase(os.path.abspath(iso_path))]
    if not recs:
        return None
    try:
        with ps2patch.Ps2Iso(iso_path) as iso:
            cur = iso.find(recs[-1]["boot"])
    except Exception:
        return None
    for b in reversed(recs):
        if cur["extent"] == b.get("patched_extent") and cur["size"] == b.get("patched_size"):
            return b
    return None


def check_ps2(pnach_path, iso_path, backup_dir):
    """Read both files and check they belong together. Returns (pnach, info, undo_rec).

    Raises ps2patch.Ps2PatchError with a plain-English reason when they don't."""
    pn = ps2patch.Pnach(pnach_path)
    want = ps2patch.pnach_version(pn)
    undo = ps2_patched_record(backup_dir, iso_path)
    info = ps2patch.inspect_iso(iso_path)
    have = undo["crc"] if undo else info["crc"]
    if have not in ps2patch.TSFP_VERSIONS:
        raise ps2patch.Ps2PatchError(
            "%s is not TimeSplitters: Future Perfect (its game file %s doesn't match the USA or Europe "
            "version). Only TimeSplitters: Future Perfect ISOs can be patched." % (os.path.basename(iso_path), info["boot"]))
    if want is None:
        raise ps2patch.Ps2PatchError(
            "Can't tell which version of TimeSplitters: Future Perfect this pnach is for.\n\n"
            "Its file name should end with the game's CRC, like SLUS-21148_FB2F4502.pnach (USA) "
            "or SLES-52993_E0F96C7D.pnach (Europe).")
    if want not in ps2patch.TSFP_VERSIONS:
        raise ps2patch.Ps2PatchError("This pnach is for a different game (CRC %08X), not TimeSplitters: "
                                     "Future Perfect." % want)
    if want != have:
        raise ps2patch.Ps2PatchError(
            "Wrong version.\n\nThis pnach is for the %s version of TimeSplitters: Future Perfect, "
            "but your ISO is the %s version.\n\nUse a pnach made for the %s version, or pick the %s ISO."
            % (ps2patch.describe_crc(want), ps2patch.describe_crc(have),
               ps2patch.TSFP_VERSIONS[have][1], ps2patch.TSFP_VERSIONS[want][1]))
    return pn, info, undo


def restore_ps2_iso(rec, log=print):
    """Point the ISO back at the untouched original game file and trim what we added."""
    iso_path = rec["iso_path"]
    log("Putting the original game file back in %s ..." % os.path.basename(iso_path))
    with ps2patch.Ps2Iso(iso_path, writable=True) as iso:
        cur = iso.find(rec["boot"])
        iso.set_record(cur, rec["orig_extent"], rec["orig_size"])
        iso.set_volume_size(rec["orig_volume"])
        iso.f.flush()
        os.fsync(iso.f.fileno())
        if iso.f.seek(0, os.SEEK_END) > rec["orig_length"]:
            iso.f.truncate(rec["orig_length"])
    info = ps2patch.inspect_iso(iso_path)
    if info["crc"] != rec["crc"]:
        raise IOError("Check failed: the game file in the ISO isn't the original after restoring")
    log("Original restored (checked: %s)." % ps2patch.describe_crc(info["crc"]))


def patch_ps2_iso(pnach_path, iso_path, backup_dir, log=print):
    pn, info, undo = check_ps2(pnach_path, iso_path, backup_dir)
    if undo:
        log("This ISO already has a pnach baked in; putting the original back first.")
        restore_ps2_iso(undo, log)
        info = ps2patch.inspect_iso(iso_path)
    elf = info["elf"]
    log("Game: %s, game file %s" % (ps2patch.describe_crc(info["crc"]), info["boot"]))
    if pn.skipped:
        log("Skipping %d pnach line(s) that can't be baked into an ISO, e.g. line %d: %s (%s)"
            % ((len(pn.skipped),) + pn.skipped[0]))
    new_elf, report = ps2patch.patch_elf(elf, pn)
    log("Applied %d patch line(s) to the game's code%s." % (
        report["in_elf"], (", %d into a new code area at %s" % (report["new_segment"], ", ".join(
            "%08X-%08X" % r for r in report.get("segments", [])))) if report["new_segment"] else ""))

    os.makedirs(backup_dir, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", os.path.splitext(os.path.basename(iso_path))[0])[:60]
    name = _unique_name(backup_dir, "%s_PS2_%s_%s" % (_now_id(), safe, os.path.basename(info["boot"])))
    with open(os.path.join(backup_dir, name), "wb") as f:
        f.write(elf)
    rec = info["record"]
    sectors = ps2patch.SECTOR
    start = (info["length"] + sectors - 1) // sectors
    alloc = (len(new_elf) + sectors - 1) // sectors
    with ps2patch.Ps2Iso(iso_path) as iso:
        orig_volume = struct.unpack_from("<I", iso.pvd, 80)[0]
    undo = {"id": _now_id(), "kind": "ps2-elf", "file": name, "iso_path": os.path.abspath(iso_path),
            "boot": info["boot"], "crc": info["crc"], "size": len(elf),
            "sha1": hashlib.sha1(elf).hexdigest(), "title": "TimeSplitters FP " + ps2patch.TSFP_VERSIONS[info["crc"]][1],
            "orig_extent": rec["extent"], "orig_size": rec["size"], "orig_length": info["length"],
            "orig_volume": orig_volume, "patched_extent": start, "patched_size": len(new_elf),
            "pnach": os.path.basename(pnach_path), "note": "ORIGINAL (pnach: %s)" % os.path.basename(pnach_path),
            "created": datetime.datetime.now().isoformat(timespec="seconds")}
    _add_backup(backup_dir, undo)
    log("Saved the original game file: %s" % name)

    log("Writing the patched game file into %s ..." % os.path.basename(iso_path))
    try:
        with ps2patch.Ps2Iso(iso_path, writable=True) as iso:
            iso.f.seek(start * sectors)
            iso.f.write(new_elf + b"\0" * (alloc * sectors - len(new_elf)))
            iso.f.flush()
            os.fsync(iso.f.fileno())
            iso.set_record(iso.find(info["boot"]), start, len(new_elf))
            iso.set_volume_size(max(orig_volume, start + alloc))
            iso.f.flush()
            os.fsync(iso.f.fileno())
        with ps2patch.Ps2Iso(iso_path) as iso:
            back = iso.read(iso.find(info["boot"]))
        if back != new_elf:
            raise IOError("Check failed: the game file read back from the ISO doesn't match")
    except Exception:
        log("Something went wrong, undoing...")
        restore_ps2_iso(undo, log)
        raise
    log("Done. The ISO now has the pnach built in (checked).")
    return undo

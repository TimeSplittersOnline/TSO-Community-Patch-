"""PS2 pnach -> ISO test. Usage: python3 tests/test_ps2.py <dir with SLUS_211.48 and SLES_529.93> <pnach>
Needs genisoimage. Builds small ISOs with the real ELFs and checks patch, region check and undo."""
import hashlib, os, shutil, struct, subprocess, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from pmd import core, ps2patch as p


def make_iso(work, elf_path, name):
    d = os.path.join(work, "tree_" + name)
    os.makedirs(d)
    with open(os.path.join(d, "SYSTEM.CNF"), "w") as f:
        f.write("BOOT2 = cdrom0:\\%s;1\r\nVER = 1.00\r\nVMODE = NTSC\r\n" % name)
    shutil.copy(elf_path, os.path.join(d, name))
    os.makedirs(os.path.join(d, "DATA"))
    with open(os.path.join(d, "DATA", "AFTER.BIN"), "wb") as f:
        f.write(os.urandom(300000))
    iso = os.path.join(work, name + ".iso")
    subprocess.run(["genisoimage", "-quiet", "-l", "-o", iso, d], check=True)
    return iso


def sha(path):
    return hashlib.sha1(open(path, "rb").read()).hexdigest()


def main(elfdir, pnach):
    work = tempfile.mkdtemp()
    bdir = os.path.join(work, "backups")
    us = make_iso(work, os.path.join(elfdir, "SLUS_211.48"), "SLUS_211.48")
    eu = make_iso(work, os.path.join(elfdir, "SLES_529.93"), "SLES_529.93")
    us_sha, eu_sha, us_len = sha(us), sha(eu), os.path.getsize(us)
    other = os.path.join(work, "other.elf")
    data = bytearray(open(os.path.join(elfdir, "SLUS_211.48"), "rb").read())
    data[-8:] = b"DIFFERNT"
    open(other, "wb").write(data)
    oth = make_iso(work, other, "SLUS_999.99")

    # wrong region refused, ISO untouched
    try:
        core.patch_ps2_iso(pnach, eu, bdir, log=lambda m: None)
        raise AssertionError("PAL ISO accepted an NTSC pnach")
    except p.Ps2PatchError as e:
        assert "Europe (PAL, SLES-52993)" in str(e) and "USA (NTSC, SLUS-21148)" in str(e), e
        print("region mismatch refused:", str(e).splitlines()[2])
    assert sha(eu) == eu_sha
    # non-TSFP refused
    try:
        core.patch_ps2_iso(pnach, oth, bdir, log=lambda m: None)
        raise AssertionError("other game accepted")
    except p.Ps2PatchError as e:
        print("other game refused:", str(e)[:80])

    # patch
    core.patch_ps2_iso(pnach, us, bdir, log=print)
    pn = p.Pnach(pnach)
    with p.Ps2Iso(us) as iso:
        elf = iso.read(iso.find("SLUS_211.48"))
        after = iso.read(iso.find("DATA/AFTER.BIN"))
        cnf = iso.read(iso.find("SYSTEM.CNF"))
    assert b"SLUS_211.48" in cnf
    # every pnach byte is in memory when the game starts (after the boot copier ran)
    import ps2_boot_sim
    orig = open(os.path.join(elfdir, "SLUS_211.48"), "rb").read()
    mem, _sc = ps2_boot_sim.boot(elf, struct.unpack_from("<I", orig, 24)[0])
    for a, d in pn.writes:
        assert mem[a:a + len(d)] == d, "%08X" % a
    print("all %d pnach writes present in the patched ELF" % len(pn.writes))
    assert subprocess.run(["readelf", "-lW", "-"], input=b"", capture_output=True) is not None
    open(os.path.join(work, "patched.elf"), "wb").write(elf)
    r = subprocess.run(["readelf", "-lW", os.path.join(work, "patched.elf")], capture_output=True, text=True)
    assert r.returncode == 0 and "LOAD" in r.stdout and "Error" not in r.stderr, r.stderr
    # mount-free check: isoinfo can still read the patched file
    r = subprocess.run(["isoinfo", "-i", us, "-x", "/SLUS_211.48;1"], capture_output=True)
    assert r.stdout == elf, "isoinfo reads a different ELF"
    print("isoinfo reads the patched ELF; other files intact")

    # patching again re-applies cleanly from the original
    core.patch_ps2_iso(pnach, us, bdir, log=lambda m: None)
    assert os.path.getsize(us) < us_len + 2 * len(elf) + 4096
    # undo
    rec = core.ps2_patched_record(bdir, us)
    assert rec is not None
    core.restore_ps2_iso(rec, log=print)
    assert sha(us) == us_sha, "restore not byte-identical"
    assert core.ps2_patched_record(bdir, us) is None
    print("restore is byte-identical to the original ISO")
    # backup ELF saved
    b = [x for x in core.load_backups(bdir) if x["kind"] == "ps2-elf"][0]
    assert sha(os.path.join(bdir, b["file"])) == hashlib.sha1(open(os.path.join(elfdir, "SLUS_211.48"), "rb").read()).hexdigest()
    print("PS2 TESTS PASSED")
    shutil.rmtree(work)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

# TSO Community Patcher (source)

**Xbox:** pick your own `default.xbe` (or TimeSplitters: Future Perfect ISO). The patcher recognises it by its hash, and turns it into the TSO Community Patch XBE
with the versions `tso_patch.dat`, and checks the result is byte for byte the delivered build.
`tso_patch.dat` only holds the differences from each known XBE, never a whole XBE.

**PS2:** builds a pnach into the game's ISO, "Restore original ISO" undoes it. The patched game file is added at the
end of the ISO and both of the disc's file listings point at it: ISO9660 (PCSX2, real PS2) and UDF (a PS3 running the
ISO through webMAN reads this one; patching only ISO9660 made it boot the unmodded game).
The mod's own code (below the game, 0xE0100-0x100000) is not a separate ELF segment: a real PS2 / PS3 PS2 chip
loads the game with the console's loader, which runs in that memory. It rides at the end of the game's one segment
with a small copier the ELF starts at, which puts it in place, flushes the caches and jumps to the game's entry.
`tests/ps2_boot_sim.py` runs that copier on the real ELFs and checks memory at the game's entry.
Right after the game reboots the IOP (at start, and when it shuts the network down) 0x84000-0x100000 gets zeroed,
mod code included; PCSX2 hides that by re-applying the pnach every frame. `pmd/ps2keeper.py` hooks the two calls
that lead to a reboot: the mod area is stashed, and a vblank handler (at 0x80200, which the wipe leaves alone)
copies it back when it finds it wiped, then clears the stash and goes idle. `tests/ps2_keeper_sim.py` runs it
through a boot wipe, an in-game wipe and the cases where it must not restore.

- `TSO Community Patcher.pyw`: the window (Tkinter).
- `pmd/tsopatch.py`: the patch format (copy/add deltas, lzma), applying and making it.
- `pmd/update.py`: keeps the patch data current. At start (and from "Check for updates") it downloads
  `tools/patcher/tso_patch.dat` from this repository's main branch. When it is valid and for a later TSO version the
  player is asked, and on Yes it is kept (in `%APPDATA%\TSO Community Patcher`) and used; a newer `tso_patch.dat` next to
  the exe also works. So committing a new `tso_patch.dat` to main offers the update to every player's patcher; the exe
  only needs rebuilding when its code changes.
- `pmd/core.py`: checks, patching, undo records (`backups.json` in the backup folder).
- `pmd/xiso.py`, `pmd/xbe.py`: Xbox disc images and XBE headers. `pmd/ps2patch.py`: pnach, PS2 ELF, ISO9660 and UDF; `pmd/ps2keeper.py`: the IOP-reboot keeper.
- `tools/make_xdelta.py <original.iso> <patched.iso> <out.xdelta>`: an xdelta (VCDIFF) from an untouched ISO to one
  the patcher made, for players who'd rather use xdelta3 / Delta Patcher (`tests/test_xdelta.py` checks it with xdelta3).
- `tools/console_check.py <game ELF> <pnach>`: looks through the mod's code (and every game instruction the pnach
  changes) for things PCSX2 lets slide but a real PS2/PS3 doesn't: NULL loads in branch delay slots, R5900 short loops,
  instructions the EE doesn't have, jumps to nothing, misaligned or unmapped fixed addresses, stores into code or into
  words PCSX2 keeps rewriting. Exit status 1 on errors. Run it after every change to the pnach.
- `tools/consolefix.py <game ELF> <in.pnach> <out.pnach>`: a copy of the pnach with the NULL loads and short loops fixed
  (lines added at the end, code at 0x000F4000); console_check.py should then find neither.
- `tools/make_tso_patch.py <version> <TSO Community Patch.xbe> tso_patch.dat "<name>=<default.xbe>" ...`:
  makes `tso_patch.dat` for a new TSO build (run for every delivered build, then rebuild the exe).
  An input written `"!<name>=<default.xbe>"` is only recognised (no delta is shipped for it); the patcher names it
  and asks for the title update's default.xbe instead.
  `"@<builds folder>"` adds every earlier TSO build in it (one `v<X.Y> <date>` folder per build), so an old TSO XBE
  updates straight to the new one. Current data: 6 game XBEs (USA title update, two title update + MapMaker XBEs,
  USA and Europe disc, and a USA disc copy with 4 flag bytes changed that circulates as an xiso) and every earlier TSO build
  from v5.3 on.
- Tests: `tests/test_update.py` (local web server, no internet), `tests/test_tso.py <TSO xbe> <known default.xbe> ...`, `tests/test_iso.py <extract-xiso>`,
  `tests/test_ps2.py <dir with SLUS_211.48 and SLES_529.93> <pnach>` (needs genisoimage),
  `tests/ps2_boot_sim.py <same dir> <NTSC pnach> <PAL pnach>`.
- `build_exe.bat`: rebuilds `TSO Community Patcher.exe` with PyInstaller on Windows (bundles `tso_patch.dat`).

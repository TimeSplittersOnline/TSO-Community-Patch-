# TSO Community Patcher (source)

**Xbox:** pick your own `default.xbe` (or TimeSplitters: Future Perfect ISO). The patcher recognises it by its hash, and turns it into the TSO Community Patch XBE
with the versions `tso_patch.dat`, and checks the result is byte for byte the delivered build.
`tso_patch.dat` only holds the differences from each known XBE, never a whole XBE.

**PS2:** builds a pnach into the game's ISO, "Put the original back" undoes it.

- `TSO Community Patcher.pyw`: the window (Tkinter).
- `pmd/tsopatch.py`: the patch format (copy/add deltas, lzma), applying and making it.
- `pmd/update.py`: keeps the patch data current. At start (and from "Check for updates") it downloads
  `tools/patcher/tso_patch.dat` from this repository's main branch and keeps it (in `%APPDATA%\TSO Community Patcher`)
  when it is valid and for a later TSO version; a newer `tso_patch.dat` next to the exe also works. So committing a new
  `tso_patch.dat` to main updates every player's patcher; the exe only needs rebuilding when its code changes.
- `pmd/core.py`: checks, patching, undo records (`backups.json` in the backup folder).
- `pmd/xiso.py`, `pmd/xbe.py`: Xbox disc images and XBE headers. `pmd/ps2patch.py`: pnach, PS2 ELF and ISO9660.
- `tools/make_tso_patch.py <version> <TSO Community Patch.xbe> tso_patch.dat "<name>=<default.xbe>" ...`:
  makes `tso_patch.dat` for a new TSO build (run for every delivered build, then rebuild the exe).
  An input written `"!<name>=<default.xbe>"` is only recognised (no delta is shipped for it); the patcher names it
  and asks for the title update's default.xbe instead.
  `"@<builds folder>"` adds every earlier TSO build in it (one `v<X.Y> <date>` folder per build), so an old TSO XBE
  updates straight to the new one. Current data: 6 game XBEs (USA title update, two title update + MapMaker XBEs,
  USA and Europe disc, and a USA disc copy with 4 flag bytes changed that circulates as an xiso) and every earlier TSO build
  from v5.3 on.
- Tests: `tests/test_update.py` (local web server, no internet), `tests/test_tso.py <TSO xbe> <known default.xbe> ...`, `tests/test_iso.py <extract-xiso>`,
  `tests/test_ps2.py <dir with SLUS_211.48 and SLES_529.93> <pnach>` (needs genisoimage).
- `build_exe.bat`: rebuilds `TSO Community Patcher.exe` with PyInstaller on Windows (bundles `tso_patch.dat`).

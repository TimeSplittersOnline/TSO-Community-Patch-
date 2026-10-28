# TSO Community Patcher (source)

Formerly PatchmeDaddy. Players only need `TSO Community Patcher.exe` from the repository's Releases page. This folder is the source it is built from.

It works only on files the user picks (it never searches the PC), for TimeSplitters: Future Perfect and nothing else.

**Xbox:** the player picks their own `default.xbe` (the title update's `TDATA\45410066\$u\default.xbe`, a disc's,
or the one inside their disc image). The patcher recognises it by its hash, turns it into the TSO Community Patch XBE
with `tso_patch.dat`, and checks the result is byte for byte the delivered build. Any file it doesn't know is refused.
The result is either put into the disc image as `default.xbe` ("Put the original back" undoes it) or saved as a file.
`tso_patch.dat` only holds the differences from each known XBE, never a whole XBE, so the TSO XBE itself is never shared.

**PS2:** builds a pnach into the game's ISO (the pnach's version must match the ISO's). "Put the original back" undoes it.

- `TSO Community Patcher.pyw`: the window (Tkinter).
- `pmd/tsopatch.py`: the patch format (copy/add deltas, lzma), applying and making it.
- `pmd/core.py`: checks, patching, undo records (`backups.json` in the backup folder).
- `pmd/xiso.py`, `pmd/xbe.py`: Xbox disc images and XBE headers. `pmd/ps2patch.py`: pnach, PS2 ELF and ISO9660.
- `tools/make_tso_patch.py <version> <TSO Community Patch.xbe> tso_patch.dat "<name>=<default.xbe>" ...`:
  makes `tso_patch.dat` for a new TSO build (run for every delivered build, then rebuild the exe).
  An input written `"!<name>=<default.xbe>"` is only recognised (no delta is shipped for it); the patcher names it
  and asks for the title update's default.xbe instead.
- Tests: `tests/test_tso.py <TSO xbe> <known default.xbe> ...`, `tests/test_iso.py <extract-xiso>`,
  `tests/test_ps2.py <dir with SLUS_211.48 and SLES_529.93> <pnach>` (needs genisoimage).
- `build_exe.bat`: rebuilds `TSO Community Patcher.exe` with PyInstaller on Windows (bundles `tso_patch.dat`).

Known XBEs in the current `tso_patch.dat`: USA title update (MD5 f0de376970932db0812bb07909189f5d), devildwarf's
title update + MapMaker patch (b45afee1c66107dcb1fa4397bbaa02b0), Jake's title update + MapMaker XBE
(d2fc3bed99456864a96fff179d5336d1), Europe disc without the title update (a048c094f604559e870fe14f33f784b3,
6270976 bytes, title id 45410066, region flag 4, disc version 2). USA disc without the title update (4aeb1a1fded674575759b681f2125966, same size; it differs from the
Europe disc XBE only in 532 header/certificate bytes).
A disc XBE is a much older build than the title update, so its delta is large (about 1 MB of the patch data).
On a real disc image the TSO XBE is bigger than the disc's default.xbe slot, so `xiso.replace_file` writes it at
the end of the image and points the directory entry there.

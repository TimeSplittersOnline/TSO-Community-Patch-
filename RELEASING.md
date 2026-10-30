# Releasing a new version

Every new version updates the whole [`patch`](patch) folder in one commit: the pnach files **and** all five xdelta patches, PS2 and Xbox together. A version whose xdeltas are missing or left at an older version is not released. Xbox fixes reach players only through the xdeltas (no XBE is ever published), so a release that only swaps the pnach files leaves every Xbox player on the old version.

| Path | What | Made from |
|---|---|---|
| `patch/VERSION` | the version, e.g. `v5.107` | |
| `patch/ps2/SLUS-21148_FB2F4502.pnach` | PS2 NTSC pnach | the delivered pnach, console-checked (consolefix'd when needed) |
| `patch/ps2/SLES-52993_E0F96C7D.pnach` | PS2 PAL pnach | the same |
| `patch/ps2/TimeSplitters - Future Perfect (USA) - TSO Community Patch.xdelta` | PS2 USA disc image | the untouched USA ISO, with the NTSC pnach above baked in |
| `patch/ps2/TimeSplitters - Future Perfect (Europe) - TSO Community Patch.xdelta` | PS2 Europe disc image | the untouched Europe ISO, with the PAL pnach above baked in |
| `patch/xbox/default.xbe (USA) - TSO Community Patch.xdelta` | Xbox XBE | stock USA disc `default.xbe` to the delivered `TSO Community Patch.xbe` |
| `patch/xbox/default.xbe (Europe) - TSO Community Patch.xdelta` | Xbox XBE | stock Europe disc `default.xbe` to the same XBE |
| `patch/xbox/TimeSplitters - Future Perfect [xiso] - TSO Community Patch.xdelta` | Xbox xiso | stock USA or Europe xiso with that XBE put in (one file fits both) |

The base files (and the checksums in the [README](README.md)) stay the same from version to version; only the patches change. The file names stay the same too, so links to `patch/` always give the newest version.

## Steps

1. **Build the files.** The game images are only on the maintainer's PC, so this runs there (Python 3.13):

   ```
   cd "C:\Users\jakep\Desktop\TimeSplitters\TSO Community Patch\release"
   python make_release.py v5.107
   ```

   It takes the delivered build from `TSFP Mod Project\builds\v5.107 <date>\` (both pnach files and `TSO Community Patch.xbe`) and writes all of the files above to `TSO Community Patch\patch\`, plus `MANIFEST.txt` with each file's size and MD5. It refuses to write anything when the pnach files and the XBE don't show the same version, when a base file isn't the untouched original, when a pnach still fails the PS2/PS3 console check, or when an xdelta doesn't decode back to its target exactly. `--check` runs only the quick checks (no disc images).

2. **Commit them.** Replace `patch/ps2/*`, `patch/xbox/*` and `patch/VERSION` with the files from `TSO Community Patch\patch\` (leave `MANIFEST.txt` out), and check each file's MD5 against `MANIFEST.txt`. Put the version's `CHANGELOG.md` entry and its `docs/versions` page in the same commit.

3. **Link the files.** A version page's "Files for this version" link, and its row in [docs/versions](docs/versions/README.md), point at `tree/<commit>/patch` (versions up to v5.106 point at `build`, which is what their commits hold).

4. Open a pull request. The maintainer merges it.

[`tools/make_xdelta.py`](tools/make_xdelta.py) is the XBE xdelta maker the release script uses. Applying any patch is described in the [README](README.md#install).

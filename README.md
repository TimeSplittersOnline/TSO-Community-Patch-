# TSO Community Patch

## Install

You need your own copy of the game. This repository contains no game files.

### PS2 (PCSX2)
1. Download the pnach for your region from the [`build`](build) folder:
   - NTSC (USA): `SLUS-21148_FB2F4502.pnach`
   - PAL (Europe): `SLES-52993_E0F96C7D.pnach`
2. Put it in PCSX2's `patches` folder, enable patches, and start the game. After updating, use Tools › Reload Cheats/Patches and start a new match (or restart the game).

### Xbox (xemu or a modded console)
Patch your own copy with an xdelta tool (xdelta UI, Delta Patcher, or `xdelta3 -d -s <original> <patch> <output>`). The files are in [`build/xbox`](build/xbox). The title update isn't needed: the patches include it.

**Whole xiso (simplest for xemu).** If your xiso matches one of these exactly, patch the image in one step:

| Patch | Your xiso must be |
|---|---|
| `TimeSplitters - Future Perfect (USA) [xiso] - TSO Community Patch.xdelta` | 4,047,372,288 bytes, CRC32 `36D57998`, MD5 `a5402ef4638fee51f7e0c89bfbfb8503`, SHA-1 `99ec856bd8d0639213b046e26d210d3822c54990` |
| `TimeSplitters - Future Perfect (Europe) [xiso] - TSO Community Patch.xdelta` | 4,047,372,288 bytes, CRC32 `611D7473`, MD5 `d4ca6163652a0da3bebb655a311d0905`, SHA-1 `5ab3b603d42232553317a70e19cabb4c291632be` |

**Just the XBE (works with any copy of your region).** Take `default.xbe` out of your disc image (e.g. with extract-xiso), patch it, and put the patched file back as `default.xbe` (or run it from an Xbox hard drive):

| Patch | Your `default.xbe` must be |
|---|---|
| `default.xbe (USA) - TSO Community Patch.xdelta` | 6,270,976 bytes, CRC32 `05BF2120`, MD5 `4aeb1a1fded674575759b681f2125966` |
| `default.xbe (Europe) - TSO Community Patch.xdelta` | 6,270,976 bytes, CRC32 `657C98FE`, MD5 `a048c094f604559e870fe14f33f784b3` |

Check your file's MD5 before patching: an xdelta doesn't check its base, so a different file (another dump, a title update XBE, an already modded XBE) gives a broken result instead of an error. Patching never changes your original; always save the output under a new name.

## Resources 

- [CHANGELOG.md](CHANGELOG.md): every version, newest first, with the date and what changes were made.
- [docs/versions](docs/versions/README.md): one page per version (v5.3 on) listing every change to the game's code and data compared with the build before it.
- [docs/changes](docs/changes/README.md): the current build's complete list of changes to the original files, with the original and new bytes or instructions.
- [docs/functions.md](docs/functions.md): the game routines and data the mod uses.

The [`build`](build) folder always holds the current version's TSO Community Patch files: the two pnach files (their names must stay as they are; PCSX2 finds a game's patch by them) and the Xbox xdelta patches in [`build/xbox`](build/xbox). Every earlier version (v5.3 on) is its own commit; the [version list](docs/versions/README.md) links each one's changes and files.

## Features

- Advanced settings menu with additional hosting options
  
   - New host settings catch-up, random weapons, spawn behaviour, respawn delay, players drop gun, disable unarmed, mercy rules, and player health added.
   - Advanced team options like disabling specific teams, unique respawn delays for each team, team spawn options. 
   - Unique modifiers for all modes.
   - Time Grenades & TNT are available.
   - Alternate versions of the: Scifi Handgun, KSMG, Minigun, Mag Charger that start in secondary fire.
   - Teamplay available on Thief, Shrink, Gladiator, Elimination, Vampire, and Bagtag.




- New game modes & changes to existing modes
  - Four teams available on Thief, Zones, Shrink, Gladiator, Elimination, Vampire, Bagtag, Regeneration, and Leech.
  - Flame Tag has been restored and fixed.
  - Siberia available on Virus.
  - Spectating and free-cam options for dead players on Elimination and Vampire.
  - Yellow and green zones are coloured appropriately rather than being blue.




- Changes to mapmaker memory limits
   - Near unlimited Mapmaker tile and item memory.
   - Split-screen co-op mapmaker story.
   - Character select for mapmaker story levels.
   - no limit for previously limited mapmaker items like bags & zones.


- Bug fixes and compatability
  - Fixes for players without the title update, including fixes for: loading into lobbies early when the host changed music settings, only hearing Scotland the brave for on-disc maps when "ban small characters is enabled.

    **The client reads settings by menu order, but becaause the host has more settings, clients would misread the settings the host was sending. "Ban small characters" was now the music select, and since it could only be off/on, only music track 0 and 1 could be selected on consoles without the title update. 0 is recommended, which only works with the setting off, and 1 is scotland the brave (small characters on). Clients would load into the lobby early because anything other than the recomended music setting would activate the "host is in match" flag for consoles without the title update** 
  - All players wait for host before spawning (no more xbox one loading advantage).
  - The final 15 seconds of zones now count over LAN and online matches.
  - On PS2, mapmaker desync is fixed.


    **Clients would check their own saved custom weapon set choice instead of the hosts when playing mapmaker, the clients would either have no weapons or it would show the wrong ones. All map items are ordered by number and the host would have differing orders for each of them if the client had empty slots in their own custom set, as one console is counting weapons and the other is not. If the host says "pickup 20 was taken", the client will misread it as a different item and it won't update correctly, which is why zones would not change colour, why guns would not spawn, etc.** 



- Mid-game menus and options
  - player management tab in host pause menu that allows team changing and kicking for all players.
  -  Return to lobby feature (Xbox only).

## Undoing a change

Each change in [docs/changes](docs/changes/README.md) lists the original next to the new. PS2 lines at address `00100000` and above change the game's own code; put back the original line. Xbox changes list the original bytes at each file offset; write them back and fix the XBE checksums (`tools/fix_xbe_checksums.py`).

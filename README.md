# TSO Community Patch

## Install

You need your own copy of the game. This repository contains no game files.

### PS2 (PCSX2)
1. Download the pnach for your region from the [`build`](build) folder:
   - NTSC (USA): `SLUS-21148_FB2F4502.pnach`
   - PAL (Europe): `SLES-52993_E0F96C7D.pnach`
2. Put it in PCSX2's `patches` folder, enable patches, and start the game. After updating, use Tools › Reload Cheats/Patches and start a new match (or restart the game).

### Xbox (xemu or a modded console)
1. Take the title update's `default.xbe` (`TDATA\45410066\$u\default.xbe`, 6,344,704 bytes, CRC32 `BDC3CEB9`, MD5 `f0de376970932db0812bb07909189f5d`).
2. Apply [`build/TSO Community Patch.bps`](<build/TSO Community Patch.bps>) to it with any BPS patcher (Floating IPS, beat, etc). If you use devildwarf's MapMaker-patched title update XBE instead (CRC32 `0A0DA47C`, MD5 `b45afee1c66107dcb1fa4397bbaa02b0`), apply [`build/TSO Community Patch (MapMaker XBE).bps`](<build/TSO Community Patch (MapMaker XBE).bps>). Both give the same XBE.
3. Use the patched XBE in place of the original.

A BPS patch only works on the exact file it was made from; a patcher that reports a checksum or size mismatch was given a different XBE (for example the disc's own `default.xbe`, which has no title update).

## Resources 

- [CHANGELOG.md](CHANGELOG.md): every version, newest first, with the date and what changes were made.
- [docs/versions](docs/versions/README.md): one page per version (v5.3 on) listing every change to the game's code and data compared with the build before it.
- [docs/changes](docs/changes/README.md): the current build's complete list of changes to the original files, with the original and new bytes or instructions.
- [docs/functions.md](docs/functions.md): the game routines and data the mod uses.

The [`build`](build) folder always holds the current version's TSO Community Patch files: the two pnach files (their names must stay as they are; PCSX2 finds a game's patch by them) and the two Xbox BPS patches (`TSO Community Patch.bps` for the title update XBE, `TSO Community Patch (MapMaker XBE).bps` for devildwarf's MapMaker XBE). Every earlier version (v5.3 on) is its own commit; the [version list](docs/versions/README.md) links each one's changes and files.

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

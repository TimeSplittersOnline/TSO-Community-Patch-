# TSO Community Patch

## Install

You need your own copy of the game. This repository contains no game files.

### PS2 (PCSX2)
1. Download the pnach for your region from the [`build`](build) folder:
   - NTSC (USA): `SLUS-21148_FB2F4502.pnach`
   - PAL (Europe): `SLES-52993_E0F96C7D.pnach`
2. Put it in PCSX2's `patches` folder, enable patches, and start the game. After updating, use Tools › Reload Cheats/Patches and start a new match (or restart the game).

### Xbox (xemu or a modded console)
The Xbox mod is shipped as a patch for your own game executable.
1. Take `default.xbe` from your copy of the game **with the title update** (the patch only applies to that exact file: size 6,344,704 bytes, MD5 `d2fc3bed99456864a96fff179d5336d1`).
2. Apply [`build/TSO Community Patch.bps`](<build/TSO Community Patch.bps>) with any BPS patcher (Floating IPS, beat, etc).
3. Use the patched XBE in place of the original (keep a backup of the original).

## Resources 

- [CHANGELOG.md](CHANGELOG.md): every version, newest first, with the date and what changed.
- [docs/versions](docs/versions/README.md): one page per version (v5.3 on) listing every change to the game's code and data compared with the build before it: what was there, what it became and why.
- [docs/changes](docs/changes/README.md): the current build's complete list of changes to the original files, by feature, with the original and new bytes or instructions.
- [docs/functions.md](docs/functions.md): the game routines and data the mod uses.
- [docs/site](docs/site/index.html): the searchable change register as a web page (also published with GitHub Pages).

The [`build`](build) folder always holds the current version's TSO Community Patch files: the two pnach files (their names must stay as they are; PCSX2 finds a game's patch by them) and `TSO Community Patch.bps` for Xbox. Every earlier version (v5.3 on) is its own commit; the [version list](docs/versions/README.md) links each one's changes and files.

## Features

- Advanced settings menu.
- New host settings catch-up, random weapons, spawn behaviour, respawn delay, players drop gun, disable unarmed, mercy rules, and player health added.
- Advanced team options like disabling specific teams, unique respawn delays for each team, team spawn options. 
- Unique modifiers for all modes.
- Teamplay available on Thief, Shrink, Gladiator, Elimination, Vampire, and Bagtag.
- Four teams available on Thief, Zones, Shrink, Gladiator, Elimination, Vampire, Bagtag, Regeneration, and Leech.
- Flame Tag has been restored and fixed.
- Additional modes: Gun Game, Showdown, Gold Rush, Team VIP, and King of the Hill have been implemented.
- Siberia available on Virus.
- Modifiers available for all modes.
- Fixes for players without the title update, including fixes for: loading into lobbies early when the host changed music settings, only hearing Scotland the brave for on-disc maps when "ban small characters is enabled.
- All players wait for host before spawning (no more xbox one loading advantage).
- The final 15 seconds of zones now count over LAN and online matches.
- Unlimited Mapmaker memory.
- no limit for previously limited mapmaker items like bags & zones.
- Alternate versions of the: Scifi Handgun, KSMG, Minigun, Mag Charger that start in secondary fire.
- Time Grenades & TNT are available.
- Spectating and free-cam options for dead players on Elimination and Vampire.
- Split-screen co-op mapmaker story.
- Character select for mapmaker story levels.
- player management tab in host pause menu that allows team changing and kicking for all players.
- Yellow and green zones are coloured appropriately rather than being blue.
-  Return to lobby feature (Xbox only)

## Undoing a change

See the "How to undo" tab of the register page. In short: PS2 lines at address `00100000` and above change the game's own code; put back the original line. Xbox changes list the original bytes at each file offset; write them back and fix the XBE checksums (`tools/fix_xbe_checksums.py`).

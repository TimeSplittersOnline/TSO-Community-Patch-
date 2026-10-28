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
2. Apply [`build/TSO Community Patch.bps`](<build/TSO Community Patch.bps>) with any BPS patcher (Floating IPS, beat, or `python tools/make_bps.py apply default.xbe "TSO Community Patch.bps" "TSO Community Patch.xbe"`). The patcher refuses a different version of the file.
3. Use the patched XBE in place of the original (keep a backup of the original).

## What is documented here

- [CHANGELOG.md](CHANGELOG.md): every version, newest first, with the date and what changed.
- [docs/versions](docs/versions/README.md): one page per version (v5.3 on) listing every change to the game's code and data compared with the build before it: what was there, what it became and why.
- [docs/changes](docs/changes/README.md): the current build's complete list of changes to the original files, by feature, with the original and new bytes or instructions.
- [docs/functions.md](docs/functions.md): the game routines and data the mod uses, with descriptive names, addresses on each platform and what each is for.
- [docs/site](docs/site/index.html): the searchable change register as a web page (also published with GitHub Pages).

The [`build`](build) folder always holds the current version's TSO Community Patch files: the two pnach files (their names must stay as they are; PCSX2 finds a game's patch by them) and `TSO Community Patch.bps` for Xbox. Every earlier version (v5.3 on) is its own commit; the [version list](docs/versions/README.md) links each one's changes and files.

## Features

- XBE header (checksums and sizes)
- Advanced Settings menu & shared hooks (used by several features)
- Team Settings: Team Spawns, Disable Team colours
- Infinite Ammo, Disable Unarmed (No Punch)
- Team Bag Tag
- LAN: allowed modes, Xbox Live option removed, original-disc compatibility
- Mercy Rule
- Gun Game: Setbacks
- Weapon Mode (Gun Game / Random Weapon), Player Drops Gun
- Catch-Up
- Team VIP
- Virus: Spread By Kills
- Showdown (Elimination, Vampire)
- LAN: Manage Players (host: move a player to another team, kick a player)
- Zones: Scoring Interval, last score at time up
- Weapon Mode: weapon switch for players without the patch (experimental)
- Flame Tag: Number of Flames, LAN play, scoring
- Capture the Bag: Overtime
- Capture the Bag: Switch Spawns
- Spawn Rule
- Gun Game and Showdown: no armouries, weapon pickups or ammo boxes
- Thief: Gold Rush, Coin Drop
- Player Health
- Capture the Bag: Reverse Scoring, Score With Bag Away
- 4 Teams, team play in more modes
- Spectate (Elimination, Vampire)
- Respawn Delay
- King of the Hill
- Assault: Auto-Complete Phase, Time Bonus After Phase
- LAN: Return to Lobby (host)
- Random Characters
- LAN: everyone starts the match together
- Team Elimination / Team Vampire, Team Lives
- MapMaker limits and story maps
- Flame Tag: Flame Pass
- Multikill, Multikill Window
- Advanced Settings on one page (scrolling list)
- Venice: the gondolas in step on LAN, no water deaths on them
- Mode list and limits
- Weapon lists (extra weapons enabled)
- Virus on Siberia

## Undoing a change

See the "How to undo" tab of the register page. In short: PS2 lines at address `00100000` and above change the game's own code; put back the original line. Xbox changes list the original bytes at each file offset; write them back and fix the XBE checksums (`tools/fix_xbe_checksums.py`).

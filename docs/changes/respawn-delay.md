# Respawn Delay

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 000D6441 | 0C6441 | 7 | `66 89 a8 0a 15 00 00` | `e8 e7 04 81 00 90 90` | at a death (call at 0xd6441, was call 0x8e8663 (all.s XRT1); eax = player; keeps every register): the respawn delay. Also \| ---------------- respawn delay: at death (call at 0xd6441, eax=player), set delayed-spawn routine \| at a death (call at 0xd6441, was call 0x8e8663 (all.s XRT1); eax = player; keeps every register): the respawn delay. Also its end, as a gameframe (XRDDF), for the host's hold of other games' players (XRDH): set once per death (its deaths count, XRDDN), so the game timing the death again (its 3 second timer running out while the player still waits) doesn't move it | v5.3 · 2026-10-16 |
| 000D64AA | 0C64AA | 5 | `e8 11 b3 ff ff` | `e8 20 22 81 00` | pad tick gate (call at 0xd64aa) \| pad tick gate (call at 0xd64aa) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E6570 | 147 bytes | xbreadfail_sp | the items (ebp = menu mode; keeps ebp, uses the others) | v5.3 · 2026-10-16 |
| 008E6603 | 156 bytes | xbreadfail_sp | refresh (esi = page): greyed out by the Teamplay setting; Teamplay's changefn (XRDCH) does it again as it is changed | v5.19 · 2026-10-17 |
| 008E669F | 52 bytes | xbreadfail_sp | Team VIP changefn (menu, item; cdecl): its options are Off (0) / On (1) | v5.3 · 2026-10-16 |
| 008E66D3 | 52 bytes | xbreadfail_sp | Teamplay changefn (menu, item; cdecl): its options are On (0) / Off (1) | v5.3 · 2026-10-16 |
| 008E6707 | 187 bytes | xbreadfail_sp | (menu, 1 = Teamplay On; cdecl): Respawn Delay greyed out with Teamplay On; the team Respawn Delays, Team Spawns and the colours greyed out with it Off, and Spawn Rule's Near Teammates becomes Default; then the team items' own rules (XTGX) | v5.40 · 2026-10-19 |
| 008E67C2 | 230 bytes | xbreadfail_sp | colour item changefn (menu, item; cdecl): its own first, then the rules again (teams are on: the colours can be changed) | v5.19 · 2026-10-17 |
| 008E68A8 | 54 bytes | xbreadfail_sp | colour item changefn (menu, item; cdecl): its own first, then the rules again (teams are on: the colours can be changed) | v5.19 · 2026-10-17 |
| 008E68DE | 38 bytes | xbreadfail_sp | Team Spawns changefn (menu, item; cdecl) | v5.89 · 2026-10-27 |
| 008E6904 | 16 bytes | xbreadfail_sp | the colours' own change routines | v5.3 · 2026-10-16 (approx.) |
| 008E6914 | 4 bytes | xbreadfail_sp | Team Spawns' own changefn | v5.3 · 2026-10-16 (approx.) |
| 008E6918 | 21 bytes | xbreadfail_sp | eax = 1 when the menu's mode has no time limit (its match settings Time limit is None: the setting after Teamplay's, +8 in the mode's settings, 0); keeps the others | v5.19 · 2026-10-17 |
| 008E692D | 83 bytes | xbreadfail_sp | at a death (call at 0xd6441, was call 0x8e8663 (all.s XRT1); eax = player; keeps every register): the respawn delay. Also its end, as a gameframe (XRDDF), for the host's hold of other games' players (XRDH): set once per death (its deaths count, XRDDN), so the game timing the death again (its 3 second timer running out while the player still waits) doesn't move it | v5.70 · 2026-10-23 |
| 008E6980 | 120 bytes | xbreadfail_sp | eax = player -> edx = its respawn delay in frames (the team's or everyone's); keeps the others | v5.70 · 2026-10-23 |
| 008E69F8 | 122 bytes | xbreadfail_sp | eax = slot (0 everyone, 1-4 the team's), ecx = match mode -> edx = Respawn Delay option (0 Off, 1-5): offline / LAN host: this game's settings; LAN player: the host's, setup bytes 64 (0xE0 \| everyone), 65 (0x80 \| Red \| Blue << 3), 66 (Yellow / Green); from a host without the patch Off, as its own delay is; keeps the others | v5.89 · 2026-10-27 |
| 008E6A72 | 98 bytes | xbreadfail_sp | the setup's bytes 64-66 for LAN players (from XGGSET): the menu mode's Respawn Delays, as XRDOPT reads them; keeps all | v5.8 · 2026-10-16 |
| 008E6AD4 | 20 bytes | xbreadfail_sp | ebx, edi = two options -> ebx = first \| second << 3 (each 0 when not 0-5); edi is changed | v5.8 · 2026-10-16 |
| 008E6AE8 | 4 bytes | xbreadfail_sp | Teamplay's own changefn | v5.3 · 2026-10-16 (approx.) |
| 008E6AEC | 4 bytes | xbreadfail_sp | Team VIP's own changefn | v5.3 · 2026-10-16 (approx.) |
| 008E8102 | 14 bytes | xbreadfail_sp | Menu / message text "Respawn Delay" | v5.3 · 2026-10-16 |
| 008E8110 | 23 bytes | xbreadfail_sp | Menu / message text "Attacker Respawn Delay" | v5.3 · 2026-10-16 |
| 008E8127 | 23 bytes | xbreadfail_sp | Menu / message text "Defender Respawn Delay" | v5.3 · 2026-10-16 |
| 008E813E | 18 bytes | xbreadfail_sp | Menu / message text "Red Respawn Delay" | v5.3 · 2026-10-16 |
| 008E8150 | 19 bytes | xbreadfail_sp | Menu / message text "Blue Respawn Delay" | v5.3 · 2026-10-16 |
| 008E8163 | 21 bytes | xbreadfail_sp | Menu / message text "Yellow Respawn Delay" | v5.3 · 2026-10-16 |
| 008E8178 | 20 bytes | xbreadfail_sp | Menu / message text "Green Respawn Delay" | v5.3 · 2026-10-16 |
| 008E818C | 9 bytes | xbreadfail_sp | Menu / message text "1 Second" | v5.3 · 2026-10-16 |
| 008E8195 | 10 bytes | xbreadfail_sp | Menu / message text "2 Seconds" | v5.3 · 2026-10-16 |
| 008E819F | 10 bytes | xbreadfail_sp | Menu / message text "3 Seconds" | v5.3 · 2026-10-16 |
| 008E81A9 | 10 bytes | xbreadfail_sp | Menu / message text "4 Seconds" | v5.3 · 2026-10-16 |
| 008E81B3 | 13 bytes | xbreadfail_sp | Menu / message text "5 Seconds" | v5.3 · 2026-10-16 |
| 008E8663 | 108 bytes | xbreadfail_sp | ---------------- respawn delay: at death (call at 0xd6441, eax=player), set delayed-spawn routine | v5.3 · 2026-10-16 |
| 008E86CF | 20 bytes | xbreadfail_sp | pad tick gate (call at 0xd64aa) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E7A98-000E7BAB | 69 | RDGR: a0 = page, a1 = 1 Teamplay On: Respawn Delay greyed out with it On; the team Respawn Delays, Team Spawns and the colours greyed out with it Off, and Spawn Rule's Near Teammates becomes Default; then the team items' own rules (TGX) | v5.40 · 2026-10-19 |
| 000E87FC-000E88F3 | 62 | RDRA: a0 = page, a1 = 0 refresh / 1 apply: refresh greys the items out by the Teamplay setting, and makes Teamplay do it again as it is changed (RDCH) | v5.19 · 2026-10-17 |
| 000E8BDC-000E8CCF | 61 | PRDI: the items | v5.3 · 2026-10-16 |
| 000EC1A0-000EC237 | 38 | PRDT: at a death (jal at 0x1CC768 in place of 'sh zero,5038(t6)', was jal rd3.py's RT1; t6 = player; leaves t7 = 0x650000): the respawn delay (PRDF). Also its end, as a gameframe (RDDF), for the host's hold of other games' players (PRDH): | v5.70 · 2026-10-23 |
| 000EF2E0-000EF327 | 18 | RDCHV: Team VIP changefn (a0 = page, a1 = item): its options are Off (0) / On (1) | v5.3 · 2026-10-16 |
| 000EF328-000EF36F | 18 | RDCH: Teamplay changefn (a0 = page, a1 = item): its options are On (0) / Off (1) | v5.3 · 2026-10-16 |

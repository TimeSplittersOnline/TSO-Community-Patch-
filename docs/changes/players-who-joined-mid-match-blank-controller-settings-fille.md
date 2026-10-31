# Players who joined mid-match: blank controller settings filled

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002C0C7D | 2B0C7D | 5 | `e8 ce 4b da ff` | `e8 10 13 62 00` | weapon picker: was call 0x65850 \| weapon picker / custom weapon set list (call at 0x2c0c7d, and via XSDDRW at 0x2d306b, was call 0x65850; cdecl (menu mode, \| weapon picker / custom weapon set list (call at 0x2c0c7d, and via XSDDRW at 0x2d306b, was call 0x65850; cdecl (menu mode, gun id)): the game's ban, the Temporal Uplink on LAN, plus guns Gun Game / Showdown cannot hand out while it is chosen for a mode that can play it | v5.3 · 2026-10-16 |
| 002C70D3 | 2B70D3 | 5 | `e8 b8 b2 da ff` | `e8 7d b0 61 00` | match settings refresh (call at 0x2c70d3, was call 0x72390 for "Always Start With Gun"; cdecl (page, 1)): greyed out \| match settings refresh (call at 0x2c70d3, was call 0x72390 for "Always Start With Gun"; cdecl (page, 1)): greyed out while Gun Game or Random Weapon is chosen for a mode that plays it | v5.3 · 2026-10-16 |
| 002C7168 | 2B7168 | 5 | `e8 23 b2 da ff` | `e8 7e ae 61 00` | match settings refresh, every frame (call at 0x2c7168, was call 0x72390 for Score Limit; cdecl (page, 7)): Score Limit greyed \| match settings refresh, every frame (call at 0x2c7168, was call 0x72390 for Score Limit; cdecl (page, 7)): Score Limit greyed out while Gun Game is chosen for a mode that can play it | v5.3 · 2026-10-16 |
| 002C7186 | 2B7186 | 5 | `e8 05 b2 da ff` | `e8 f1 af 61 00` | Score Method item: was call 0x72390 (Gun Game, Showdown grey it out) \| match settings refresh (call at 0x2c7186, was call 0x72390 for Score Method; cdecl (page, 8)): greyed out while Gun Game or \| match settings refresh (call at 0x2c7186, was call 0x72390 for Score Method; cdecl (page, 8)): greyed out while Gun Game or Showdown is chosen for a mode that plays it (Gun Game scores the ladder, Showdown kills) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008CC000 | 187 bytes | xbreadfail_sp | Code: XCTLFIX (see the code shown) | v5.109 · 2026-10-31 |
| 008CC0BB | 21 bytes | xbreadfail_sp | edi = player: ZF clear when any of its controls is set | v5.109 · 2026-10-31 |
| 008CC0D0 | 15 bytes | xbreadfail_sp | eax = offset: ebx's dword to edi's when edi's is 0 | v5.109 · 2026-10-31 |
| 008E161B | 85 bytes | xbreadfail_sp | every frame (via 0x8e9841, call at 0x68c2f): then the Team VIP timer, which goes on to the game's own tick | v5.109 · 2026-10-31 |
| 008E1670 | 662 bytes | xbreadfail_sp | every frame (XGGT, first): a new match (the gameframe back into its first 20 seconds) clears, for every chr, the tables that are | v5.109 · 2026-10-31 |
| 008E1906 | 272 bytes | xbreadfail_sp | Code: XNMCLR (see the code shown) | v5.109 · 2026-10-31 |
| 008E1A16 | 4 bytes | xbreadfail_sp | Data: XNMLAST | v5.3 · 2026-10-16 (approx.) |
| 008E1A1A | 4 bytes | xbreadfail_sp | Gun Game / Showdown start: "picked up" resends left | v5.3 · 2026-10-16 (approx.) |
| 008E1A1E | 4 bytes | xbreadfail_sp | the gameframe of the next | v5.3 · 2026-10-16 (approx.) |
| 008E1A22 | 6 bytes | xbreadfail_sp | network player table whose game asked for its first spawn point this match (bit each; cleared at a new match only: | v5.3 · 2026-10-16 (approx.) |
| 008E1A28 | 1 bytes | xbreadfail_sp | (test programs only: 1 = XGGHELD off) | v5.3 · 2026-10-16 (approx.) |
| 008E1A29 | 1 bytes | xbreadfail_sp | (test programs only: 1 = no direct pickup of a hand-out, XGGDROP) | v5.3 · 2026-10-16 (approx.) |
| 008E1A2A | 1 bytes | xbreadfail_sp | frames between the characters' start hand-outs (the test programs set 0: all at once) | v5.3 · 2026-10-16 (approx.) |
| 008E1A2B | 23 bytes | xbreadfail_sp | ZF set (je) while the gameframe is in the match's first 20 seconds; keeps every register. Every new-match check: the gameframe went back AND is in its first 20 seconds (a gameframe that only steps back, as a LAN player's game may when the host corrects its clock, is not a new match) | v5.16 · 2026-10-17 |
| 008E1A42 | 28 bytes | xbreadfail_sp | mk.s (built into the base) and its new-match checks, ebx = chr id, ecx = gameframe: | v5.16 · 2026-10-17 |
| 008E1A5E | 21 bytes | xbreadfail_sp | kill count routine' bonus kills (call at 0x8e92ac, was cmp LASTF(,%ebx,4),%ecx, then jae: keep them): CF clear (keep) unless the | v5.16 · 2026-10-17 |
| 008E1A73 | 19 bytes | xbreadfail_sp | kill count routine' bonus kills (call at 0x8e92ac, was cmp LASTF(,%ebx,4),%ecx, then jae: keep them): CF clear (keep) unless the gameframe went back into the first 20 seconds (a new match: cleared) | v5.16 · 2026-10-17 |
| 008E1A86 | 89 bytes | xbreadfail_sp | kill count routine (via 0x8e9846, call at 0x64afc; esi = chr; eax returned = the match's lives, non-zero: score = lives left): Gun Game score = weapon level; Showdown: eax 0, so the score is the kills | v5.3 · 2026-10-16 |
| 008E1ADF | 51 bytes | xbreadfail_sp | eax = 1 when Gun Game can be picked for the menu's mode (its modes, teams off), else 0; keeps ecx/edx | v5.3 · 2026-10-16 |
| 008E1B12 | 385 bytes | xbreadfail_sp | Advanced page mode items (via 0x8e9819): Weapon Mode for the deathmatch-style modes (Gun Game, Showdown only where they can be played), the other mode items, then Player Drops Gun (every mode) | v5.67 · 2026-10-23 |
| 008E1C93 | 163 bytes | xbreadfail_sp | refresh (via 0x8e9805, esi = page). Weapon Mode's options: Off, [Gun Game], Random Weapon, [Showdown] (XGGVOPT) | v5.76 · 2026-10-24 |
| 008E1D36 | 160 bytes | xbreadfail_sp | apply (via 0x8e980a, esi = page) | v5.109 · 2026-10-31 |
| 008E1DD6 | 132 bytes | xbreadfail_sp | Kills To Advance refresh (esi = page): value; greyed out unless Weapon Mode is Gun Game; Player Drops Gun greyed out with Gun Game or Showdown; Weapon Mode updates those on change (every mode that lists it) | v5.3 · 2026-10-16 |
| 008E1E5A | 45 bytes | xbreadfail_sp | Kills To Advance apply (esi = page) | v5.3 · 2026-10-16 |
| 008E1E87 | 183 bytes | xbreadfail_sp | Weapon Mode changefn (menu, item; cdecl), also run by Showdown's (XSDCH): Kills To Advance only selectable with Gun Game, Player Drops Gun only without Gun Game or Showdown, Weapon Mode itself only with Showdown Off | v5.3 · 2026-10-16 |
| 008E1F3E | 84 bytes | xbreadfail_sp | XGGUSE(gun id): eax = 1 if Gun Game can hand it out (a droppable gun with ammo, as XGGGC), or no gun; keeps all but eax | v5.3 · 2026-10-16 |
| 008E1F92 | 89 bytes | xbreadfail_sp | weapon picker / custom weapon set list (call at 0x2c0c7d, and via XSDDRW at 0x2d306b, was call 0x65850; cdecl (menu mode, gun id)): the game's ban, the Temporal Uplink on LAN, plus guns Gun Game / Showdown cannot hand out while it is chosen for a mode that can play it | v5.102 · 2026-10-29 |
| 008E1FEB | 50 bytes | xbreadfail_sp | match settings refresh, every frame (call at 0x2c7168, was call 0x72390 for Score Limit; cdecl (page, 7)): Score Limit greyed out while Gun Game is chosen for a mode that can play it | v5.3 · 2026-10-16 |
| 008E201D | 246 bytes | xbreadfail_sp | end of the setup builder (XIAFLAG's jmp 0x119de, then the No Punch flag code): Gun Game: no score limit (kill limit 0x7be05c), so the match only ends when someone finishes the ladder (or on time) | v5.89 · 2026-10-27 |
| 008E2113 | 66 bytes | xbreadfail_sp | eax = 1 when the menu's Weapon Mode applies to the menu's mode (Gun Game: XGGMOK; Random Weapon: its modes; Showdown: XSDMOK); keeps ecx, edx | v5.76 · 2026-10-24 |
| 008E2155 | 39 bytes | xbreadfail_sp | match settings refresh (call at 0x2c70d3, was call 0x72390 for "Always Start With Gun"; cdecl (page, 1)): greyed out while Gun Game or Random Weapon is chosen for a mode that plays it | v5.3 · 2026-10-16 |
| 008E217C | 50 bytes | xbreadfail_sp | match settings refresh (call at 0x2c7186, was call 0x72390 for Score Method; cdecl (page, 8)): greyed out while Gun Game or Showdown is chosen for a mode that plays it (Gun Game scores the ladder, Showdown kills) | v5.3 · 2026-10-16 |
| 008E2217 | 24 bytes | xbreadfail_sp | ecx = Weapon Mode option -> ecx = its setting for the menu's mode. The options: Off, [Gun Game], Random Weapon, Gun Game only where the mode lists it (XGGLST); keeps the others | v5.3 · 2026-10-16 |
| 008E222F | 28 bytes | xbreadfail_sp | ecx = Weapon Mode setting (0-2; 3 Showdown: shown as Off) -> ecx = its option on the menu's mode; keeps the others | v5.3 · 2026-10-16 |
| 008E224B | 24 bytes | xbreadfail_sp | eax = 1 when the menu's mode lists Gun Game (its modes; it only plays with Teamplay Off), else 0; keeps the others | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E887C-000E8973 | 62 | CTLFIX: every frame, every console: a player whose controller settings (+24, 22 words) were never set gets them from another player's (a remote one first, else this console's own); a mid-match joiner could have none | v5.109 · 2026-10-31 |

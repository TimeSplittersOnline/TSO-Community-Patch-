# Team Elimination / Team Vampire, Team Lives

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002F2072 | 2E2072 | 13 | `3c 09 75 28 80 3d 56 d2 82 00 04 75 1f` | `e9 61 4e 5f 00 90 90 90 90 90 90 90 90` | Scores page player rows: Deathmatch with Teamplay shows the Team Deathmatch number (kills of other teams); jumps to XERS, which in Team Elimination / Vampire with lives shows the game's own lives / time instead ("N Lives" for a player still in, else the time it was knocked out). | v5.86 · 2026-10-27 |
| 004D6FEC | 4C760C | 5 | `00 00 00 00 00` | `02 00 00 00 01` | Mode table, Elimination: Teamplay possible (+0xc = 2) and its team spawn points used (+0x10 = 1): Team Elimination. Was 0, 0. | v5.40 · 2026-10-19 |
| 004D702C | 4C764C | 5 | `00 00 00 00 00` | `02 00 00 00 01` | Mode table, Vampire: the same (Team Vampire). Was 0, 0. | v5.40 · 2026-10-19 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013A90C | 962E0A68 | 0C039620 | lhu t6,2664(s1) | jal 0xe5880 | Hook: a death's lives: Team Lives (TLDEC returns t6 / t7 as the game's two) | v5.40 · 2026-10-19 |
| 0013ADBC | 8E0F0A74 | 0C038AF3 | lw t7,2676(s0) | jal 0xe2bcc | Hook: ranking: Elimination / Vampire with teams: the team's time (delay slot lw t6,2668(s0) kept) | v5.42 · 2026-10-19 |
| 0013B1F0 | 11E00008 | 0803BB84 | beq t7,zero,0x13b214 | j 0xeee10 | Hook: ranking: Team Lives' team scores kept out of Elimination / Vampire rank scores (delay slot kept) | v5.40 · 2026-10-19 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E2BCC-000E2E2F | 153 | TLAGE: jal at 0x13ADBC in the ranking (was lw t7,2676(s0); its delay slot lw t6,2668(s0) has run; then t7 += t6 is the rank score; s0 = chr): Elimination / Vampire with Teamplay: the team's time, the longest any of its players (connected) | v5.98 · 2026-10-28 |
| 000E4688-000E485B | 117 | TLFRM: every frame of a lives match (from SDEND, before the end check), when this game decides a Teamplay match (TLM): a new match (the gameframe went back, within its first 20 seconds) fills the pools with the Lives setting; the team scores | v5.41 · 2026-10-19 |
| 000E4A28-000E4BEB | 113 | JNTM: a0 = a chr whose team becomes a1 (team write hook, LAN). On the host of a Team Elimination / Vampire match being played, for a player that joined it mid-match (JNF; its lives were the fewest of the players in, SDMIN), once: on a team with | v5.98 · 2026-10-28 |
| 000E5880-000E59FF | 96 | TLDEC: jal at 0x13A90C in add-kill routine (was lhu t6,2664(s1); its delay slot sll t7,t6,16 now a nop; s1 = the victim's chr; then the game takes one off its lives left when it has any): with Team Lives, the pool is the team's lives as the HUD shows | v5.90 · 2026-10-27 |
| 000E6BC4-000E6D07 | 81 | PSTSC: jal at 0x475424 in the Scores page's team rows (was jal 0xFE180, the Bag Tag team row: a0 the row's text, a1 the team score; s1 = the team 1-4): Team Elimination / Vampire with lives: a team knocked out (score 0: no lives left) that | v5.88 · 2026-10-27 |
| 000ECF4C-000ECFC7 | 31 | TLRA: a0 = page, a1 = 0 refresh / 1 apply: refresh shows it and greys it out while Teamplay is Off; apply stores it | v5.40 · 2026-10-19 |
| 000ED418-000ED48F | 30 | TLON: v0 = 1 with Team Lives on in such a match, else 0 | v5.89 · 2026-10-27 |
| 000ED580-000ED5F3 | 29 | TLM: v0 = 1 in a lives match with Teamplay that this game decides, Elimination / Vampire, not Showdown, else 0; uses t, v | v5.40 · 2026-10-19 |
| 000EDE64-000EDEC7 | 25 | TLITEM: the item: Off / On | v5.40 · 2026-10-19 |
| 000EE2E8-000EE343 | 23 | ISSPN: leaf: a0 = a chr id -> v0 = 1 if the ranking takes it: offline always; LAN when its game (network player table +4) has spawned (that game's entry 0x6E41B0 + id x 0x30C, +0x34 bit 0x10, as the game's ranking); uses t8, t9 | v5.86 · 2026-10-27 |
| 000EE344-000EE39F | 23 | TLSV: from PFALL, instead of 0x139D88 (the end scores saved, before game state 8; e.g. the match ended on its time limit): on the host (or offline) the ranking runs once more (0x13ACC0, a0 0) with no out-player time (TLNP: TLAGE), so with | v5.84 · 2026-10-26 |
| 000EEE10-000EEE5B | 19 | TLRK: j at 0x13B1F0 in the ranking (was beq t7,zero,<own score>; its delay slot addiu t7,zero,16 has run; t6 = the match's parms): Teamplay (not Assault) ranks by the team score, except in Elimination / Vampire with lives: a player's own score, | v5.40 · 2026-10-19 |
| 000EF370-000EF3B3 | 17 | PERS: j at 0x475028 in the Scores page's player rows (was beq t6,zero,0x4750E8 / nop / bne t5,zero,0x4750E8; t6 = the Teamplay flag, t5 = game type - 9): Deathmatch with Teamplay shows the Team Deathmatch number (0x475038, kills of other | v5.90 · 2026-10-27 |
| 000EF478-000EF4B7 | 16 | TPGR: a0 = page, a1 = 1 greyed out: its Teamplay item greyed out or not | v5.40 · 2026-10-19 |
| 000EFB24-000EFB4F | 11 | TPON: a0 = page: v0 = 1 when it has a Teamplay item (25) set On (option 0), else 0 | v5.40 · 2026-10-19 |
| 000F0080-000F008B | 3 | LTL: text | v5.40 · 2026-10-19 |
| 000F0128-000F0133 | 3 | PTFMT: code | v5.86 · 2026-10-27 |

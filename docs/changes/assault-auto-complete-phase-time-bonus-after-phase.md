# Assault: Auto-Complete Phase, Time Bonus After Phase

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002299D4 | 2199D4 | 5 | `e8 57 99 00 00` | `e8 c7 ab 6b 00` | Assault tick: Auto-Complete Phase first \| objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick \| objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick (same stack) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E45A0 | 288 bytes | xbreadfail_sp | objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick (same stack) | v5.89 · 2026-10-27 |
| 008E46C0 | 4 bytes | xbreadfail_sp | the phase the timer is for (-1 none) | v5.3 · 2026-10-16 (approx.) |
| 008E46C4 | 4 bytes | xbreadfail_sp | the match clock when it started | v5.3 · 2026-10-16 (approx.) |
| 008E46C8 | 4 bytes | xbreadfail_sp | the gameframe when it started | v5.3 · 2026-10-16 (approx.) |
| 008E46CC | 4 bytes | xbreadfail_sp | gameframe last seen | v5.3 · 2026-10-16 (approx.) |
| 008E46D0 | 91 bytes | xbreadfail_sp | Assault menu: Time Bonus After Phase | v5.20 · 2026-10-17 |
| 008E472B | 50 bytes | xbreadfail_sp | refresh (esi = page): value; greyed out with no time limit | v5.20 · 2026-10-17 |
| 008E475D | 35 bytes | xbreadfail_sp | Code: XTBA (see the code shown) | v5.20 · 2026-10-17 |
| 008E4780 | 23 bytes | xbreadfail_sp | Assault menu: Auto-Complete Phase | v5.20 · 2026-10-17 |
| 008E4797 | 84 bytes | xbreadfail_sp | Assault menu: Auto-Complete Phase | v5.11 · 2026-10-16 |
| 008E47EB | 36 bytes | xbreadfail_sp | refresh / apply (esi = page) | v5.11 · 2026-10-16 |
| 008E480F | 35 bytes | xbreadfail_sp | Code: XASA (see the code shown) | v5.11 · 2026-10-16 |
| 008E4832 | 20 bytes | xbreadfail_sp | Menu / message text "Auto-Complete Phase" | v5.11 · 2026-10-16 |
| 008E4846 | 70 bytes | xbreadfail_sp | (as the game's own times) | v5.20 · 2026-10-17 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 003772FC | 0C0E1348 | 0C038CB6 | jal 0x384d20 | jal 0xe32d8 | Hook: objectives update's Assault tick: Auto-Complete Phase first (was jal 0x384D20; delay slot nop kept) | v5.11 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E32D8-000E3503 | 139 | ASK: timer is for + 1 (0 none: RAM starts at 0), the match clock / gameframe when it started, gameframe last seen jal at 0x3772FC (objectives update's Assault tick, was jal 0x384D20): the skip check and the time bonus, then the tick (same args) | v5.89 · 2026-10-27 |
| 000E7CF8-000E7E03 | 67 | ASITEM: Assault menu: Auto-Complete Phase (Off, 1 Min .. 10 Mins, as the game's own times) | v5.11 · 2026-10-16 |
| 000EBB80-000EBC1B | 39 | TBITEM: Assault menu: Time Bonus After Phase (Off, 1 Min, 2 Mins, 3 Mins) | v5.20 · 2026-10-17 |
| 000ED0C0-000ED13B | 31 | TBRA: a0 = page, a1 = 0 refresh / 1 apply: Time Bonus After Phase value (0-3); refresh greys it out with no time limit | v5.20 · 2026-10-17 |
| 000EEBD8-000EEC2B | 21 | ASRA: a0 = page, a1 = 0 refresh / 1 apply: Auto-Complete Phase value (0-10) | v5.11 · 2026-10-16 |
| 000EFE78-000EFE8F | 6 | LTB: text | v5.20 · 2026-10-17 |
| 000EFEB8-000EFECB | 5 | LAS: text | v5.11 · 2026-10-16 |
| 000F01FC-000F0203 | 2 | LAS1: text | v5.11 · 2026-10-16 (approx.) |
| 000F0204-000F020B | 2 | LAS2: text | v5.11 · 2026-10-16 (approx.) |
| 000F020C-000F0213 | 2 | LAS3: text | v5.11 · 2026-10-16 (approx.) |
| 000F0214-000F021B | 2 | LAS4: text | v5.11 · 2026-10-16 (approx.) |
| 000F021C-000F0223 | 2 | LAS5: text | v5.11 · 2026-10-16 (approx.) |
| 000F0224-000F022B | 2 | LAS6: text | v5.11 · 2026-10-16 (approx.) |
| 000F022C-000F0233 | 2 | LAS7: text | v5.11 · 2026-10-16 (approx.) |
| 000F0234-000F023B | 2 | LAS8: text | v5.11 · 2026-10-16 (approx.) |
| 000F023C-000F0243 | 2 | LAS9: text | v5.11 · 2026-10-16 (approx.) |
| 000F0244-000F024B | 2 | LAS10: text | v5.11 · 2026-10-16 (approx.) |

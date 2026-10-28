# Assault: Auto-Complete Phase, Time Bonus After Phase

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002299D4 | 2199D4 | 5 | `e8 57 99 00 00` | `e8 e3 ab 6b 00` | Assault tick: Auto-Complete Phase first \| objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick \| objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick (same stack) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E45BC | 288 bytes | xbreadfail_sp | objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick (same stack) | v5.89 · 2026-10-27 |
| 008E46DC | 4 bytes | xbreadfail_sp | the phase the timer is for (-1 none) | v5.3 · 2026-10-16 (approx.) |
| 008E46E0 | 4 bytes | xbreadfail_sp | the match clock when it started | v5.3 · 2026-10-16 (approx.) |
| 008E46E4 | 4 bytes | xbreadfail_sp | the gameframe when it started | v5.3 · 2026-10-16 (approx.) |
| 008E46E8 | 4 bytes | xbreadfail_sp | gameframe last seen | v5.3 · 2026-10-16 (approx.) |
| 008E46EC | 91 bytes | xbreadfail_sp | Assault menu: Time Bonus After Phase | v5.20 · 2026-10-17 |
| 008E4747 | 50 bytes | xbreadfail_sp | refresh (esi = page): value; greyed out with no time limit | v5.20 · 2026-10-17 |
| 008E4779 | 35 bytes | xbreadfail_sp | Code: XTBA (see the code shown) | v5.20 · 2026-10-17 |
| 008E479C | 23 bytes | xbreadfail_sp | Assault menu: Auto-Complete Phase | v5.20 · 2026-10-17 |
| 008E47B3 | 84 bytes | xbreadfail_sp | Assault menu: Auto-Complete Phase | v5.11 · 2026-10-16 |
| 008E4807 | 36 bytes | xbreadfail_sp | refresh / apply (esi = page) | v5.11 · 2026-10-16 |
| 008E482B | 35 bytes | xbreadfail_sp | Code: XASA (see the code shown) | v5.11 · 2026-10-16 |
| 008E484E | 20 bytes | xbreadfail_sp | Menu / message text "Auto-Complete Phase" | v5.11 · 2026-10-16 |
| 008E4862 | 70 bytes | xbreadfail_sp | (as the game's own times) | v5.20 · 2026-10-17 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 003772FC | 0C0E1348 | 0C038CB6 | jal 0x384d20 | jal 0xe32d8 | Hook: objectives update's Assault tick: Auto-Complete Phase first (was jal 0x384D20; delay slot nop kept) | v5.11 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E32D8-000E3503 | 139 | ASK: timer is for + 1 (0 none: RAM starts at 0), the match clock / gameframe when it started, gameframe last seen jal at 0x3772FC (objectives update's Assault tick, was jal 0x384D20): the skip check and the time bonus, then the tick (same args) | v5.89 · 2026-10-27 |
| 000E7D30-000E7E3B | 67 | ASITEM: Assault menu: Auto-Complete Phase (Off, 1 Min .. 10 Mins, as the game's own times) | v5.11 · 2026-10-16 |
| 000EBD30-000EBDCB | 39 | TBITEM: Assault menu: Time Bonus After Phase (Off, 1 Min, 2 Mins, 3 Mins) | v5.20 · 2026-10-17 |
| 000ED144-000ED1BF | 31 | TBRA: a0 = page, a1 = 0 refresh / 1 apply: Time Bonus After Phase value (0-3); refresh greys it out with no time limit | v5.20 · 2026-10-17 |
| 000EED2C-000EED7F | 21 | ASRA: a0 = page, a1 = 0 refresh / 1 apply: Auto-Complete Phase value (0-10) | v5.11 · 2026-10-16 |
| 000EFFC8-000EFFDF | 6 | LTB: text | v5.20 · 2026-10-17 |
| 000F0008-000F001B | 5 | LAS: text | v5.11 · 2026-10-16 |
| 000F034C-000F0353 | 2 | LAS1: text | v5.11 · 2026-10-16 (approx.) |
| 000F0354-000F035B | 2 | LAS2: text | v5.11 · 2026-10-16 (approx.) |
| 000F035C-000F0363 | 2 | LAS3: text | v5.11 · 2026-10-16 (approx.) |
| 000F0364-000F036B | 2 | LAS4: text | v5.11 · 2026-10-16 (approx.) |
| 000F036C-000F0373 | 2 | LAS5: text | v5.11 · 2026-10-16 (approx.) |
| 000F0374-000F037B | 2 | LAS6: text | v5.11 · 2026-10-16 (approx.) |
| 000F037C-000F0383 | 2 | LAS7: text | v5.11 · 2026-10-16 (approx.) |
| 000F0384-000F038B | 2 | LAS8: text | v5.11 · 2026-10-16 (approx.) |
| 000F038C-000F0393 | 2 | LAS9: text | v5.11 · 2026-10-16 (approx.) |
| 000F0394-000F039B | 2 | LAS10: text | v5.11 · 2026-10-16 (approx.) |

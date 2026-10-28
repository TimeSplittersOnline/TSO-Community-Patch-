# Assault: Auto-Complete Phase, Time Bonus After Phase

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002299D4 | 2199D4 | 5 | `e8 57 99 00 00` | `e8 f3 ab 6b 00` | Assault tick: Auto-Complete Phase first \| objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick \| objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick (same stack) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E45CC | 288 bytes | xbreadfail_sp | objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick (same stack) | v5.89 · 2026-10-27 |
| 008E46EC | 4 bytes | xbreadfail_sp | the phase the timer is for (-1 none) | v5.3 · 2026-10-16 (approx.) |
| 008E46F0 | 4 bytes | xbreadfail_sp | the match clock when it started | v5.3 · 2026-10-16 (approx.) |
| 008E46F4 | 4 bytes | xbreadfail_sp | the gameframe when it started | v5.3 · 2026-10-16 (approx.) |
| 008E46F8 | 4 bytes | xbreadfail_sp | gameframe last seen | v5.3 · 2026-10-16 (approx.) |
| 008E46FC | 91 bytes | xbreadfail_sp | Assault menu: Time Bonus After Phase | v5.20 · 2026-10-17 |
| 008E4757 | 50 bytes | xbreadfail_sp | refresh (esi = page): value; greyed out with no time limit | v5.20 · 2026-10-17 |
| 008E4789 | 35 bytes | xbreadfail_sp | Code: XTBA (see the code shown) | v5.20 · 2026-10-17 |
| 008E47AC | 23 bytes | xbreadfail_sp | Assault menu: Auto-Complete Phase | v5.20 · 2026-10-17 |
| 008E47C3 | 84 bytes | xbreadfail_sp | Assault menu: Auto-Complete Phase | v5.11 · 2026-10-16 |
| 008E4817 | 36 bytes | xbreadfail_sp | refresh / apply (esi = page) | v5.11 · 2026-10-16 |
| 008E483B | 35 bytes | xbreadfail_sp | Code: XASA (see the code shown) | v5.11 · 2026-10-16 |
| 008E485E | 20 bytes | xbreadfail_sp | Menu / message text "Auto-Complete Phase" | v5.11 · 2026-10-16 |
| 008E4872 | 70 bytes | xbreadfail_sp | (as the game's own times) | v5.20 · 2026-10-17 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 003772FC | 0C0E1348 | 0C038CC5 | jal 0x384d20 | jal 0xe3314 | Hook: objectives update's Assault tick: Auto-Complete Phase first (was jal 0x384D20; delay slot nop kept) | v5.11 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E3314-000E353F | 139 | ASK: timer is for + 1 (0 none: RAM starts at 0), the match clock / gameframe when it started, gameframe last seen jal at 0x3772FC (objectives update's Assault tick, was jal 0x384D20): the skip check and the time bonus, then the tick (same args) | v5.89 · 2026-10-27 |
| 000E7DD4-000E7EDF | 67 | ASITEM: Assault menu: Auto-Complete Phase (Off, 1 Min .. 10 Mins, as the game's own times) | v5.11 · 2026-10-16 |
| 000EBE04-000EBE9F | 39 | TBITEM: Assault menu: Time Bonus After Phase (Off, 1 Min, 2 Mins, 3 Mins) | v5.20 · 2026-10-17 |
| 000ED2A8-000ED323 | 31 | TBRA: a0 = page, a1 = 0 refresh / 1 apply: Time Bonus After Phase value (0-3); refresh greys it out with no time limit | v5.20 · 2026-10-17 |
| 000EEE90-000EEEE3 | 21 | ASRA: a0 = page, a1 = 0 refresh / 1 apply: Auto-Complete Phase value (0-10) | v5.11 · 2026-10-16 |
| 000F0130-000F0147 | 6 | LTB: text | v5.20 · 2026-10-17 |
| 000F0170-000F0183 | 5 | LAS: text | v5.11 · 2026-10-16 |
| 000F04B4-000F04BB | 2 | LAS1: text | v5.11 · 2026-10-16 (approx.) |
| 000F04BC-000F04C3 | 2 | LAS2: text | v5.11 · 2026-10-16 (approx.) |
| 000F04C4-000F04CB | 2 | LAS3: text | v5.11 · 2026-10-16 (approx.) |
| 000F04CC-000F04D3 | 2 | LAS4: text | v5.11 · 2026-10-16 (approx.) |
| 000F04D4-000F04DB | 2 | LAS5: text | v5.11 · 2026-10-16 (approx.) |
| 000F04DC-000F04E3 | 2 | LAS6: text | v5.11 · 2026-10-16 (approx.) |
| 000F04E4-000F04EB | 2 | LAS7: text | v5.11 · 2026-10-16 (approx.) |
| 000F04EC-000F04F3 | 2 | LAS8: text | v5.11 · 2026-10-16 (approx.) |
| 000F04F4-000F04FB | 2 | LAS9: text | v5.11 · 2026-10-16 (approx.) |
| 000F04FC-000F0503 | 2 | LAS10: text | v5.11 · 2026-10-16 (approx.) |

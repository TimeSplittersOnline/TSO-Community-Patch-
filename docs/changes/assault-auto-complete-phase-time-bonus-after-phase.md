# Assault: Auto-Complete Phase, Time Bonus After Phase

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002299D4 | 2199D4 | 5 | `e8 57 99 00 00` | `e8 56 ac 6b 00` | Assault tick: Auto-Complete Phase first \| objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick \| objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick (same stack) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E462F | 309 bytes | xbreadfail_sp | objectives update's Assault tick (call at 0x2299d4, was call 0x233330): the skip check and the time bonus, then the tick (same stack) | v5.106 · 2026-10-29 |
| 008E4764 | 4 bytes | xbreadfail_sp | the phase the timer is for (-1 none) | v5.3 · 2026-10-16 (approx.) |
| 008E4768 | 4 bytes | xbreadfail_sp | the match clock when it started | v5.3 · 2026-10-16 (approx.) |
| 008E476C | 4 bytes | xbreadfail_sp | the gameframe when it started | v5.3 · 2026-10-16 (approx.) |
| 008E4770 | 4 bytes | xbreadfail_sp | gameframe last seen | v5.3 · 2026-10-16 (approx.) |
| 008E4774 | 91 bytes | xbreadfail_sp | Assault menu: Time Bonus After Phase | v5.20 · 2026-10-17 |
| 008E47CF | 50 bytes | xbreadfail_sp | refresh (esi = page): value; greyed out with no time limit | v5.20 · 2026-10-17 |
| 008E4801 | 35 bytes | xbreadfail_sp | Code: XTBA (see the code shown) | v5.20 · 2026-10-17 |
| 008E4824 | 23 bytes | xbreadfail_sp | Assault menu: Auto-Complete Phase | v5.20 · 2026-10-17 |
| 008E483B | 84 bytes | xbreadfail_sp | Assault menu: Auto-Complete Phase | v5.11 · 2026-10-16 |
| 008E488F | 36 bytes | xbreadfail_sp | refresh / apply (esi = page) | v5.11 · 2026-10-16 |
| 008E48B3 | 35 bytes | xbreadfail_sp | Code: XASA (see the code shown) | v5.11 · 2026-10-16 |
| 008E48D6 | 20 bytes | xbreadfail_sp | Menu / message text "Auto-Complete Phase" | v5.11 · 2026-10-16 |
| 008E48EA | 70 bytes | xbreadfail_sp | (as the game's own times) | v5.20 · 2026-10-17 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 003772FC | 0C0E1348 | 0C038CDC | jal 0x384d20 | jal 0xe3370 | Hook: objectives update's Assault tick: Auto-Complete Phase first (was jal 0x384D20; delay slot nop kept) | v5.11 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E3370-000E35C3 | 149 | ASK: timer is for + 1 (0 none: RAM starts at 0), the match clock / gameframe when it started, gameframe last seen jal at 0x3772FC (objectives update's Assault tick, was jal 0x384D20): the skip check and the time bonus, then the tick (same args) | v5.106 · 2026-10-29 |
| 000E7F4C-000E8057 | 67 | ASITEM: Assault menu: Auto-Complete Phase (Off, 1 Min .. 10 Mins, as the game's own times) | v5.11 · 2026-10-16 |
| 000EC2B8-000EC353 | 39 | TBITEM: Assault menu: Time Bonus After Phase (Off, 1 Min, 2 Mins, 3 Mins) | v5.20 · 2026-10-17 |
| 000ED9A0-000EDA1B | 31 | TBRA: a0 = page, a1 = 0 refresh / 1 apply: Time Bonus After Phase value (0-3); refresh greys it out with no time limit | v5.20 · 2026-10-17 |
| 000EF51C-000EF56F | 21 | ASRA: a0 = page, a1 = 0 refresh / 1 apply: Auto-Complete Phase value (0-10) | v5.11 · 2026-10-16 |
| 000F0874-000F088B | 6 | LTB: text | v5.20 · 2026-10-17 |
| 000F08B4-000F08C7 | 5 | LAS: text | v5.11 · 2026-10-16 |
| 000F0C08-000F0C0F | 2 | LAS1: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C10-000F0C17 | 2 | LAS2: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C18-000F0C1F | 2 | LAS3: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C20-000F0C27 | 2 | LAS4: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C28-000F0C2F | 2 | LAS5: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C30-000F0C37 | 2 | LAS6: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C38-000F0C3F | 2 | LAS7: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C40-000F0C47 | 2 | LAS8: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C48-000F0C4F | 2 | LAS9: text | v5.11 · 2026-10-16 (approx.) |
| 000F0C50-000F0C57 | 2 | LAS10: text | v5.11 · 2026-10-16 (approx.) |

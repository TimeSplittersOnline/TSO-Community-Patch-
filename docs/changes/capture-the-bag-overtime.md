# Capture the Bag: Overtime

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00068DBC | 058DBC | 8 | `85 c0 0f 8f a8 00 00 00` | `e9 17 b4 87 00 90 90 90` | time limit check: was test %eax,%eax / jg 0x68e6c (Overtime) \| time limit check (jmp at 0x68dbc, was test %eax,%eax / jg 0x68e6c; eax = time left): time not up -> 0x68e6c. Time up: \| time limit check (jmp at 0x68dbc, was test %eax,%eax / jg 0x68e6c; eax = time left): time not up -> 0x68e6c. Time up: Overtime holds the match (once) while a bag is carried, else the game's time-up at 0x68dc4 | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E4144 | 44 bytes | xbreadfail_sp | a new match (gameframe went back into the first 20 seconds) clears the overtime state; keeps all but eax | v5.16 · 2026-10-17 |
| 008E4170 | 61 bytes | xbreadfail_sp | eax = 1 when Overtime applies to the match being played (Capture the Bag; offline / LAN host: the setting; LAN player: the host's, setup byte 72 bit 2 under its 0xB0 marker); keeps ecx/edx | v5.89 · 2026-10-27 |
| 008E41AD | 43 bytes | xbreadfail_sp | eax = 1 when any active chr is carrying a bag (chr +0x80); keeps ecx/edx | v5.3 · 2026-10-16 |
| 008E41D8 | 81 bytes | xbreadfail_sp | time limit check (jmp at 0x68dbc, was test %eax,%eax / jg 0x68e6c; eax = time left): time not up -> 0x68e6c. Time up: Overtime holds the match (once) while a bag is carried, else the game's time-up at 0x68dc4 | v5.64 · 2026-10-22 |
| 008E4229 | 64 bytes | xbreadfail_sp | the Text Sweep sound (SND_SWEEP 3433, the way the game plays it: 48-byte sound parms) and "Overtime!" to every local player; keeps all | v5.3 · 2026-10-16 |
| 008E4269 | 112 bytes | xbreadfail_sp | LAN player with the patch: "Overtime!" once the host's time has run out but the match has gone on for 1.5 seconds (the host holds it in overtime). The time-up check above only sees bag carriers this game knows about, which misses other players carrying a bag. Only after time was left this match (no time limit: the time left stays 0); keeps all | v5.15 · 2026-10-16 |
| 008E42D9 | 86 bytes | xbreadfail_sp | Capture the Bag menu: Overtime | v5.64 · 2026-10-22 |
| 008E432F | 65 bytes | xbreadfail_sp | Capture the Bag menu: Overtime | v5.3 · 2026-10-16 |
| 008E4370 | 46 bytes | xbreadfail_sp | refresh / apply (esi = page) | v5.19 · 2026-10-17 |
| 008E439E | 30 bytes | xbreadfail_sp | Code: XOTA (see the code shown) | v5.3 · 2026-10-16 |
| 008E43BC | 4 bytes | xbreadfail_sp | Data: XOTLAST | v5.3 · 2026-10-16 (approx.) |
| 008E43C0 | 1 bytes | xbreadfail_sp | Data: XOTST | v5.3 · 2026-10-16 (approx.) |
| 008E43C1 | 1 bytes | xbreadfail_sp | LAN player: the host's time left was seen above 0 this match | v5.3 · 2026-10-16 (approx.) |
| 008E43C4 | 4 bytes | xbreadfail_sp | LAN player: frames the host's time has been up while the match goes on | v5.3 · 2026-10-16 (approx.) |
| 008E79E4 | 9 bytes | xbreadfail_sp | Menu / message text "Overtime" | v5.3 · 2026-10-16 |
| 008E7A0D | 10 bytes | xbreadfail_sp | Menu / message text "Overtime!" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013E53C | 1DC00013 | 0803A534 | bgtz t6,0x13e58c | j 0xe94d0 | Hook: time limit check: was bgtz t6,0x13E58C (Overtime; delay slot lui t7,0x63 kept) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E7C3C-000E7D4F | 69 | OTCL: LAN player with the patch: "Overtime!" once the host's time has run out but the match has gone on for 1.5 s (the host holds it in overtime). The time-up check (OTH) only sees bag carriers this game knows about, which misses | v5.15 · 2026-10-16 |
| 000E94D0-000E95B3 | 57 | OTH: j at 0x13E53C (was bgtz t6,0x13E58C; its delay slot lui t7,0x63 done; t6 = time left): time not up -> 0x13E58C. Time up: Overtime holds the match (once) while a bag is carried, else the game's time-up at 0x13E544 | v5.64 · 2026-10-22 |
| 000EB248-000EB2F7 | 44 | OTT: every frame (called at the start of GGT): new-match check; host / offline in overtime: once no bag is carried, or after a minute of it, 1 frame of time left, so the game's own time-up ends the match this frame | v5.64 · 2026-10-22 |
| 000EB70C-000EB7B7 | 43 | OTON: leaf: v0 = 1 when Overtime applies to the match being played (Capture the Bag; offline / LAN host: the setting; LAN player: the host's, setup byte 72 bit 2 under its 0xB0 marker); uses t8,t9 | v5.89 · 2026-10-27 |
| 000ED3C0-000ED43B | 31 | OTITEM: Capture the Bag menu: Overtime | v5.3 · 2026-10-16 |
| 000ED8EC-000ED95F | 29 | OTRA: a0 = page, a1 = 0 refresh / 1 apply: Overtime value; refresh greys it out with no time limit (time never runs out) | v5.19 · 2026-10-17 |
| 000EF1B0-000EF1FB | 19 | OTRST: leaf: a new match clears the overtime state; uses t8,t9,v1 | v5.16 · 2026-10-17 |
| 000EF7C8-000EF807 | 16 | OTBAG: leaf: v0 = 1 when any active chr is carrying a bag (character record +128); uses t7-t9 | v5.3 · 2026-10-16 |
| 000F04C0-000F04CB | 3 | LOTI: text | v5.3 · 2026-10-16 (approx.) |
| 000F04FC-000F0507 | 3 | LOT: text | v5.3 · 2026-10-16 |

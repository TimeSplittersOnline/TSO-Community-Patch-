# Capture the Bag: Overtime

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00068DBC | 058DBC | 8 | `85 c0 0f 8f a8 00 00 00` | `e9 43 b4 87 00 90 90 90` | time limit check: was test %eax,%eax / jg 0x68e6c (Overtime) \| time limit check (jmp at 0x68dbc, was test %eax,%eax / jg 0x68e6c; eax = time left): time not up -> 0x68e6c. Time up: \| time limit check (jmp at 0x68dbc, was test %eax,%eax / jg 0x68e6c; eax = time left): time not up -> 0x68e6c. Time up: Overtime holds the match (once) while a bag is carried, else the game's time-up at 0x68dc4 | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E4170 | 44 bytes | xbreadfail_sp | a new match (gameframe went back into the first 20 seconds) clears the overtime state; keeps all but eax | v5.16 · 2026-10-17 |
| 008E419C | 61 bytes | xbreadfail_sp | eax = 1 when Overtime applies to the match being played (Capture the Bag; offline / LAN host: the setting; LAN player: the host's, setup byte 72 bit 2 under its 0xB0 marker); keeps ecx/edx | v5.89 · 2026-10-27 |
| 008E41D9 | 43 bytes | xbreadfail_sp | eax = 1 when any active chr is carrying a bag (chr +0x80); keeps ecx/edx | v5.3 · 2026-10-16 |
| 008E4204 | 81 bytes | xbreadfail_sp | time limit check (jmp at 0x68dbc, was test %eax,%eax / jg 0x68e6c; eax = time left): time not up -> 0x68e6c. Time up: Overtime holds the match (once) while a bag is carried, else the game's time-up at 0x68dc4 | v5.64 · 2026-10-22 |
| 008E4255 | 64 bytes | xbreadfail_sp | the Text Sweep sound (SND_SWEEP 3433, the way the game plays it: 48-byte sound parms) and "Overtime!" to every local player; keeps all | v5.3 · 2026-10-16 |
| 008E4295 | 110 bytes | xbreadfail_sp | LAN player with the patch: "Overtime!" once the host's time has run out but the match has gone on for 3 seconds (the host holds it in overtime). The time-up check above only sees bag carriers this game knows about, which misses other players carrying a bag. Only after time was left this match (no time limit: the time left stays 0); keeps all | v5.106 · 2026-10-29 |
| 008E4303 | 86 bytes | xbreadfail_sp | Capture the Bag menu: Overtime | v5.64 · 2026-10-22 |
| 008E4359 | 65 bytes | xbreadfail_sp | Capture the Bag menu: Overtime | v5.3 · 2026-10-16 |
| 008E439A | 46 bytes | xbreadfail_sp | refresh / apply (esi = page) | v5.19 · 2026-10-17 |
| 008E43C8 | 32 bytes | xbreadfail_sp | Code: XOTA (see the code shown) | v5.106 · 2026-10-29 |
| 008E43E8 | 4 bytes | xbreadfail_sp | Data: XOTLAST | v5.3 · 2026-10-16 (approx.) |
| 008E43EC | 1 bytes | xbreadfail_sp | Data: XOTST | v5.3 · 2026-10-16 (approx.) |
| 008E43ED | 1 bytes | xbreadfail_sp | LAN player: the host's time left was seen above 0 this match | v5.3 · 2026-10-16 (approx.) |
| 008E43F0 | 4 bytes | xbreadfail_sp | LAN player: frames the host's time has been up while the match goes on | v5.3 · 2026-10-16 (approx.) |
| 008E7A34 | 9 bytes | xbreadfail_sp | Menu / message text "Overtime" | v5.3 · 2026-10-16 |
| 008E7A5D | 10 bytes | xbreadfail_sp | Menu / message text "Overtime!" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013E53C | 1DC00013 | 0803A56C | bgtz t6,0x13e58c | j 0xe95b0 | Hook: time limit check: was bgtz t6,0x13E58C (Overtime; delay slot lui t7,0x63 kept) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E7E34-000E7F43 | 68 | OTCL: LAN player with the patch: "Overtime!" once the host's time has run out but the match has gone on for 3 s (the host holds it in overtime). The time-up check (OTH) only sees bag carriers this game knows about, which misses | v5.106 · 2026-10-29 |
| 000E95B0-000E9693 | 57 | OTH: j at 0x13E53C (was bgtz t6,0x13E58C; its delay slot lui t7,0x63 done; t6 = time left): time not up -> 0x13E58C. Time up: Overtime holds the match (once) while a bag is carried, else the game's time-up at 0x13E544 | v5.64 · 2026-10-22 |
| 000EB328-000EB3D7 | 44 | OTT: every frame (called at the start of GGT): new-match check; host / offline in overtime: once no bag is carried, or after a minute of it, 1 frame of time left, so the game's own time-up ends the match this frame | v5.64 · 2026-10-22 |
| 000EB7EC-000EB897 | 43 | OTON: leaf: v0 = 1 when Overtime applies to the match being played (Capture the Bag; offline / LAN host: the setting; LAN player: the host's, setup byte 72 bit 2 under its 0xB0 marker); uses t8,t9 | v5.89 · 2026-10-27 |
| 000ED77C-000ED7F7 | 31 | OTITEM: Capture the Bag menu: Overtime | v5.3 · 2026-10-16 |
| 000EDCA8-000EDD1B | 29 | OTRA: a0 = page, a1 = 0 refresh / 1 apply: Overtime value; refresh greys it out with no time limit (time never runs out) | v5.19 · 2026-10-17 |
| 000EF550-000EF59B | 19 | OTRST: leaf: a new match clears the overtime state; uses t8,t9,v1 | v5.16 · 2026-10-17 |
| 000EFB68-000EFBA7 | 16 | OTBAG: leaf: v0 = 1 when any active chr is carrying a bag (character record +128); uses t7-t9 | v5.3 · 2026-10-16 |
| 000F0878-000F0883 | 3 | LOTI: text | v5.3 · 2026-10-16 (approx.) |
| 000F08B4-000F08BF | 3 | LOT: text | v5.3 · 2026-10-16 |

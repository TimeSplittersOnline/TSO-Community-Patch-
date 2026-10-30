# Team VIP

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00064ECC | 054ECC | 12 | `3b 05 20 d1 82 00 0f 85 52 01 00 00` | `e9 61 49 88 00 90 90 90 90 90 90 90` | killing the VIP (jmp at 0x64ecc in add-kill routine' Gladiator check; eax = killer prop, | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E94B0 | 238 bytes | xbreadfail_sp | Team VIP timer: per frame (call at 0x68c2f via 0x8e9841, replaces call 0x651f0; its argument is already pushed). Every 5 seconds, if the same VIP has moved at least 8 units (x/z) since the last tick, the VIP's team scores a point and so does every player on it | v5.34 · 2026-10-18 |
| 008E959E | 52 bytes | xbreadfail_sp | ZF clear when Team VIP applies (setting on, Gladiator, Teamplay, offline or host) | v5.89 · 2026-10-27 |
| 008E95D2 | 4 bytes | xbreadfail_sp | 8 units squared (xgg_patch.py writes it into the XBE) | v5.3 · 2026-10-16 (approx.) |
| 008E989A | 65 bytes | xbreadfail_sp | the mode's own items (first on the Advanced page): Capture the Bag: Reverse Scoring, Score With Bag Away; Virus: Spread By Kills (LAN) | v5.3 · 2026-10-16 |
| 008E9DD4 | 59 bytes | xbreadfail_sp | ---- Team VIP (Gladiator + Teamplay, host / offline): the Gladiator is the VIP. Every 5 seconds the VIP's team scores a point and so does every player on it (scores reach every player through the host's score updates) ZF clear (jnz) when Team VIP applies; keeps all registers | v5.89 · 2026-10-27 |
| 008E9E0F | 31 bytes | xbreadfail_sp | kill count routine (call at 0x64afc, replaces call to the multikill code): esi chr, edi kills | v5.3 · 2026-10-16 |
| 008E9E2E | 89 bytes | xbreadfail_sp | killing the VIP (jmp at 0x64ecc in add-kill routine' Gladiator check; eax = killer prop, | v5.3 · 2026-10-16 |
| 008E9E87 | 14 bytes | xbreadfail_sp | Menu / message text "Infinite Ammo" | v5.3 · 2026-10-16 |
| 008E9E95 | 4 bytes | xbreadfail_sp | Menu / message text "Off" | v5.3 · 2026-10-16 (approx.) |
| 008E9E99 | 3 bytes | xbreadfail_sp | Menu / message text "On" | v5.3 · 2026-10-16 (approx.) |
| 008E9ED0 | 146 bytes | xbreadfail_sp | Menu / message text "Team VIP" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013A7F0 | 15ED002C | 0803FA50 | bne t7,t5,0x13a8a4 | j 0xfe940 | new[0x13A7F0]=j(0xFE940) | v5.3 · 2026-10-16 |
| 0013E3DC | 0C04EB30 | 0C03FB68 | jal 0x13acc0 | jal 0xfeda0 | new[0x13E3DC]=jal(0xFEDA0) | v5.3 · 2026-10-16 |
| 00232798 | 27BDFFA0 | 0803FA90 | addiu sp,sp,-96 | j 0xfea40 | new[0x232798]=j(0xFEA40) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000EA614-000EA6D7 | 49 | VIPAD2: Team VIP's kill count routine step (ia.py: j from the multikill code's exit at 0xFF5C0; delay slot lw t6,108(t7) done, keep t6 / t7): s0 += the chr's VIP points (VBON 0xFEFC0) when Team VIP applies (on, Gladiator with Teamplay, offline / LAN | v5.89 · 2026-10-27 |
| 000F0824-000F082F | 3 | LVIP: text | v5.3 · 2026-10-16 (approx.) |
| 000FE940-000FEA3B | 63 | for _i,_x in enumerate(_w): new[0xFE940+4*_i]=_x | v5.89 · 2026-10-27 |
| 000FEA40-000FEAC7 | 34 | for _i,_x in enumerate(_w): new[0xFEA40+4*_i]=_x | v5.3 · 2026-10-16 |
| 000FEDA0-000FEF4F | 108 | for _i,_x in enumerate(_w): new[0xFEDA0+4*_i]=_x | v5.89 · 2026-10-27 |
| 000FEF50-000FEFBF | 28 | for _x in range(_e,VBON,4): new[_x]=0 | v5.3 · 2026-10-16 (approx.) |

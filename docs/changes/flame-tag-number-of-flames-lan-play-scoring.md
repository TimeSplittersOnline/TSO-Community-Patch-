# Flame Tag: Number of Flames, LAN play, scoring

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00068B37 | 058B37 | 32 | `80 3d 56 d2 82 00 0b 75 17 8b 04 9d 80 23 7f 00 85 c0 74 0c 8b 0d c4 c8 4e 00 29 88 64 0a 00 00` | `e8 0d f9 87 00 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90` | ---------------- scoring: every burning chr loses time (call at 0x68b37) \| ---------------- scoring: every burning chr loses time (call at 0x68b37) | v5.3 · 2026-10-16 |
| 00068FE5 | 058FE5 | 10 | `e8 46 f9 ff ff e8 71 03 1d 00` | `e8 ec f3 87 00 e8 b9 8e fa ff` | Flame Tag: run the mod's offline flame logic (0x8E83D6) before the flame tag tick; then the Mercy Rule check (0x11EA8) for this mode. | v5.3 · 2026-10-16 |
| 000BB092 | 0AB092 | 7 | `80 3d 56 d2 82 00 0c` | `e8 f0 d3 82 00 90 90` | ---------------- hit slowdown exemption (call at 0xbb092): ZF=1 -> check burning bit \| ---------------- hit slowdown exemption (call at 0xbb092): ZF=1 -> check burning bit | v5.3 · 2026-10-16 |
| 0035624E | 34624E | 6 | `3b 0d 6c dc 4e 00` | `e8 fa c0 58 00 90` | host's scores-to-clients timer (call at 0x35624e, was cmp FPS,%ecx; jle follows): Flame Tag sends the scores 8 times a \| host's scores-to-clients timer (call at 0x35624e, was cmp FPS,%ecx; jle follows): Flame Tag sends the scores 8 times a second instead of once, so clients' burn times count up smoothly; ecx = timer | v5.3 · 2026-10-16 |
| 003562A4 | 3462A4 | 7 | `a0 56 d2 82 00 3c 0c` | `e8 17 21 59 00 90 90` | ---------------- host per-net-frame check (call at 0x3562a4, replaces mov al,[mod]; cmp al,0xc) \| ---------------- host per-net-frame check (call at 0x3562a4, replaces mov al,[mod]; cmp al,0xc) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E234D | 27 bytes | xbreadfail_sp | host's scores-to-clients timer (call at 0x35624e, was cmp FPS,%ecx; jle follows): Flame Tag sends the scores 8 times a second instead of once, so clients' burn times count up smoothly; ecx = timer | v5.102 · 2026-10-29 |
| 008E8000 | 192 bytes | xbreadfail_sp | Flame Tag / Respawn Delay settings and state (COOL, FLAMES, respawn-delay tables). | v5.3 · 2026-10-16 |
| 008E80C0 | 17 bytes | xbreadfail_sp | Menu / message text "Number of Flames" | v5.3 · 2026-10-16 |
| 008E80D1 | 9 bytes | xbreadfail_sp | Menu / message text "1 Player" | v5.3 · 2026-10-16 |
| 008E80DA | 10 bytes | xbreadfail_sp | Menu / message text "2 Players" | v5.3 · 2026-10-16 |
| 008E80E4 | 10 bytes | xbreadfail_sp | Menu / message text "3 Players" | v5.3 · 2026-10-16 |
| 008E80EE | 10 bytes | xbreadfail_sp | Menu / message text "4 Players" | v5.3 · 2026-10-16 |
| 008E80F8 | 10 bytes | xbreadfail_sp | Menu / message text "5 Players" | v5.3 · 2026-10-16 |
| 008E8216 | 394 bytes | xbreadfail_sp | ---------------- XFT2: flame tag host/offline logic (cdecl, preserves callee regs) | v5.89 · 2026-10-27 |
| 008E83A0 | 4 bytes | xbreadfail_sp | Code: C144 (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E83A4 | 12 bytes | xbreadfail_sp | Code: C16 (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E83B0 | 16 bytes | xbreadfail_sp | ---------------- host per-net-frame check (call at 0x3562a4, replaces mov al,[mod]; cmp al,0xc) | v5.3 · 2026-10-16 (approx.) |
| 008E83C0 | 22 bytes | xbreadfail_sp | ---------------- host per-net-frame check (call at 0x3562a4, replaces mov al,[mod]; cmp al,0xc) | v5.3 · 2026-10-16 |
| 008E83D6 | 115 bytes | xbreadfail_sp | ---------------- offline: before flame tag tick (call at 0x68fe5) | v5.3 · 2026-10-16 |
| 008E8449 | 62 bytes | xbreadfail_sp | ---------------- scoring: every burning chr loses time (call at 0x68b37) | v5.3 · 2026-10-16 |
| 008E8487 | 26 bytes | xbreadfail_sp | ---------------- hit slowdown exemption (call at 0xbb092): ZF=1 -> check burning bit | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0043E460 / PAL 0043E4B0 | 562F001E | 122F0002 | bnel s1,t7,0x43e4dc | beq s1,t7,0x43e46c | Flame Tag: allow it in the network/arcade mode list (adds mode 11 to the list of allowed modes) | v5.3 · 2026-10-16 |
| 0043E464 / PAL 0043E4B4 | 26310001 | 240F000B | addiu s1,s1,1 | addiu t7,zero,11 | Flame Tag: allow it in the network/arcade mode list (adds mode 11 to the list of allowed modes) | v5.3 · 2026-10-16 |
| 0043E468 / PAL 0043E4B8 | 3C0E006B | 162F001B | lui t6,0x6b | bne s1,t7,0x43e4d8 | Flame Tag: allow it in the network/arcade mode list (adds mode 11 to the list of allowed modes) | v5.3 · 2026-10-16 |
| 00628530 / PAL 00628630 | 00000000 | 00000001 | nop | .word 0x00000001 | Flame Tag (hidden mode, re-enabled): show it in the mode list | v5.3 · 2026-10-16 |
| 004F1338 / PAL 004F13E0 | 91AE004E | 0C03F2E0 | lbu t6,78(t5) | jal 0xfcb80 | Flame Tag on LAN (host only): the host sends the "who is on fire" status every network frame (as it does for Virus), and passes the flame when the player on fire touches another player (1.2m, 1.5s cooldown) | v5.3 · 2026-10-16 |
| 004F133C / PAL 004F13E4 | 240F000C | 00000000 | addiu t7,zero,12 | nop | Flame Tag on LAN (host only): the host sends the "who is on fire" status every network frame (as it does for Virus), and passes the flame when the player on fire touches another player (1.2m, 1.5s cooldown) | v5.3 · 2026-10-16 |
| 0013E6E0 | 0C04F65A | 0C03F134 | jal 0x13d968 | jal 0xfc4d0 | Flame Tag offline: run the same flame-passing check in local matches and move the flames to the new "it" player (burning bots get the no-fire-damage handler, as in Virus) | v5.3 · 2026-10-16 |
| 001AF538 | 240E000C | 0C03F8F9 | addiu t6,zero,12 | jal 0xfe3e4 | Flame Tag offline: the "it" player is not slowed by the burning hit reaction (same exemption Virus has); online unchanged so everyone keeps the same speed | v5.3 · 2026-10-16 |
| 0013DB64 | 3C0F0063 | 0803F39C | lui t7,0x63 | j 0xfce70 | Flame Tag scoring: every burning player gains burn time (the game only counted one "it" player) Flame Tag on LAN: the host sends the scores to the other players 8 times a second instead of once a second, so their scoreboard burn times count up smoothly (the game's own scores packet, so unpatched players get it too; code with Weapon Mode, hook at 0x004F12BC) | v5.3 · 2026-10-16 |
| 0013DB68 | 8DEE8FB0 | 00000000 | lw t6,-28752(t7) | nop | Flame Tag scoring: every burning player gains burn time (the game only counted one "it" player) Flame Tag on LAN: the host sends the scores to the other players 8 times a second instead of once a second, so their scoreboard burn times count up smoothly (the game's own scores packet, so unpatched players get it too; code with Weapon Mode, hook at 0x004F12BC) | v5.3 · 2026-10-16 |
| 004F12BC / PAL 004F1364 | 8DCFEBA8 | 0C03BFE5 | lw t7,-5208(t6) | jal 0xeff94 | Hook: scores to LAN players: was lw t7,-5208(t6) / slt t7,t7,t5 | v5.3 · 2026-10-16 |
| 004F12C0 / PAL 004F1368 | 01ED782A | 00000000 | slt t7,t7,t5 | nop | Hook: scores to LAN players: was lw t7,-5208(t6) / slt t7,t7,t5 | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FC4D0-000FC5A7 | 54 | Flame Tag offline: run the same flame-passing check in local matches and move the flames to the new "it" player (burning bots get the no-fire-damage handler, as in Virus) | v5.3 · 2026-10-16 |
| 000FE3E4-000FE3FF | 7 | Flame Tag offline: the "it" player is not slowed by the burning hit reaction (same exemption Virus has); online unchanged so everyone keeps the same speed | v5.3 · 2026-10-16 |
| 000FC920-000FCE6F | 264 | Flame Tag: "Number of Flames" (Advanced Settings, 1-5 Players): host/offline keeps that many players on fire; flames still pass by touch (unpatched players see every flame). Covers up to 16 characters (players + bots) | v5.89 · 2026-10-27 |
| 000FCE70-000FCEC3 | 21 | Flame Tag scoring: every burning player gains burn time (the game only counted one "it" player) Flame Tag on LAN: the host sends the scores to the other players 8 times a second instead of once a second, so their scoreboard burn times count up smoothly (the game's own scores packet, so unpatched players get it too; code with Weapon Mode, hook at 0x004F12BC) | v5.3 · 2026-10-16 |
| 000EFF94-000EFFBB | 10 | SCTIM: jal at 0x4F12BC (host's scores-to-clients timer; was lw t7,FPS / slt t7,t7,t5): Flame Tag sends the scores 8 times a second instead of once, so clients' burn times count up smoothly; t5 = timer | v5.3 · 2026-10-16 |

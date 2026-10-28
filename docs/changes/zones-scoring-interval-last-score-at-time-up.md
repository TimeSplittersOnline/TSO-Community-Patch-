# Zones: Scoring Interval, last score at time up

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00065FDD | 055FDD | 9 | `8b 0d 6c dc 4e 00 6b c9 0f` | `e8 b3 2c 88 00 90 90 90 90` | zones tick (call at 0x65fdd): ecx = interval, eax kept \| zones tick (call at 0x65fdd): ecx = interval, eax kept | v5.3 · 2026-10-16 |
| 0013F8A7 | 12F8A7 | 8 | `a1 6c dc 4e 00 6b c0 0f` | `e8 94 93 7a 00 90 90 90` | eax = Zones scoring interval in frames (host/offline: own setting; LAN player: host's value if sent, else 15s). keeps other registers | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E8C10 | 40 bytes | xbreadfail_sp | time up (host / offline path, call at 0x68e27): Zones scores the held zones once more before the match ends | v5.3 · 2026-10-16 |
| 008E8C40 | 85 bytes | xbreadfail_sp | eax = Zones scoring interval in frames (host/offline: own setting; LAN player: host's value if sent, else 15s). keeps other registers | v5.89 · 2026-10-27 |
| 008E8C95 | 10 bytes | xbreadfail_sp | zones tick (call at 0x65fdd): ecx = interval, eax kept | v5.3 · 2026-10-16 |
| 008E8C9F | 21 bytes | xbreadfail_sp | LAN host: team-list byte 74 = 0xC0 \| interval (jmp at 0x11535 / 0x117f8) | v5.3 · 2026-10-16 |
| 008E8D0C | 67 bytes | xbreadfail_sp | refresh loop step (jmp at 0x8e8620): ids 28, 40-44, then the interval item | v5.3 · 2026-10-16 |
| 008E8D4F | 69 bytes | xbreadfail_sp | apply loop step (jmp at 0x8e865b) | v5.3 · 2026-10-16 |
| 008E8D94 | 4 bytes | xbreadfail_sp | Data: SECT | v5.3 · 2026-10-16 (approx.) |
| 008E8D98 | 4 bytes | xbreadfail_sp | Data: PERM | v5.3 · 2026-10-16 (approx.) |
| 008E8D9C | 22 bytes | xbreadfail_sp | Menu / message text "Zone Scoring Interval" | v5.3 · 2026-10-16 |
| 008E8DB2 | 11 bytes | xbreadfail_sp | Menu / message text "10 Seconds" | v5.3 · 2026-10-16 |
| 008E8DBD | 11 bytes | xbreadfail_sp | Menu / message text "15 Seconds" | v5.3 · 2026-10-16 |
| 008E8DC8 | 10 bytes | xbreadfail_sp | Menu / message text "20 Seconds" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013E578 | 0C04F22E | 0C03BA62 | jal 0x13c8b8 | jal 0xee988 | Zones: when time runs out, held zones score once more before the match ends (the last 15-second scoring tick landed after the end, so the final 15 seconds never counted). Host only on LAN (the player scores on the results screen are refreshed too) | v5.3 · 2026-10-16 |
| 0013DDCC | 000E7900 | 0C03EEF4 | sll t7,t6,4 | jal 0xfbbd0 | Zones: "Zone Scoring Interval" (Advanced Settings, 10/15/20 Seconds, default 15). The host scores on its setting and sends it to patched players (spare team-list byte); players without the patch still get the right scores from the host | v5.89 · 2026-10-27 |
| 0013DDD0 | 01EE7823 | 00000000 | subu t7,t7,t6 | nop | Zones: "Zone Scoring Interval" (Advanced Settings, 10/15/20 Seconds, default 15). The host scores on its setting and sends it to patched players (spare team-list byte); players without the patch still get the right scores from the host | v5.89 · 2026-10-27 |
| 0013A910 | 000E7C00 | 00000000 | sll t7,t6,16 | nop | Hook: new[0x13A910]=NOP | v5.40 · 2026-10-19 |
| 001448C0 | AFC00000 | AFC00000 | sw zero,0(fp) | sw zero,0(fp) | Hook: (an earlier Switch Spawns hook there, on the Assault path, removed: the original word) | v5.3 · 2026-10-16 |
| 001B8118 | 01F27804 | 01F27804 | sllv t7,t7,s2 | sllv t7,t7,s2 | Hook: zone beams removed again: original words back (sllv / sw / sllv) | v5.3 · 2026-10-16 |
| 001B811C | ADAF0040 | ADAF0040 | sw t7,64(t5) | sw t7,64(t5) | Hook: zone beams removed again: original words back (sllv / sw / sllv) | v5.3 · 2026-10-16 |
| 001C9594 | 8C8F0014 | 8C8F0014 | lw t7,20(a0) | lw t7,20(a0) | Hook: (the hook moved to after the respawn test: the retail words again) | v5.76 · 2026-10-24 |
| 001C9598 | 8DF10004 | 8DF10004 | lw s1,4(t7) | lw s1,4(t7) | Hook: (the hook moved to after the respawn test: the retail words again) | v5.76 · 2026-10-24 |
| 001CE4D8 | C6400C04 | C6400C04 | lwc1 zero,3076(s2) | lwc1 zero,3076(s2) | Hook: (v5.45-v5.47's Venice gondola hooks | v5.47 · 2026-10-20 |
| 001CE4DC | 46000836 | 46000836 | .word 0x46000836 | .word 0x46000836 | Hook: (v5.45-v5.47's Venice gondola hooks | v5.47 · 2026-10-20 |
| 002620DC | 11E00225 | 11E00225 | beq t7,zero,0x262974 | beq t7,zero,0x262974 | Hook: name tags' Teamplay check: the game's own again (beq t7,zero,0x262974 / nop; v5.90-v5.91's HTTP | v5.92 · 2026-10-27 |
| 002620E0 | 00000000 | 00000000 | nop | nop | Hook: name tags' Teamplay check: the game's own again (beq t7,zero,0x262974 / nop; v5.90-v5.91's HTTP | v5.92 · 2026-10-27 |
| 0036F270 | 0C1409A0 | 0C1409A0 | jal 0x502680 | jal 0x502680 | Hook: removed: their original words back) | v5.47 · 2026-10-20 |
| 0046DA4C / PAL 0046DAEC | 0C053A3C | 0C053A3C | jal 0x14e8f0 | jal 0x14e8f0 | Hook: (Return to Lobby removed on PS2: the original words back) | v5.68 · 2026-10-23 |
| 0046ECF8 / PAL 0046ED98 | 0C13D554 | 0C13D554 | jal 0x4f5550 | jal 0x4f5550 | Hook: (Return to Lobby removed on PS2: the original words back) | v5.68 · 2026-10-23 |
| 0047759C / PAL 0047763C | 0C13D554 | 0C13D554 | jal 0x4f5550 | jal 0x4f5550 | Hook: (Return to Lobby removed on PS2: the original words back) | v5.68 · 2026-10-23 |
| 004F8960 / PAL 004F8A08 | 15600012 | 15600012 | bne t3,zero,0x4f89ac | bne t3,zero,0x4f89ac | Hook: new[0x4F8960]=0x15600012; new[0x4F8984]=0x3C0F0075; new[0x4F8988]=0x25EF3C24 | v5.3 · 2026-10-16 |
| 004F8984 / PAL 004F8A2C | 3C0F0075 | 3C0F0075 | lui t7,0x75 | lui t7,0x75 | Hook: new[0x4F8960]=0x15600012; new[0x4F8984]=0x3C0F0075; new[0x4F8988]=0x25EF3C24 | v5.3 · 2026-10-16 |
| 004F8988 / PAL 004F8A30 | 25EF3C24 | 25EF3C24 | addiu t7,t7,15396 | addiu t7,t7,15396 | Hook: new[0x4F8960]=0x15600012; new[0x4F8984]=0x3C0F0075; new[0x4F8988]=0x25EF3C24 | v5.3 · 2026-10-16 |
| 004FC884 / PAL 004FC92C | C66000B0 | C66000B0 | lwc1 zero,176(s3) | lwc1 zero,176(s3) | Hook: (v5.45-v5.47's Venice gondola hooks | v5.47 · 2026-10-20 |
| 00500D88 / PAL 00500E30 | 01E75804 | 01E75804 | sllv t3,t7,a3 | sllv t3,t7,a3 | Hook: zone beams removed again: original words back (sllv / sw / sllv) | v5.3 · 2026-10-16 |
| 006284A0 / PAL 006285A0 | 00000000 | 00000001 | nop | .word 0x00000001 | Hook: mode table, Bag Tag: team spawn points used (was 0: the setup always had 0x2000000, so Bag Tag | v5.39 · 2026-10-19 |
| 006284BC / PAL 006285BC | 00000000 | 00000002 | nop | srl zero,zero,0 | Hook: mode table, Elimination: Teamplay possible (2), its team spawn points (1) (Team Elimination) | v5.40 · 2026-10-19 |
| 006284C0 / PAL 006285C0 | 00000000 | 00000001 | nop | .word 0x00000001 | Hook: mode table, Elimination: Teamplay possible (2), its team spawn points (1) (Team Elimination) | v5.40 · 2026-10-19 |
| 006284FC / PAL 006285FC | 00000000 | 00000002 | nop | srl zero,zero,0 | Hook: Vampire: the same | v5.40 · 2026-10-19 |
| 00628500 / PAL 00628600 | 00000000 | 00000001 | nop | .word 0x00000001 | Hook: Vampire: the same | v5.40 · 2026-10-19 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FB9E0-000FBA3B | 23 | Zones: when time runs out, held zones score once more before the match ends (the last 15-second scoring tick landed after the end, so the final 15 seconds never counted). Host only on LAN (the player scores on the results screen are refreshed too) | v5.3 · 2026-10-16 |
| 000FBA40-000FBC4B | 111 | Zones: "Zone Scoring Interval" (Advanced Settings, 10/15/20 Seconds, default 15). The host scores on its setting and sends it to patched players (spare team-list byte); players without the patch still get the right scores from the host | v5.89 · 2026-10-27 |
| 000FBC50-000FE083 | 203 | Advanced Settings folders at the bottom: "Team Settings" (Teamplay, Disable [colour] Team; hidden in Capture the Bag / Assault) and "Spawn Settings" (Team Spawns, Respawn Delay / team delays). Advanced Settings keeps Disable Unarmed, Mercy Rule, Number of Flames, Zone Scoring Interval. Settings that can never apply to a mode are left out: modes that can never have teams (Deathmatch, Elimination, Vampire, Flame Tag, Virus, Monkey Assistant...) show no Team Settings folder and no Team Spawns item, and the Spawn Settings folder is left out too when it would be empty (Gladiator counts as a team mode because Team VIP can turn teams on). Layout: same look as the match settings page (small upper-case items); the mode's own settings come first, then Disable Unarmed, Mercy Rule, Multikill Bonus Window, Infinite Ammo, then the folder links ("Team Settings >", "Spawn Settings >") | v5.3 · 2026-10-16 |

# 4 Teams, team play in more modes

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 000C1CF0 | 0B1CF0 | 5 | `e8 5b d4 04 00` | `e8 cb f9 f4 ff` | Zone captured: turn on the zone flame through 0x116C0, which picks a yellow / green flame for teams 3 and 4 (was: game's own flame-on 0x10F150). | v5.3 · 2026-10-16 |
| 000C1D0E | 0B1D0E | 5 | `e8 3d d4 04 00` | `e8 ad f9 f4 ff` | As above, for the second flame-on call. | v5.3 · 2026-10-16 |
| 000C1D24 | 0B1D24 | 5 | `e8 27 d4 04 00` | `e8 97 f9 f4 ff` | As above, for the third flame-on call. | v5.3 · 2026-10-16 |
| 001104D0 | 1004D0 | 5 | `e8 0b cb ff ff` | `e8 3b 12 f0 ff` | Zone light colour: call the original 0x10CFE0, then 0x11710 tints the light yellow / green for teams 3 and 4. | v5.3 · 2026-10-16 |
| 0011095F | 10095F | 5 | `e8 7c c6 ff ff` | `e8 ac 0d f0 ff` | As above (another light-colour call). | v5.3 · 2026-10-16 |
| 00110D95 | 100D95 | 5 | `e8 46 c2 ff ff` | `e8 76 09 f0 ff` | As above (another light-colour call). | v5.3 · 2026-10-16 |
| 001113C8 | 1013C8 | 5 | `e8 13 bc ff ff` | `e8 43 03 f0 ff` | As above (another light-colour call). | v5.3 · 2026-10-16 |
| 001116F0 | 1016F0 | 5 | `e8 eb b8 ff ff` | `e8 1b 00 f0 ff` | As above (another light-colour call). | v5.3 · 2026-10-16 |
| 0013CE68 | 12CE68 | 9 | `80 3d 56 d2 82 00 04 75 2e` | `f6 05 58 d2 82 00 01 74 2e` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 00150336 | 140336 | 9 | `80 3d 56 d2 82 00 04 75 0d` | `f6 05 58 d2 82 00 01 74 0d` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C199B | 2B199B | 5 | `a0 4e e0 7b 00` | `a0 4d e0 7b 00` | 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C19A6 | 2B19A6 | 21 | `3c 04 8b 82 54 2f 79 00 0f 94 c1 99 8d 4c 09 02 f7 f9 8d 04 92` | `3c 06 8b 82 54 2f 79 00 0f 9d c1 99 8d 4c 09 02 e8 94 f9 d4 ff` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C1C7E | 2B1C7E | 5 | `a0 4e e0 7b 00` | `a0 4d e0 7b 00` | 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C1C91 | 2B1C91 | 11 | `3c 04 8b 82 54 2f 79 00 0f 94 c1` | `3c 06 8b 82 54 2f 79 00 0f 9d c1` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C1DE3 | 2B1DE3 | 5 | `a0 4e e0 7b 00` | `a0 4d e0 7b 00` | 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C1DED | 2B1DED | 5 | `3c 04 0f 94 c2` | `3c 06 0f 9d c2` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C34B0 | 2B34B0 | 14 | `8a 15 4e e0 7b 00 33 c9 80 fa 04 0f 94 c1` | `8a 15 4d e0 7b 00 33 c9 80 fa 06 0f 9d c1` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C36D3 | 2B36D3 | 15 | `a0 4e e0 7b 00 33 c9 3c 04 8b 45 04 0f 94 c1` | `a0 4d e0 7b 00 33 c9 3c 06 8b 45 04 0f 9d c1` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C6D3F | 2B6D3F | 6 | `8a 15 4e e0 7b 00` | `8a 15 4d e0 7b 00` | 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002D8000 | 2C8000 | 47 | `80 3d 4e e0 7b 00 04 c6 05 fd df 7b 00 02 c6 05 fc df 7b 00 01 75 17 c6 05 fb df 7b 00 04 c6 05 fe df 7b 00 03 c6 05 ff df 7b 00 04 eb 75 c6` | `e8 fb 94 d3 ff e9 99 00 00 00 df 7b 00 02 c6 05 fc df 7b 00 01 7c 17 c6 05 fb df 7b 00 04 c6 05 fe df 7b 00 03 c6 05 ff df 7b 00 04 eb 75 c6` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002D8015 | 2C8015 | 2 | `75 17` | `7c 17` | 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002D82AA | 2C82AA | 6 | `8a 15 4e e0 7b 00` | `8a 15 4d e0 7b 00` | 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002D82B5 | 2C82B5 | 13 | `80 fa 04 0f 94 c1 99 8d 4c 09 02 f7 f9` | `80 fa 06 0f 9d c1 99 e8 c5 90 d3 ff 90` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002D831D | 2C831D | 6 | `8a 15 4e e0 7b 00` | `8a 15 4d e0 7b 00` | 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002D8328 | 2C8328 | 13 | `80 fa 04 0f 94 c1 99 8d 4c 09 02 f7 f9` | `80 fa 06 0f 9d c1 99 e8 52 90 d3 ff 90` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002ED98F | 2DD98F | 9 | `80 3d 56 d2 82 00 04 75 04` | `f6 05 58 d2 82 00 01 74 04` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002ED9CC | 2DD9CC | 9 | `80 3d 56 d2 82 00 04 75 04` | `f6 05 58 d2 82 00 01 74 04` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 0035BC02 | 34BC02 | 10 | `80 3d 56 d2 82 00 04 0f 94 c3` | `b3 01 eb 06 82 00 06 0f 9d c3` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E230C | 32 bytes | xbreadfail_sp | number of team colours on the menus / LAN (jmp at 0x1105c, which counted 4 only for game type >= 6): 4 for Bag Tag (game type 1) too, as PS2 does; eax only. Used by the Select Team screen, the LAN team list, LAN default teams, Disable [colour] Team | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0042BD18 | 27BDFFF0 | 3C0E006B | addiu sp,sp,-16 | lui t6,0x6b | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD1C | 3C0E006B | 91CF4E06 | lui t6,0x6b | lbu t7,19974(t6) | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD20 | FFBE0000 | 3C0E0063 | sd fp,0(sp) | lui t6,0x63 | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD24 | 24020004 | 000F7940 | addiu v0,zero,4 | sll t7,t7,5 | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD28 | 91CF4E06 | 01EE7821 | lbu t7,19974(t6) | addu t7,t7,t6 | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD2C | 03A0F02D | 8DEF83D4 | daddu fp,sp,zero | lw t7,-31788(t7) | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD30 | 39EF0004 | 24020004 | xori t7,t7,0x4 | addiu v0,zero,4 | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD34 | 240E0002 | 25EFFFFE | addiu t6,zero,2 | addiu t7,t7,-2 | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD38 | 01CF100B | 2DEF0004 | movn v0,t6,t7 | sltiu t7,t7,4 | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD3C | 03C0E82D | 240E0002 | daddu sp,fp,zero | addiu t6,zero,2 | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD40 | DFBE0000 | 03E00008 | ld fp,0(sp) | jr ra | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD44 | 03E00008 | 01CF100B | jr ra | movn v0,t6,t7 | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0042BD48 | 27BD0010 | 00000000 | addiu sp,sp,16 | nop | team count (menu/LAN): look up mode type from mode table, 4 teams if type>=6 or Bag Tag | v5.3 · 2026-10-16 |
| 0044D1EC / PAL 0044D23C | 240F0004 | 00000000 | addiu t7,zero,4 | nop | LAN default teams: use team count (4 in four-team modes) | v5.3 · 2026-10-16 |
| 0044D200 / PAL 0044D250 | A22D003F | A222003F | sb t5,63(s1) | sb v0,63(s1) | LAN default teams: use team count (4 in four-team modes) | v5.3 · 2026-10-16 |
| 0044D210 / PAL 0044D260 | A22D003B | A222003B | sb t5,59(s1) | sb v0,59(s1) | LAN default teams: use team count (4 in four-team modes) | v5.3 · 2026-10-16 |
| 0062849C / PAL 0062859C | 00000000 | 00000002 | nop | srl zero,zero,0 | Bag Tag: teams optional (Teamplay option) | v5.3 · 2026-10-16 |
| 006284DC / PAL 006285DC | 00000000 | 00000002 | nop | srl zero,zero,0 | Shrink: teams optional | v5.3 · 2026-10-16 |
| 0062851C / PAL 0062861C | 00000000 | 00000002 | nop | srl zero,zero,0 | Thief: teams optional | v5.3 · 2026-10-16 |
| 00628520 / PAL 00628620 | 00000000 | 00000001 | nop | .word 0x00000001 | Thief: team flag | v5.3 · 2026-10-16 |
| 00628570 / PAL 00628670 | 00000000 | 00000001 | nop | .word 0x00000001 | Regeneration: enabled | v5.3 · 2026-10-16 |
| 00628580 / PAL 00628680 | 00000000 | 00000001 | nop | .word 0x00000001 | Regeneration: team flag | v5.3 · 2026-10-16 |
| 00628590 / PAL 00628690 | 00000000 | 00000001 | nop | .word 0x00000001 | Leech: enabled | v5.3 · 2026-10-16 |
| 006285A0 / PAL 006286A0 | 00000000 | 00000001 | nop | .word 0x00000001 | Leech: team flag | v5.3 · 2026-10-16 |
| 006285BC / PAL 006286BC | 00000001 | 00000002 | .word 0x00000001 | srl zero,zero,0 | Zones: teams optional | v5.3 · 2026-10-16 |
| 004F82A8 / PAL 004F8350 | 91CF004E | 91CF004D | lbu t7,78(t6) | lbu t7,77(t6) | team count (in match): read mode type | v5.3 · 2026-10-16 |
| 004F82B0 / PAL 004F8358 | 39EF0004 | 240F0000 | xori t7,t7,0x4 | addiu t7,zero,0 | team scores sent to LAN players: always all 4 teams | v5.3 · 2026-10-16 |
| 0025E6B0 | 3C0E00FF | 8E0F0050 | lui t6,0xff | lw t7,80(s0) | team HUD: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 0025E6B4 | 8E0F004C | 920E004D | lw t7,76(s0) | lbu t6,77(s0) | team HUD: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 0025E6B8 | 35CEFF00 | 31EF0001 | ori t6,t6,0xff00 | andi t7,t7,0x1 | team HUD: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 0025E6BC | 3C0D0004 | 25CEFFF7 | lui t5,0x4 | addiu t6,t6,-9 | team HUD: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 0025E6C0 | 01EE7824 | 11E00006 | and t7,t7,t6 | beq t7,zero,0x25e6dc | team HUD: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 0025E6C4 | 35AD0900 | 4600B306 | ori t5,t5,0x900 | .word 0x4600B306 | team HUD: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 0025E6C8 | 15ED0004 | 15C00004 | bne t7,t5,0x25e6dc | bne t6,zero,0x25e6dc | team HUD: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 00261B7C | 3C0E00FF | 8DAF0050 | lui t6,0xff | lw t7,80(t5) | team colours: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 00261B80 | 8DAF004C | 91AE004D | lw t7,76(t5) | lbu t6,77(t5) | team colours: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 00261B84 | 35CEFF00 | 31EF0001 | ori t6,t6,0xff00 | andi t7,t7,0x1 | team colours: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 00261B88 | 3C0D0004 | 25CEFFF7 | lui t5,0x4 | addiu t6,t6,-9 | team colours: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 00261B8C | 01EE7824 | 11E00016 | and t7,t7,t6 | beq t7,zero,0x261be8 | team colours: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 00261B90 | 35AD0900 | 24040001 | ori t5,t5,0x900 | addiu a0,zero,1 | team colours: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 00261B94 | 15ED0014 | 15C00014 | bne t7,t5,0x261be8 | bne t6,zero,0x261be8 | team colours: team game = type 9 and teams on | v5.3 · 2026-10-16 |
| 00475018 / PAL 004750B8 | 3C0D00FF | 8DEE8EA0 | lui t5,0xff | lw t6,-29024(t7) | scoreboard: kill-based score column only for Deathmatch-type team games | v5.90 · 2026-10-27 |
| 0047501C / PAL 004750BC | 8DEE8E9C | 91ED8E9D | lw t6,-29028(t7) | lbu t5,-29027(t7) | scoreboard: kill-based score column only for Deathmatch-type team games | v5.90 · 2026-10-27 |
| 00475020 / PAL 004750C0 | 35ADFF00 | 31CE0001 | ori t5,t5,0xff00 | andi t6,t6,0x1 | scoreboard: kill-based score column only for Deathmatch-type team games | v5.90 · 2026-10-27 |
| 00475024 / PAL 004750C4 | 3C0F0004 | 25ADFFF7 | lui t7,0x4 | addiu t5,t5,-9 | scoreboard: kill-based score column only for Deathmatch-type team games | v5.90 · 2026-10-27 |
| 00475028 / PAL 004750C8 | 01CD7024 | 0803B82E | and t6,t6,t5 | j 0xee0b8 | scoreboard: kill-based score column only for Deathmatch-type team games | v5.90 · 2026-10-27 |
| 0047502C / PAL 004750CC | 35EF0900 | 00000000 | ori t7,t7,0x900 | nop | scoreboard: kill-based score column only for Deathmatch-type team games | v5.90 · 2026-10-27 |
| 00475030 / PAL 004750D0 | 15CF002D | 00000000 | bne t6,t7,0x4750e8 | nop | scoreboard: kill-based score column only for Deathmatch-type team games | v5.90 · 2026-10-27 |
| 0046E988 / PAL 0046EA28 | 3C1300FF | 3C130000 | lui s3,0xff | lui s3,0x0 | pause menu team items | v5.3 · 2026-10-16 |
| 0046E990 / PAL 0046EA30 | 3C120004 | 3C120000 | lui s2,0x4 | lui s2,0x0 | pause menu team items | v5.3 · 2026-10-16 |
| 0046E994 / PAL 0046EA34 | 3673FF00 | 36730001 | ori s3,s3,0xff00 | ori s3,s3,0x1 | pause menu team items | v5.3 · 2026-10-16 |
| 0046E9A0 / PAL 0046EA40 | 36520900 | 36520001 | ori s2,s2,0x900 | ori s2,s2,0x1 | pause menu team items | v5.3 · 2026-10-16 |
| 0046E9C8 / PAL 0046EA68 | 8E06004C | 8E060050 | lw a2,76(s0) | lw a2,80(s0) | pause menu team items | v5.3 · 2026-10-16 |
| 0046E9F8 / PAL 0046EA98 | 8E06004C | 8E060050 | lw a2,76(s0) | lw a2,80(s0) | pause menu team items | v5.3 · 2026-10-16 |
| 001B8150 | 0C0876CA | 0C03F769 | jal 0x21db28 | jal 0xfdda4 | Zones: yellow team uses a yellow-tinted red flame, green team a green-tinted blue flame (local drawing only; players without the patch are unaffected) | v5.3 · 2026-10-16 |
| 0021F2D4 | 0C087202 | 0C03F738 | jal 0x21c808 | jal 0xfdce0 | Zones: yellow team uses a yellow-tinted red flame, green team a green-tinted blue flame (local drawing only; players without the patch are unaffected) | v5.3 · 2026-10-16 |
| 0021F8C0 | 0C087202 | 0C03F738 | jal 0x21c808 | jal 0xfdce0 | Zones: yellow team uses a yellow-tinted red flame, green team a green-tinted blue flame (local drawing only; players without the patch are unaffected) | v5.3 · 2026-10-16 |
| 0021FCD4 | 0C087202 | 0C03F738 | jal 0x21c808 | jal 0xfdce0 | Zones: yellow team uses a yellow-tinted red flame, green team a green-tinted blue flame (local drawing only; players without the patch are unaffected) | v5.3 · 2026-10-16 |
| 00220370 | 0C087202 | 0C03F738 | jal 0x21c808 | jal 0xfdce0 | Zones: yellow team uses a yellow-tinted red flame, green team a green-tinted blue flame (local drawing only; players without the patch are unaffected) | v5.3 · 2026-10-16 |
| 00220774 | 0C087202 | 0C03F738 | jal 0x21c808 | jal 0xfdce0 | Zones: yellow team uses a yellow-tinted red flame, green team a green-tinted blue flame (local drawing only; players without the patch are unaffected) | v5.3 · 2026-10-16 |
| 0044D300 / PAL 0044D360 | 3C0E006B | 0C03FE06 | lui t6,0x6b | jal 0xff818 | Zones flame colour code at 0x000FDCE0 | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FDA00-000FDA87 | 34 | LAN team list builder at 0x000FDA00 (sends host's disabled colours to patched clients; team count is cut to the highest enabled colour so unpatched clients cannot pick disabled colours at the end of the list) | v5.3 · 2026-10-16 |
| 000FDCE0-000FDDF7 | 70 | Zones flame colour code at 0x000FDCE0 | v5.3 · 2026-10-16 |

# Mode list and limits

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0043E39C / PAL 0043E3EC | 11CF0003 | 0C03B289 | beq t6,t7,0x43e3ac | jal 0xeca24 | mod: mode list context 13 (LAN lobby): LAN mode checks skipped, but Assault only when the selected map has it (LM13) | v5.3 · 2026-10-16 |
| 0043E6A0 / PAL 0043E6F0 | 29EF0002 | 29EF0005 | slti t7,t7,2 | slti t7,t7,5 | mod: mode 2 player limit 1 -> 4 | v5.3 · 2026-10-16 |
| 0043E014 / PAL 0043E064 | 29EF0002 | 29EF0005 | slti t7,t7,2 | slti t7,t7,5 | mod: mode 2 icon player limit 1 -> 4 | v5.3 · 2026-10-16 |
| 0047F8B8 / PAL 0047F958 | 3C0E0040 | 3C0E0000 | lui t6,0x40 | lui t6,0x0 | mod: never set 0x400000 limit flag | v5.35 · 2026-10-18 |
| 0064E864 / PAL 0064E964 | 00000004 | 00000005 | sllv zero,zero,zero | .word 0x00000005 | mod: data swap A | v5.3 · 2026-10-16 |
| 0064E870 / PAL 0064E970 | 00000005 | 00000004 | .word 0x00000005 | sllv zero,zero,zero | mod: data swap A | v5.3 · 2026-10-16 |
| 0064F0D8 / PAL 0064F1D8 | 00000004 | 00000005 | sllv zero,zero,zero | .word 0x00000005 | mod: data swap B | v5.3 · 2026-10-16 |
| 0064F0DC / PAL 0064F1DC | 00000005 | 00000004 | .word 0x00000005 | sllv zero,zero,zero | mod: data swap B | v5.3 · 2026-10-16 |
| 0043F020 / PAL 0043F070 | 3C0F006B | 0803F57F | lui t7,0x6b | j 0xfd5fc | Hook: jumps to MAPA: j at 0x43F020 in the map list (was lui t7,0x6b / lw t6,0x3E48(t7)), reached for a map not made for the mode: Assault only lists the maps made for it in Change Game Type (where the game otherwise lists every map; on LAN the | v5.3 · 2026-10-16 |
| 0043F024 / PAL 0043F074 | 8DEE3E48 | 00000000 | lw t6,15944(t7) | nop | Hook: jumps to MAPA: j at 0x43F020 in the map list (was lui t7,0x6b / lw t6,0x3E48(t7)), reached for a map not made for the mode: Assault only lists the maps made for it in Change Game Type (where the game otherwise lists every map; on LAN the | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000ECA24-000ECAAB | 34 | LM13: jal at 0x43E39C in the mode list (an earlier change left a nop there; the original was beq t6,t7,0x43E3AC for context 13, the LAN lobby; delay slot addiu t7,zero,12 kept). Context 13 still skips the LAN mode checks (more | v5.3 · 2026-10-16 |
| 000FD5FC-000FD627 | 11 | MAPA: j at 0x43F020 in the map list (was lui t7,0x6b / lw t6,0x3E48(t7)), reached for a map not made for the mode: Assault only lists the maps made for it in Change Game Type (where the game otherwise lists every map; on LAN the | v5.13 · 2026-10-16 |

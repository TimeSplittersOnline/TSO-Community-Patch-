# Catch-Up

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00064B80 | 054B80 | 7 | `f6 05 58 d2 82 00 01` | `e9 a1 fe 87 00 90 90` | team score add routine: was testb $1,0x82d258 (Catch-Up) \| team score add routine (jmp at 0x64b80; team at 4(%esp), points in ecx): Catch-Up doubles points for the last-placed team \| team score add routine(killer's team), 3 points \| team score add routine(team) with points in ecx \| team score add routine(team), points in ecx \| team score add routine (jmp at 0x64b80; team at 4(%esp), points in ecx): Catch-Up doubles points for the last-placed team | v5.3 · 2026-10-16 |
| 00064E40 | 054E40 | 5 | `a1 0c d1 82 00` | `e9 0f fc 87 00` | add-points routine: was mov 0x82d10c,%eax (Catch-Up) \| add-points routine(chr, 1) \| add-points routine (jmp at 0x64e40; chr at 4(%esp), points at 8(%esp)): Catch-Up doubles points for the last-placed player (team games: team) \| add-points routine (jmp at 0x64e40; chr at 4(%esp), points at 8(%esp)): Catch-Up doubles points for the last-placed player (team games: team) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E48B8 | 111 bytes | xbreadfail_sp | eax = Catch-Up setting (bit 0 On, bit 1 Last Minute) when it applies to the match being played (offline / LAN host, its modes), else 0; keeps ecx/edx | v5.89 · 2026-10-27 |
| 008E4927 | 67 bytes | xbreadfail_sp | eax = 1 when Catch-Up is active right now (Last Minute: 60 seconds or less left of the time limit, Overtime holding the match after its time ran out, or all match when there is no time limit); keeps ecx/edx | v5.19 · 2026-10-17 |
| 008E496A | 142 bytes | xbreadfail_sp | eax = chr (or 0 and edx = team) -> eax = 1 if that player / team is in last place: its ranking score is the lowest of the ranked characters (monkey assistants left out) and below the highest; keeps the other registers | v5.3 · 2026-10-16 |
| 008E49F8 | 46 bytes | xbreadfail_sp | a new match (gameframe went back into the first 20 seconds) clears the Catch-Up kills; keeps ecx/edx | v5.16 · 2026-10-17 |
| 008E4A26 | 46 bytes | xbreadfail_sp | team score add routine (jmp at 0x64b80; team at 4(%esp), points in ecx): Catch-Up doubles points for the last-placed team | v5.3 · 2026-10-16 |
| 008E4A54 | 47 bytes | xbreadfail_sp | add-points routine (jmp at 0x64e40; chr at 4(%esp), points at 8(%esp)): Catch-Up doubles points for the last-placed player (team games: team) | v5.3 · 2026-10-16 |
| 008E4A83 | 94 bytes | xbreadfail_sp | kills (XFPK's exit, then jmp 0x8e916a multikill; esi = killer or 0, edx = victim): in the kill-scored modes a kill by the last-placed player (team games: team) counts 2 (the team's extra point goes through team score add routine) | v5.3 · 2026-10-16 |
| 008E4AE1 | 133 bytes | xbreadfail_sp | Advanced page: Catch-Up, Catch-Up Period (its modes) | v5.3 · 2026-10-16 |
| 008E4B66 | 132 bytes | xbreadfail_sp | refresh (esi = page): values for the menu's mode; Catch-Up Period greyed out while Catch-Up is Off; Catch-Up updates that on change | v5.3 · 2026-10-16 |
| 008E4BEA | 80 bytes | xbreadfail_sp | (menu, 1 when Gun Game is chosen for the menu's mode; cdecl): Catch-Up greyed out with Gun Game, Catch-Up Period greyed out with Gun Game or while Catch-Up is Off | v5.19 · 2026-10-17 |
| 008E4C3A | 95 bytes | xbreadfail_sp | apply (esi = page) | v5.3 · 2026-10-16 |
| 008E4C99 | 53 bytes | xbreadfail_sp | Catch-Up changefn (menu, item; cdecl): Catch-Up Period only selectable with Catch-Up On | v5.19 · 2026-10-17 |
| 008E7808 | 32 bytes | xbreadfail_sp | Catch-Up per menu mode (bit 0 On, bit 1 Last Minute) | v5.3 · 2026-10-16 (approx.) |
| 008E7828 | 64 bytes | xbreadfail_sp | Catch-Up extra kills per chr id this match | v5.3 · 2026-10-16 (approx.) |
| 008E7868 | 8 bytes | xbreadfail_sp | gameframe last seen | v5.3 · 2026-10-16 (approx.) |
| 008E799B | 9 bytes | xbreadfail_sp | Menu / message text "Catch-Up" | v5.3 · 2026-10-16 |
| 008E79D7 | 16 bytes | xbreadfail_sp | Menu / message text "Catch-Up Period" | v5.3 · 2026-10-16 |
| 008E79E7 | 10 bytes | xbreadfail_sp | Menu / message text "All Match" | v5.3 · 2026-10-16 |
| 008E79F1 | 12 bytes | xbreadfail_sp | Menu / message text "Last Minute" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013A208 | 27BDFFF0 | 0803B9DB | addiu sp,sp,-16 | j 0xee76c | Hook: team score add routine: was addiu sp,sp,-16 (Catch-Up; delay slot lui t7,0x63 kept) | v5.3 · 2026-10-16 |
| 0013A6F0 | 27BDFFE0 | 0803B9F2 | addiu sp,sp,-32 | j 0xee7c8 | Hook: add-points routine: was addiu sp,sp,-32 (Catch-Up; delay slot lui t6,0x63 kept) | v5.3 · 2026-10-16 |
| 0013A774 | 0804E882 | 0803B9EF | j 0x13a208 | j 0xee7bc | Hook: add-points routine's tail call to team score add routine: was j 0x13A208 (points already doubled there) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E80F4-000E81FB | 66 | CUEN: leaf: v0 = Catch-Up setting (bit 0 On, bit 1 Last Minute) when it applies to the match being played (offline / LAN host, its modes), else 0; uses t8,t9 | v5.89 · 2026-10-27 |
| 000E8DC4-000E8EB7 | 61 | CURA: a0 = page, a1 = 0 refresh / 1 apply: Catch-Up and Catch-Up Period for the menu's mode; Catch-Up Period is greyed out while Catch-Up is Off | v5.3 · 2026-10-16 |
| 000E9524-000E9603 | 56 | CUITEM: Advanced page: Catch-Up, Catch-Up Period (its modes) | v5.3 · 2026-10-16 |
| 000EB108-000EB1B7 | 44 | CUDOG: leaf (a0 = character record, or 0 and a1 = team): v0 = 1 if that player / team is in last place: its ranking score is the lowest of the ranked characters (monkey assistants left out) and below the highest; uses t0-t9 | v5.3 · 2026-10-16 |
| 000EC490-000EC523 | 37 | CUK: kills (FPK's exit, then j 0xFF370 multikill; s0 = killer data or 0, s1 = victim data): in the kill-scored modes a kill by the last-placed player (team games: team) counts 2 (the team's extra point goes through team score add routine) | v5.3 · 2026-10-16 |
| 000EC888-000EC913 | 35 | CUGR: a0 = page, a1 = 1 when Gun Game is chosen for the menu's mode: Catch-Up greyed out with Gun Game, Catch-Up Period greyed out with Gun Game, while Catch-Up is Off, or with no time limit (Catch-Up then runs all match) | v5.19 · 2026-10-17 |
| 000ECF40-000ECFBF | 32 | CUNOW: v0 = 1 when Catch-Up is active right now (CUEN; Last Minute: the time limit has 60 seconds or less left, Overtime holds the match after its time ran out, or all match when there is no time limit); uses t7-t9 | v5.19 · 2026-10-17 |
| 000EE42C-000EE48B | 24 | CUCH: Catch-Up changefn (a0 = page, a1 = item): Catch-Up Period only selectable with Catch-Up On | v5.19 · 2026-10-17 |
| 000EE76C-000EE7C7 | 23 | CUTA: j at 0x13A208, team score add routine (a0 = team, a1 = points; its delay slot lui t7,0x63 done): Catch-Up doubles points for the last-placed team. CUTAR: the plain entry, for add-points routine's tail call (it has doubled them already) | v5.3 · 2026-10-16 |
| 000EE7C8-000EE823 | 23 | CUSC: j at 0x13A6F0, add-points routine (a0 = character record, a1 = points; its delay slot lui t6,0x63 done): Catch-Up doubles points for the last-placed player (team games: the last-placed team) | v5.3 · 2026-10-16 |
| 000EEDE8-000EEE3B | 21 | CURST: leaf: a new match (gameframe went back into the first 20 seconds) clears the Catch-Up kills; uses t8,t9,v0,v1 | v5.16 · 2026-10-17 |
| 000EEE3C-000EEE8F | 21 | CUGG: a0 = page, a1 = 0 refresh / 1 apply (after CURA): refresh greys Catch-Up out while Gun Game is chosen (CUGR) | v5.3 · 2026-10-16 |
| 000F02D4-000F02E3 | 4 | LCUW: text | v5.3 · 2026-10-16 |
| 000F03B0-000F03BB | 3 | LCU: text | v5.3 · 2026-10-16 (approx.) |
| 000F0404-000F040F | 3 | LCUA: text | v5.3 · 2026-10-16 |
| 000F0410-000F041B | 3 | LCUL: text | v5.3 · 2026-10-16 |

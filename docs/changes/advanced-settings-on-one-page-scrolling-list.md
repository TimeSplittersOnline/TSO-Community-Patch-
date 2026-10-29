# Advanced Settings on one page (scrolling list)

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E5977 | 75 bytes | xbreadfail_sp | title (call at 0x8e8e64 in XTPF, was call 0x11680; XTPF keeps eax only with PG 1): the first part: the title, the scrolled part starts, PG 1 so Teamplay follows (eax = the mode's team game, 2: Teamplay); later parts: no title, no Teamplay | v5.4 · 2026-10-16 |
| 008E59C2 | 26 bytes | xbreadfail_sp | colour count (jmp at 0x8e8e84, was cmpl $1,PG / jne / jmp 0x8e8b89): only in the colour part | v5.3 · 2026-10-16 |
| 008E59DC | 168 bytes | xbreadfail_sp | end of a part (jmp at 0x8e8eb9, was jmp 0x11cbd): the next part, or the end of the page | v5.89 · 2026-10-27 |
| 008E5A84 | 4 bytes | xbreadfail_sp | the part being built (0 title / Teamplay, 1 Advanced, 2 colours) | v5.3 · 2026-10-16 (approx.) |
| 008E5A88 | 33 bytes | xbreadfail_sp | the Advanced items' text margins (left 5, right 3) and item flags (0x22100), as the title set them; keeps every register | v5.3 · 2026-10-16 |
| 008E5AA9 | 29 bytes | xbreadfail_sp | eax = 1 when the menu's mode had a Team Settings page (teams possible, not Capture the Bag / Assault) | v5.3 · 2026-10-16 |
| 008E5AC6 | 28 bytes | xbreadfail_sp | eax = the menu's last item (0 = none); keeps the others | v5.3 · 2026-10-16 |
| 008E5AE2 | 178 bytes | xbreadfail_sp | the scrolled part's height: with 15 options or fewer, all of it (never scrolls); with more, its rows up to and including the 15th option (every item's height counted, options are text items (types 4, 7, 8) that can be selected (no flag 4)); then menu scroll end routine. In a level (not the front end, level 0x65, as the game's own in-level flag at 0x357f68) 11 in place of 15: its panel is smaller, and the rows past it were out of sight and out of reach. | v5.18 · 2026-10-17 |
| 008E5B94 | 4 bytes | xbreadfail_sp | Advanced Settings in sections (from XOPEND, once every item is made and finished): General Settings, Modifiers, | v5.3 · 2026-10-16 (approx.) |
| 008E5B98 | 740 bytes | xbreadfail_sp | which sections have items | v5.3 · 2026-10-16 |
| 008E5E7C | 28 bytes | xbreadfail_sp | ZF clear when eax is one of A's items; keeps the others | v5.3 · 2026-10-16 |
| 008E5E98 | 25 bytes | xbreadfail_sp | eax = the first item of the scrolled part (0 = none) | v5.3 · 2026-10-16 |
| 008E5EB1 | 36 bytes | xbreadfail_sp | eax = id -> eax = its section (1-3; 0 = not listed); keeps the others but edx | v5.3 · 2026-10-16 |
| 008E5ED5 | 40 bytes | xbreadfail_sp | eax = id: the item of A with it (if any) goes next in B; keeps the others | v5.3 · 2026-10-16 |
| 008E5EFD | 27 bytes | xbreadfail_sp | eax = A index: next in B; keeps the others | v5.3 · 2026-10-16 |
| 008E5F18 | 83 bytes | xbreadfail_sp | the sections: id, section (1 General Settings, 2 Modifiers, 3 Team Settings), in their order | v5.67 · 2026-10-23 |
| 008E5F6B | 17 bytes | xbreadfail_sp | Menu / message text "General Settings" | v5.3 · 2026-10-16 |
| 008E5F7C | 10 bytes | xbreadfail_sp | Menu / message text "Modifiers" | v5.3 · 2026-10-16 |
| 008E5F86 | 14 bytes | xbreadfail_sp | Menu / message text "Team Settings" | v5.3 · 2026-10-16 |
| 008E5F94 | 12 bytes | xbreadfail_sp | ---------------- Showdown (Elimination, Vampire): the match uses the mode's own Lives; a player with none left doesn't respawn. | v5.3 · 2026-10-16 (approx.) |
| 008E5FA0 | 28 bytes | xbreadfail_sp | Code: VERTXT (see the code shown) | v5.106 · 2026-10-29 |
| 008E5FBC | 12 bytes | xbreadfail_sp | Data: OPCNT | v5.3 · 2026-10-16 (approx.) |
| 008E5FC8 | 4 bytes | xbreadfail_sp | Data: OPN | v5.3 · 2026-10-16 (approx.) |
| 008E5FCC | 4 bytes | xbreadfail_sp | Data: OPNB | v5.3 · 2026-10-16 (approx.) |
| 008E5FD0 | 256 bytes | xbreadfail_sp | Data: OPA | v5.3 · 2026-10-16 (approx.) |
| 008E60D0 | 256 bytes | xbreadfail_sp | Data: OPB | v5.3 · 2026-10-16 (approx.) |
| 008E61D0 | 256 bytes | xbreadfail_sp | ---------------- Showdown (Elimination, Vampire): the match uses the mode's own Lives; a player with none left doesn't respawn. | v5.3 · 2026-10-16 (approx.) |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E0AC8-000E0F5F | 294 | OPORD: Advanced Settings in sections (from OPEND, once every item is made and finished): General Settings, Modifiers, Team Settings, each under a header (a text item that can't be selected; a section with none of its items in the | v5.3 · 2026-10-16 |
| 000E8A64-000E8B5B | 62 | OPEND: the scrolled part's height: with 15 options or fewer, all of it (never scrolls); with more, its rows up to and including the 15th option (every item's height counted; options: text items (types 4, 7, 8) without flag 4); | v5.18 · 2026-10-17 |
| 000E94CC-000E95AF | 57 | OPT: j at 0xFD2DC (was lui a0,0x64; 0xFD2E0 lw a0,0x3674(a0) is now a nop): end of a part: the next part (back to the builder's item part at 0xFD158), or the end of the page | v5.3 · 2026-10-16 |
| 000EBF7C-000EC017 | 39 | SRADD: Spawn Rule item (not in Assault) | v5.3 · 2026-10-16 |
| 000EC44C-000EC4E3 | 38 | OPHD: jal at 0xFD150 (was jal 0xFDC80, the title; delay slot daddu s2 kept; only the first part comes here): the title, the scrolled part starts, part 0 with PG 1 (Teamplay follows); returns t7 = 0x6B0000 as the title does | v5.4 · 2026-10-16 |
| 000EC6A4-000EC737 | 37 | TSADD: Team Spawns item (as the builder's, 0xFD1E4): modes that can have teams, not Assault | v5.3 · 2026-10-16 |
| 000EF0EC-000EF13F | 21 | OPSEC: code | v5.67 · 2026-10-23 |
| 000EF5A8-000EF5EF | 18 | OPPUT: leaf: a0 = id: the item of A with it (if any) goes next in B (OPPUTI); uses t7-t9, a0 | v5.3 · 2026-10-16 |
| 000EFC18-000EFC4F | 14 | OPINA: leaf: v0 = 1 when a0 is one of A's items; uses t7-t9 | v5.3 · 2026-10-16 |
| 000EFC50-000EFC87 | 14 | OPPUTI: leaf: a0 = A index: next in B; uses t7-t9 | v5.3 · 2026-10-16 |
| 000EFDFC-000EFE2F | 13 | OPMARG: the Advanced items' text margins and item flags, as the title set them | v5.3 · 2026-10-16 |
| 000F0124-000F014B | 10 | OPFIRST: leaf: v0 = the first item of the scrolled part (0 = none) | v5.3 · 2026-10-16 |
| 000F0228-000F024B | 9 | PTPC: j at 0xFD17C (was j 0xFBD10, sub.py's Teamplay step): no Teamplay in the colour part | v5.3 · 2026-10-16 (approx.) |
| 000F024C-000F026F | 9 | PCOL: jal at 0xFD23C (was jal 0xFBD80, sub.py's colour count): colours only in the colour part | v5.3 · 2026-10-16 |
| 000F0364-000F0377 | 5 | OPHL1: code | v5.3 · 2026-10-16 |
| 000F0430-000F043F | 4 | OPHL3: code | v5.3 · 2026-10-16 |
| 000F0548-000F0553 | 3 | OPHL2: code | v5.3 · 2026-10-16 |
| 000F0554-000F055F | 3 | OPHLAB: code | v5.106 · 2026-10-29 |
| 000F068C-000F0693 | 2 | NTL: folder links (j at 0xFBE58 in sub.py's ZA 'after', was mtc1 zero,$f12; its delay slot mtc1 zero,$f13 kept): none: every Advanced Settings item is on one page (OPT), so no divider and no Team / Spawn Settings links | v5.3 · 2026-10-16 (approx.) |
| 000FB3A4-000FB3BF | 7 | VERT: code | v5.106 · 2026-10-29 |

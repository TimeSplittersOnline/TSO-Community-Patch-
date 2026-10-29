# Random Characters

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002D83B8 | 2C83B8 | 5 | `5b 83 c4 48 c3` | `e9 a7 af 60 00` | setup builder exit: was pop %ebx / add $0x48,%esp / ret (Random Characters) \| When the match setup is built (the builder's exits at 0x2d83b8 / 0x2d83c7) every player and bot gets a random character \| jmp from the builder's exit (was pop %ebx / add $0x48,%esp / ret) | v5.3 · 2026-10-16 |
| 002D83C7 | 2C83C7 | 5 | `5b 83 c4 48 c3` | `e9 98 af 60 00` | its other exit (network matches, no bots) \| When the match setup is built (the builder's exits at 0x2d83b8 / 0x2d83c7) every player and bot gets a random character \| jmp from the builder's exit (was pop %ebx / add $0x48,%esp / ret) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E3364 | 171 bytes | xbreadfail_sp | jmp from the builder's exit (was pop %ebx / add $0x48,%esp / ret) | v5.99 · 2026-10-28 |
| 008E340F | 56 bytes | xbreadfail_sp | Advanced page (every mode): Random Characters | v5.3 · 2026-10-16 |
| 008E3447 | 32 bytes | xbreadfail_sp | Code: XRCR (see the code shown) | v5.3 · 2026-10-16 |
| 008E3467 | 30 bytes | xbreadfail_sp | ---------------- Player Health (Advanced Settings, every mode but Leech: Default / Low / Weakling / Pathetic = 75% / 50% / 25%), decided by the host (offline: | v5.3 · 2026-10-16 |
| 008E7A4B | 18 bytes | xbreadfail_sp | Menu / message text "Random Characters" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0044CBE4 / PAL 0044CC34 | 03E00008 | 0803A014 | jr ra | j 0xe8050 | Hook: setup builder's return: was jr ra (Random Characters; delay slot addiu sp,sp,240 kept) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E8050-000E815B | 67 | RCEND: j at 0x44CBE4, the setup builder's return (was jr ra; its delay slot addiu sp,sp,240 done): every player and bot now has a character, so Random Characters can replace them; then return | v5.15 · 2026-10-16 |
| 000EE398-000EE3FB | 25 | RCITEM: Advanced page (every mode): Random Characters | v5.3 · 2026-10-16 |
| 000EF360-000EF3AB | 19 | RCRA: a0 = page, a1 = 0 refresh / 1 apply: Random Characters value | v5.3 · 2026-10-16 |
| 000F03A0-000F03B3 | 5 | LRC: text | v5.3 · 2026-10-16 |

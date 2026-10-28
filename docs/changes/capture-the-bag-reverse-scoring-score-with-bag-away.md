# Capture the Bag: Reverse Scoring, Score With Bag Away

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 000C0B00 | 0B0B00 | 15 | `8b 8b 84 00 00 00 3b 4d 1c 0f 84 1d 02 00 00` | `e9 0f 8d 82 00 90 90 90 90 90 90 90 90 90 90` | A (jmp at 0xc0b00): bag touched, chr has no bag. same team -> 0xc0d2c (return a dropped bag / nothing), else pick it up (0xc0b0f). al = mode | v5.3 · 2026-10-16 |
| 000C14C8 | 0B14C8 | 29 | `8b 47 1c 8b 8b 84 00 00 00 83 c4 08 3b c8 0f 85 a8 01 00 00 39 45 1c 0f 84 92 01 00 00` | `e9 56 83 82 00 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90` | D (jmp at 0xc14c8): capture. normal: base must be the chr's own (else 0xc1684); own bag carried -> 0xc1677 (return it), else score (0xc14e5) | v5.3 · 2026-10-16 |
| 000C1562 | 0B1562 | 5 | `3b 4d 1c 75 61` | `e9 c1 82 82 00` | capture message loop (jmp at 0xc1562, replaces cmp 0x1c(%ebp),%ecx / jne 0xc15c8) | v5.3 · 2026-10-16 |
| 000C1D44 | 0B1D44 | 15 | `8b 8f 84 00 00 00 3b 48 1c 0f 85 de 00 00 00` | `e9 d5 7a 82 00 90 90 90 90 90 90 90 90 90 90` | C (jmp at 0xc1d44): base touched while carrying a bag. normal: own base -> capture check (0xc1d53), else nothing (0xc1e31) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E9A72 | 48 bytes | xbreadfail_sp | ---- Wrong Way Bag: the host (or an offline game) swaps which team's bag a player can carry and which base scores dl = 1 when it applies (setting on, Capture the Bag, offline or LAN host); keeps every other register | v5.89 · 2026-10-27 |
| 008E9AA2 | 131 bytes | xbreadfail_sp | C (jmp at 0xc1d44): base touched while carrying a bag. normal: own base -> capture check (0xc1d53), else nothing (0xc1e31) | v5.3 · 2026-10-16 |
| 008E9B25 | 71 bytes | xbreadfail_sp | C (jmp at 0xc1d44): base touched while carrying a bag. normal: own base -> capture check (0xc1d53), else nothing (0xc1e31) Wrong Way Bag: your own bag to an enemy base, or an enemy bag to your own base | v5.3 · 2026-10-16 |
| 008E9B6C | 198 bytes | xbreadfail_sp | own bag at an enemy base. An unpatched game cannot see this capture, so the host tells every player's game two things | v5.3 · 2026-10-16 |
| 008E9C32 | 17 bytes | xbreadfail_sp | capture message loop (jmp at 0xc1562, replaces cmp 0x1c(%ebp),%ecx / jne 0xc15c8) | v5.3 · 2026-10-16 (approx.) |
| 008E9C43 | 161 bytes | xbreadfail_sp | enemy bag at your own base (edi = chr data, ebx = base prop). Bag Must Be Home = No (host / offline): if your bag is away, the host tells every player's game (1) your bag is at its base, (2) the carrier touched their base (an unpatched game then runs a normal capture), (3) where your bag really is (on its pad, or on the player carrying it), then skips the check itself | v5.89 · 2026-10-27 |
| 008E9CE4 | 76 bytes | xbreadfail_sp | BSYNC(team, state 1 on pad / 2 carried, pad number / chr id): one-bag bag sync to every player, sent reliably (cdecl) | v5.3 · 2026-10-16 |
| 008E9E9C | 16 bytes | xbreadfail_sp | Menu / message text "Reverse Scoring" | v5.3 · 2026-10-16 |
| 008E9EAC | 20 bytes | xbreadfail_sp | Menu / message text "Score With Bag Away" | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FE8C0-000FE91F | 24 | for _i,_x in enumerate(_w): new[0xFE8C0+4*_i]=_x | v5.15 · 2026-10-16 |
| 000FE920-000FE93F | 8 | the rest of the block written as zeros (no stale words) | v5.3 · 2026-10-16 (approx.) |
| 000FFC20-000FFE97 | 156 | emit(a) | v5.89 · 2026-10-27 |
| 000FFE98-000FFE9B | 1 | if new.get(w0+k)==jal(0x7777770): new[w0+k]=jal(SYM['BSYNC']) | v5.3 · 2026-10-16 (approx.) |
| 000FFE9C-000FFEF7 | 23 | emit(a) | v5.3 · 2026-10-16 |
| 000FFEF8-000FFEFB | 1 | if new.get(w0+k)==jal(0x7777770): new[w0+k]=jal(SYM['BSYNC']) | v5.3 · 2026-10-16 (approx.) |
| 000FFEFC-000FFF13 | 6 | emit(a) | v5.3 · 2026-10-16 |

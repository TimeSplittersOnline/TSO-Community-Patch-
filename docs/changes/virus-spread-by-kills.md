# Virus: Spread By Kills

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00064FB4 | 054FB4 | 14 | `80 3d 55 d2 82 00 09 75 6d a1 74 d2 82 00` | `e8 74 48 88 00 90 90 75 6d e8 68 14 88 00` | XINFK (call at 0x64fb4 in add-kill routine, esi = killer or 0, edx = victim; then on to the multikill code at 0x8e916a): \| add-kill routine after the kill is counted (call at 0x64fb4): esi killer, edx victim chr \| kills add team points: Showdown has lives too (was mov 0x82d274,%eax) \| The host (offline: this game) keeps the score as kills, not lives left (XGGADD; team kills XSDNL at 0x64fbd; the ranking \| eax = the match's number of lives, 0 in a Showdown match this game decides (call at 0x64fbd, was mov 0x82d274,%eax: kills add \| eax = the match's number of lives, 0 in a Showdown match this game decides (call at 0x64fbd, was mov 0x82d274,%eax: kills add team points; also used by XSDNT for the ranking (XSDRK, 0x652a3) and by the score text (XSDTX, 0x2e8651)); keeps the others | v5.3 · 2026-10-16 |
| 00125D30 | 115D30 | 6 | `83 ec 14 0f 57 c0` | `e9 07 3b 7c 00 90` | Infection: no spreading by touch. set-on-fire routine entry (jmp at 0x125d30, cdecl, [esp+4] = cfx, cfx+0 = chr data): once someone is | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E9D30 | 69 bytes | xbreadfail_sp | XINFK (call at 0x64fb4 in add-kill routine, esi = killer or 0, edx = victim; then on to the multikill code at 0x8e916a): Virus with Infect On Kill (host / offline): an infected player's kill infects the victim, who respawns infected | v5.3 · 2026-10-16 |
| 008E9D75 | 50 bytes | xbreadfail_sp | Infection: infected bots keep fighting with guns instead of switching to the Virus "chase and touch" behaviour. jmp at 0x125e2b / 0x12611d in the two burn functions (replaces add $8,%esp / cmp %eax,%ecx / jl <skip bot flamer state>) ZF clear (jnz) when Infection applies (setting on, Virus, offline or host); keeps eax/ecx/edx | v5.3 · 2026-10-16 |
| 008E9DA7 | 45 bytes | xbreadfail_sp | Infection: no spreading by touch. set-on-fire routine entry (jmp at 0x125d30, cdecl, [esp+4] = cfx, cfx+0 = chr data): once someone is infected, a survivor (status bit clear) is not set alight by an infected player's fire. Kill infections set the bit first, so they still burn; the very first infected player (status 0) still starts normally | v5.3 · 2026-10-16 |
| 008E9EC0 | 16 bytes | xbreadfail_sp | Menu / message text "Spread By Kills" | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FEB00-000FEBA7 | 42 | for _i,_x in enumerate(_w): new[0xFEB00+4*_i]=_x | v5.3 · 2026-10-16 |
| 000FEC00-000FED87 | 98 | for _i,_x in enumerate(_w): new[0xFEC00+4*_i]=_x | v5.89 · 2026-10-27 |
| 000FED88-000FED9F | 6 | the rest of the block written as zeros (no stale words) | v5.3 · 2026-10-16 (approx.) |
| 000FFF20-000FFF2B | 3 | emit(a) | v5.3 · 2026-10-16 (approx.) |

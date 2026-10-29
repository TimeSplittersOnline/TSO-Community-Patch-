# Capture the Bag: Switch Spawns

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 0006CC7E | 05CC7E | 6 | `8b 89 84 00 00 00` | `e8 6a 77 87 00 90` | team spawn points: Switch Spawns swaps Red / Blue \| spawn point picker's team spawn points (call at 0x6cc7e, was mov 0x84(%ecx),%ecx; ecx = the chr being spawned; then the pad flag bit \| spawn point picker's team spawn points (call at 0x6cc7e, was mov 0x84(%ecx),%ecx; ecx = the chr being spawned; then the pad flag bit team + 1 is required; teams 1-4, Red 1, Blue 2): ecx = its team, Red and Blue swapped with Switch Spawns; keeps the others | v5.3 · 2026-10-16 |
| 000D183D | 0C183D | 5 | `e8 fe e2 ff ff` | `e8 ca 2b 81 00` | host's spawn pick: Switch Spawns moves own-base picks (first spawn) \| a spawn point already chosen (start spawn point routine's callers: the host's pick for a player at 0xd183d, a game placing its own player at \| a spawn point already chosen (start spawn point routine's callers: the host's pick for a player at 0xd183d, a game placing its own player at 0xd5a59; was call start spawn point routine 0xcfb40, [esp+4] = the player): with Switch Spawns, a pick at the player's own team's spawn points goes to one of the other team's. Covers the spawns spawn point picker's team swap (XSWTM) does not see, e.g. the first spawn of a match (fixed start points); a pick already at the other team's is kept. eax = the pad index; keeps ebx/esi/edi/ebp | v5.3 · 2026-10-16 |
| 000D5A59 | 0C5A59 | 5 | `e8 e2 a0 ff ff` | `e8 ae e9 80 00` | placing this game's player: the same \| 0xd5a59; was call start spawn point routine 0xcfb40, [esp+4] = the player): with Switch Spawns, a pick at the player's own team's spawn points \| a spawn point already chosen (start spawn point routine's callers: the host's pick for a player at 0xd183d, a game placing its own player at 0xd5a59; was call start spawn point routine 0xcfb40, [esp+4] = the player): with Switch Spawns, a pick at the player's own team's spawn points goes to one of the other team's. Covers the spawns spawn point picker's team swap (XSWTM) does not see, e.g. the first spawn of a match (fixed start points); a pick already at the other team's is kept. eax = the pad index; keeps ebx/esi/edi/ebp | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E43B0 | 61 bytes | xbreadfail_sp | eax = 1 when Switch Spawns applies to the match being played (Capture the Bag; offline / LAN host: the setting; LAN player: the host's, byte 74 bit 2 under its 0xC0 marker); keeps ecx/edx | v5.89 · 2026-10-27 |
| 008E43ED | 31 bytes | xbreadfail_sp | spawn point picker's team spawn points (call at 0x6cc7e, was mov 0x84(%ecx),%ecx; ecx = the chr being spawned; then the pad flag bit team + 1 is required; teams 1-4, Red 1, Blue 2): ecx = its team, Red and Blue swapped with Switch Spawns; keeps the others | v5.7 · 2026-10-16 |
| 008E440C | 17 bytes | xbreadfail_sp | a spawn point already chosen (start spawn point routine's callers: the host's pick for a player at 0xd183d, a game placing its own player at 0xd5a59; was call start spawn point routine 0xcfb40, [esp+4] = the player): with Switch Spawns, a pick at the player's own team's spawn points goes to one of the other team's. Covers the spawns spawn point picker's team swap (XSWTM) does not see, e.g. the first spawn of a match (fixed start points); a pick already at the other team's is kept. eax = the pad index; keeps ebx/esi/edi/ebp | v5.6 · 2026-10-16 |
| 008E441D | 254 bytes | xbreadfail_sp | eax = a pad index (into the level's pads, 0x749014, 0x805464 of them), ecx = the player -> eax = it, or with Switch Spawns (Teamplay, team spawn points on, Red / Blue) a random usable one of the other team's spawn points when it is one of the player's own team's (its team flag, not the other's) | v5.70 · 2026-10-23 |
| 008E451B | 66 bytes | xbreadfail_sp | esi = setup, edi = k (-1: count), [esp+4] = other team's flag, [esp+8] = own: eax = the k-th usable spawn point of the other team (entry), or their number; keeps esi/edi/ebx/ebp | v5.6 · 2026-10-16 |
| 008E455D | 65 bytes | xbreadfail_sp | Capture the Bag menu: Switch Spawns | v5.3 · 2026-10-16 |
| 008E459E | 32 bytes | xbreadfail_sp | refresh / apply (esi = page) | v5.3 · 2026-10-16 |
| 008E45BE | 30 bytes | xbreadfail_sp | ---------------- Auto-Complete Phase (Advanced Settings, Assault: Off / 1 Min - 10 Mins), decided by the host (offline: this game) | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 00144898 | 8EEF0084 | 0C03A9EB | lw t7,132(s7) | jal 0xea7ac | Hook: team spawn points: Switch Spawns swaps Red / Blue (the team load in the delay slot; SWTM adds the 1) | v5.3 · 2026-10-16 |
| 0014489C | 25EF0001 | 8EEF0084 | addiu t7,t7,1 | lw t7,132(s7) | Hook: team spawn points: Switch Spawns swaps Red / Blue (the team load in the delay slot; SWTM adds the 1) | v5.3 · 2026-10-16 |
| 001C83E8 | 0C072058 | 0C038EDF | jal 0x1c8160 | jal 0xe3b7c | Hook: spawn picks: Switch Spawns moves own-base picks (the first spawn) | v5.6 · 2026-10-16 |
| 001CC378 | 0C072058 | 0C038EDF | jal 0x1c8160 | jal 0xe3b7c | Hook: spawn picks: Switch Spawns moves own-base picks (the first spawn) | v5.6 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E3B7C-000E3D77 | 127 | SWSP: jal at 0x1C83E8 (a game placing its own player) and 0x1CC378 (the host's pick for a player) in place of jal start spawn point routine 0x1C8160 (a0 = the player): v0 = its pick, or with Switch Spawns (Teamplay, team spawn points on, | v5.89 · 2026-10-27 |
| 000EA7AC-000EA86B | 48 | SWTM: jal at 0x144898 in spawn point picker's team spawn points (was lw t7,132(s7) / addiu t7,t7,1; the load is kept in the delay slot, s7 = the chr being spawned; then the pad flag bit team + 1 is required; teams 1-4, Red 1, Blue 2): t7 = its team + 1, Red and | v5.89 · 2026-10-27 |
| 000EBA54-000EBAF3 | 40 | SWSCAN: s4 = setup (pads +36, +40 of them; number +4, flags +8), s5 = the other team's flag, s2 = own, a1 = k (-1: count): v0 = the k-th usable spawn point of the other team (entry), or their number | v5.6 · 2026-10-16 |
| 000ED3AC-000ED427 | 31 | SWITEM: Capture the Bag menu: Switch Spawns | v5.3 · 2026-10-16 |
| 000EF16C-000EF1B7 | 19 | SWRA: a0 = page, a1 = 0 refresh / 1 apply: Switch Spawns value | v5.3 · 2026-10-16 |
| 000F02F0-000F02FF | 4 | LSWI: text | v5.3 · 2026-10-16 |

# Spawn Rule

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 0006CDC5 | 05CDC5 | 5 | `e8 e6 77 0e 00` | `e8 13 59 87 00` | spawn point picker: was call rand (Spawn Rule) \| spawn pick (call at 0x6cdc5 in spawn point picker, replaces call rand; ebp = number of candidates in SPLIST, [esp+0x18] = setup, | v5.3 · 2026-10-16 |
| 000CFB88 | 0BFB88 | 5 | `e8 83 4c 28 00` | `e8 fb 29 81 00` | respawn: was call network game flag (Spawn Rule: another game's player at its own pick) \| start spawn point routine's net check (call at 0xcfb88, was call 0x354810 network game check; esi = player): in a LAN match with a Spawn Rule on, every \| start spawn point routine's net check (call at 0xcfb88, was call 0x354810 network game check; esi = player): in a LAN match with a Spawn Rule on, every console's own player spawns at the host's pick (as a game without the patch does: the host picks again while the player waits, XSRAG); another console's player, here, at the pad its respawn message gave (the pick that game had last). eax = 0 (drop) or network game check | v5.3 · 2026-10-16 |
| 0035F28E | 34F28E | 5 | `e8 dd be ff ff` | `e8 c5 33 58 00` | the host's 1.5 s resend to a dead LAN player: Spawn Rule picks again first \| the host's resend of a dead LAN player's spawn point every 1.5 seconds (call at 0x35f28e, was call spawn point message; the player \| the host's resend of a dead LAN player's spawn point every 1.5 seconds (call at 0x35f28e, was call spawn point message; the player pushed): picked again first (XSRAG); then sent as before, unless that sent it | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E2350 | 35 bytes | xbreadfail_sp | eax = 1 if the menu's mode can have teams (mode table team game, or Gladiator: Team VIP) | v5.3 · 2026-10-16 |
| 008E2373 | 87 bytes | xbreadfail_sp | Spawn Rule item (not in Assault) | v5.3 · 2026-10-16 |
| 008E23CA | 124 bytes | xbreadfail_sp | refresh (esi = page): value for the menu's mode (Near Teammates shows Default where there are no teams, or with Teamplay Off) | v5.3 · 2026-10-16 |
| 008E2446 | 71 bytes | xbreadfail_sp | Spawn Rule changefn (menu, item; cdecl): with the menu's Teamplay item Off, Near Teammates is skipped (on to Default, or back to Away From Enemies) | v5.3 · 2026-10-16 |
| 008E248D | 86 bytes | xbreadfail_sp | XSRTOFF(menu): eax = 1 when the menu's mode has a Teamplay item and the menu's one is Off (Gladiator: its Team VIP item Off), else 0 | v5.3 · 2026-10-16 |
| 008E24E3 | 45 bytes | xbreadfail_sp | apply (esi = page) | v5.3 · 2026-10-16 |
| 008E2510 | 76 bytes | xbreadfail_sp | eax = Spawn Rule for the match being played: offline / LAN host: its setting for the mode; LAN player: the host's, from setup byte 72 (0xB0 \| rule), else 0; keeps other registers. Every console picks its own player's spawn point | v5.89 · 2026-10-27 |
| 008E255C | 44 bytes | xbreadfail_sp | eax = Spawn Rule when it applies to the match being played (XSRV; not Assault / Escort; Near Teammates only in team games), else 0; keeps other registers | v5.3 · 2026-10-16 |
| 008E2588 | 89 bytes | xbreadfail_sp | start spawn point routine's net check (call at 0xcfb88, was call 0x354810 network game check; esi = player): in a LAN match with a Spawn Rule on, every console's own player spawns at the host's pick (as a game without the patch does: the host picks again while the player waits, XSRAG); another console's player, here, at the pad its respawn message gave (the pick that game had last). eax = 0 (drop) or network game check | v5.64 · 2026-10-22 |
| 008E25E1 | 119 bytes | xbreadfail_sp | LAN host, esi = a dead player: with a Spawn Rule on (not its first spawn), its spawn point picked again now, from where everyone is now (the game's own death pick 0xd17c0, which sends it to that player's game). eax = 1 if that sent it, else 0; keeps the others. Every player gets the same: picked again every 1.5 seconds while it waits (another game's at the game's own resend, XSRRS; the host's own, XSRLT), each spawning at the last pick its game had | v5.64 · 2026-10-22 |
| 008E2658 | 25 bytes | xbreadfail_sp | the host's resend of a dead LAN player's spawn point every 1.5 seconds (call at 0x35f28e, was call spawn point message; the player pushed): picked again first (XSRAG); then sent as before, unless that sent it | v5.64 · 2026-10-22 |
| 008E2671 | 108 bytes | xbreadfail_sp | Code: XSRLT (see the code shown) | v5.64 · 2026-10-22 |
| 008E26DD | 715 bytes | xbreadfail_sp | candidates (ebp = count). Team game: every player spawn point whatever its team (the game's list only has this team's | v5.89 · 2026-10-27 |
| 008E29A8 | 4 bytes | xbreadfail_sp | Data: HUGE | v5.3 · 2026-10-16 (approx.) |
| 008E29AC | 4 bytes | xbreadfail_sp | Data: NHUGE | v5.3 · 2026-10-16 (approx.) |
| 008E29B0 | 4 bytes | xbreadfail_sp | ---------------- Flame Pass (Advanced Settings, Flame Tag, LAN only: Touch / Kill / Touch Or Kill), decided by the host | v5.3 · 2026-10-16 (approx.) |
| 008E7949 | 11 bytes | xbreadfail_sp | Menu / message text "Spawn Rule" | v5.3 · 2026-10-16 |
| 008E7978 | 8 bytes | xbreadfail_sp | Menu / message text "Default" | v5.3 · 2026-10-16 |
| 008E7980 | 18 bytes | xbreadfail_sp | Menu / message text "Away From Enemies" | v5.3 · 2026-10-16 |
| 008E7992 | 15 bytes | xbreadfail_sp | Menu / message text "Near Teammates" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0014498C | 0C09DF90 | 0C0385C5 | jal 0x277e40 | jal 0xe1714 | Hook: spawn pick in spawn point picker: was jal 0x277E40 (rand); delay slot nop kept | v5.3 · 2026-10-16 |
| 001C81EC | 0C13D554 | 0C03B01C | jal 0x4f5550 | jal 0xec070 | Hook: start spawn point routine: was jal 0x4F5550 (network game check): Spawn Rule (another game's player: its own pick) | v5.3 · 2026-10-16 |
| 004FCAE0 / PAL 004FCB88 | 0C140370 | 0C03BE8E | jal 0x500dc0 | jal 0xefa38 | Hook: the host's 1.5 s resend to a dead LAN player: Spawn Rule picks again first | v5.64 · 2026-10-22 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E1714-000E1AB3 | 232 | SRN: spawn pick (jal at 0x14498C in spawn point picker, replaces jal rand; delay slot nop): with a Spawn Rule on, keeps the best quarter of the candidate spawn points (furthest from the nearest living enemy) or the best | v5.16 · 2026-10-17 |
| 000E8704-000E87FB | 62 | SRLT: every frame (GGT), LAN host: its own players waiting to respawn get their spawn point picked again every 1.5 s (SRAG) | v5.64 · 2026-10-22 |
| 000E8CD0-000E8DC3 | 61 | SRRA: a0 = page, a1 = 0 refresh / 1 apply: Spawn Rule value for the menu's mode; refresh shows Near Teammates as Default where there are no teams or the Teamplay setting is Off (Gladiator: Team VIP Off), and sets its changefn | v5.3 · 2026-10-16 |
| 000E9D84-000E9E53 | 52 | SRAG: LAN host, a0 = a dead player: with a Spawn Rule on (not its first spawn), its spawn point picked again now, from where everyone is now (the game's own death pick 0x1CC2A0, which sends it to that player's game). v0 = 1 if that | v5.64 · 2026-10-22 |
| 000EAE38-000EAEEB | 45 | SRV: leaf: v0 = Spawn Rule for the match being played: offline / LAN host: its setting for the mode; LAN player: the host's, from setup byte 72 (0xB0 \| rule), else 0; uses t5-t9 | v5.89 · 2026-10-27 |
| 000EC070-000EC107 | 38 | SRP: jal at 0x1C81EC in start spawn point routine (was jal 0x4F5550 network game check; s0 = player): in a LAN match with a Spawn Rule on, every console's own player spawns at the host's pick (as a game without the patch does: the host picks again | v5.64 · 2026-10-22 |
| 000ECECC-000ECF4B | 32 | SRTOFF: a0 = page: v0 = 1 when the menu's mode has a Teamplay item and the page's one is Off (Gladiator: its Team VIP item Off), else 0 | v5.3 · 2026-10-16 |
| 000EE71C-000EE777 | 23 | SRCH: Spawn Rule changefn (a0 = page, a1 = item): with the page's Teamplay item Off (Gladiator: Team VIP Off), Near Teammates is skipped (on to Default, or back to Away From Enemies) | v5.3 · 2026-10-16 |
| 000EECA4-000EECF7 | 21 | SRON: v0 = Spawn Rule when it applies to the match being played (SRV; not Assault / Escort; Near Teammates only in team games), else 0; uses t5-t9 | v5.3 · 2026-10-16 |
| 000EFA38-000EFA6F | 14 | SRRS: jal at 0x4FCAE0 (was jal spawn point message; a0 = the player, delay slot kept): the host's resend of a dead LAN player's spawn point every 1.5 seconds: picked again first (SRAG); then sent as before, unless that sent it | v5.64 · 2026-10-22 |
| 000EFCE8-000EFD17 | 12 | SRTEAM: leaf: v0 = 1 if the menu's mode can have teams (mode table team game, or Gladiator: Team VIP); uses t6,t7 | v5.3 · 2026-10-16 |
| 000F0198-000F01AB | 5 | LSR1: text | v5.3 · 2026-10-16 |
| 000F0210-000F021F | 4 | SRITEM: Spawn Settings page tail (j at 0xFBDE4, frame open, ra at 0(sp); was j 0xFB180 = Respawn Delay items; not used now): Spawn Rule, then the Respawn Delay items | v5.3 · 2026-10-16 (approx.) |
| 000F02B0-000F02BF | 4 | LSR2: text | v5.3 · 2026-10-16 |
| 000F03B0-000F03BB | 3 | LSR: text | v5.3 · 2026-10-16 |
| 000F04C0-000F04C7 | 2 | LSR0: text | v5.3 · 2026-10-16 (approx.) |

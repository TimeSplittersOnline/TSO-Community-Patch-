# Thief: Gold Rush, Coin Drop

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 000BBB4E | 0ABB4E | 5 | `e8 ed 78 1f 00` | `e8 39 70 82 00` | character death routine's Thief death coin: was call pickup spawn routine \| character death routine's Thief death coin (call at 0xbbb4e, was call 0x2b3440 pickup spawn routine(victim prop); esi = damage info: \| character death routine's Thief death coin (call at 0xbbb4e, was call 0x2b3440 pickup spawn routine(victim prop); esi = damage info: 0 target prop, 4 original attacker prop): no coin with Coin Rush, or with Player Kills unless another player's chr killed it | v5.3 · 2026-10-16 |
| 0035C253 | 34C253 | 5 | `e8 d8 70 f5 ff` | `e8 89 69 58 00` | a LAN player's death coin arriving: was call pickup spawn routine \| a LAN player's death coin arriving (call at 0x35c253, was call 0x2b3330 pickup spawn routine(prop, pad)): the host \| a LAN player's death coin arriving (call at 0x35c253, was call 0x2b3330 pickup spawn routine(prop, pad)): the host ignores it with Coin Rush, or with Player Kills when it saw that chr die without a kill in the last 3 seconds, then XCDRM tells that player's game to remove the coin it made | v5.3 · 2026-10-16 |
| 0035E3BF | 34E3BF | 5 | `e8 ac 93 f5 ff` | `e8 0a 4a 58 00` | Thief collect message: was call pickup removal routine (Coin Rush) \| Thief collect message (call at 0x35e3bf in its decode, was call 0x2b7770 pickup removal routine(chr id, pad)): with \| Thief collect message (call at 0x35e3bf in its decode, was call 0x2b7770 pickup removal routine(chr id, pad)): with Coin Rush, a coin another console says it picked up still scores when this game no longer has it (taken or gone here a moment earlier), so every console counts the same coins | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E2AC4 | 90 bytes | xbreadfail_sp | eax = bit 0 Coin Rush, bit 1 Player Kills only, when they apply (Thief; host / offline: the settings, LAN player: the host's, from byte 74), else 0; keeps other registers | v5.89 · 2026-10-27 |
| 008E2B1E | 110 bytes | xbreadfail_sp | eax = team-list byte 74 for LAN players: 0xC0 \| Zone Interval \| Coin Rush << 2 \| Player Kills << 3; keeps other registers (call at 0x8e8ca4 (zi.s XZW, the setup) and 0x8e93d4 (mk.s, menu apply), was movzbl ZVAR,%eax / or $0xc0,%al) | v5.95 · 2026-10-27 |
| 008E2B8C | 85 bytes | xbreadfail_sp | character death routine's Thief death coin (call at 0xbbb4e, was call 0x2b3440 pickup spawn routine(victim prop); esi = damage info: 0 target prop, 4 original attacker prop): no coin with Coin Rush, or with Player Kills unless another player's chr killed it | v5.3 · 2026-10-16 |
| 008E2BE1 | 142 bytes | xbreadfail_sp | a LAN player's death coin arriving (call at 0x35c253, was call 0x2b3330 pickup spawn routine(prop, pad)): the host ignores it with Coin Rush, or with Player Kills when it saw that chr die without a kill in the last 3 seconds, then XCDRM tells that player's game to remove the coin it made | v5.17 · 2026-10-17 |
| 008E2C6F | 226 bytes | xbreadfail_sp | XCDRM(victim prop, pad), LAN host, a death coin of another game's player dropped (XCDF): that game (without the patch: a game with it makes none) already shows the coin on its own, where it fills one of the game's 30 dropped-pickup slots (with enough of them it stops showing the host's coins) and, picked up, would still score with Coin Rush (XCRNR). So that game alone is told this game's player collected the coins on that pad (message 36: it removes every coin there, and on its own screen only that player gets the point), then the coins this game really has on that pad are sent to it again (message 35, as XCRJOIN). Its own game ignores a message 36 that names its own player, so this game's player is named. Keeps all | v5.17 · 2026-10-17 |
| 008E2D51 | 125 bytes | xbreadfail_sp | Thief, LAN host: a mid-match joiner gets the coins already out (Coin Rush coins stay until someone takes them, so its game never saw them come): each one sent again to that game only (message 35, as the host's player's coin at its pad; cdecl, [esp+4] = the joining client). Every other game is unchanged | v5.63 · 2026-10-22 |
| 008E2DCE | 76 bytes | xbreadfail_sp | Thief collect message (call at 0x35e3bf in its decode, was call 0x2b7770 pickup removal routine(chr id, pad)): with Coin Rush, a coin another console says it picked up still scores when this game no longer has it (taken or gone here a moment earlier), so every console counts the same coins | v5.3 · 2026-10-16 |
| 008E2E1A | 159 bytes | xbreadfail_sp | every frame (XGGT): Coin Rush, host / offline: a coin every 5/8 second, the first 3 seconds in | v5.64 · 2026-10-22 |
| 008E2EB9 | 783 bytes | xbreadfail_sp | put a Coin Rush coin on a random spawn point (not one that already has a coin), as this game's player; bots go for it | v5.15 · 2026-10-16 |
| 008E31C8 | 120 bytes | xbreadfail_sp | Thief menu: Coin Rush, Coin Drop | v5.3 · 2026-10-16 |
| 008E3240 | 87 bytes | xbreadfail_sp | refresh (esi = page): values; Coin Drop greyed out while Coin Rush is On; Coin Rush updates that on change | v5.3 · 2026-10-16 |
| 008E3297 | 59 bytes | xbreadfail_sp | apply (esi = page) | v5.3 · 2026-10-16 |
| 008E32D2 | 46 bytes | xbreadfail_sp | Coin Rush changefn (menu, item; cdecl): Coin Drop only selectable with Coin Rush Off | v5.95 · 2026-10-27 |
| 008E7921 | 10 bytes | xbreadfail_sp | Menu / message text "Gold Rush" | v5.3 · 2026-10-16 |
| 008E798D | 10 bytes | xbreadfail_sp | Menu / message text "Coin Drop" | v5.3 · 2026-10-16 |
| 008E7997 | 10 bytes | xbreadfail_sp | Menu / message text "Any Death" | v5.3 · 2026-10-16 |
| 008E79A1 | 13 bytes | xbreadfail_sp | Menu / message text "Player Kills" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 001B04FC | 0C107D9A | 0C03B57D | jal 0x41f668 | jal 0xed5f4 | Hook: Thief death coin in character death routine: was jal 0x41F668 | v5.3 · 2026-10-16 |
| 004F9168 / PAL 004F9210 | 0C107E62 | 0C03B411 | jal 0x41f988 | jal 0xed044 | Hook: Thief collect message: was jal 0x41F988 (Coin Rush: still scores when the coin is gone here) | v5.3 · 2026-10-16 |
| 004F933C / PAL 004F93E4 | 0C107D20 | 0C03AB6A | jal 0x41f480 | jal 0xeada8 | Hook: a LAN player's death coin arriving: was jal 0x41F480 | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E0100-000E05EB | 315 | CRSP: put a Coin Rush coin on one of 48 random navigation pads without a coin (else a spawn point), picked at random from the quarter furthest from the coins already out and from every player / bot (so they spread over the map, away from campers), as this game's player | v5.15 · 2026-10-16 |
| 000E5E68-000E5FD3 | 91 | CDRM: a0 = victim prop, a1 = pad, LAN host, a death coin of another game's player dropped (CDF): that game (without the patch: a game with it makes none) already shows the coin on its own, where it fills one of the game's 30 dropped- | v5.17 · 2026-10-17 |
| 000E70B4-000E71E7 | 77 | CRT: every frame (called at the start of GGT): Coin Rush, host / offline: a coin every 5/8 second, 3 seconds in | v5.83 · 2026-10-26 |
| 000E8CE4-000E8DD3 | 60 | CRJOIN: Thief, LAN host: a mid-match joiner gets the coins already out (Coin Rush coins stay until someone takes them, so its game never saw them come): each one sent again to that game only (message 35, as the host's player's coin at its | v5.63 · 2026-10-22 |
| 000E9C64-000E9D2F | 51 | CRITEM: Thief menu: Coin Rush, Coin Drop | v5.3 · 2026-10-16 |
| 000EA730-000EA7EB | 47 | CDS: leaf: v0 = bit 0 Coin Rush, bit 1 Player Kills only, when they apply (Thief; host / offline: the settings, LAN client: the host's, from byte 74), else 0; uses t8,t9 | v5.89 · 2026-10-27 |
| 000EADA8-000EAE5B | 45 | CDF: jal at 0x4F933C (a LAN player's death coin arriving, was jal 0x41F480; a0 = victim prop, a1 = pad): the host drops it with Coin Rush, or with Player Kills when it saw that chr die without a kill in the last 3 seconds, | v5.17 · 2026-10-17 |
| 000EAE5C-000EAF0F | 45 | CRRA: a0 = page, a1 = 0 refresh / 1 apply: Coin Rush and Coin Drop; Coin Drop is greyed out while Coin Rush is On | v5.3 · 2026-10-16 |
| 000EB7CC-000EB86B | 40 | CB74: leaf: t6 = team-list byte 74 for LAN players: 0xC0 \| Zone Interval \| bits 2-3: King of the Hill in Zones, else Coin Rush << 2 \| Player Kills << 3 (Thief), Switch Spawns << 2 (Capture the Bag); uses t7,t8 (jal at 0xFBBB0, the team list, | v5.95 · 2026-10-27 |
| 000ED044-000ED0BF | 31 | CRNR: jal at 0x4F9168 in collect reader (was jal 0x41F988 pickup removal routine; a0 = chr id, a1 = pad): with Coin Rush, a coin another console says it picked up still scores when this game no longer has it (taken | v5.3 · 2026-10-16 |
| 000ED5F4-000ED667 | 29 | CDK: jal at 0x1B04FC in character death routine (Thief death coin, was jal 0x41F668 pickup spawn routine; a0 = victim prop, s1 = damage info: 0 target prop, 4 original attacker prop): no coin with Coin Rush, or with Player Kills | v5.3 · 2026-10-16 |
| 000EF3B4-000EF3F7 | 17 | CRCH: Coin Rush changefn (a0 = page, a1 = item): Coin Drop only selectable with Coin Rush Off | v5.3 · 2026-10-16 |
| 000EF69C-000EF6D7 | 15 | CDREC: leaf (a0 = victim prop, t6 = 1 no coin / 0 coin): remember it for the host's check of LAN players' coins; uses t7-t9 | v5.3 · 2026-10-16 |
| 000EFF9C-000EFFAB | 4 | LCD1: text | v5.3 · 2026-10-16 |
| 000F00C8-000F00D3 | 3 | LCR: text | v5.3 · 2026-10-16 |
| 000F00D4-000F00DF | 3 | LCD: text | v5.3 · 2026-10-16 |
| 000F00E0-000F00EB | 3 | LCD0: text | v5.3 · 2026-10-16 |

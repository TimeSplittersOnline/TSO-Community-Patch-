# Team Bag Tag

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 0006884A | 05884A | 9 | `03 f2 89 30 a1 e0 d1 82 00` | `e8 c1 91 fa ff 90 90 90 90` | team Bag Tag: called from 0x6884a (replaces add %edx,%esi; mov %esi,(%eax); mov 0x82d1e0,%eax) \| team Bag Tag: called from 0x6884a (replaces add %edx,%esi; mov %esi,(%eax); mov 0x82d1e0,%eax) | v5.3 · 2026-10-16 |
| 002C391D | 2B391D | 14 | `8a 0d 4e e0 7b 00 33 c0 80 f9 04 0f 94 c0` | `8a 0d 4d e0 7b 00 33 c0 e8 46 e1 d4 ff 90` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| team count: 4 teams if game mode >= 6 or Bag Tag (1); input cl/dl, output al/cl | v5.3 · 2026-10-16 |
| 002C3A54 | 2B3A54 | 14 | `8a 0d 4e e0 7b 00 33 c0 80 f9 04 0f 94 c0` | `8a 0d 4d e0 7b 00 33 c0 e8 0f e0 d4 ff 90` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| team count: 4 teams if game mode >= 6 or Bag Tag (1); input cl/dl, output al/cl | v5.3 · 2026-10-16 |
| 002C4D5A | 2B4D5A | 14 | `8a 15 4e e0 7b 00 33 c0 80 fa 04 0f 94 c0` | `8a 15 4d e0 7b 00 33 c0 e8 18 cd d4 ff 90` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002C6D52 | 2B6D52 | 6 | `80 fa 04 0f 94 c1` | `e8 37 ad d4 ff 90` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002D5B97 | 2C5B97 | 23 | `8a 15 4e e0 7b 00 47 33 c9 80 fa 04 0f 94 c1 8b c7 89 be 0c 01 00 00` | `8a 15 4d e0 7b 00 47 33 c9 e8 e9 be d3 ff 90 8b c7 e8 eb b7 d3 ff 90` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) | v5.3 · 2026-10-16 |
| 002D5BC4 | 2C5BC4 | 22 | `ff 8e 0c 01 00 00 79 19 8a 0d 4e e0 7b 00 33 c0 80 f9 04 0f 94 c0` | `e8 eb b7 d3 ff 90 79 19 8a 0d 4d e0 7b 00 33 c0 e8 97 be d3 ff 90` | 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| 4-team patch: team count / team checks for 4 teams (incl. Zones) \| team count: 4 teams if game mode >= 6 or Bag Tag (1); input cl/dl, output al/cl | v5.3 · 2026-10-16 |
| 002F070C | 2E070C | 5 | `e8 83 b9 0d 00` | `e8 73 69 5f 00` | Scoreboard text: in Bag Tag (mode 1) the score shown comes from 0x65A20 (team total) through 0x11AA0; other modes unchanged. | v5.3 · 2026-10-16 |
| 002F2353 | 2E2353 | 5 | `e8 3c 9d 0d 00` | `e8 2c 4d 5f 00` | Same as above for the second scoreboard. | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 00011A10 | 96 bytes | XBE header | team Bag Tag: called from 0x6884a (replaces add %edx,%esi; mov %esi,(%eax); mov 0x82d1e0,%eax) | v5.3 · 2026-10-16 |
| 00011A70 | 15 bytes | XBE header | team count: 4 teams if game mode >= 6 or Bag Tag (1); input cl/dl, output al/cl | v5.3 · 2026-10-16 |
| 00011A7F | 15 bytes | XBE header | Code: DLAL (see the code shown) | v5.3 · 2026-10-16 |
| 00011A8E | 18 bytes | XBE header | Code: DLCL (see the code shown) | v5.3 · 2026-10-16 |
| 00011AA0 | 48 bytes | XBE header | Code: _start (see the code shown) | v5.3 · 2026-10-16 |
| 008E7084 | 240 bytes | xbreadfail_sp | ---- Score page, team rows (0x2f22a0, drawn on consoles where Bag Tag has Teamplay, so only with the patch): each team's score goes through sprintf (text, "%d", score) into an 8-byte stack buffer just under the function's return address. The XBE this mod started from sends that call (0x2f2353) to its own 0x11aa0, which in Bag Tag writes the team's bag time with the game's time text (0x65a20, e.g. "148.5 secs"): longer than 7 characters, it ran over the return address and the console crashed when the score page was shown. Here (call at 0x2f2353, was call 0x11aa0; cdecl text, format, score): Bag Tag: the time as the Results page shows it, m:ss.t ("2:28.5", at most "99:59.9", 7 characters); otherwise sprintf as before | v5.86 · 2026-10-27 |
| 008E7174 | 12 bytes | xbreadfail_sp | ---------------- Manage Players (LAN host, during a match): move a player to another team, or kick a player off another console. | v5.29 · 2026-10-18 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013D728 | 8DAF0A6C | 0C03F840 | lw t7,2668(t5) | jal 0xfe100 | team Bag Tag: bag time counts for the carrier's whole team and is kept when the bag is dropped (team total shown as each player's bag time; synced to LAN players by the host) | v5.3 · 2026-10-16 |
| 0013D72C | 01EB7821 | 00000000 | addu t7,t7,t3 | nop | team Bag Tag: bag time counts for the carrier's whole team and is kept when the bag is dropped (team total shown as each player's bag time; synced to LAN players by the host) | v5.3 · 2026-10-16 |
| 00475418 / PAL 004754B8 | 3C0F0075 | 0040282D | lui t7,0x75 | daddu a1,v0,zero | team Bag Tag: team scores on the scoreboard shown as times | v5.3 · 2026-10-16 |
| 0047541C / PAL 004754BC | 0040302D | 00000000 | daddu a2,v0,zero | nop | team Bag Tag: team scores on the scoreboard shown as times | v5.3 · 2026-10-16 |
| 00475420 / PAL 004754C0 | 25E5F3D0 | 00000000 | addiu a1,t7,-3120 | nop | team Bag Tag: team scores on the scoreboard shown as times | v5.3 · 2026-10-16 |
| 00475424 / PAL 004754C4 | 0C176686 | 0C039B85 | jal 0x5d9a18 | jal 0xe6e14 | team Bag Tag: team scores on the scoreboard shown as times | v5.3 · 2026-10-16 |
| 001CC768 | A5C013AE | 0C03B0ED | sh zero,5038(t6) | jal 0xec3b4 | Respawn Delay (Advanced Settings, Off/1-5 Seconds): Bag Tag, Elimination, Flame Tag, Virus, Monkey Assistant have one delay; Capture the Bag (Red/Blue), Zones (Red/Blue/Yellow/Green) and Assault (Attacker/Defender) have one per team. Host-only for LAN: the host holds back the spawn point until the delay is over | v5.3 · 2026-10-16 |
| 001CC7E0 | 0C0730A8 | 0C03ED58 | jal 0x1cc2a0 | jal 0xfb560 | Respawn Delay (Advanced Settings, Off/1-5 Seconds): Bag Tag, Elimination, Flame Tag, Virus, Monkey Assistant have one delay; Capture the Bag (Red/Blue), Zones (Red/Blue/Yellow/Green) and Assault (Attacker/Defender) have one per team. Host-only for LAN: the host holds back the spawn point until the delay is over | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FE100-000FE17F | 32 | team Bag Tag: bag time counts for the carrier's whole team and is kept when the bag is dropped (team total shown as each player's bag time; synced to LAN players by the host) | v5.3 · 2026-10-16 |
| 000FE180-000FE1AB | 11 | team Bag Tag: team scores on the scoreboard shown as times | v5.3 · 2026-10-16 |
| 000FB000-000FB57B | 327 | Respawn Delay (Advanced Settings, Off/1-5 Seconds): Bag Tag, Elimination, Flame Tag, Virus, Monkey Assistant have one delay; Capture the Bag (Red/Blue), Zones (Red/Blue/Yellow/Green) and Assault (Attacker/Defender) have one per team. Host-only for LAN: the host holds back the spawn point until the delay is over | v5.3 · 2026-10-16 |

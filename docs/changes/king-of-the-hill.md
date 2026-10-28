# King of the Hill

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00134982 | 124982 | 5 | `a1 7c f4 77 00` | `e8 0c 06 7b 00` | radar zone blips: was mov 0x77f47c,%eax \| the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 00134A0D | 124A0D | 5 | `a1 7c f4 77 00` | `e8 81 05 7b 00` | (its loop end) \| the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 0013F730 | 12F730 | 5 | `a1 7c f4 77 00` | `e8 5e 58 7a 00` | zone bar: was mov 0x77f47c,%eax \| the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 0013F954 | 12F954 | 8 | `f3 0f 2a 1d 7c f4 77 00` | `e8 49 56 7a 00 90 90 90` | (its width): was cvtsi2ss 0x77f47c,%xmm3 \| zone bar (call at 0x13f954, was cvtsi2ss 0x77f47c,%xmm3) \| zone bar (call at 0x13f954, was cvtsi2ss 0x77f47c,%xmm3) | v5.3 · 2026-10-16 |
| 0013FA1E | 12FA1E | 5 | `a1 7c f4 77 00` | `e8 70 55 7a 00` | (its loop start) \| the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 0013FB37 | 12FB37 | 6 | `8b 0d 7c f4 77 00` | `e8 72 54 7a 00 90` | (its loop end): was mov 0x77f47c,%ecx \| zone bar (call at 0x13fb37, was mov 0x77f47c,%ecx) \| zone bar (call at 0x13fb37, was mov 0x77f47c,%ecx) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E4F02 | 90 bytes | xbreadfail_sp | eax = King of the Hill setting (1 / 2 / 3) for the match being played (Zones; offline / LAN host: the setting; LAN player: the host's byte 74 bits 2-3 under its 0xC0 marker), else 0; keeps other registers | v5.89 · 2026-10-27 |
| 008E4F5C | 24 bytes | xbreadfail_sp | eax = 1 when this game decides (offline or LAN host); keeps ecx/edx | v5.3 · 2026-10-16 |
| 008E4F74 | 31 bytes | xbreadfail_sp | eax = 1 while King of the Hill runs in this match on this game (Zones, set up), else 0; keeps other registers | v5.3 · 2026-10-16 |
| 008E4F93 | 15 bytes | xbreadfail_sp | the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 008E4FA2 | 12 bytes | xbreadfail_sp | zone bar (call at 0x13f954, was cvtsi2ss 0x77f47c,%xmm3) | v5.3 · 2026-10-16 |
| 008E4FAE | 10 bytes | xbreadfail_sp | zone bar (call at 0x13fb37, was mov 0x77f47c,%ecx) | v5.3 · 2026-10-16 |
| 008E4FB8 | 53 bytes | xbreadfail_sp | eax = this game's first player's character record (the zone drops are made "by" it), or chr slot 0 when it has none; keeps ecx/edx. The drop reads only the chr's prop (Story only) and id (kept as the dropper; only bags use it), never looks for a pad near it (the forced pad is set), and its message carries the chr's slot number, so slot 0 (the host's own chr, which exists before anyone has spawned) works and every game reads a real slot | v5.3 · 2026-10-16 |
| 008E4FED | 78 bytes | xbreadfail_sp | (zone prop, pad; cdecl): drop the zone on the pad as the game drops a bag (every player's game moves it there, and its beam goes out); this game's capture check then uses the pad's height | v5.3 · 2026-10-16 |
| 008E503B | 102 bytes | xbreadfail_sp | LAN host: send every other player their spawn pad again, which carries the zone owners (their game sets the zones' colours). Only players this game holds no spawn pad for (0x7fffffff: alive, their last one used): one still held may be a pad they have just spawned at, and sent again it would be used once more at their next death without asking | v5.89 · 2026-10-27 |
| 008E7568 | 4 bytes | xbreadfail_sp | gameframe last seen | v5.3 · 2026-10-16 (approx.) |
| 008E756C | 4 bytes | xbreadfail_sp | the Hill's period last seen | v5.3 · 2026-10-16 (approx.) |
| 008E7570 | 4 bytes | xbreadfail_sp | host: 1 while XKHZONES sends the spawn pads (XRDYSP) | v5.3 · 2026-10-16 (approx.) |
| 008E7574 | 4 bytes | xbreadfail_sp | host: gameframe to resync the zones for a late joiner (0 = none) | v5.3 · 2026-10-16 (approx.) |
| 008E76C4 | 4 bytes | xbreadfail_sp | host: the second resync for a game entering late (XENTER; 0 = none) | v5.3 · 2026-10-16 (approx.) |
| 008E76C8 | 4 bytes | xbreadfail_sp | host: gameframe to drop every zone on the Hill again (0 = none) | v5.3 · 2026-10-16 (approx.) |
| 008E76CC | 4 bytes | xbreadfail_sp | host: gameframe to send the zones' colours again | v5.3 · 2026-10-16 (approx.) |
| 008E76D0 | 80 bytes | xbreadfail_sp | host: the zones' own pads (the Hill's places), 20 at most | v5.3 · 2026-10-16 (approx.) |
| 008E7720 | 1 bytes | xbreadfail_sp | 0 Off, 1 30 s, 2 60 s, 3 90 s | v5.3 · 2026-10-16 (approx.) |
| 008E7721 | 1 bytes | xbreadfail_sp | King of the Hill running this frame | v5.3 · 2026-10-16 (approx.) |
| 008E7722 | 1 bytes | xbreadfail_sp | this match set up | v5.3 · 2026-10-16 (approx.) |
| 008E7723 | 1 bytes | xbreadfail_sp | LAN player: the Hill's place noted this match | v5.3 · 2026-10-16 (approx.) |
| 008E7724 | 4 bytes | xbreadfail_sp | LAN player: the Hill's place last frame | v5.3 · 2026-10-16 (approx.) |
| 008E7728 | 4 bytes | xbreadfail_sp | Code: XKHMZ (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E772C | 4 bytes | xbreadfail_sp | no Hill message before this gameframe | v5.3 · 2026-10-16 (approx.) |
| 008E7730 | 4 bytes | xbreadfail_sp | moved more than half a unit in a frame: the Hill is moving | v5.3 · 2026-10-16 (approx.) |
| 008E7734 | 4 bytes | xbreadfail_sp | host: which of the places the Hill is at | v5.3 · 2026-10-16 (approx.) |
| 008E7738 | 4 bytes | xbreadfail_sp | host: the places the Hill has been to this round (bit per place) | v5.3 · 2026-10-16 (approx.) |
| 008E773C | 4 bytes | xbreadfail_sp | Data: XKHSECS | v5.3 · 2026-10-16 (approx.) |
| 008E7740 | 17 bytes | xbreadfail_sp | Menu / message text "King of the Hill" | v5.3 · 2026-10-16 |
| 008E7751 | 15 bytes | xbreadfail_sp | Menu / message text "30 Second Hill" | v5.3 · 2026-10-16 |
| 008E7760 | 15 bytes | xbreadfail_sp | Menu / message text "60 Second Hill" | v5.3 · 2026-10-16 |
| 008E776F | 15 bytes | xbreadfail_sp | Menu / message text "90 Second Hill" | v5.3 · 2026-10-16 |
| 008E777E | 22 bytes | xbreadfail_sp | Menu / message text "The Hill has moved!" | v5.44 · 2026-10-19 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013DDA0 | 3C0F0067 | 0C038A52 | lui t7,0x67 | jal 0xe2948 | Hook: zone tick routine: was lui t7,0x67 (delay slot lw t6,32524(t3) kept; KHT returns t7 = 0x670000) | v5.3 · 2026-10-16 |
| 0025E714 | 0C0950CC | 0C03BA0C | jal 0x254330 | jal 0xee830 | Hook: the radar: was jal 0x254330 (delay slot nop kept) | v5.3 · 2026-10-16 |
| 00266428 | 3C0F0026 | 3C0F000F | lui t7,0x26 | lui t7,0xf | Hook: Zones score bar: was lui t7,0x26 / addiu s4,t7,0x5230 | v5.3 · 2026-10-16 |
| 00266430 | 25F45230 | 25F4E888 | addiu s4,t7,21040 | addiu s4,t7,-6008 | Hook: Zones score bar: was lui t7,0x26 / addiu s4,t7,0x5230 | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E2948-000E2BCB | 161 | KHT: zones tick (jal at 0x13DDA0 in zone tick routine, was lui t7,0x67; its delay slot lw t6,32524(t3) kept): every game works out the Hill's period; host / offline set the match up, move the Hill when the period moves on and resync | v5.83 · 2026-10-26 |
| 000E669C-000E67EF | 85 | KHMID: v0 = the middle place: the one with the shortest total distance to the other places (the first of equals; 0 with none; a pad the game does not know counts as 0,0,0); 20 places at most; uses t0-t9, f0-f4 | v5.3 · 2026-10-16 |
| 000E8120-000E8227 | 66 | KHCOL: host / offline, after the zones were dropped: their colours back on this game, then on every other player's game (the zone owners when any zone is not held, then each held zone's capture replayed, which also gives a | v5.3 · 2026-10-16 |
| 000E8910-000E8A07 | 62 | KHMOVE: host / offline: the Hill moves to another of the places at random, one it has not been to yet this round (every place once before any repeats; a new round never starts at the place it is at); the top 16 bits of the random number | v5.44 · 2026-10-19 |
| 000E9B94-000E9C63 | 52 | KHMV: LAN player with the patch: the message when the Hill actually moves (the first zone flies to its new place), as well as on this game's own count of the periods | v5.3 · 2026-10-16 |
| 000E9D30-000E9DFB | 51 | KHGATHER: host / offline: every zone dropped on the Hill's pad (offline the game would scatter them around a big pad, so its size is 0 meanwhile), then their colours back | v5.3 · 2026-10-16 |
| 000EA8A8-000EA963 | 47 | KHZONES: LAN host: every other game's connected player gets their spawn pad again, which carries the zone owners (their game sets the zones' colours). Only players this game holds no spawn pad for (0x7fffffff: alive, their last one | v5.89 · 2026-10-27 |
| 000EB280-000EB32F | 44 | KHEFF: leaf: v0 = King of the Hill setting (1 / 2 / 3) for the match being played (Zones; offline / LAN host: the setting; LAN player: the host's byte 74 bits 2-3 under its 0xC0 marker), else 0; uses t8,t9 | v5.89 · 2026-10-27 |
| 000EB688-000EB72B | 41 | KHMSG: "The Hill has moved!" to every player of this game and the sting; at most one every 5 seconds (a LAN player has two ways to notice a move) | v5.3 · 2026-10-16 |
| 000EBCB8-000EBD53 | 39 | KHITEM: Advanced page (Zones): King of the Hill, the mode's own setting, first (after Zone Scoring Interval) | v5.3 · 2026-10-16 |
| 000EC8C8-000EC94F | 34 | KHSTART: host / offline, match start: the zones' own places noted (the Hill's places), the Hill starts at the middle one | v5.44 · 2026-10-19 |
| 000ED234-000ED2AF | 31 | KHDROP: a0 = zone prop, a1 = pad: drop the zone on the pad as the game drops a bag (every player's game moves it there), then this game's capture check uses where it lands (home position +32 = target position +144) | v5.3 · 2026-10-16 |
| 000ED914-000ED983 | 28 | KHVIS: a game with the patch: the Hill drawn as one zone (every other zone in it without its beam and flame) | v5.3 · 2026-10-16 |
| 000EE830-000EE887 | 22 | KHRAD: jal at 0x25E714 (was jal 0x254330, the radar): the radar's zone blips, one for the Hill | v5.3 · 2026-10-16 |
| 000EE888-000EE8DF | 22 | KHZB: the Zones score bar (its address, loaded at 0x266428 / 0x266430, was 0x265230): one circle for the Hill | v5.3 · 2026-10-16 |
| 000EE8E0-000EE937 | 22 | KHJOINED: host: a player is joining mid-match (from GGJOIN): resync the zones 5 seconds later | v5.3 · 2026-10-16 |
| 000EEC2C-000EEC7F | 21 | KHRA: a0 = page, a1 = 0 refresh / 1 apply: King of the Hill value | v5.3 · 2026-10-16 |
| 000EED74-000EEDC3 | 20 | KHCHR: leaf: v0 = this game's first player's character record (the zone drops are made "by" it), or chr slot 0 when it has none (the host before it has spawned, or dead); uses t0-t3. The drop only reads the chr's prop (Story only) and id (the | v5.3 · 2026-10-16 |
| 000EF898-000EF8CF | 14 | KHLATER: leaf: LAN host: every zone dropped on the Hill again 2 seconds later (a game whose network let a drop or capture arrive late or out of order puts it right); uses t8,t9 | v5.3 · 2026-10-16 |
| 000EF9D4-000EFA07 | 13 | KHON: leaf: v0 = 1 while King of the Hill runs in this match on this game (Zones, set up), else 0; uses t9 | v5.3 · 2026-10-16 |
| 000EFC98-000EFCBF | 10 | KHAUTH: leaf: v0 = 1 when this game decides (offline or LAN host); uses t9 | v5.3 · 2026-10-16 |
| 000EFEF4-000EFF07 | 5 | LKH: text | v5.3 · 2026-10-16 |
| 000EFF08-000EFF1B | 5 | LKHM: text | v5.3 · 2026-10-16 |
| 000F002C-000F003B | 4 | LKH30: text | v5.3 · 2026-10-16 |
| 000F003C-000F004B | 4 | LKH60: text | v5.3 · 2026-10-16 |
| 000F004C-000F005B | 4 | LKH90: text | v5.3 · 2026-10-16 |

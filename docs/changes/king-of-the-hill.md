# King of the Hill

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00134982 | 124982 | 5 | `a1 7c f4 77 00` | `e8 b0 06 7b 00` | radar zone blips: was mov 0x77f47c,%eax \| the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 00134A0D | 124A0D | 5 | `a1 7c f4 77 00` | `e8 25 06 7b 00` | (its loop end) \| the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 0013F730 | 12F730 | 5 | `a1 7c f4 77 00` | `e8 02 59 7a 00` | zone bar: was mov 0x77f47c,%eax \| the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 0013F954 | 12F954 | 8 | `f3 0f 2a 1d 7c f4 77 00` | `e8 ed 56 7a 00 90 90 90` | (its width): was cvtsi2ss 0x77f47c,%xmm3 \| zone bar (call at 0x13f954, was cvtsi2ss 0x77f47c,%xmm3) \| zone bar (call at 0x13f954, was cvtsi2ss 0x77f47c,%xmm3) | v5.3 · 2026-10-16 |
| 0013FA1E | 12FA1E | 5 | `a1 7c f4 77 00` | `e8 14 56 7a 00` | (its loop start) \| the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 0013FB37 | 12FB37 | 6 | `8b 0d 7c f4 77 00` | `e8 16 55 7a 00 90` | (its loop end): was mov 0x77f47c,%ecx \| zone bar (call at 0x13fb37, was mov 0x77f47c,%ecx) \| zone bar (call at 0x13fb37, was mov 0x77f47c,%ecx) | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E4FA6 | 90 bytes | xbreadfail_sp | eax = King of the Hill setting (1 / 2 / 3) for the match being played (Zones; offline / LAN host: the setting; LAN player: the host's byte 74 bits 2-3 under its 0xC0 marker), else 0; keeps other registers | v5.89 · 2026-10-27 |
| 008E5000 | 24 bytes | xbreadfail_sp | eax = 1 when this game decides (offline or LAN host); keeps ecx/edx | v5.3 · 2026-10-16 |
| 008E5018 | 31 bytes | xbreadfail_sp | eax = 1 while King of the Hill runs in this match on this game (Zones, set up), else 0; keeps other registers | v5.3 · 2026-10-16 |
| 008E5037 | 15 bytes | xbreadfail_sp | the zone count the radar and the zone bar draw: just the Hill (the first zone) while King of the Hill runs (calls replacing mov 0x77f47c,%eax); keeps other registers | v5.3 · 2026-10-16 |
| 008E5046 | 12 bytes | xbreadfail_sp | zone bar (call at 0x13f954, was cvtsi2ss 0x77f47c,%xmm3) | v5.3 · 2026-10-16 |
| 008E5052 | 10 bytes | xbreadfail_sp | zone bar (call at 0x13fb37, was mov 0x77f47c,%ecx) | v5.3 · 2026-10-16 |
| 008E505C | 53 bytes | xbreadfail_sp | eax = this game's first player's character record (the zone drops are made "by" it), or chr slot 0 when it has none; keeps ecx/edx. The drop reads only the chr's prop (Story only) and id (kept as the dropper; only bags use it), never looks for a pad near it (the forced pad is set), and its message carries the chr's slot number, so slot 0 (the host's own chr, which exists before anyone has spawned) works and every game reads a real slot | v5.3 · 2026-10-16 |
| 008E5091 | 78 bytes | xbreadfail_sp | (zone prop, pad; cdecl): drop the zone on the pad as the game drops a bag (every player's game moves it there, and its beam goes out); this game's capture check then uses the pad's height | v5.3 · 2026-10-16 |
| 008E50DF | 102 bytes | xbreadfail_sp | LAN host: send every other player their spawn pad again, which carries the zone owners (their game sets the zones' colours). Only players this game holds no spawn pad for (0x7fffffff: alive, their last one used): one still held may be a pad they have just spawned at, and sent again it would be used once more at their next death without asking | v5.89 · 2026-10-27 |
| 008E766C | 4 bytes | xbreadfail_sp | gameframe last seen | v5.3 · 2026-10-16 (approx.) |
| 008E7670 | 4 bytes | xbreadfail_sp | the Hill's period last seen | v5.3 · 2026-10-16 (approx.) |
| 008E7674 | 4 bytes | xbreadfail_sp | the gameframe this match's King of the Hill was set up (its periods count from it) | v5.3 · 2026-10-16 (approx.) |
| 008E7678 | 4 bytes | xbreadfail_sp | host: 1 while XKHZONES sends the spawn pads (XRDYSP) | v5.3 · 2026-10-16 (approx.) |
| 008E767C | 4 bytes | xbreadfail_sp | host: gameframe to resync the zones for a late joiner (0 = none) | v5.3 · 2026-10-16 (approx.) |
| 008E77CC | 4 bytes | xbreadfail_sp | host: the second resync for a game entering late (XENTER; 0 = none) | v5.3 · 2026-10-16 (approx.) |
| 008E77D0 | 4 bytes | xbreadfail_sp | host: gameframe to drop every zone on the Hill again (0 = none) | v5.3 · 2026-10-16 (approx.) |
| 008E77D4 | 4 bytes | xbreadfail_sp | host: gameframe to send the zones' colours again | v5.3 · 2026-10-16 (approx.) |
| 008E77D8 | 80 bytes | xbreadfail_sp | host: the zones' own pads (the Hill's places), 20 at most | v5.3 · 2026-10-16 (approx.) |
| 008E7828 | 1 bytes | xbreadfail_sp | 0 Off, 1 30 s, 2 60 s, 3 90 s | v5.3 · 2026-10-16 (approx.) |
| 008E7829 | 1 bytes | xbreadfail_sp | King of the Hill running this frame | v5.3 · 2026-10-16 (approx.) |
| 008E782A | 1 bytes | xbreadfail_sp | this match set up | v5.3 · 2026-10-16 (approx.) |
| 008E782B | 1 bytes | xbreadfail_sp | LAN player: the Hill's place noted this match | v5.3 · 2026-10-16 (approx.) |
| 008E782C | 4 bytes | xbreadfail_sp | LAN player: the Hill's place last frame | v5.3 · 2026-10-16 (approx.) |
| 008E7830 | 4 bytes | xbreadfail_sp | Code: XKHMZ (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E7834 | 4 bytes | xbreadfail_sp | no Hill message before this gameframe | v5.3 · 2026-10-16 (approx.) |
| 008E7838 | 4 bytes | xbreadfail_sp | moved more than half a unit in a frame: the Hill is moving | v5.3 · 2026-10-16 (approx.) |
| 008E783C | 4 bytes | xbreadfail_sp | host: which of the places the Hill is at | v5.3 · 2026-10-16 (approx.) |
| 008E7840 | 4 bytes | xbreadfail_sp | host: the places the Hill has been to this round (bit per place) | v5.3 · 2026-10-16 (approx.) |
| 008E7844 | 4 bytes | xbreadfail_sp | Data: XKHSECS | v5.3 · 2026-10-16 (approx.) |
| 008E7848 | 17 bytes | xbreadfail_sp | Menu / message text "King of the Hill" | v5.3 · 2026-10-16 |
| 008E7859 | 15 bytes | xbreadfail_sp | Menu / message text "30 Second Hill" | v5.3 · 2026-10-16 |
| 008E7868 | 15 bytes | xbreadfail_sp | Menu / message text "60 Second Hill" | v5.3 · 2026-10-16 |
| 008E7877 | 15 bytes | xbreadfail_sp | Menu / message text "90 Second Hill" | v5.3 · 2026-10-16 |
| 008E7886 | 22 bytes | xbreadfail_sp | Menu / message text "The Hill has moved!" | v5.44 · 2026-10-19 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013DDA0 | 3C0F0067 | 0C0389BF | lui t7,0x67 | jal 0xe26fc | Hook: zone tick routine: was lui t7,0x67 (delay slot lw t6,32524(t3) kept; KHT returns t7 = 0x670000) | v5.3 · 2026-10-16 |
| 0025E714 | 0C0950CC | 0C03BBB5 | jal 0x254330 | jal 0xeeed4 | Hook: the radar: was jal 0x254330 (delay slot nop kept) | v5.3 · 2026-10-16 |
| 00266428 | 3C0F0026 | 3C0F000F | lui t7,0x26 | lui t7,0xf | Hook: Zones score bar: was lui t7,0x26 / addiu s4,t7,0x5230 | v5.3 · 2026-10-16 |
| 00266430 | 25F45230 | 25F4EF2C | addiu s4,t7,21040 | addiu s4,t7,-4308 | Hook: Zones score bar: was lui t7,0x26 / addiu s4,t7,0x5230 | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E26FC-000E2997 | 167 | KHT: zones tick (jal at 0x13DDA0 in zone tick routine, was lui t7,0x67; its delay slot lw t6,32524(t3) kept): every game works out the Hill's period; host / offline set the match up, move the Hill when the period moves on and resync | v5.107 · 2026-10-29 |
| 000E68EC-000E6A3F | 85 | KHMID: v0 = the middle place: the one with the shortest total distance to the other places (the first of equals; 0 with none; a pad the game does not know counts as 0,0,0); 20 places at most; uses t0-t9, f0-f4 | v5.3 · 2026-10-16 |
| 000E836C-000E8473 | 66 | KHCOL: host / offline, after the zones were dropped: their colours back on this game, then on every other player's game (the zone owners when any zone is not held, then each held zone's capture replayed, which also gives a | v5.3 · 2026-10-16 |
| 000E8C54-000E8D4B | 62 | KHMOVE: host / offline: the Hill moves to another of the places at random, one it has not been to yet this round (every place once before any repeats; a new round never starts at the place it is at); the top 16 bits of the random number | v5.44 · 2026-10-19 |
| 000E9FC4-000EA093 | 52 | KHMV: LAN player with the patch: the message when the Hill actually moves (the first zone flies to its new place), as well as on this game's own count of the periods | v5.3 · 2026-10-16 |
| 000EA160-000EA22B | 51 | KHGATHER: host / offline: every zone dropped on the Hill's pad (offline the game would scatter them around a big pad, so its size is 0 meanwhile), then their colours back | v5.3 · 2026-10-16 |
| 000EAC10-000EACCB | 47 | KHZONES: LAN host: every other game's connected player gets their spawn pad again, which carries the zone owners (their game sets the zones' colours). Only players this game holds no spawn pad for (0x7fffffff: alive, their last one | v5.89 · 2026-10-27 |
| 000EB538-000EB5E7 | 44 | KHEFF: leaf: v0 = King of the Hill setting (1 / 2 / 3) for the match being played (Zones; offline / LAN host: the setting; LAN player: the host's byte 74 bits 2-3 under its 0xC0 marker), else 0; uses t8,t9 | v5.89 · 2026-10-27 |
| 000EB9E4-000EBA87 | 41 | KHMSG: "The Hill has moved!" to every player of this game and the sting; at most one every 5 seconds (a LAN player has two ways to notice a move) | v5.3 · 2026-10-16 |
| 000EC150-000EC1EB | 39 | KHITEM: Advanced page (Zones): King of the Hill, the mode's own setting, first (after Zone Scoring Interval) | v5.3 · 2026-10-16 |
| 000ECF8C-000ED013 | 34 | KHSTART: host / offline, match start: the zones' own places noted (the Hill's places), the Hill starts at the middle one | v5.44 · 2026-10-19 |
| 000ED874-000ED8EF | 31 | KHDROP: a0 = zone prop, a1 = pad: drop the zone on the pad as the game drops a bag (every player's game moves it there), then this game's capture check uses where it lands (home position +32 = target position +144) | v5.3 · 2026-10-16 |
| 000EDF54-000EDFC3 | 28 | KHVIS: a game with the patch: the Hill drawn as one zone (every other zone in it without its beam and flame) | v5.3 · 2026-10-16 |
| 000EEED4-000EEF2B | 22 | KHRAD: jal at 0x25E714 (was jal 0x254330, the radar): the radar's zone blips, one for the Hill | v5.3 · 2026-10-16 |
| 000EEF2C-000EEF83 | 22 | KHZB: the Zones score bar (its address, loaded at 0x266428 / 0x266430, was 0x265230): one circle for the Hill | v5.3 · 2026-10-16 |
| 000EEF84-000EEFDB | 22 | KHJOINED: host: a player is joining mid-match (from GGJOIN): resync the zones 5 seconds later | v5.3 · 2026-10-16 |
| 000EF2D0-000EF323 | 21 | KHRA: a0 = page, a1 = 0 refresh / 1 apply: King of the Hill value | v5.3 · 2026-10-16 |
| 000EF468-000EF4B7 | 20 | KHCHR: leaf: v0 = this game's first player's character record (the zone drops are made "by" it), or chr slot 0 when it has none (the host before it has spawned, or dead); uses t0-t3. The drop only reads the chr's prop (Story only) and id (the | v5.3 · 2026-10-16 |
| 000EFF48-000EFF7F | 14 | KHLATER: leaf: LAN host: every zone dropped on the Hill again 2 seconds later (a game whose network let a drop or capture arrive late or out of order puts it right); uses t8,t9 | v5.3 · 2026-10-16 |
| 000F00B8-000F00EB | 13 | KHON: leaf: v0 = 1 while King of the Hill runs in this match on this game (Zones, set up), else 0; uses t9 | v5.3 · 2026-10-16 |
| 000F03D4-000F03FB | 10 | KHAUTH: leaf: v0 = 1 when this game decides (offline or LAN host); uses t9 | v5.3 · 2026-10-16 |
| 000F0650-000F0663 | 5 | LKH: text | v5.3 · 2026-10-16 |
| 000F0664-000F0677 | 5 | LKHM: text | v5.3 · 2026-10-16 |
| 000F0788-000F0797 | 4 | LKH30: text | v5.3 · 2026-10-16 |
| 000F0798-000F07A7 | 4 | LKH60: text | v5.3 · 2026-10-16 |
| 000F07A8-000F07B7 | 4 | LKH90: text | v5.3 · 2026-10-16 |

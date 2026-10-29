# LAN: everyone starts the match together

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002EF7D5 | 2DF7D5 | 5 | `e8 86 39 d5 ff` | `e8 cb 87 5f 00` | Select Team (team games on LAN): the second A press after picking a team calls XHBTN, which reads it as pressed on the LAN host, so the host spawns as soon as its players have picked a team and an away host no longer holds the match up (was: call 0x43160, the pad's pressed buttons). Clients still press A. | v5.3 · 2026-10-16 |
| 0035B176 | 34B176 | 5 | `e8 e5 c7 ff ff` | `e8 e8 56 58 00` | Start of a match (spawn point message): the server check calls XRDYSP, so the host holds the spawn point for another game's player while the host is still on its start screen or Select Team (game state 4 or 6). Their game asks again every frame and gets it as soon as the host moves on, so everyone counts down together (was: call 0x357960, network host check). | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E0863 | 123 bytes | xbreadfail_sp | ---- Start of a match, LAN host: each game starts its 3-2-1 once the host has sent it a spawn point. Games that loaded early (Series X) or picked a team at once counted down and moved while the host was still on its start screen or Select Team. The host now holds spawn points for other games' players while it is still there (game state 4 or 6), and sends every one it held as soon as it moves on (XRDYGO), so everyone counts down together (their games ask again only every 1.5 seconds). call at 0x35b176 in spawn point message(player) (was call 0x357960, network host check) | v5.89 · 2026-10-27 |
| 008E0D20 | 145 bytes | xbreadfail_sp | every frame (XGGT), LAN host: once it has left its start screen and Select Team, the spawn points it held go out now to every other game's player who has one (not 0x7fffffff), as spawn point message would have sent them; keeps all | v5.60 · 2026-10-22 |
| 008E0DB1 | 1 bytes | xbreadfail_sp | 1 while XRDYGO sends the spawn points held at the start | v5.3 · 2026-10-16 (approx.) |
| 008E43EE | 2 bytes | xbreadfail_sp | LAN host: a spawn point was held back at the start of the match (XRDYSP) | v5.3 · 2026-10-16 (approx.) |
| 008E7FA5 | 26 bytes | xbreadfail_sp | Select Team's second A press (call at 0x2ef7d5, was call 0x43160, the pad's pressed buttons; then bit 0x80 = A sets the step to 2, everyone picked and ready): on the LAN host it reads as pressed, so the host spawns as soon as its players have picked a team (the others wait for the host, XRDY: an away host no longer holds the match up); only Teamplay games reach it (state 6); keeps esi..ebp | v5.43 · 2026-10-19 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 00471C5C / PAL 00471CFC | 0C0439FA | 0C03BD10 | jal 0x10e7e8 | jal 0xef440 | Hook: Select Team: the host's second press made for it (spawns once picked; delay slot kept) | v5.43 · 2026-10-19 |
| 00500DD4 / PAL 00500E7C | 0C13D616 | 0C03A789 | jal 0x4f5858 | jal 0xe9e24 | Hook: jumps to LRDYSP: jal at 0x500DD4 in spawn point message(player) (was jal 0x4F5858 network host check; delay slot move s0,a0 kept). LAN host: other games' players get their spawn point (and so start their 3-2-1) only once the host has left | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E9E24-000E9EF3 | 52 | LRDYSP: jal at 0x500DD4 in spawn point message(player) (was jal 0x4F5858 network host check; delay slot move s0,a0 kept). LAN host: other games' players get their spawn point (and so start their 3-2-1) only once the host has left | v5.89 · 2026-10-27 |
| 000EF440-000EF487 | 18 | HBTN: jal at 0x471C5C in Select Team (was jal 0x10E7E8, the pad's pressed buttons; delay slot lw a0,60(t5) kept; then bit 0x40 sets the step to 2, everyone picked and ready): on the LAN host it reads as pressed, so the host spawns as soon as | v5.76 · 2026-10-24 |

# Spectate (Elimination, Vampire)

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 000CDA98 | 0BDA98 | 6 | `8b 96 a0 02 00 00` | `e9 af 63 81 00 90` | the first-person camera (jmp at 0xcda98, was mov 0x2a0(%esi),%edx / mov %edx,0x2a4(%esi) ...; esi = the view, edi = its player): \| the first-person camera (jmp at 0xcda98, was mov 0x2a0(%esi),%edx / mov %edx,0x2a4(%esi) ...; esi = the view, edi = its player): as the game's own, except while this player watches another (XSPSRC): the camera at that player's eyes (its feet + eye height), looking the way it looks (its angles: the game's own look direction is cos(up) sin(round), sin(up), cos(up) cos(round)), in its room, and it as the view's own prop (not drawn in this view); then XSP3P takes it behind them. The angles are the watching player's own (XSPCTL); in free cam the camera is where XSPCTL moved it. The view's first-person bit is cleared (no hands). Then on as the game's own (0xcec6c) | v5.78 · 2026-10-26 |
| 0013D05F | 12D05F | 20 | `8b 45 08 3b 01 75 0d f6 82 1c 02 00 00 04 0f 85 64 0a 00 00` | `e9 9c ef 78 00 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90` | Name tags over team-mates (Teamplay): the own-chr test jumps to XHAT, which keeps it (its own tag in first person skipped) and skips the tag of the player being watched (Spectate); everyone else as the game draws them. | v5.85 · 2026-10-26 |
| 0014FC87 | 13FC87 | 9 | `83 3b 0b 0f 84 cf 0a 00 00` | `e9 62 3d 79 00 90 90 90 90` | the HUD: was cmpl $0xb,(%ebx) / je 0x15075f (Spectate)   # first-person camera: was mov 0x2a0(%esi),%edx (Spectate) \| the HUD (jmp at 0x14fc87, was cmpl $0xb,(%ebx) / je 0x15075f; ebx = this player's HUD): a player of this game who is out with \| the HUD (jmp at 0x14fc87, was cmpl $0xb,(%ebx) / je 0x15075f; ebx = this player's HUD): a player of this game who is out with Spectate (XSPOUT) gets only its messages (the game's own message draw 0x14b6f0, as the HUD does after its parts: the kill messages, "Spectating <name>") and none of the rest (the Vampire bar, score, timer, ammo ...) | v5.79 · 2026-10-26 |
| 0015095F | 14095F | 5 | `e8 6c c6 fe ff` | `e8 13 de 77 00` | Name tags while spectating: the call of the name tags' draw goes to XHATW, which, while this player watches someone or is in free cam, has the draw see from the camera (its position and room) instead of the knocked-out player, putting the player's own back after; otherwise the draw as before. | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008CC000 | 54 bytes | xbreadfail_sp | edi = a local number -> eax = its Spectate entry while it is still ours (a kill message saying "Spec..."), else 0; keeps the others | v5.91 · 2026-10-27 |
| 008CC036 | 399 bytes | xbreadfail_sp | edi = a view's player -> eax = the player it watches (Spectate), else 0; keeps the others | v5.86 · 2026-10-27 |
| 008CEAB0 | 42 bytes | xbreadfail_sp | the buttons while watching, bottom left as the game's own remote gun / camera ones (0x136090: its font, place, colours, the | v5.98 · 2026-10-28 |
| 008CEADA | 305 bytes | xbreadfail_sp | the buttons while watching, bottom left as the game's own remote gun / camera ones (0x136090: its font, place, colours, the button names 0x436c0 and text 0x427e0): "<Activate> Freecam" (in free cam "Exit freecam", then "<RT> Speed up", one line higher) and "<D-pad> Switch player" (in .text2 since v5.98) | v5.99 · 2026-10-28 |
| 008CEC0B | 79 bytes | xbreadfail_sp | one line: [esp+4] = a button (popped), ebx = the text; the caller's frame: 0 the text, 0x100 x, 0x104 y (here +8) | v5.79 · 2026-10-26 |
| 008CEC5A | 9 bytes | xbreadfail_sp | Menu / message text " Freecam" | v5.79 · 2026-10-26 |
| 008CEC63 | 14 bytes | xbreadfail_sp | Menu / message text " Exit freecam" | v5.79 · 2026-10-26 |
| 008CEC71 | 15 bytes | xbreadfail_sp | Menu / message text " Switch player" | v5.79 · 2026-10-26 |
| 008CEC80 | 10 bytes | xbreadfail_sp | ---------------- Team Elimination: the Scores page's team rows show the team's lives | v5.98 · 2026-10-28 |
| 008E3723 | 5 bytes | xbreadfail_sp | ---------------- Spectate (Elimination / Vampire, always on for games with the patch: no setting). A player of this game who is out (no lives left) watches a player still in through their eyes: their position and eye height, the way they face and look, their room. D-pad right / left picks the next / previous one; with Teamplay only team-mates; when the one watched is out the next one follows; "Spectating <name>" on each change. Only this game's own view changes (each game draws its own camera; nothing is sent), so games without the patch keep the game's own view and the match plays as before. The view is the game's first-person camera, which XSPFP takes behind the player watched (third person, XSP3P: pulled in by walls; right up against one, at their eyes with them not drawn). per local player number: the PLAYERS index it watches + 1 (0 = none) | v5.3 · 2026-10-16 (approx.) |
| 008E3728 | 4 bytes | xbreadfail_sp | this frame: Spectate applies (XSPON) | v5.3 · 2026-10-16 (approx.) |
| 008E372C | 16 bytes | xbreadfail_sp | per local player number: its "Spectating <name>" HUD entry (XSPMSG) | v5.3 · 2026-10-16 (approx.) |
| 008E373C | 12 bytes | xbreadfail_sp | eax = 1 when Spectate applies to the match being played (Elimination / Vampire with lives); keeps ecx/edx | v5.78 · 2026-10-26 |
| 008E3748 | 35 bytes | xbreadfail_sp | eax = 1 when Spectate applies to the match being played (Elimination / Vampire with lives); keeps ecx/edx | v5.78 · 2026-10-26 |
| 008E376B | 100 bytes | xbreadfail_sp | ecx = a PLAYERS index, ebx = this player's -> eax = 1 if it is another player, in the match, alive (not checked while XSPNA: still in, waiting to respawn) and with lives left (team: XSPOK); keeps the others | v5.98 · 2026-10-28 |
| 008E37CF | 53 bytes | xbreadfail_sp | ecx = a PLAYERS index (-1: none), edx = 1 / -1, ebx = this player's -> ecx = the next / previous one that can be watched (round the list; itself if it is the only one), -1 if none; keeps the others but eax | v5.78 · 2026-10-26 |
| 008E3804 | 165 bytes | xbreadfail_sp | esi = a player of this game who is out: back to the game's death view on itself (the camera from its own eyes first, the way its death left it); keeps ebx, esi, edi, ebp | v5.84 · 2026-10-26 |
| 008E38A9 | 68 bytes | xbreadfail_sp | edi = a local number -> eax = its Spectate entry while it is still ours (a kill message saying "Spec..."), else 0; keeps the others | v5.79 · 2026-10-26 |
| 008E38ED | 29 bytes | xbreadfail_sp | edi = a local number -> eax = its Spectate entry while it is still ours (a kill message saying "Spec..."), else 0; keeps the others | v5.79 · 2026-10-26 |
| 008E390A | 66 bytes | xbreadfail_sp | eax = this player's Spectate entry, edi = its local number -> ZF clear when another entry of its ring is a message the game holds back while a kill message shows (types 2, 6, 9, 10: one kill message at a time, and these wait behind it); keeps all | v5.79 · 2026-10-26 |
| 008E394C | 162 bytes | xbreadfail_sp | after XSPT: each local player watching keeps its message on screen while nothing waits behind it (none in free cam) (its time held at 0.5, inside the 2 seconds it stays; written over by 16 newer HUD entries: made again); stopped watching: it fades | v5.86 · 2026-10-27 |
| 008E39EE | 56 bytes | xbreadfail_sp | the HUD (jmp at 0x14fc87, was cmpl $0xb,(%ebx) / je 0x15075f; ebx = this player's HUD): a player of this game who is out with Spectate (XSPOUT) gets only its messages (the game's own message draw 0x14b6f0, as the HUD does after its parts: the kill messages, "Spectating <name>") and none of the rest (the Vampire bar, score, timer, ammo ...) | v5.84 · 2026-10-26 |
| 008E3A26 | 56 bytes | xbreadfail_sp | esi = a player -> eax = 1 when it is out (Spectate applies this frame, it has a view, it is dead with no lives left) | v5.78 · 2026-10-26 |
| 008E3A5E | 66 bytes | xbreadfail_sp | edi = a view's player -> eax = the player it watches (Spectate), else 0; keeps the others | v5.98 · 2026-10-28 |
| 008E3AA0 | 4 bytes | xbreadfail_sp | degrees to radians | v5.3 · 2026-10-16 (approx.) |
| 008E3AA4 | 4 bytes | xbreadfail_sp | Code: XSPK2 (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E3AA8 | 4 bytes | xbreadfail_sp | per local player number: free cam on | v5.3 · 2026-10-16 (approx.) |
| 008E3AAC | 16 bytes | xbreadfail_sp | per local player number: the camera's angles (degrees), the watching player's to turn | v5.3 · 2026-10-16 (approx.) |
| 008E3ABC | 16 bytes | xbreadfail_sp | Code: XSPPIT (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E3ACC | 48 bytes | xbreadfail_sp | per local player number: free cam position | v5.3 · 2026-10-16 (approx.) |
| 008E3AFC | 64 bytes | xbreadfail_sp | per local player number: its view's camera (position, room) when it started watching, for XSPDV | v5.3 · 2026-10-16 (approx.) |
| 008E3B3C | 4 bytes | xbreadfail_sp | per local player number: XSPSV holds one | v5.3 · 2026-10-16 (approx.) |
| 008E3B40 | 16 bytes | xbreadfail_sp | per local player number: free cam room | v5.3 · 2026-10-16 (approx.) |
| 008E3B50 | 44 bytes | xbreadfail_sp | 1, turn (deg/s), up/down (deg/s), free cam (m/s), up limits, wall gap, still, round limits | v5.79 · 2026-10-26 |
| 008E3B7C | 4 bytes | xbreadfail_sp | the player's control slots for axes 1-4 here (strafe, forward, turn, look) | v5.3 · 2026-10-16 (approx.) |
| 008E3B80 | 48 bytes | xbreadfail_sp | ecx = the PLAYERS index now watched, edi = the local number: no free cam, the camera's angles its own; keeps all but eax | v5.79 · 2026-10-26 |
| 008E3BB0 | 93 bytes | xbreadfail_sp | esi = the player, edi = its local number: free cam on (from where the camera is, in its room) / off; keeps all but eax | v5.86 · 2026-10-27 |
| 008E3C0D | 575 bytes | xbreadfail_sp | esi = the player, edi = its local number: its sticks (the game's 0x43320(player number, axis), each from the player's own control slot as the game's look does, so a southpaw layout works) turn the camera (as the game's own look: right turns the angle down, up raises it, the player's Invert Look) and in free cam move it (left stick: along the look and across; a wall or door in the way (the game's line test, 0.3 short) stops it, the room traced along); keeps all | v5.98 · 2026-10-28 |
| 008E3E4C | 380 bytes | xbreadfail_sp | the first-person camera (jmp at 0xcda98, was mov 0x2a0(%esi),%edx / mov %edx,0x2a4(%esi) ...; esi = the view, edi = its player): as the game's own, except while this player watches another (XSPSRC): the camera at that player's eyes (its feet + eye height), looking the way it looks (its angles: the game's own look direction is cos(up) sin(round), sin(up), cos(up) cos(round)), in its room, and it as the view's own prop (not drawn in this view); then XSP3P takes it behind them. The angles are the watching player's own (XSPCTL); in free cam the camera is where XSPCTL moved it. The view's first-person bit is cleared (no hands). Then on as the game's own (0xcec6c) | v5.86 · 2026-10-27 |
| 008E3FC8 | 304 bytes | xbreadfail_sp | third person: esi = the view (at the eyes of the one watched, looking its way, in its room), edi = the view's player. The camera goes XSP3D back along the look and XSP3H up; a line from the eyes to there (walls and doors stop it, the game's own camera test) pulls it in, XSP3G short of what it hits; if that leaves less than XSP3M of the way, it stays at the eyes (first person, the one watched not drawn). Else its room from the eyes' (the game's room trace), and the view's own prop is its player's, so the one watched is drawn | v5.86 · 2026-10-27 |
| 008E40F8 | 4 bytes | xbreadfail_sp | back (along the look) | v5.3 · 2026-10-16 (approx.) |
| 008E40FC | 4 bytes | xbreadfail_sp | up | v5.3 · 2026-10-16 (approx.) |
| 008E4100 | 4 bytes | xbreadfail_sp | short of a wall | v5.3 · 2026-10-16 (approx.) |
| 008E4104 | 4 bytes | xbreadfail_sp | the least share of the way (0.7 back) | v5.3 · 2026-10-16 (approx.) |
| 008E4108 | 4 bytes | xbreadfail_sp | ---------------- Capture the Bag Overtime (Advanced Settings, Capture the Bag: Off / On), decided by the host (offline: this game) | v5.3 · 2026-10-16 (approx.) |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 001C2010 | 3C0F0065 | 08038DC9 | lui t7,0x65 | j 0xe3724 | Hook: first-person camera: was lui t7,0x65 / lwc1 f0,184(s2) (Spectate) | v5.78 · 2026-10-26 |
| 001C2014 | C64000B8 | 00000000 | lwc1 zero,184(s2) | nop | Hook: first-person camera: was lui t7,0x65 / lwc1 f0,184(s2) (Spectate) | v5.78 · 2026-10-26 |
| 0025E174 | 8E6F0000 | 0803B252 | lw t7,0(s3) | j 0xec948 | Hook: the HUD: was lw t7,0(s3) / beq t7,s0,0x25EB2C (delay slot lui s5,0x68 kept) (Spectate) | v5.79 · 2026-10-26 |
| 0025E178 | 11F0026C | 3C150068 | beq t7,s0,0x25eb2c | lui s5,0x68 | Hook: the HUD: was lw t7,0(s3) / beq t7,s0,0x25EB2C (delay slot lui s5,0x68 kept) (Spectate) | v5.79 · 2026-10-26 |
| 0025EC70 | 0C098812 | 0C03A3FA | jal 0x262048 | jal 0xe8fe8 | Hook: name tags' draw: while spectating, sight from the camera (HATW; was jal 0x262048) | v5.93 · 2026-10-27 |
| 00262178 | 55CF0008 | 0803B839 | bnel t6,t7,0x26219c | j 0xee0e4 | Hook: name tags: not the watched player's (Spectate) | v5.85 · 2026-10-26 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E0F60-000E1363 | 257 | SPCTL: a0 = the player, a1 = its local number: its sticks (the game's 0x10EB90(a0 player number, a1 axis) -> f0: 1 / 2 left stick across / up, 3 / 4 right stick) turn the camera (right stick, as the game's own look: right turns the angle down) and in | v5.98 · 2026-10-28 |
| 000E2404-000E26BF | 175 | SPTK: every frame (GGT): each player of this game who is out picks who it watches | v5.86 · 2026-10-27 |
| 000E3724-000E393F | 135 | SPFP: j at 0x1C2010 (the first-person camera, was lui t7,0x65 / lwc1 f0,184(s2) ...; s2 = this view's player): as the game's own, except while this player watches another (SPT): the camera at that player's eyes (its feet + eye height), looking | v5.86 · 2026-10-27 |
| 000E4894-000E4A5F | 115 | SP3P: third person: a0 = the view (at the eyes of the one watched, looking its way, in its room), s2 = the view's player. The camera goes 2 back along the look and 0.35 up (SPK +8 / +12); a line from the eyes to there (walls and doors stop it, the | v5.78 · 2026-10-26 |
| 000E5730-000E58B7 | 98 | SPLEG: the buttons while watching, bottom left as the game's own remote gun / camera ones (0x257... : its font, place, colours, the button names 0x10F408 and text 0x10D158): "<Activate> Freecam" (in free cam "Exit freecam", then | v5.98 · 2026-10-28 |
| 000E78DC-000E79F3 | 70 | SPKA: after SPTK: each local player watching keeps its message on screen (its time held at 0.5, inside the 2 seconds it stays; written over by 16 newer HUD entries: made again); stopped watching: it fades | v5.86 · 2026-10-27 |
| 000E8FE8-000E90D3 | 59 | HATW: jal at 0x25EC70 (was jal 0x262048, the name tags' draw, every frame per local player 0x653AB0): it decides who is in sight (a line from this player's eyes +184, in its room +3576, to the other's head) from the player itself. While it | v5.93 · 2026-10-27 |
| 000EA240-000EA307 | 50 | SPOK0: a0 = a PLAYERS index, a1 = this player's, v1 = 0 / 1 -> v0 = 1 if it is another player, in the match, alive (not checked with v1 1: still in, waiting to respawn) and with lives left; keeps a0-a3 (uses the t registers) | v5.84 · 2026-10-26 |
| 000EB194-000EB243 | 44 | SPOK: a0 = a PLAYERS index, a1 = this player's -> v0 = 1 if it can be watched: another player, in the match, alive, with lives left (SPOK0); with Teamplay on this player's team, or anyone once nobody on its team is still in (lives left, | v5.84 · 2026-10-26 |
| 000EB244-000EB2F3 | 44 | SPOKK: (as SPOK, for the one already watched: alive or not, still in: a death with lives left keeps it; then) a0 = a PLAYERS index, a1 = this player's -> v0 = 1 if it can be watched: another player, in the match, alive, with | v5.86 · 2026-10-27 |
| 000EB654-000EB6FB | 42 | SPDV: a0 = a player of this game who is out: back to the game's death view on itself (the camera from its own eyes first, the way its death left it) | v5.84 · 2026-10-26 |
| 000EC450-000EC4E3 | 37 | SPMSG: a0 = the PLAYERS index now watched, a1 = this player's local number: "Spectating <name>" as a kill message (the game's own HUD entry 0x2491E0: the text, then the name in its team colour, at the bottom), kept on screen while | v5.79 · 2026-10-26 |
| 000EC694-000EC723 | 36 | SPL1: one line: a0 = a button, a1 = a second one (0: none), a2 = the text; the caller's frame (SPLEG's, at sp+32 here): 0 the text, 256 x, 260 y | v5.79 · 2026-10-26 |
| 000EC948-000EC9CF | 34 | SPHUD: j at 0x25E174 in the HUD (was lw t7,0(s3) / beq t7,s0,0x25EB2C; s3 = this player's HUD, s0 = 11): a player of this game who is out with Spectate (SPAP, its view, dead, no lives) gets only its messages (the game's own message | v5.84 · 2026-10-26 |
| 000ED58C-000ED603 | 30 | SPFCT: leaf: a0 = the player, a1 = its local number: free cam on (from where the camera is, in its room) / off; uses t4-t9 | v5.86 · 2026-10-27 |
| 000ED760-000ED7D3 | 29 | SPSAME: leaf: a0, a1 = PLAYERS indexes -> v0 = 1 if their characters are on the same team; uses t5-t9 | v5.84 · 2026-10-26 |
| 000ED7D4-000ED847 | 29 | SPNEXT: a0 = a PLAYERS index (-1: none), a2 = 1 / -1, a1 = this player's -> v0 = the next / previous one that can be watched (round the list; itself if it is the only one), -1 if none; uses a0, a3, t5-t9 | v5.78 · 2026-10-26 |
| 000EDC24-000EDC8F | 27 | SPEV: leaf: a0 = a local number -> v0 = its Spectate HUD entry (SPE) while it is still ours (a kill message saying "Spec..."), else 0; uses t5-t9 | v5.79 · 2026-10-26 |
| 000EE0E4-000EE147 | 25 | HTSK: j at 0x262178 in the name tags' draw (Teamplay: the name over each team-mate; was bnel t6,t7,0x26219C, its delay slot lw t5,0x14(t4) now always run; t6 = the chr's id, t7 = this player's number, t4 = this player, s2 = the chr): | v5.91 · 2026-10-27 |
| 000EF2D8-000EF31F | 18 | SPANG0: leaf: a0 = the PLAYERS index now watched, a1 = the local number: no free cam, the camera's angles its own; uses t6-t9 | v5.79 · 2026-10-26 |
| 000EF970-000EF9A7 | 14 | SPON: leaf: v0 = 1 when Spectate applies to the match being played (Elimination / Vampire with lives; always on for games with the patch, no setting); uses t8, t9 | v5.78 · 2026-10-26 |
| 000EFC60-000EFC8B | 11 | SPK2: code | v5.79 · 2026-10-26 |
| 000EFF4C-000EFF67 | 7 | SPK: code | v5.78 · 2026-10-26 |
| 000F00BC-000F00CB | 4 | LSPFX: text | v5.79 · 2026-10-26 |
| 000F00CC-000F00DB | 4 | LSPSW: text | v5.79 · 2026-10-26 |
| 000F01DC-000F01E7 | 3 | LSPG: text | v5.78 · 2026-10-26 |
| 000F01E8-000F01F3 | 3 | LSPF: text | v5.78 · 2026-10-26 (approx.) |
| 000F0304-000F030B | 2 | SPK3: code | v5.78 · 2026-10-26 (approx.) |

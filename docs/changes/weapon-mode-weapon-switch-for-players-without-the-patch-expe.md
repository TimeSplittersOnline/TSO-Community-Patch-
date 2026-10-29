# Weapon Mode: weapon switch for players without the patch (experimental)

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 000679F3 | 0579F3 | 5 | `e8 98 ce ff ff` | `e8 a0 88 87 00` | end-of-level code: was call 0x64890 (the "Always" overrides go back) \| the end of a match (call at 0x679f3 in the end-of-level code every mode's end goes through, was call 0x64890): every \| the end of a match (call at 0x679f3 in the end-of-level code every mode's end goes through, was call 0x64890): every "Always" still on goes back now (XPFT only runs while the match is played, so one handed out in the last seconds stayed) | v5.3 · 2026-10-16 |
| 00356B67 | 346B67 | 6 | `0f 84 81 03 00 00` | `0f 84 2a 6d 57 00` | Packet decoder: the jump taken when this game is not in the match yet (its in-game traffic flag clear) now goes to XPFGATE, which keeps a copy of a player's settings (packet 15) that the game would throw away there, so the LAN host can still use them at the weapon hand-out; then on to the game's own path as before (was je 0x356eee). | v5.3 · 2026-10-16 |
| 00356EB2 | 346EB2 | 5 | `e8 09 30 00 00` | `e8 c5 69 57 00` | packet 15 received: was call player settings reader (a copy kept by name, XPFRCV) \| call at 0x356eb2 (packet 15 received; was call player settings reader): player settings reader, then (LAN) keep a copy of another game's player's prefs \| call at 0x356eb2 (packet 15 received; was call player settings reader): player settings reader, then (LAN) keep a copy of another game's player's prefs under their name; an "Always" that is our own override (XPFON) keeps their own setting | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008CD69A | 51 bytes | xbreadfail_sp | esi = chr, eax = gun id -> ZF clear (jnz) if the gun in its hands (+0x94) is that gun (by gun type); keeps all | v5.77 · 2026-10-25 |
| 008CD7F0 | 67 bytes | xbreadfail_sp | edi = a name (as network player table +8) -> eax = the kept entry with that name (0 = none), ebp = the first empty one (0 = none); keeps the others | v5.100 · 2026-10-28 |
| 008CD833 | 73 bytes | xbreadfail_sp | ebx = slot -> ZF clear if another player in the game (another network player table slot with an owner) has the same name; keeps the others | v5.81 · 2026-10-26 |
| 008CD87C | 27 bytes | xbreadfail_sp | call at 0x356eb2 (packet 15 received; was call player settings reader): player settings reader, then (LAN) keep a copy of another game's player's prefs under their name; an "Always" that is our own override (XPFON) keeps their own setting | v5.82 · 2026-10-26 |
| 008CD897 | 28 bytes | xbreadfail_sp | The game takes packet 15 only while its own game is in the match (its in-game traffic flag, 0x79e2e4); one that comes sooner (this game still loading or on its start screen while the other is already in) is thrown away, and the other game doesn't send it again (it sends only when the prefs changed since it last sent them). So the host lost a player's prefs whenever their game got into the match first. XPFGATE: the packet decoder's "not in the match" jump (je at 0x356b67, was je 0x356eee) comes here: a packet 15 thrown away is kept (XPFKEEP; the game's own copy isn't touched, its players may not be set up yet), and XPFREST takes it at the hand-out | v5.82 · 2026-10-26 |
| 008CD8B3 | 208 bytes | xbreadfail_sp | XPFKEEP(packet 15 data: slot, then 124 bytes of prefs; the game it came from, 0: not checked), LAN: keep a copy of another game's player's prefs under their name; an "Always" that is our own override (XPFON) keeps their own setting | v5.100 · 2026-10-28 |
| 008CD983 | 99 bytes | xbreadfail_sp | ecx = slot (XENTER, LAN host: another game's player entering): their own setting sent once more if it was put back at the last match's end (that message can arrive after their game has left the match, and is thrown away there) and this game's copy of their prefs still says "Always" (their game's report of the change hasn't come); once per put-back; keeps all | v5.100 · 2026-10-28 |
| 008CD9E6 | 111 bytes | xbreadfail_sp | eax = slot (another game's player whose prefs this host doesn't have) -> eax = 1 if a copy kept under their name was taken as if they sent it (player settings reader: this game's copy and its flag), else 0; keeps the others | v5.89 · 2026-10-27 |
| 008CDADC | 16 bytes | xbreadfail_sp | host: 1 = that player's own setting was put back at the last match's end (XPFBACK; XPFENT) | v5.3 · 2026-10-16 (approx.) |
| 008CDAEC | 2688 bytes | xbreadfail_sp | the kept prefs: 16 entries, each the player's name (40 bytes, as network player table +8), then their prefs (124), then the game they came from (4) | v5.3 · 2026-10-16 (approx.) |
| 008CEAC8 | 64 bytes | xbreadfail_sp | per row: the game frame its own setting was last sent back (XPFDONE) | v5.3 · 2026-10-16 (approx.) |
| 008DFF44 | 105 bytes | xbreadfail_sp | eax = player slot of chr esi when it is another game's connected player whose prefs this host has, else -1; keeps the others | v5.81 · 2026-10-26 |
| 008DFFAD | 25 bytes | xbreadfail_sp | eax = slot -> eax = this game's copy of that player's prefs (0 = none); keeps the others | v5.3 · 2026-10-16 |
| 008DFFC6 | 84 bytes | xbreadfail_sp | XPFSEND(slot, setting): send that player's prefs (this game's copy) with that weapon setting to their game only | v5.3 · 2026-10-16 |
| 008E001A | 265 bytes | xbreadfail_sp | XPFON(chr, weapon), LAN host, Gun Game, Random Weapon or Showdown, just before the weapon is dropped at the feet of another game's player: their game to "Always" until they hold it (at most 4 seconds in Gun Game and Showdown; 1 second in Random Weapon, where map weapons stay, so a map gun picked up meanwhile is the only other one they would switch to). Their own setting is saved first (an "Always" seen after we changed it is our own change coming back from their game, so the saved one is kept) | v5.102 · 2026-10-29 |
| 008E0123 | 80 bytes | xbreadfail_sp | ebx = slot: the override is over: their own setting back to their game, if that player is still there | v5.102 · 2026-10-29 |
| 008E0173 | 293 bytes | xbreadfail_sp | every frame (XGGT, Weapon Mode on; LAN host): end the overrides that are done (the player holds the weapon, 4 seconds passed, the game frame went back = a new match, or someone finished the ladder: before the match ends); forget players who left | v5.100 · 2026-10-28 |
| 008E0298 | 15 bytes | xbreadfail_sp | the end of a match (call at 0x679f3 in the end-of-level code every mode's end goes through, was call 0x64890): every "Always" still on goes back now (XPFT only runs while the match is played, so one handed out in the last seconds stayed) | v5.3 · 2026-10-16 (approx.) |
| 008E02A7 | 51 bytes | xbreadfail_sp | every "Always" override still on goes back now (LAN host; a LAN player's table can only hold stale ones); keeps all | v5.100 · 2026-10-28 |
| 008E7604 | 64 bytes | xbreadfail_sp | host: per chr, the gameframe it made another game's player take a hand-out (XGGDROP; XPFT) | v5.3 · 2026-10-16 (approx.) |
| 008E7AE8 | 64 bytes | xbreadfail_sp | Gun Game weapon switch: owner client of each player slot when its setting was saved | v5.3 · 2026-10-16 (approx.) |
| 008E7B28 | 64 bytes | xbreadfail_sp | gameframe the "Always" override ends (0 = none) | v5.3 · 2026-10-16 (approx.) |
| 008E7B68 | 16 bytes | xbreadfail_sp | its half seconds added (the weapon still on the floor), 16 at most | v5.3 · 2026-10-16 (approx.) |
| 008E7B78 | 16 bytes | xbreadfail_sp | that player's own setting + 1 (0 = not known yet) | v5.3 · 2026-10-16 (approx.) |
| 008E7B88 | 16 bytes | xbreadfail_sp | the weapon handed out | v5.3 · 2026-10-16 (approx.) |
| 008E7B98 | 16 bytes | xbreadfail_sp | 1 = they already held it when it was handed out (wait for the time instead) | v5.3 · 2026-10-16 (approx.) |
| 008E7BA8 | 132 bytes | xbreadfail_sp | packet 15: 4-byte header, slot, then the 124 bytes of prefs (0x81 bytes) | v5.3 · 2026-10-16 (approx.) |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013C994 | 0C04E762 | 0C03AE1D | jal 0x139d88 | jal 0xeb874 | Hook: end-of-level code: was jal 0x139D88 (delay slot daddu s0,zero,zero kept): the "Always" overrides go back | v5.15 · 2026-10-16 |
| 004F462C / PAL 004F46D4 | 8DEE3D2C | 0803F285 | lw t6,15660(t7) | j 0xfca14 | Hook: packet decode, not in the match: packet 15 kept (PFGATE) | v5.82 · 2026-10-26 |
| 004F4630 / PAL 004F46D8 | 11C0000C | 8DEE3D2C | beq t6,zero,0x4f4664 | lw t6,15660(t7) | Hook: packet decode, not in the match: packet 15 kept (PFGATE) | v5.82 · 2026-10-26 |
| 004F4910 / PAL 004F49B8 | 0C13F9CE | 0C03F7EC | jal 0x4fe738 | jal 0xfdfb0 | Hook: packet 15 received: keep a copy (PFRCV) | v5.81 · 2026-10-26 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E48EC-000E4ABF | 117 | PFKEEP: a0 = packet 15 data (slot, then 128 bytes of prefs), a1 = the game it came from (0: not checked), LAN: keep a copy of another game's player's prefs under their name; an "Always" that is our own override (PFON) keeps their own setting | v5.89 · 2026-10-27 |
| 000E5004-000E519B | 102 | PFON: a0 = character record, a1 = weapon (GGGIVE / SDGIVE, LAN host, just before the weapon is dropped at the feet of another game's player): their game to "Always" until they hold it (at most 4 s in Gun Game and Showdown, 1 s in | v5.96 · 2026-10-28 |
| 000E519C-000E532F | 101 | PFT: every frame (GGT, Weapon Mode on; LAN host): end the overrides that are done (the player holds the weapon, 4 seconds passed, the game frame went back = a new match, or someone finished the ladder: before the | v5.83 · 2026-10-26 |
| 000E9098-000E9183 | 59 | PFREST: a0 = slot (another game's player whose prefs this host doesn't have): v0 = 1 if a copy kept under their name was taken as if they sent it (player settings reader: this game's copy and its flag), else 0 | v5.89 · 2026-10-27 |
| 000EA0BC-000EA183 | 50 | PFSLOT: a0 = character record -> v0 = its player slot when it is another game's connected player whose prefs this host has, else -1 | v5.81 · 2026-10-26 |
| 000EB524-000EB5CF | 43 | PFENT: a0 = slot (ENTER, LAN host: another game's player entering): their own setting sent once more if it was put back at the last match's end (that message can arrive after their game has left the match, and is thrown away there) and this | v5.83 · 2026-10-26 |
| 000EB874-000EB913 | 40 | PFALL: jal at 0x13C994 in the end-of-level code 0x13C980 that every mode's end goes through (was jal 0x139D88; its delay slot daddu s0,zero,zero kept): every "Always" override still on goes back now (PFT only runs while the match is | v5.99 · 2026-10-28 |
| 000EBB94-000EBC2F | 39 | PFSEND: a0 = slot, a1 = setting: send that player's prefs (this game's copy) with that weapon setting to their game only | v5.3 · 2026-10-16 |
| 000EBC30-000EBCCB | 39 | PFDONE: a0 = slot: the override is over: their own setting back to their game, if that player is still there | v5.99 · 2026-10-28 |
| 000EBFD8-000EC06F | 38 | PFBACK: every "Always" override still on goes back now (LAN host; a LAN player's table can only hold stale ones) | v5.83 · 2026-10-26 |
| 000ED048-000ED0C3 | 31 | PFDUP: leaf (a0 = slot): v0 = 1 if another player in the game (another network player table slot with an owner) has the same name; uses t0-t7 | v5.81 · 2026-10-26 |
| 000ED4A4-000ED51B | 30 | PFKFIND: leaf (a0 = a name, as network player table +8): v0 = the kept entry with that name (0 = none), v1 = the first empty one (0 = none); uses t0-t5 | v5.81 · 2026-10-26 |
| 000EFE7C-000EFEA3 | 10 | PFPREFS: leaf (a0 = slot): v0 = this game's copy of that player's prefs (0 = none); uses t0,t1 | v5.3 · 2026-10-16 |
| 000FC5A8-000FC5FF | 22 | PFHELD: leaf: a0 = character record, a1 = gun id -> v0 = 1 if the gun in its hands (+148) is that gun (by gun type); uses t0-t5 | v5.77 · 2026-10-25 |
| 000FCA14-000FCA3F | 11 | PFGATE: The game takes packet 15 only while its own game is in the match (its in-game traffic flag, 0x6E3D2C); one that comes sooner (this game still loading or on its start screen while the other is already in) is thrown away, and the other game doesn't send it again (it sends only when the prefs changed since it last sent them). So the host lost a player's prefs whenever their game got into the match first. PFGATE: j at 0x4F462C (was lw t6,0x3D2C(t7) / beqz t6,0x4F4664, its delay slot sltiu t7,a1,0x47 kept at 0x4F4634; the load now in the jump's delay slot): a packet 15 thrown away is kept (PFKEEP; the game's own copy isn't touched, its players may not be set up yet), and PFREST takes it at the hand-out | v5.82 · 2026-10-26 |
| 000FCB44-000FCB7F | 15 | PFKIX: leaf (a0 = a PFK entry): v0 = its PFKC byte's address; uses t0, t1 | v5.89 · 2026-10-27 |
| 000FDFB0-000FDFDF | 12 | PFRCV: jal at 0x4F4910 (packet 15 received; was jal player settings reader, its delay slot move a0,s3 kept): player settings reader, then keep a copy (PFKEEP) | v5.82 · 2026-10-26 |

# Team Settings: Team Spawns, Disable Team colours

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00067C8A | 057C8A | 7 | `5e 89 1d 88 d2 82 00` | `e8 91 99 fa ff 5e 90` | At the end of team set-up: clear the team entries of disabled colours (header code 0x11620), then the original store. | v5.3 · 2026-10-16 |
| 0006CC69 | 05CC69 | 5 | `a1 58 d2 82 00` | `e9 7c 46 fa ff` | Spawn point choice: when Team Spawns is Off, add flag 0x2000000 so players use every spawn point instead of their team's (header code 0x112EA). | v5.3 · 2026-10-16 |
| 0006CD61 | 05CD61 | 6 | `3b f0 7c c1 8b fa` | `e9 9a ba 87 00 90` | ---------------- XZ: end of the generic team-spawn loop (jmp at 0x6cd61) \| ---------------- XZ: end of the generic team-spawn loop (jmp at 0x6cd61) | v5.3 · 2026-10-16 |
| 002C1CA5 | 2B1CA5 | 5 | `f7 f9 8d 34 92` | `e8 b6 f6 d4 ff` | Team colour cycling: the "next colour" division goes through 0x11360, which skips disabled colours. | v5.3 · 2026-10-16 |
| 002C1E0A | 2B1E0A | 5 | `f7 fe 5e 89 11` | `e8 62 f5 d4 ff` | Team colour cycling (other direction / bots): goes through 0x11371, which skips disabled colours. | v5.3 · 2026-10-16 |
| 002C711E | 2B711E | 5 | `e8 6d b2 da ff` | `e8 5e b0 61 00` | Friendly Fire item: was call 0x72390 (greyed out with Teamplay Off) \| match settings refresh (call at 0x2c711e, was call 0x72390 for Friendly Fire; cdecl (page, 4)): greyed out while the menu's \| match settings refresh (call at 0x2c711e, was call 0x72390 for Friendly Fire; cdecl (page, 4)): greyed out while the menu's mode has a Teamplay item and Teamplay is Off (the game greyed it by its own Teamplay item, which is not on this page any more) | v5.3 · 2026-10-16 |
| 002EF399 | 2DF399 | 5 | `e8 c2 3d d5 ff` | `e8 6a 22 d2 ff` | Team select screen: build the colour list through 0x11608, leaving out disabled colours. | v5.3 · 2026-10-16 |
| 002EF3A5 | 2DF3A5 | 23 | `8b 4e 48 49 8b c1 3b c5 89 4e 48 7d 0a 0f b6 0d 03 d2 82 00 89 4e 48` | `ff 4e 48 6a ff e8 e1 21 d2 ff e9 08 00 00 00 90 90 90 90 90 90 90 90` | Team select screen, previous colour: step through 0x11590, skipping disabled colours (rest of the old code jumped over). | v5.3 · 2026-10-16 |
| 002EF410 | 2DF410 | 23 | `8b 56 48 42 8b c2 89 56 48 0f b6 15 03 d2 82 00 3b c2 7e 03 89 6e 48` | `ff 46 48 6a 01 e8 76 21 d2 ff e9 08 00 00 00 90 90 90 90 90 90 90 90` | Team select screen, next colour: step through 0x11590, skipping disabled colours. | v5.3 · 2026-10-16 |
| 00356D3A | 346D3A | 5 | `e8 51 5b 00 00` | `e8 c1 aa cb ff` | LAN team-change message: before the game handles it (0x35C890), 0x11800 moves a player who picked a disabled colour on to the next enabled one. | v5.3 · 2026-10-16 |
| 004D6FD0 | 4C75F0 | 1 | `00` | `01` | Mode table, Bag Tag: team spawn points used, so Bag Tag teams start at their own spawn points with Teamplay On and Team Spawns On (the setup no longer always gets flag 0x2000000). Was 0. | v5.39 · 2026-10-19 |
| 004D7010 | 4C7630 | 1 | `00` | `01` | Game mode table, entry with menu text 0x144: field +4 set from 0 to 1 (lets this mode be played with teams). | v5.3 · 2026-10-16 |
| 004D7060 | 4C7680 | 1 | `00` | `01` | Game mode table, entry with menu text 0x141: team flag (+0x14) set from 0 to 1 (lets this mode be played with teams). | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 000113E7 | 250 bytes | XBE header | Pointers and texts: "Advanced Settings", "Team Spawns", "On", "Off", "Disable Red/Blue/Yellow/Green Team", "Teamplay", then the grey-out helper start. | v5.3 · 2026-10-16 |
| 00011500 | 5 bytes | XBE header | Jump to the LAN team-list code at 0x117B0 (disabled colours). | v5.3 · 2026-10-16 (approx.) |
| 00011540 | 68 bytes | XBE header | Grey out a colour item when that colour is disabled (LAN mask from byte 0x82D213 under marker 0xA0). | v5.3 · 2026-10-16 |
| 00011590 | 131 bytes | XBE header | Team select: step to the previous / next enabled colour. | v5.70 · 2026-10-23 |
| 00011620 | 64 bytes | XBE header | Clear the team entries of disabled colours (from 0x67C8A). | v5.3 · 2026-10-16 |
| 000117B0 | 80 bytes | XBE header | Code: _start (see the code shown) | v5.3 · 2026-10-16 |
| 00011800 | 155 bytes | XBE header | Code: XHOOK (see the code shown) | v5.3 · 2026-10-16 |
| 0001189B | 24 bytes | XBE header | direction in edi: -1 if P==T+1 or (T==cnt && P==1) else +1 | v5.3 · 2026-10-16 |
| 000118B3 | 5 bytes | XBE header | Code: back (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 000118B8 | 12 bytes | XBE header | Code: direction check (see the code shown) | v5.3 · 2026-10-16 |
| 000118C4 | 36 bytes | XBE header | Code: lp (see the code shown) | v5.3 · 2026-10-16 |
| 000118E8 | 4 bytes | XBE header | Code: callz (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 000118EC | 10 bytes | XBE header | Code: found (see the code shown) | v5.3 · 2026-10-16 |
| 000118F6 | 76 bytes | XBE header | Code: call (see the code shown) | v5.3 · 2026-10-16 |
| 00011942 | 12 bytes | XBE header | Code: done (see the code shown) | v5.3 · 2026-10-16 |
| 008E2181 | 59 bytes | xbreadfail_sp | match settings refresh (call at 0x2c711e, was call 0x72390 for Friendly Fire; cdecl (page, 4)): greyed out while the menu's mode has a Teamplay item and Teamplay is Off (the game greyed it by its own Teamplay item, which is not on this page any more) | v5.3 · 2026-10-16 |
| 008E6AE0 | 37 bytes | xbreadfail_sp | ---------------- Team icons: the "Disable Red / Blue / Yellow / Green Team", "Red / Blue / Yellow / Green Respawn Delay" and Assault's "Attacker / Defender Respawn Delay" (red / blue) items (Advanced Settings) show the game's own figure icon (icon 22, the male figure of the bot / team display on the match settings page) in the team's colour, with the same shadow that display gives it, just after the text (one space after it), in the middle of the row. Only menu drawing on this game. Front end only: in a level (End of match > New game) the icon isn't there and it drew as a bar of the team's colour. team Respawn Delay items (from XRDI, in place of all.s's item adder 0x8e84b3 (eax label, edx id 0x29 + team, ecx options, ebx count; keeps all registers); esi = team 0-3): the item's draw is XTIC0-3 too | v5.3 · 2026-10-16 |
| 008E6B05 | 10 bytes | xbreadfail_sp | Assault's Attacker / Defender Respawn Delay items (from XRDI; edx id 0x29 / 0x2a): attackers are red, defenders blue | v5.3 · 2026-10-16 |
| 008E6B0F | 13 bytes | xbreadfail_sp | colour items (call at 0x11176 in the builder, was call 0x7a7b0, menu add routine (label, id, flags, height, select, draw); ebx = | v5.3 · 2026-10-16 |
| 008E6B1C | 16 bytes | xbreadfail_sp | colour items (call at 0x11176 in the builder, was call 0x7a7b0, menu add routine (label, id, flags, height, select, draw); ebx = colour 0-3): the item's draw is XTIC0-3 | v5.3 · 2026-10-16 |
| 008E6B2C | 16 bytes | xbreadfail_sp | Data: XTICT | v5.3 · 2026-10-16 (approx.) |
| 008E6B3C | 4 bytes | xbreadfail_sp | Code: XTIC0 (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E6B40 | 7 bytes | xbreadfail_sp | Code: XTIC1 (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E6B47 | 7 bytes | xbreadfail_sp | Code: XTIC2 (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E6B4E | 5 bytes | xbreadfail_sp | item draw (cdecl (menu, item, rect: left, top, right, bottom pixels), eax = colour 0-3): drawn before the item's text; | v5.3 · 2026-10-16 (approx.) |
| 008E6B53 | 385 bytes | xbreadfail_sp | item draw (cdecl (menu, item, rect: left, top, right, bottom pixels), eax = colour 0-3): drawn before the item's text; nothing in a level | v5.18 · 2026-10-17 |
| 008E6CD4 | 4 bytes | xbreadfail_sp | Code: XTHALF (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E6CD8 | 4 bytes | xbreadfail_sp | Code: XT64 (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E6CDC | 4 bytes | xbreadfail_sp | Code: XT3 (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E6CE0 | 4 bytes | xbreadfail_sp | Code: XTONE (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E6CE4 | 4 bytes | xbreadfail_sp | ---------------- Return to Lobby (LAN host, during a match or after it): every console goes back to the lobby, the session kept. | v5.3 · 2026-10-16 (approx.) |
| 008E8800 | 582 bytes | xbreadfail_sp | ---------------- XZ: end of the generic team-spawn loop (jmp at 0x6cd61) | v5.3 · 2026-10-16 |
| 008E8A46 | 61 bytes | xbreadfail_sp | xmm0 = SGN*((Z-MZ)*DX - (X-MX)*DZ) | v5.3 · 2026-10-16 |
| 008E8A83 | 97 bytes | xbreadfail_sp | esi = entry index, edi = spawn set -> eax=1 and X,Z in SCR if usable for this mode | v5.3 · 2026-10-16 |
| 008E8AE4 | 52 bytes | xbreadfail_sp | ---------------- XAU: Assault spawn lists (jmp at 0x6ccb5); Team Spawns Off = attack + defend spawns of the current phase | v5.3 · 2026-10-16 |
| 008E8B18 | 24 bytes | xbreadfail_sp | Code: CP (see the code shown) | v5.3 · 2026-10-16 (approx.) |
| 008E8B30 | 4 bytes | xbreadfail_sp | Data: HALF | v5.3 · 2026-10-16 (approx.) |
| 008E8B40 | 47 bytes | xbreadfail_sp | Team Spawns item: not added in Assault (call at 0x11133) | v5.3 · 2026-10-16 |
| 008E8B6F | 26 bytes | xbreadfail_sp | first selected item: Team Spawns, or Disable Unarmed in Assault (call at 0x111a3, replaces add $4,%esp; push $0x1e) | v5.3 · 2026-10-16 (approx.) |
| 008E8B89 | 26 bytes | xbreadfail_sp | colour count for the Disable [colour] items: 0 in Capture the Bag / Assault (call at 0x1115a) | v5.3 · 2026-10-16 |
| 008E8BA3 | 94 bytes | xbreadfail_sp | match settings page: CTB / Assault set aside the disabled colours, other modes get them back (call at 0x11009, replaces add $4,%esp; mov 0x7945b4,%eax -> call XMSK; add $4,%esp) | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 006284E0 / PAL 006285E0 | 00000000 | 00000001 | nop | .word 0x00000001 | Shrink: team spawns on (Team Spawns option can disable) | v5.3 · 2026-10-16 |
| 0043AD2C | 0C0545D0 | 0C03F9AD | jal 0x151740 | jal 0xfe6b4 | "Advanced Settings" page (first line of match settings) with: Teamplay: On/Off (moved here from match settings) Team Spawns: On/Off (Off = team games spawn like deathmatch) Disable Red/Blue/Yellow/Green Team: Off/On (disabled colours cannot be picked: menus and Select Team screen; on LAN the host's settings apply to everyone) Team options are greyed out when Teamplay is Disabled or the mode has no teams. match settings: "Advanced Settings" link, the first of the big links (just above Weapon Set) | v5.3 · 2026-10-16 |
| 0043B1F8 | 15AE001B | 1000001B | bne t5,t6,0x43b268 | beq zero,zero,0x43b268 | match settings: Teams option moved to Additional Settings (hidden here) | v5.3 · 2026-10-16 |
| 00144884 | 8DAF0050 | 0803F58A | lw t7,80(t5) | j 0xfd628 | spawn picker: Team Spawns disabled -> ignore team spawn points | v5.3 · 2026-10-16 |
| 0042FB80 | 00007010 | 0C03F5BD | mfhi t6,zero,zero | jal 0xfd6f4 | team colours: skip disabled colours (player list colour) | v5.3 · 2026-10-16 |
| 0042FC8C | 00006810 | 0C03F5D6 | mfhi t5,zero,zero | jal 0xfd758 | team colours: skip disabled colours (player list) | v5.3 · 2026-10-16 |
| 0044D3A8 / PAL 0044D408 | 00007810 | 0C03F5EF | mfhi t7,zero,zero | jal 0xfd7bc | team colours: skip disabled colours (match setup) | v5.3 · 2026-10-16 |
| 0044D478 / PAL 0044D4D8 | 00007810 | 0C03F609 | mfhi t7,zero,zero | jal 0xfd824 | team colours: skip disabled colours (match setup, LAN) | v5.3 · 2026-10-16 |
| 0042FE6C | 00007810 | 0C03F623 | mfhi t7,zero,zero | jal 0xfd88c | team colours: skip disabled colours when changing team | v5.3 · 2026-10-16 |
| 00439670 | 8E2F010C | 0C03F63D | lw t7,268(s1) | jal 0xfd8f4 | team colours: skip disabled colours (team select, next) | v5.3 · 2026-10-16 |
| 0043976C | 8E2F010C | 0C03F65B | lw t7,268(s1) | jal 0xfd96c | team colours: skip disabled colours (team select, previous) | v5.3 · 2026-10-16 |
| 0044D1F0 / PAL 0044D240 | 922D0086 | 0C03F680 | lbu t5,134(s1) | jal 0xfda00 | LAN: team list = all teams + host's disabled-colour mask sent to clients | v5.3 · 2026-10-16 |
| 0044D1F4 / PAL 0044D244 | 15AF00E4 | 00000000 | bne t5,t7,0x44d588 | nop | LAN: team list = all teams + host's disabled-colour mask sent to clients | v5.3 · 2026-10-16 |
| 0044D1F8 / PAL 0044D248 | 240E0002 | 10000007 | addiu t6,zero,2 | beq zero,zero,0x44d218 | LAN: team list = all teams + host's disabled-colour mask sent to clients | v5.3 · 2026-10-16 |
| 0044D1FC / PAL 0044D24C | 240F0001 | 00000000 | addiu t7,zero,1 | nop | LAN: team list = all teams + host's disabled-colour mask sent to clients | v5.3 · 2026-10-16 |
| 00471968 / PAL 00471A08 | 1DE00005 | AE2F0048 | bgtz t7,0x471980 | sw t7,72(s1) | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 0047196C / PAL 00471A0C | AE2F0048 | 26210048 | sw t7,72(s1) | addiu at,s1,72 | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00471970 / PAL 00471A10 | 3C0E0063 | 0C03F6B4 | lui t6,0x63 | jal 0xfdad0 | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00471974 / PAL 00471A14 | 25CE8E50 | 2403FFFF | addiu t6,t6,-29104 | addiu v1,zero,-1 | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00471978 / PAL 00471A18 | 91CF0003 | 00000000 | lbu t7,3(t6) | nop | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 0047197C / PAL 00471A1C | AE2F0048 | 00000000 | sw t7,72(s1) | nop | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00471D34 / PAL 00471DD4 | 91AF0003 | 26210048 | lbu t7,3(t5) | addiu at,s1,72 | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00471D38 / PAL 00471DD8 | 01EE782A | 0C03F6B4 | slt t7,t7,t6 | jal 0xfdad0 | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00471D3C / PAL 00471DDC | 11E00002 | 24030001 | beq t7,zero,0x471d48 | addiu v1,zero,1 | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00471D40 / PAL 00471DE0 | 240F0001 | 00000000 | addiu t7,zero,1 | nop | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00471D44 / PAL 00471DE4 | AE2F0048 | 00000000 | sw t7,72(s1) | nop | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 00472384 / PAL 00472424 | 8E240048 | 0C03F6F0 | lw a0,72(s1) | jal 0xfdbc0 | "Select Team" screen: left/right skip disabled colours, and a disabled starting colour moves to the next enabled one (host's settings on LAN) | v5.3 · 2026-10-16 |
| 0047194C / PAL 004719EC | 0C0439FA | 0C03F6FC | jal 0x10e7e8 | jal 0xfdbf0 | "Select Team" screen: check the current colour every frame (before input) | v5.3 · 2026-10-16 |
| 0013EB20 | 3C100063 | 0C03F706 | lui s0,0x63 | jal 0xfdc18 | LAN: hide the host's disabled colours from the Teams/Scores panel | v5.3 · 2026-10-16 |
| 0013EB24 | 260F8E50 | 3C100063 | addiu t7,s0,-29104 | lui s0,0x63 | LAN: hide the host's disabled colours from the Teams/Scores panel | v5.3 · 2026-10-16 |
| 004F4A24 / PAL 004F4ACC | 0C13EA36 | 0C03F900 | jal 0x4fa8d8 | jal 0xfe400 | LAN host: check team picks received from other players (code at 0x000FE400): a disabled colour moves the player on to the next enabled colour in the direction they were scrolling, so on their Select Team screen the disabled colour is skipped | v5.15 · 2026-10-16 |
| 00144CE0 | 1000FF0C | 0803ED80 | beq zero,zero,0x144914 | j 0xfb600 | Zones (and other 4-team modes): on maps without yellow/green spawn points (e.g. Vietnam), Yellow and Green get their own spawn areas on either side of the line between the red and blue spawns (host only on LAN) | v5.3 · 2026-10-16 |
| 0043A334 | 0C054408 | 0C03B8F3 | jal 0x151020 | jal 0xee3cc | Hook: match settings refresh, Friendly Fire: was jal 0x151020 (greyed out with Teamplay Off) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FDAD0-000FDBEB | 71 | "Select Team" helper code at 0x000FDAD0 | v5.70 · 2026-10-23 |
| 000FDBF0-000FDC17 | 10 | "Select Team" screen: check the current colour every frame (before input) | v5.3 · 2026-10-16 |
| 000FDC18-000FDC7B | 25 | LAN: hide the host's disabled colours from the Teams/Scores panel | v5.3 · 2026-10-16 |
| 000FE400-000FE637 | 142 | LAN host: check team picks received from other players (code at 0x000FE400): a disabled colour moves the player on to the next enabled colour in the direction they were scrolling, so on their Select Team screen the disabled colour is skipped | v5.15 · 2026-10-16 |
| 000FB600-000FB8F3 | 189 | Zones (and other 4-team modes): on maps without yellow/green spawn points (e.g. Vietnam), Yellow and Green get their own spawn areas on either side of the line between the red and blue spawns (host only on LAN) | v5.3 · 2026-10-16 |
| 000FB974-000FB9D7 | 25 | Advanced Settings in Assault / Capture the Bag: Team Spawns hidden in Assault; Disable Red/Blue/Yellow/Green Team hidden in both (disabled colours are set aside while one of these modes is picked and come back for other modes) | v5.3 · 2026-10-16 |
| 000E470C-000E48EB | 120 | PTIC: item draw (a0 menu, a1 item, a2 rect: left, top, right, bottom pixels; v1 = colour 0-3): drawn before the item's text; nothing in a level | v5.18 · 2026-10-17 |
| 000EE3CC-000EE42B | 24 | FFI: match settings refresh (jal at 0x43A334, was jal 0x151020 for Friendly Fire, a1 = 4): greyed out while the menu's mode has a Teamplay item and Teamplay is Off (the game greyed it by its own Teamplay item, not on this page now) | v5.3 · 2026-10-16 |
| 000EEF8C-000EEFDB | 20 | PTICR: adds the item, then its draw is PTICS + 8 * team | v5.3 · 2026-10-16 |
| 000F0074-000F0093 | 8 | PTICRS: team Respawn Delay items (jal at 0xFB204 / 0xFB214 / 0xFB238 / 0xFB248, was jal 0xFB100, the item adder (a0 label, a1 id 30-33)): v1 = team, then PTICR | v5.3 · 2026-10-16 |
| 000F0094-000F00B3 | 8 | PTICS: the four item draws: v1 = colour, then PTIC | v5.3 · 2026-10-16 |
| 000F0118-000F012F | 6 | PTICADD: jal at 0xFD284 in the builder's colour loop (was jal 0x14E8F0, menu add routine; s3 = colour 0-3): the item's draw (t0) is PTICS + 8 * colour | v5.3 · 2026-10-16 |
| 000F050C-000F050F | 1 | LTSPC: text | v5.3 · 2026-10-16 (approx.) |

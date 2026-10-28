# Game functions and data

Game routines and data the mod uses, with descriptive names of our own, as found in the Xbox XBE and the PS2 executable. Xbox addresses are in the title update XBE; PS2 addresses are NTSC, with the PAL address where it differs (game data from 0x60CD00 to 0x77D000 is 0x100 higher on PAL; code and the data above are at the same address). Entries marked (hook site) are places the mod writes over.

## Xbox

| Address | Kind | Name | What it is | Used for |
|---|---|---|---|---|
| 0x17520 | function | set state | Game state setter noted in the project notes (named "set-state" there). | Project notes reference (key addresses) |
| 0x1a740 | function | draw filled box | Draws a filled rectangle: floats left, top, right, bottom, then corner colours. | Manage Players page drawing |
| 0x1f000 | function | screen rectangle call | Takes an integer screen rectangle (left, top, right, bottom; cdecl); the mod calls it when drawing Manage Players row boxes. | Manage Players rows |
| 0x3e170 | function | get text by id | Returns a game text string by text id (the leave-confirm question used text 0x1a7e through it). | Return to Lobby confirm question (XRLTXT hook), Manage Players |
| 0x40370 | function | set text size | Sets the text size (the mod starts it from 1 and puts the font back afterwards). | Manage Players option rows (fitting text) |
| 0x403c0 | function | set font | Selects the font used for following text drawing. | Manage Players, Spectate button hints, Team icons, kill message text |
| 0x40f70 | function | text width | Returns the drawn width of a text string (cdecl: text). | Manage Players rows (XMPATW), Team icons text placement |
| 0x413f0 | function | fit text to width | Scales text to a width: (text, width, mode 0 = only smaller, 1 = only across). | Manage Players option rows |
| 0x427e0 | function | draw button hint text | Draws a button hint text line, as the game's own remote gun / camera hints. | Spectate on-screen button hints |
| 0x43110 | function | pad held buttons | Returns a controller's currently held buttons (bit 0x800 = right trigger held). | Spectate free cam speed-up (right trigger) |
| 0x43160 | function | pad new presses | Returns a controller's newly pressed buttons this frame (bit 0x80 = A). | Spectate controls; LAN host auto second A on Select Team (XHBTN hook at 0x2ef7d5) |
| 0x432d0 | function | stick with dead zone | Called with the 0.25 dead zone the game's own look uses; the mod uses it when reading the sticks for the spectate camera. | Spectate camera look |
| 0x43320 | function | read stick axis | Reads a stick axis for a player: (player number, axis), from the player's own control slot so southpaw layouts work. | Spectate camera turning |
| 0x436c0 | function | button name | Returns the display name of a controller button. | Spectate on-screen button hints |
| 0x45d40 | function | sound parms init | Initialises a 48-byte sound parameter buffer (cdecl: buf); the sound id goes at +0. | Overtime "Text Sweep" sound, Setbacks laugh, multikill sound, King of the Hill sounds |
| 0x46041 | function | sound loader decision (hook site) | Point in the level sound loader that decides whether a sound is loaded; the mod forces the multikill jingle (3455) and Setbacks laugh (5659) to load (XSNDLD). | Multikill, Setbacks |
| 0x461d0 | function | play sound | Plays a sound from a filled 48-byte sound parameter buffer (cdecl: buf). | Overtime, Setbacks, multikill, King of the Hill sounds |
| 0x62f48 | function | level pak name suffix (hook site) | Builds the level pak file suffix from the game type (test-only story-level hook XSTPAK). | Story-level LAN test build only |
| 0x62fdb | function | level pak folder (hook site) | Picks pak/arcade or pak/story by game type 10 (test-only hook XSTPAK). | Story-level LAN test build only |
| 0x64890 | function | save end-of-match scores | End-of-level step that saves the match's end scores (called from the end-of-level code at 0x679f3). | Weapon switch "Always" overrides restored at match end (XPFALL), Team Lives ranking (XTLSV) |
| 0x64aa0 | function | kill count routine | Counts a chr's kills for its score. | Showdown score on LAN players (XSDCL) |
| 0x64afc | function | kill count routine score (hook site) | Point in the score code where a chr's score is set (esi = chr); the mod sets Gun Game score = weapon level, Showdown score = kills. | Gun Game, Showdown, Team VIP, Multikill (mk.s) |
| 0x64b80 | function | add team score | Adds points to a team's score (cdecl: team at 4(%esp), points in ecx). | Catch-Up (doubles points for last team, XCUTA hook), Team VIP points |
| 0x64b87 | function | add team score (resume) | Resume point inside add team score after the Catch-Up hook. | Catch-Up |
| 0x64e40 | function | add points | Adds points to a chr (cdecl: chr, points). | Catch-Up (XCUSC hook), Coin Rush / Coin Drop scoring |
| 0x64e45 | function | add points (resume) | Resume point inside add points after the Catch-Up hook. | Catch-Up |
| 0x64eb0 | function | add kills | Counts a kill: [esp+4] = killer, [esp+8] = victim id. | Gun Game level-up on kill (XGGK hook), Setbacks, Showdown |
| 0x64eb6 | function | add kills (resume) | Resume point inside add kills after the Gun Game hook. | Gun Game |
| 0x64ecc | function | add kills Gladiator check (hook site) | Gladiator branch in add kills (eax = killer prop) where the mod scores killing the VIP. | Team VIP (XVK) |
| 0x64ed8 | function | add kills Gladiator check (resume) | Return point after the Team VIP kill check. | Team VIP |
| 0x64f85 | function | death lives (hook site) | Where a death takes one off the victim's lives (was mov 0x82d274,%eax; edx = victim chr). | Team Lives (XTLDEC) |
| 0x64fb4 | function | after kill counted (hook site) | Point in add kills after the kill is counted (esi = killer or 0, edx = victim chr), before the multikill code. | Infect On Kill (XINFK), Multikill (mk.s) |
| 0x64fbd | function | kill team points (hook site) | Where kills add team points (was mov 0x82d274,%eax). | Showdown team kills (XSDNL) |
| 0x651f0 | function | rank players | Ranks players / teams by score (cdecl, one argument; the mod calls it with 0 for one more ranking pass). | Team Lives end ranking, Team VIP timer, Zones end scoring (ze.s), kill messages |
| 0x65264 | function | ranking team step (hook site) | Ranking step that chooses team score vs own score (was testb $1,0x82d258). | Team Elimination / Team Vampire (XTLRK) |
| 0x652a3 | function | ranking lives check (hook site) | Ranking reads the match lives (was mov 0x82d274,%eax; esi = chr). | Showdown ranks by kills (XSDRK) |
| 0x652c8 | function | ranking survival time (hook site) | Ranking reads survival time and score (+0xa6c, +0xa64) in Elimination / Vampire. | Team Elimination / Team Vampire team time (XTLAGE) |
| 0x652e3 | function | ranking sets lives left | Ranking code that sets a chr's lives left (+0xa70), which the host score sync uses. | Showdown (noted so lives left stay set) |
| 0x652e9 | function | ranking mode step (hook site) | Ranking reads the mode (was movzbl 0x82d256) to take 3*FPS off rank scores in Elimination / Vampire. | Showdown (XSDRM) |
| 0x65850 | function | weapon allowed check | Checks if a gun can be picked for a menu mode (cdecl: menu mode, gun id); used by the weapon picker and custom weapon set list. | Gun Game / Showdown weapon bans (XGGBAN, XSDDRW) |
| 0x65a20 | function | time text | Formats a time as text (e.g. "148.5 secs"). | Score page Bag Tag team time fix (XBTSC) |
| 0x65fc0 | function | zones tick (hook site) | Per-frame zones tick (was cmpl $5,GSTATE). | King of the Hill (XKHT) |
| 0x65fdd | function | zones tick interval (hook site) | Point in the zones tick where the interval is used (ecx = interval). | Zone Interval (zi.s) |
| 0x66007 | function | zone scoring (hook site) | Zone scoring: picks the zone holder (esi = zone index). | King of the Hill (koth.s) |
| 0x66014 | function | zone scoring points push | Where zone scoring pushes the points (ecx). | King of the Hill |
| 0x66300 | function | copy setup to match | Copies the received setup into the next match's parameters (0x82d140). | Project notes: setup data path |
| 0x679f3 | function | end-of-level code (hook site) | End-of-level code every mode's end goes through (call to save end scores). | Weapon switch overrides restored (XPFALL) |
| 0x67e80 | function | level done | Ends the level / match (called with 1). | Gun Game / Showdown end of match |
| 0x683fa | function | lives match end (hook site) | Lives end check (ebp = players with lives left). | Showdown with Teamplay ends with one team left (XSDEND) |
| 0x68468 | function | lives match end (continue) | Code reached when more than one player still has lives (the old jg target). | Showdown |
| 0x6884a | function | Bag Tag scoring (hook site) | Bag Tag time scoring step. | Team Bag Tag (bt.s) |
| 0x68b37 | function | burning time scoring (hook site) | Scoring point used so every burning chr loses time. | Flame Tag scoring (all.s) |
| 0x68c2f | function | match frame tick (hook site) | Per-frame call in the match tick (replaced call 0x651f0). | Team VIP timer, Gun Game frame tick |
| 0x68dbc | function | time limit check (hook site) | Time limit check (eax = time left). | Capture the Bag Overtime (XOTH) |
| 0x68dc4 | function | time up | The game's time-up path. | Capture the Bag Overtime |
| 0x68e27 | function | time up scoring (hook site) | Host / offline time-up path. | Zones last score at time up (XZENC / ze.s) |
| 0x68e6c | function | time not up | Code reached while time is not up. | Capture the Bag Overtime |
| 0x68f5a | function | special flag check call site | Call site of 0x232ae0 that only runs for special game flags (0x40 / 0x8000000); the Mercy Rule check was moved off it. | Mercy Rule (old hook restored) |
| 0x68f7c | function | mode tick call site 1 (hook site) | One of the 7 calls to the mode tick 0x239360 in the per-mode ticks; the mod points it at the Mercy Rule check (XCHK), which then jumps on to 0x239360. | Mercy Rule |
| 0x68f92 | function | mode tick call site 2 (hook site) | One of the 7 calls to the mode tick 0x239360 in the per-mode ticks; the mod points it at the Mercy Rule check (XCHK), which then jumps on to 0x239360. | Mercy Rule |
| 0x68fa8 | function | mode tick call site 3 (hook site) | One of the 7 calls to the mode tick 0x239360 in the per-mode ticks; the mod points it at the Mercy Rule check (XCHK), which then jumps on to 0x239360. | Mercy Rule |
| 0x68fbe | function | mode tick call site 4 (hook site) | One of the 7 calls to the mode tick 0x239360 in the per-mode ticks; the mod points it at the Mercy Rule check (XCHK), which then jumps on to 0x239360. | Mercy Rule |
| 0x68fd4 | function | mode tick call site 5 (hook site) | One of the 7 calls to the mode tick 0x239360 in the per-mode ticks; the mod points it at the Mercy Rule check (XCHK), which then jumps on to 0x239360. | Mercy Rule |
| 0x68fe5 | function | Flame Tag tick (hook site) | Point before the Flame Tag tick (offline). | Flame Tag (all.s) |
| 0x68fea | function | mode tick call site 6 (hook site) | One of the 7 calls to the mode tick 0x239360 in the per-mode ticks; the mod points it at the Mercy Rule check (XCHK), which then jumps on to 0x239360. | Mercy Rule |
| 0x69000 | function | mode tick call site 7 (hook site) | One of the 7 calls to the mode tick 0x239360 in the per-mode ticks; the mod points it at the Mercy Rule check (XCHK), which then jumps on to 0x239360. | Mercy Rule |
| 0x69402 | function | start-of-level wait (hook site) | Start wait that calls the "everyone ready" check. | Gun Game / Showdown map gun removal (XGGRDY), armoury moves |
| 0x69920 | function | set in-game flag | Sets the in-game flag 0x79e2e4 right before a client's first spawn point request. | Project notes (Gun Game resends) |
| 0x6b200 | function | level setup by map | Returns the level setup for a map (cdecl: map). | Assault map list, LAN mode list |
| 0x6b2a0 | function | level setup | Returns a level's setup (its pads at +0x24 / +0x28; number +4, flags +8). | Switch Spawns, Coin Rush |
| 0x6bb50 | function | mode allows pad | Checks whether a spawn pad is usable in the mode (as spawn point picker checks). | Spawn Rule, Switch Spawns, zs.s team spawns |
| 0x6c780 | function | give gun | Gives a gun to a chr. | Gun Game / Player Drops Gun hand-outs |
| 0x6c960 | function | pickup subtype | Weapon of a map pickup's weapon-set slot (type, slot); -1 = not made. | Showdown empty weapon slots (XNWPST), disc-version new match |
| 0x6cc7e | function | spawn point picker team flag (hook site) | Spawn pick reads the chr's team (was mov 0x84(%ecx),%ecx); the pad flag bit team+1 is required. | Capture the Bag Switch Spawns (XSWTM) |
| 0x6ccb5 | function | Assault spawn lists (hook site) | Assault spawn list building in the spawn pick. | Team Spawns Off in Assault (zs.s XAU) |
| 0x6ccba | function | Assault spawn lists (resume) | Resume point after the Assault spawn hook. | zs.s XAU |
| 0x6cd61 | function | team spawn loop end (hook site) | End of the generic team-spawn loop. | zs.s XZ |
| 0x6cd67 | function | team spawn loop end (resume) | Resume point after the team-spawn hooks. | zs.s |
| 0x6cdc5 | function | spawn point picker random pick (hook site) | Spawn pick's call to rand (ebp = number of candidates). | Spawn Rule (XSRN), King of the Hill spawns |
| 0x6e48b | function | level pickups builder | Level pickup building code (checked before patching the call at 0x6e491). | Showdown slot-1-only pickups |
| 0x6e491 | function | level pickups subtype call (hook site) | Level pickups call pickup subtype (type, slot 0-5). | Showdown / Gun Game empty weapon set (XNWPST) |
| 0x72150 | function | menu get text | Returns a menu text as drawn (text, option flags, 0), upper case applied. | Manage Players, Team icons |
| 0x72220 | function | add menu option | Adds an option to the current menu item. | Every Advanced Settings item |
| 0x72250 | function | add menu option text | Adds an option with a text pointer to a menu item (used for team names and "Kick"). | Manage Players rows |
| 0x72390 | function | get menu item by id | Returns a menu item by id (cdecl: page, id). | Advanced Settings, match settings greying (Score Limit, Always Start With Gun, One Shot Kill, Score Method, Friendly Fire) |
| 0x72560 | function | menu heading | Adds a page heading (part of the "Manage Players" heading build). | Manage Players page |
| 0x72630 | function | menu text margins | Sets menu text margins (left, right). | Advanced Settings layout, Manage Players |
| 0x726a0 | function | menu item flags | Sets item flags for following items. | Advanced Settings layout, Manage Players |
| 0x761f0 | function | menu option shown | Sets / gets the option an item shows. | Manage Players rows |
| 0x765c0 | function | menu page box | Builds the page box (part of the Manage Players heading build). | Manage Players page |
| 0x769b0 | function | option text colour | Option text colour (cdecl: menu, item, &colour, ...). | Manage Players waiting move greyed (XMPTCOL hook at 0x7c092) |
| 0x78aa0 | function | menu start scroll | Starts a scrolling list (float height, int items). | Advanced Settings one-page list, Manage Players |
| 0x78bf0 | function | menu end scroll | Ends a scrolling list. | Advanced Settings, Manage Players |
| 0x78f90 | function | menu gap | Adds the game's gap below a heading. | Manage Players page |
| 0x7a160 | function | menu divider | Adds a divider / break (cdecl: index). | Advanced Settings link above Weapon Set (XADVL), layouts |
| 0x7a5c0 | function | open menu page | Opens a menu page (ctx 0x794d84[[0x8097e0]], page). | Return to Lobby confirm page, Manage Players |
| 0x7a650 | function | close menu page | Closes the current menu page. | Manage Players back / after a kick |
| 0x7a7b0 | function | add menu text item | Adds a text item (label, id, flags, height, select, draw). | Every Advanced Settings item, weapon set page (XSDSLOT) |
| 0x7b1f0 | function | menu back a page | Goes back a page (item at 4(%esp)). | Return to Lobby confirm No |
| 0x7c070 | function | option text draw | Draws an option's text (cdecl: option, x, y, 0; eax its menu). | Manage Players centred row text (XMPTXT) |
| 0x7c092 | function | option text colour call (hook site) | Call to option text colour inside the option text draw. | Manage Players (XMPTCOL) |
| 0x7c200 | function | option arrows draw | Draws an option's arrows (esi = item), placed from the option's end (+0xdc) and text width. | Manage Players rows |
| 0x7c2e7 | function | option arrows end (hook site) | Arrow draw reads the option end (movss 0xdc(%esi)). | Manage Players (XMPADC) |
| 0x7c36a | function | option arrows text width (hook site) | Arrow draw's call to text width. | Manage Players (XMPATW) |
| 0x7c4c3 | function | option text draw call (hook site) | Call to the option text draw. | Manage Players (XMPTXT) |
| 0x826d0 | function | icon height | Returns an icon's height. | Team icons |
| 0x826f0 | function | draw icon | Draws an icon (x, y, icon, colour). | Team icons |
| 0x89360 | function | collision move | Moves along a way from a point with collision (used for the spectate camera move). | Spectate camera |
| 0x89720 | function | line of sight in room | Checks a way from the eyes within a room (pushes room 0x2a0(chr)). | Spectate camera |
| 0x9aea0 | function | pad number from ref | Returns a pad number from a spawn pad reference. | Spawn Rule, King of the Hill, zs.s |
| 0x9af00 | function | pad pointer | Pad lookup by number; returns NULL for a bad pad (-1 = no pad). Clobbers ecx/edx. | Gun Game drops, armouries, King of the Hill, kill messages |
| 0x9c7d0 | function | closest pad | Closest pad to a position (pos, min distance) -> pad. | Gun Game hand-out drops, Player Drops Gun |
| 0x9d720 | function | pad index | Returns a pad's index / number. | Spawn Rule, Switch Spawns, Coin Rush, zs.s |
| 0xa7a70 | function | model lookup (crash with -1) | Called from 0xdbda0; with -1 (a gun with no model) it likely crashes every console. | Project notes (hidden weapons) |
| 0xa9b50 | function | free prop | Frees a prop, as the game's own collect frees a taken pickup (cdecl: prop). | Gun Game hand-outs (XGGDROP, XGGT) |
| 0xbaff1 | function | One Shot Kill check (hook site) | Damage code's One Shot Kill test (was testb $4,0x82d258; esi = damage info). | Showdown one-hit kills (XSDOS) |
| 0xbb092 | function | hit slowdown (hook site) | Hit slowdown call; the mod's hook spares burning characters offline in Flame Tag. | Flame Tag (offline only) |
| 0xbb830 | function | kill chr | Kills a chr (the mod recognises its return address to tell another chr's kill). | Setbacks |
| 0xbbb4e | function | Thief death coin (hook site) | Kill code's call that spawns the victim's Thief coin. | Coin Rush / Coin Drop (XCDK) |
| 0xbc1a0 | function | damage routine | The game's damage routine (cdecl: [esp+4] = the hit). | Player Health (XPHDA hook) |
| 0xbc1a5 | function | damage routine (resume) | Resume point after the Player Health hook. | Player Health |
| 0xbc1fa | function | damage hit report (hook site) | Damage routine's call that sends a hit this game decides. | Player Health (XPHNH) |
| 0xbed60 | function | host drop pad choice | The host's drop pad choice, which skips marked pads. | Gun Game drops on pads |
| 0xbf9e0 | function | show pickup | Makes a pickup come back (respawn). | Gun Game / Showdown map pickups never return (XGGVIS) |
| 0xbf9e8 | function | show pickup (resume) | Resume point after the show pickup hook. | Gun Game |
| 0xbfe40 | function | pickup taken | Marks a pickup prop as taken. | Gun Game hand-outs, start of match |
| 0xc0b00 | function | bag touched, no bag (hook site) | Bag touched by a chr with no bag (al = mode). | Wrong Way Bag (ia.s A) |
| 0xc0b0f | function | bag pick up | Picks up the touched bag. | Wrong Way Bag |
| 0xc0d2c | function | own bag touched | Own team's bag touched: return a dropped bag / nothing. | Wrong Way Bag |
| 0xc0d34 | function | bag return path (hook site) | Bag return path: same team returns a dropped bag, else nothing. | Wrong Way Bag (ia_ww1.s B) |
| 0xc0d43 | function | return dropped bag | Returns a dropped bag to its base. | Wrong Way Bag |
| 0xc0de1 | function | bag touch: nothing | Bag touch path that does nothing. | Wrong Way Bag |
| 0xc14c8 | function | bag capture check (hook site) | Capture: base must be the chr's own; own bag carried returns it, else score. | Wrong Way Bag (ia.s D) |
| 0xc14e5 | function | bag capture score | Scores a bag capture (every console handles it). | Wrong Way Bag, Bag Must Be Home |
| 0xc1562 | function | capture message loop (hook site) | Capture message loop (replaced cmp 0x1c(%ebp),%ecx / jne 0xc15c8). | Wrong Way Bag |
| 0xc1567 | function | capture message loop (resume) | Resume point in the capture message loop. | Wrong Way Bag |
| 0xc15c8 | function | capture message loop next | Next step of the capture message loop. | Wrong Way Bag |
| 0xc1677 | function | return carried own bag | Own team's carried bag at own base: just return it. | Wrong Way Bag |
| 0xc1684 | function | capture: wrong base | Capture path when the base is not the chr's own: nothing. | Wrong Way Bag |
| 0xc1c80 | function | capture code | Bag / zone capture code (project notes, Zones). | Project notes reference |
| 0xc1d44 | function | base touched carrying bag (hook site) | Base touched while carrying a bag: own base goes to the capture check, else nothing. | Wrong Way Bag (ia.s C) |
| 0xc1d53 | function | capture check | Capture check after touching a base with a bag. | Wrong Way Bag |
| 0xc1d66 | function | capture check past home test | Point in the capture check after the "your bag must be home" test. | Wrong Way Bag, Bag Must Be Home |
| 0xc1e31 | function | base touch: nothing | Base touch path that does nothing. | Wrong Way Bag |
| 0xc1e40 | function | chr picks up pickup | A chr picks up a pickup, the game's own path as when walking over it (cdecl: pickup, chr prop). | Gun Game hand-outs (XGGDROP), Player Drops Gun |
| 0xc2040 | function | collect pickup | The game's own collect, which frees a taken pickup. | Referenced as the model for FREEPROP use (Gun Game) |
| 0xc2b70 | function | prop placing routine | Puts / drops a prop at a place (cdecl: prop, chr, chr gun); online sends message 0x16, flight 10 frames. | Gun Game drops on pads, King of the Hill zone gathering, armouries |
| 0xc36f3 | function | crash point on bad pad | Where a NULL pad from the pad lookup crashes (project notes). | Project notes (zone drops) |
| 0xcc7d0 | function | set view camera | Sets a view's camera (view, mode e.g. 1 = death view, prop). | Spectate |
| 0xcda98 | function | first-person camera (hook site) | First-person camera code (esi = view, edi = its player). | Spectate (XSPFP) |
| 0xcec6c | function | first-person camera (continue) | Rest of the game's camera code after the spectate camera placement. | Spectate |
| 0xcfb40 | function | start pad | Places a player at a spawn point already chosen ([esp+4] = player). | Capture the Bag Switch Spawns (XSWSP) |
| 0xcfb88 | function | start pad net check (hook site) | Start pad's network check (was call 0x354810; esi = player). | Spawn Rule (XSRP) |
| 0xd17c0 | function | death spawn pick | The game's death spawn pick, which sends the pick to the player's console. | Spawn Rule re-pick (LAN host), start of match |
| 0xd183d | function | host spawn pick (hook site) | The host picks every player's spawn pad and sends packet 0x40. | Switch Spawns (XSWSP) |
| 0xd5a59 | function | place own player (hook site) | A console placing its own player at its spawn point. | Switch Spawns (XSWSP) |
| 0xd5be1 | function | respawn (hook site) | Respawn code (esi = player). | Gun Game weapon on respawn (XGGPR) |
| 0xd6441 | function | at death (hook site) | Call at a player's death (eax = player). | Respawn Delay (XRDT) |
| 0xd64aa | function | pad tick gate (hook site) | Respawn pad tick gate. | Respawn delay (all.s) |
| 0xdb64b | function | death drop (hook site) | Death drop call to prop placing routine. | Player Drops Gun / Gun Game (XGGPD) |
| 0xdb696 | function | death drop 2 (hook site) | Second death drop call to prop placing routine. | Player Drops Gun / Gun Game (XGGPD) |
| 0xdbda0 | function | model-less gun drop crash path | Pickup / drop code that calls 0xa7a70 with -1 for a gun with no model. | Project notes (hidden weapons) |
| 0x10f150 | function | emitter on | Turns one flame emitter on. | Project notes (zone flames) |
| 0x10f160 | function | emitter off | Turns one flame emitter off. | Project notes (zone flames) |
| 0x10f660 | function | all emitters on | Turns every flame emitter of a prop on. | Project notes (zone flames) |
| 0x10f690 | function | all emitters off | Turns every flame (particle emitter) of a prop off. | King of the Hill zone glow, kill messages |
| 0x125d30 | function | set-on-fire routine | Sets a chr alight (cdecl: [esp+4] = burn info whose +0 is the chr data). | Infection: no spreading by touch (ia.s) |
| 0x125d36 | function | set-on-fire routine (resume) | Resume point in set-on-fire routine after the hook. | Infection |
| 0x125e2b | function | burn bot flamer state (hook site) | In a burn function: skip to bot flamer state. | Infection: bots keep using guns |
| 0x12611d | function | burn bot flamer state 2 (hook site) | In the second burn function: skip to bot flamer state. | Infection: bots keep using guns |
| 0x12ddc0 | function | HUD message | Shows a HUD message (local number, type 4 = centre, msg, 0). | Overtime, Setbacks "Humiliation!", King of the Hill, Multikill messages |
| 0x12e120 | function | HUD kill message entry | Adds a kill message style HUD entry: the text, then a name in its team colour. | Spectate "Spectating <name>" |
| 0x12e1c7 | function | kill message made (hook site) | Where a kill message entry stores the chr id (+0x168). | Kill messages keep the victim's colour (XKMC) |
| 0x12e277 | function | kill message made 2 (hook site) | The other kill message adder. | Kill messages (XKMC) |
| 0x134982 | function | radar zone blips (hook site) | Radar reads the zone count NDROPS. | King of the Hill (XKHCNT) |
| 0x134a0d | function | radar zone blips loop end (hook site) | Radar zone loop end reading NDROPS. | King of the Hill (XKHCNT) |
| 0x136090 | function | remote camera button hints | The game's remote gun / camera button hints drawing (font, place, colours). | Spectate hints (model) |
| 0x13cfd0 | function | name tags draw | Draws name tags every frame per local player and decides who is in sight. | Spectate name tags (XHATW) |
| 0x13cffa | function | name tags Teamplay check | The name tags' Teamplay check (restored to the game's own). | Spectate (crash fix) |
| 0x13d05f | function | name tags own-chr test (hook site) | Name tags own-chr test. | Spectate (XHAT) |
| 0x13d073 | function | name tags draw (continue) | Name tags draw for everyone else. | Spectate |
| 0x13dad7 | function | name tags loop next | The name tag loop's next chr. | Spectate |
| 0x13f730 | function | zone bar (hook site) | Zone score bar reads NDROPS. | King of the Hill (XKHCNT) |
| 0x13f954 | function | zone bar width (hook site) | Zone bar width (was cvtsi2ss 0x77f47c,%xmm3). | King of the Hill (XKHCV3) |
| 0x13fa1e | function | zone bar loop start (hook site) | Zone bar loop start reading NDROPS. | King of the Hill (XKHCNT) |
| 0x13fb37 | function | zone bar loop end (hook site) | Zone bar loop end (was mov 0x77f47c,%ecx). | King of the Hill (XKHCNTC) |
| 0x14a5a0 | function | kill message draw | Draws kill messages, colouring the name from the chr's team every frame. | Kill messages keep the victim's colour |
| 0x14a823 | function | kill message team read (hook site) | Kill message draw reads the chr's team (mov 0x84(%ebx)). | Kill messages (XKMD) |
| 0x14aba5 | function | match info team read (hook site) | Match info panel reads the team. | Kill messages (XKMD) |
| 0x14b6f0 | function | HUD message draw | The game's HUD message draw. | Spectate HUD |
| 0x14fc87 | function | HUD draw (hook site) | The HUD (ebx = player's HUD). | Spectate (XSPHUD) |
| 0x14fc90 | function | HUD draw (resume) | Resume point in the HUD draw. | Spectate |
| 0x15075f | function | HUD draw skip | HUD code jumped to for state 0xb. | Spectate |
| 0x15095f | function | name tags draw call (hook site) | Per-frame call of the name tags draw. | Spectate (XHATW) |
| 0x1545b0 | function | rand | Random number. Clobbers ecx/edx. | Spawn Rule, Random Weapon, Coin Rush, Random Characters, King of the Hill |
| 0x19ee10 | function | map-send reset | The map-send screen sender's reset. | MapMaker maps on LAN (XMMPREP) |
| 0x19f940 | function | Players row draw | The game's Players page row draw (menu, item, rect). | Manage Players rows (model) |
| 0x1a1b30 | function | match list | Match list with its cable / Live checks. | LAN menu flow |
| 0x1a3c00 | function | Xbox Live option add (patched out) | Call that adds the "Xbox Live" option; the mod nops it. | Xbox Live option hidden |
| 0x1aac94 | function | map-send screen start (hook site) | Start of the map-send screen. | MapMaker maps on LAN (XMMPREP) |
| 0x1baee0 | function | switch gun | Switches a chr to a gun (chr, gun id). | Gun Game hand-outs |
| 0x1bb243 | function | gun switch flag check | Where players are kept from switching to flag-0x2 gun ids (hidden weapons). | Project notes (hidden weapons not usable) |
| 0x1c09b0 | function | take gun | Takes a gun away from a chr (chr, gun id). | Gun Game level change |
| 0x1cce90 | function | add menu choice | Adds a choice on the Xbox Live / System Link page (its "Xbox Live" call is nopped). | Xbox Live option hidden |
| 0x1cea30 | function | unlock check | Character unlock check (Random Characters does not use it). | Project notes (Random Characters) |
| 0x1ceb90 | function | local player count | Returns the number of local players. | Manage Players layout, Overtime / King of the Hill messages to every local player |
| 0x228580 | function | complete objective | Completes an Assault objective (objective, 0.0). | Auto-Complete Phase (Assault) |
| 0x2299d4 | function | Assault tick call (hook site) | Objectives update's call to the Assault tick. | Auto-Complete Phase / Time Bonus After Phase (XASK) |
| 0x232ae0 | function | special match flags check | Check that only runs for special game flags (0x40 Arcade League / 0x8000000 Challenges); the Mercy Rule hook was moved off it. | Mercy Rule (hook restored) |
| 0x2331c0 | function | current Assault phase | Returns the current Assault phase (the first one not complete). | Auto-Complete Phase, Time Bonus After Phase |
| 0x233330 | function | Assault tick | The Assault mode's tick. | Auto-Complete Phase / Time Bonus After Phase (XASK), custom-match gate thunks |
| 0x234453 | function | Assault spawn re-pick return | Return address of Assault's re-pick of spawn points (the mod checks it on the stack). | Start of match spawn resends (LAN host) |
| 0x239360 | function | mode tick | Called from every mode's tick (7 calls); the Mercy Rule check now ends in a jump to it. | Mercy Rule (XCHK) |
| 0x24265b | function | MapMaker gun item build (hook site) | Level builder reads a MapMaker gun item's "always available" flag. | MapMaker maps on LAN: no factories (XMMGUN) |
| 0x24a520 | function | vehicle setup | Vehicle setup with three vehicle types by model. | Project notes (MapMaker research) |
| 0x2754e0 | function | bag is home | Returns 1 if the chr's team bag is at home. | Wrong Way Bag, Bag Must Be Home |
| 0x2b3330 | function | spawn pickup prop at pad | Spawns a pickup prop at a pad (prop, pad). | Coin Rush / Coin Drop (death coin arriving, mid-match joiner coins) |
| 0x2b3440 | function | spawn death pickup | Spawns a pickup from a victim prop (the Thief death coin). | Coin Rush / Coin Drop (XCDK) |
| 0x2b5ddd | function | bot respawn send (hook site) | Arcade bot respawn send call ([esp+4] = chr). | Gun Game bot weapons (XGGBR) |
| 0x2b60f6 | function | AI mode-5 check | AI check hard-wired to mode 5 (Flame Tag / Virus). | Project notes (Virus AI) |
| 0x2b63cb | function | first infected pick | Match-start pick of the first infected player (do not bypass). | Project notes (Virus) |
| 0x2b6c38 | function | AI mode-5 check 2 | AI check hard-wired to mode 5. | Project notes (Virus AI) |
| 0x2b7770 | function | remove pickup prop | Removes a pickup prop for a collect message (chr id, pad). | Coin Rush collect message (XCRNR) |
| 0x2b8c8e | function | AI mode-5 check 3 | AI check hard-wired to mode 5. | Project notes (Virus AI) |
| 0x2bfb90 | function | character allowed check | Character check (character type dword); returns 0 for banned characters with Ban Small Characters, and for monkeys in Monkey Assistant. | Random Characters rerolls banned picks |
| 0x2c0c7d | function | weapon picker check (hook site) | Weapon picker's call to the weapon allowed check. | Gun Game / Showdown weapon bans (XGGBAN) |
| 0x2c7020 | function | match settings set-options | Match settings set-options, run every frame from its tick 0x2c7540. | Match settings greying hooks |
| 0x2c70d3 | function | match settings refresh: Always Start With Gun (hook site) | Refresh call for item 1. | Gun Game / Random Weapon (XGGSGI) |
| 0x2c711e | function | match settings refresh: Friendly Fire (hook site) | Refresh call for item 4. | Friendly Fire greyed with Teamplay Off (XFFI) |
| 0x2c7168 | function | match settings refresh: Score Limit (hook site) | Refresh call for item 7. | Gun Game (XGGSLI) |
| 0x2c7186 | function | match settings refresh: Score Method (hook site) | Refresh call for item 8. | Gun Game / Showdown (XGGSMI) |
| 0x2c719e | function | match settings refresh: One Shot Kill (hook site) | Refresh call for item 9. | Showdown (XSDOSI) |
| 0x2c7540 | function | match settings tick | Tick that runs the match settings set-options every frame. | Project notes (menus) |
| 0x2c7f6f | function | divider before Weapon Set (hook site) | Match settings page divider before Weapon Set. | Advanced Settings link (XADVL) |
| 0x2c9f53 | function | LAN lobby mode list check | Mode list check code in the LAN lobby (context 13), verified before patching. | Mode list: Assault only with an Assault map |
| 0x2c9f56 | function | LAN lobby mode check je | The je for context 13 that the base XBE nops. | Mode list |
| 0x2c9f58 | function | mode list context check (hook site) | Mode list context check (eax = context, edi = mode). | Mode list (XMODA) |
| 0x2c9f61 | function | mode list LAN checks | The game's own LAN mode checks. | Mode list (XMODA) |
| 0x2c9fde | function | LAN mode whitelist (hook site) | LAN mode whitelist check; the mod allows modes 6 or 11. | LAN whitelist (all.s) |
| 0x2ca01c | function | mode list not LAN | Mode list path for non-LAN contexts. | Mode list (XMODA) |
| 0x2ca152 | function | mode not listed | Mode list path that leaves the mode out. | Mode list: Assault |
| 0x2ca157 | function | mode list next | Mode list return point used by the LAN whitelist code. | LAN whitelist (all.s, ls.s) |
| 0x2ca300 | function | map pick callback | The map pick callback. | Project notes (levels) |
| 0x2ca321 | function | map pick level write (hook site) | Map pick writes the arena's level id (mov %al,0x7be04c). | Story-level test build only (XSTORYT) |
| 0x2ca710 | function | map list mode check (hook site) | Map list check for a map not made for the mode. | Map list: Assault only (XMAPA) |
| 0x2ca71c | function | map list (resume) | Map list continue point. | Map list (XMAPA) |
| 0x2ca728 | function | map list listed | Map list path that lists the map. | Map list (XMAPA) |
| 0x2ca7e0 | function | map list leave out | Map list path that leaves the map out. | Map list: Assault |
| 0x2d08ab | function | network menu target | Patched so the menu goes to the match list (0x1a1b30) instead of the Xbox Live / System Link choice page. | System Link straight to the match list |
| 0x2d0a66 | function | main menu network item | Patched so the main menu network item goes straight to System Link. | System Link straight to the match list |
| 0x2d2c40 | function | lobby player setup | Start-of-match player setup that swaps banned characters to Harry Tipper. | Disc-version new match, Ban Small Characters notes |
| 0x2d306b | function | weapon set slot drawing (hook site) | Weapon set page slot drawing call (bl = '1' + slot). | Showdown slot greying (XSDDRW) |
| 0x2d3524 | function | weapon set slot add (hook site) | Weapon set page construct's add of its 6 slots. | Showdown (XSDSLOT) |
| 0x2d7647 | function | menus rebuilt after level (hook site) | Menus rebuilt after a level (was mov $0x4ee3bc,%esi, the choice page). | Return to Lobby (XFELB) |
| 0x2d7667 | function | menus rebuilt: to lobby | Path to the host's lobby when the lost-connection flag is clear. | Return to Lobby |
| 0x2d7699 | function | menus rebuilt (continue) | Continue point after the menu page is chosen. | Return to Lobby |
| 0x2d80c7 | function | lobby player setup call | Call to the lobby player setup (Ban Small Characters swap). | Project notes |
| 0x2d823d | function | setup builder flags (hook site) | Setup builder point where Infinite Ammo sets flag 0x100, then the No Punch code. | Infinite Ammo / No Punch (ia.s) |
| 0x2d83b8 | function | setup builder exit (hook site) | Match setup builder exit. | Random Characters (XRCEND) |
| 0x2d83c7 | function | setup builder exit 2 (hook site) | The builder's other exit (network matches, no bots). | Random Characters (XRCEND) |
| 0x2e60a0 | function | in-match menu buttons | Handles a player's buttons while its in-match menu (pause, Scores) is open. | Spectate |
| 0x2e8651 | function | score text lives read (hook site) | Score text reads the match lives (mov 0x82d274,%eax). | Showdown shows kills (XSDTX) |
| 0x2ed2b0 | function | leave match | Leave-confirm Yes: leave the match. | Return to Lobby |
| 0x2ed360 | function | confirm page select handler | Leave-confirm page select handler. | Return to Lobby, Manage Players kick |
| 0x2ed372 | function | confirm page No | Confirm page No path (back a page). | Manage Players kick |
| 0x2ed385 | function | confirm page Yes jump (hook site) | Confirm Yes jump. | Return to Lobby / kick (XRLYES) |
| 0x2ed418 | function | confirm question text call (hook site) | Leave-confirm page question text. | Return to Lobby (XRLTXT) |
| 0x2ed530 | function | end-of-match Return to Lobby | The update's end-of-match Return to Lobby callback. | Return to Lobby |
| 0x2ed5a0 | function | Leave Match callback | Opens the leave-confirm page as Leave Match does. | Return to Lobby |
| 0x2ef7d5 | function | Select Team second A (hook site) | Select Team reads pad presses for the second A press. | LAN host auto ready (XHBTN) |
| 0x2f070c | function | score text call (hook site) | A second call to the header score text routine 0x11aa0. | Bag Tag team score fix (XBTSC) |
| 0x2f1480 | function | in-match Players page | The game's in-match Players page builder. | Manage Players layout (model) |
| 0x2f1a21 | function | Xbox Live Options heading | The in-match "Xbox Live Options" page heading code. | Manage Players heading (model) |
| 0x2f2072 | function | Scores page player rows (hook site) | Scores page player rows (al = game type). | Team Elimination / Team Vampire scores (XERS) |
| 0x2f207f | function | Scores page player rows (resume) | Continue point in the Scores rows. | Team Elimination / Team Vampire |
| 0x2f209e | function | Scores page lives / time | Scores rows showing "N Lives" or the time. | Team Elimination / Team Vampire |
| 0x2f22a0 | function | score page team rows | Score page team rows drawing (8-byte stack buffer per score). | Bag Tag team time fix |
| 0x2f2353 | function | team row score text (hook site) | Team row score text call. | Bag Tag team time fix (XBTSC) |
| 0x2f407a | function | end-of-match Live check | Live check on the end-of-match menu (patched to mov $1,%eax). | Return to Lobby on LAN |
| 0x2f4095 | function | end-of-match callback push | Push of the Return to Lobby callback. | Return to Lobby (XRLCB) |
| 0x2f4830 | function | pause tab check | Pause tab code that bails if this player's bit is set in 0x7bc8e0 or 0x7bc79c. | Project notes (pause menu) |
| 0x2f4880 | function | pause tab check 2 | The second pause tab check. | Project notes (pause menu) |
| 0x2f6a80 | function | match-over page | The match-over page (Change Game Type). | Return to Lobby |
| 0x2f6ba5 | function | match-over pause page (hook site) | Match-over pause page build. | Return to Lobby (XRLP) |
| 0x2f6e30 | function | pause Options tab builder | The in-match pause menu Options tab builder. | Return to Lobby, Manage Players |
| 0x2f706d | function | pause Options before Leave Match (hook site) | Call just before Leave Match in the Options tab. | Manage Players item (XMPO) |
| 0x2f70a0 | function | pause Options after Leave Match (hook site) | Call after Leave Match in the Options tab. | Return to Lobby item (XRLO) |
| 0x2feec0 | function | MapMaker count links | Counts a MapMaker tile's links (tile number). | MapMaker maps on LAN (factory conversion tile counters) |
| 0x30a2d0 | function | MapMaker set-up | The game's MapMaker set-up, which makes the layer cell pointers. | MapMaker maps on LAN (model for layer pointers) |
| 0x333fe0 | function | MapMaker count plugs | Counts a MapMaker tile's plugs (tile number). | MapMaker maps on LAN |
| 0x352cae | function | disc music read | Disc build's match info receive that reads Music from +0x134 (noted for the disc build). | Music fix notes (XMUSF) |
| 0x3547e0 | function | clear lost-connection flag | Clears the lost-connection flag 0x79e2f0 (run when the choice page opens). | Return to Lobby (XFELB) |
| 0x354810 | function | is network game | Returns network game flag (non-zero in a network game). | Spawn Rule, Return to Lobby, Manage Players, King of the Hill |
| 0x354d10 | function | match info receiver | Match info receiver (client, data, type). | Disc-version host match info (XDSI) |
| 0x354df1 | function | client copies match info (hook site) | A client copies the host's match info back into its setup (mov $0x7bdff8,%edi / rep movsl). | Setup bytes 64-75 from a patched host (XHPCP) |
| 0x354df2 | function | client copies match info (call) | Call position of the match info copy hook. | Setup bytes 64-75 (XHPCP) |
| 0x354ebd | function | update consoles ban swap | Where update consoles run the Ban Small Characters swap on match info with +0x134 set. | Project notes |
| 0x354ee5 | function | match info copy 2 (hook site) | Second match info copy into the setup. | Setup bytes 64-75 (XHPCP) |
| 0x354f1f | function | match info copy 3 (hook site) | Third match info copy into the setup. | Setup bytes 64-75 (XHPCP) |
| 0x355150 | function | SENDTO | Sends a packet to a client (client, type, data, size, reliable, in game); 4-byte header. | Gun Game joiner resends, armouries, Coin Rush, team settings |
| 0x3552c0 | function | game message send routine | Sends a game packet (cdecl: from client, type, data with 4-byte header, size, guaranteed, in game). | Armouries, Gun Game drops, Wrong Way Bag bag sync |
| 0x3553c0 | function | send packet from client | Sends a packet from this console's client (conn, type, buf, len, flag). | Showdown kills, Player Health, Manage Players |
| 0x3555e0 | function | client name | Returns a player's / client's name. | Manage Players rows |
| 0x3559c0 | function | SEND | Sends data to a client (client, 0 = every player; type, data, size, reliable). | MapMaker map send, match info sends, Player Drops Gun |
| 0x355c20 | function | settings send (packet 44) | Lobby match info builder / settings send (packet 44). | Disc-version match info fixes |
| 0x355c36 | function | match info +0x134 write (hook site) | Builder writes the host's Ban Small Characters to +0x134. | Music fix for disc consoles (XMUSF) |
| 0x355d4d | function | settings send call (hook site) | Lobby match info send call. | No Music in disc consoles' in-match flag (XSETS) |
| 0x35624e | function | scores-to-clients timer (hook site) | Host scores-to-clients timer (cmp FPS,%ecx). | Flame Tag score sync 8 times a second (XSCTIM) |
| 0x3562a4 | function | host per-net-frame check (hook site) | Host per-network-frame mode check. | all.s host check |
| 0x356af7 | function | mid-match start send (other) | Other mid-match start send, checked before patching. | Showdown empty weapon set for joiners |
| 0x356b1a | function | joiner match info send (hook site) | Send of the match info to a joiner (client, 0x3b, SINFO, 0x144, 1). | Showdown / empty weapon set for joiners |
| 0x356b67 | function | packet decoder not-in-match jump (hook site) | Packet decoder's "not in the match" je. | Weapon switch prefs kept (XPFGATE) |
| 0x356b68 | function | packet decoder not-in-match jump (operand) | Operand address of that je. | XPFGATE |
| 0x356eb2 | function | packet 15 received (hook site) | Call to read prefs when packet 15 arrives. | Weapon switch prefs kept by name (XPFRCV) |
| 0x356eee | function | packet decoder skip | Path where a packet is thrown away. | XPFGATE |
| 0x357003 | function | match info receive call (hook site) | Call to the match info receiver. | Disc-version host 0x140 match info (XDSI) |
| 0x357278 | function | receive logger hook point 1 | Packet receive point used by the debug receive logger. | LKDBG debug builds |
| 0x3572dd | function | receive logger hook point 2 | Packet receive point used by the debug receive logger. | LKDBG debug builds |
| 0x3573af | function | receive logger hook point 3 | Packet receive point used by the debug receive logger. | LKDBG debug builds |
| 0x35760e | function | network link check | The check that sets the lost-connection flag. | Return to Lobby (notes) |
| 0x357960 | function | host check | Is LAN host (returns non-zero on the host). | Most host-decided features |
| 0x357e54 | function | MapMaker map send (hook site) | Map-send screen's send of the MapMaker map (client, 0x30, map, 0x8000, 1). | MapMaker no factories (XMMSEND) |
| 0x357ef5 | function | MapMaker map send to joiner (hook site) | Send of the MapMaker map to a mid-match joiner. | MapMaker (XMMSEND) |
| 0x357f11 | function | mid-match start send | Mid-match start send code (checked). | Joiner match info |
| 0x357f1e | function | joiner match info send 2 (hook site) | Send of the match info to a mid-match joiner. | Showdown empty weapon set (XNW59) |
| 0x357f30 | function | match start | Match-start packet builder (packet 45). | Disc-version new match |
| 0x357f68 | function | host in-level flag write | Where match start writes the "host is in a level" flag. | Disc-version new match, Advanced Settings in a level |
| 0x357f73 | function | match info +0x134 write 2 (hook site) | Second builder writing +0x134. | Music fix (XMUSFD) |
| 0x357fef | function | match start send (hook site) | Match start before the packet send (push $1 / push $0x144). | Disc-version new match (XNMS) |
| 0x357ff6 | function | match start send (resume) | Resume point of the match start send. | XNMS, XNWSEND |
| 0x357fff | function | match start send call | The SEND call in match start. | Checked by the patcher |
| 0x358370 | function | is connected | Is a player / chr id connected. | Weapon switch prefs, King of the Hill, Manage Players |
| 0x358e20 | function | respawn message pad | Returns the pad from another console's respawn message. | Spawn Rule |
| 0x359ec0 | function | read prefs | Reads a player's weapon prefs from packet 15 (slot byte, then 124 bytes). | Weapon switch for unpatched players |
| 0x359f10 | function | send prefs | Sends a player's weapon prefs (packet 15 layout model). | Weapon switch for unpatched players |
| 0x35a040 | function | send all prefs | Sends every prefs to a client: first host step for a mid-match joiner. | Gun Game joiner |
| 0x35a1c0 | function | send restarting | Restart / rematch send. | Showdown slot-1 set again (XNWRS1) |
| 0x35a1c6 | function | send restarting (resume) | Resume point after the restart hook. | XNWRS1 |
| 0x35a350 | function | return to lobby | Records the match, closes menus and leaves the level for the lobby (packet 11 handler). | Return to Lobby |
| 0x35a970 | function | joiner lives | Fewest lives left of the other players, given to a joiner (cdecl: client). | Showdown joiner lives (XSDMIN) |
| 0x35b170 | function | send spawn pad | Sends a player's spawn pad and the zone owners. | Spawn Rule, King of the Hill, start of match |
| 0x35b176 | function | send spawn pad host check (hook site) | Host check inside send spawn pad. | Start of a match (XRDYSP) |
| 0x35bbd4 | function | score sync write (hook site) | Host score sync writes the rank score (ebx) and lives left. | Showdown players out shown "--" (XSDSS) |
| 0x35bed0 | function | ready start | Returns 1 once every player has loaded (offline: always). | Gun Game start, start of a match |
| 0x35bf80 | function | ready start code | Ready start code checked to be the original. | Start of a match |
| 0x35bf96 | function | ready start code 2 | Ready start code checked to be the original. | Start of a match |
| 0x35c210 | function | coin message receive | Coin message (type 35) receive. | Setbacks "Humiliation!" signal (XSBRX) |
| 0x35c22f | function | coin message own player (hook site) | Coin message arriving (ebx = local number, cx = pad). | Setbacks (XSBRX) |
| 0x35c23f | function | coin message branch | Branch target in the coin message code. | Setbacks (XSBRX) |
| 0x35c253 | function | death coin arriving (hook site) | A LAN player's death coin arriving. | Coin Rush / Coin Drop |
| 0x35c25b | function | coin message (continue) | Continue point after the coin message. | Setbacks |
| 0x35c2e4 | function | damage report decode (hook site) | Damage report decode (packet 17) at the amount. | Player Health (XPHRX) |
| 0x35c890 | function | team message handler | Handles a team message (conn, payload, type, len). | Manage Players team moves |
| 0x35c8bb | function | team write (hook site) | Team message writes the chr's team (mov %edx,0x84(%ecx)). | Manage Players banks kills (XMPTW1) |
| 0x35c954 | function | spawn request handler return | Return point of send spawn pad from the spawn request handler. | Gun Game resends after first spawn request |
| 0x35cc40 | function | take pickup message (hook site) | Take pickup message. | King of the Hill: only the hill can be captured |
| 0x35cc45 | function | take pickup message (resume) | Resume point after the KotH hook. | King of the Hill |
| 0x35cc90 | function | read drop message | Runs a drop message (packet 22) on this console. | Gun Game drops on pads (XGGMV) |
| 0x35cf2d | function | drop message other branch (hook site) | Read drop message's DROPMSG_OTHER branch (esi = pickup prop). | Armouries (XLKDEC) |
| 0x35cf38 | function | drop message other (continue) | Continue point in that branch. | Armouries |
| 0x35d033 | function | drop message end | End of the drop message handler. | Armouries |
| 0x35d990 | function | send if local | Sends a message if the prop is this console's. | Showdown kills, Player Health (XSDKL) |
| 0x35dcd4 | function | leaver kills clear | Branch that cleared a leaver's kills by its own team (patched). | Manage Players kill banking |
| 0x35df17 | function | greet joiner (hook site) | Host greets a mid-match joiner (call to send all prefs). | Gun Game / King of the Hill joiner (XGGJOIN) |
| 0x35df46 | function | joiner lives call (hook site) | Call to the joiner lives function. | Showdown (XSDMIN) |
| 0x35e3bf | function | Thief collect message (hook site) | Thief collect message decode. | Coin Rush (XCRNR) |
| 0x35e4c0 | function | send hit report | Sends a hit this console decides ([esp+4] = hit; eax 1 = take it now). | Player Health |
| 0x35eaa1 | function | send kill message (hook site) | Kill message send in the kill sender (esi = prop it goes by, ebx = size, edi = reliable; types 18 host / 19 player). | Showdown one-hit kills, Player Health (XSDKL) |
| 0x35ebd0 | function | weapon set entry | Returns weapon [esp+4] of the match's weapon set (0 = none); edx = number of usable weapons. | Random Weapon / Gun Game hand-outs |
| 0x35ec60 | function | pickup message send | Sends "picked up" for a pickup (pickup, chr prop). | Gun Game hand-outs, King of the Hill, Wrong Way Bag replays |
| 0x35ef7f | function | state packet team write (hook site) | State packet writes the chr's team (mov %eax,0x84(%ebp)). | Manage Players kill banking (XMPTW2) |
| 0x35f28e | function | dead player spawn resend (hook site) | Host's 1.5 s resend of a dead LAN player's spawn point. | Spawn Rule (XSRRS) |
| 0x35f740 | function | kick player | The game's kick / drop of a LAN player (network player entry, reason 2 = kicked). | Manage Players kick |
| 0x360630 | function | Live check | The Live check that the end-of-match menu called (replaced by mov $1,%eax). | Return to Lobby on LAN |
| 0x3cc094 | function | format text | Formats text (text, format, value), sprintf style. | Score page team rows (XBTSC) |
| 0x47c4cc | data | float 1.1 | Float constant the mod uses as "1.1 lines" for text placement. | Spectate button hints |
| 0x481268 | data | float 2.2 | Float constant used as "2.2 lines" for text placement. | Spectate button hints |
| 0x4a32a4 | data | the final level's data raw file name | Address of the string data/the final level's data file (Future Perfect level file). | Story-level test build only |
| 0x4c53d8 | data | language index | Current language index, used to pick the "Return to Lobby" text. | Return to Lobby |
| 0x4c53e4 | data | widescreen factor | Float used as the widescreen factor for text shadow offsets. | Team icons text |
| 0x4d6dc4 | data | team colours | Team colour table (Red 0x7f202080, Blue, Yellow, Green). | Manage Players, Team icons |
| 0x4d6f00 | data | mode table | Mode table (0x20 per mode); +8 = 4 marks modes whose arcade setups need the Deathmatch bit. | Story-level test build, mode list |
| 0x4d6f08 | data | mode table +8 | Mode table field: which setup type the mode needs (4 = Deathmatch, Assault has its own). | Map list / mode list: Assault only on Assault maps |
| 0x4d6f0c | data | mode table team game | Mode table team-game value (0 no, 1 always, 2 Teamplay item). | Respawn Delay, Spawn Rule, hide.s |
| 0x4d6fd0 | data | mode table Bag Tag team spawns | Bag Tag entry: team spawn points used (patched to 1). | Team Bag Tag spawns |
| 0x4d6fec | data | mode table Elimination teams | Elimination entry: Teamplay possible (2), team spawn points (1). | Team Elimination |
| 0x4d702c | data | mode table Vampire teams | Vampire entry: Teamplay possible (2), team spawn points (1). | Team Vampire |
| 0x4d714c | data | mode table Gladiator team game | Gladiator entry's team game, set from the Team VIP setting. | Team VIP |
| 0x4d7150 | data | mode table Gladiator team spawns | Gladiator entry's team spawns, set from the Team VIP setting. | Team VIP |
| 0x4d7318 | data | arcade arena list | Arcade arena list (0x3c each, 16 arenas). | Project notes (levels) |
| 0x4dd7f8 | data | MapMaker icon list | MapMaker editor icon list (index 31 = vehicle). | Project notes (MapMaker) |
| 0x4ec200 | data | font handle | Font passed to set font for the debug text. | Debug build text |
| 0x4ec8c4 | data | frame step | Per-frame tick count the game uses (damage routine and respawn delay read it). | Player Health, Respawn Delay, Flame Tag scoring |
| 0x4ec8cc | data | frame time | This tick's frames (0 while paused) / FPS, as a float. | Spectate camera speed |
| 0x4edc6c | data | FPS | Frames per second (int). | Timers across the mod (Gun Game, Overtime, Spawn Rule, Team VIP, Multikill ...) |
| 0x4ede9c | data | Return to Lobby text table | The update's "Return to Lobby" text per language. | Return to Lobby |
| 0x4ee3bc | data | choice page menu | The Xbox Live / System Link choice page. | Return to Lobby (XFELB) |
| 0x4ee66c | data | match list menu | The match list page. | Return to Lobby |
| 0x4eeabc | data | host lobby menu | The host's lobby page. | Return to Lobby |
| 0x4feca4 | data | gun info table pointer | Pointer to the gun info table (0x29c per gun type: +0xc flags, +0x14 / +0x1c ammo types, +0x28 / +0x2a arcade ammo). | Gun Game ammo, armouries |
| 0x4ff220 | data | GCOMBO gun id table | gun id table (0x3c per gun id, +0x10 gun type). | Gun Game / Showdown weapon checks |
| 0x510bf0 | data | story level list | A story setup list pointer copied into the test arcade setup. | Story-level test build only |
| 0x51b0f8 | data | level table | Level table (0x80 per entry: +8 id, +0x24 story setup, +0x28 arcade setup). | Project notes (levels) |
| 0x51d778 | data | level 0x51 entry | Level table entry for level 0x51 (Future Perfect). | Story-level test build only |
| 0x51d7a0 | data | level 0x51 arcade setup | Level 0x51 entry +0x28 (arcade setup pointer, normally 0). | Story-level test build only |
| 0x526b18 | data | character select table | 150-character select list (48 bytes each: +1 head, +4 character type). | Random Characters |
| 0x5298c4 | data | pause tab table | Pause tab table (12-byte entries: text id, page, enable function). | Project notes (pause menu) |
| 0x529b90 | data | confirm page | The leave-confirm page. | Return to Lobby, Manage Players kick |
| 0x52e620 | data | MapMaker tiles | MapMaker tiles (0x140 each: +0x14 / +0x18 cells across / down, +0x1c layers, +0x20 slots). | MapMaker maps on LAN |
| 0x537210 | data | disc music table | Music table in the disc build (8 bytes each). | Project notes (music fix) |
| 0x53c320 | data | music table | Music table (8 bytes each: +0 track, +4 name text id; entry 0 = level music). | Project notes (music fix) |
| 0x546de4 | data | network link | The console's network link state. | Return to Lobby |
| 0x546fb0 | data | forced drop pad | The game's forced drop pad (-1 = choose one). | Gun Game drops, King of the Hill, Player Drops Gun |
| 0x725fc8 | data | spawn candidate list | spawn point picker's candidate spawn list (count in ebp). | Spawn Rule, King of the Hill, zs.s |
| 0x72a4d0 | data | menu state | The menu's state (3, 4 or 6: no labels drawn). | Manage Players |
| 0x749014 | data | level pads pointer | Pointer to the level's pads (32 bytes: +0 number, +4 flags, +0xc position). | Armouries, Switch Spawns, Coin Rush |
| 0x74901c | data | placement pads pointer | Pointer to the placement pads (32 bytes each). | Armouries |
| 0x7613d0 | data | disc music setting | Disc build's music setting written from match info +0x134. | Project notes |
| 0x7626d0 | data | level props pointer | Pointer to the level props (0x2e8 each). | Armouries, Gun Game map gun removal |
| 0x7687c0 | data | chr list pointer | Pointer to the chr data list. | Gun Game, Coin Rush, Multikill, Infection |
| 0x774040 | data | disc SINFO | Disc build's match info (SINFO). | Project notes |
| 0x77f464 | data | active chr count | Number of active characters. | Gun Game, Catch-Up, Team VIP, Flame Tag |
| 0x77f47c | data | NDROPS zone count | Number of zones (max 20). | King of the Hill, Wrong Way Bag |
| 0x77f498 | data | Assault phase list | Assault phase list (+0 count, +4 phases 0xa8 each, +0 objective id). | Auto-Complete Phase, Time Bonus After Phase |
| 0x78ad58 | data | disc setup copy | Disc build's setup copy. | Project notes |
| 0x7927b8 | data | pickup pads | Coin pickup pads (30 words). | Coin Rush / Coin Drop |
| 0x792830 | data | pickup props | Coin pickup props (30 words). | Coin Rush / Coin Drop |
| 0x7928a8 | data | pickup count | Number of coin pickups. | Coin Rush / Coin Drop |
| 0x794594 | data | host Music setting | The host's Music setting (match settings item 15). | Music fix (XMUSF) |
| 0x7945a8 | data | menu context | Menu context passed when opening the Advanced sub-pages. | Advanced Settings folder links (sub.s) |
| 0x7945b4 | data | pause menu flag | Non-zero in the pause menu. | Match settings layout (layA.s, ts.s) |
| 0x794d84 | data | menu contexts | Menu context per player (indexed by 0x8097e0). | Return to Lobby, Manage Players |
| 0x795bec | data | leave-confirm kind | The leave-confirm page's kind (game writes 0 / 1; mod uses 2). | Return to Lobby / Manage Players kick |
| 0x79e2dc | data | network game flag | Network game word: non-zero in a network (LAN) match. | Almost every host-decided feature |
| 0x79e2e4 | data | in-game traffic flag | Set when this console is in the match; game packets (pickups, spawn points, packet 15) are dropped before it is set. | Weapon switch prefs, Gun Game resends |
| 0x79e2f0 | data | lost-connection flag | Set when a cable check failed or the host was lost in a level. | Return to Lobby menus |
| 0x79e340 | data | pickup forced flag | 1 while a pickup another console reported is done here (chr picks up pickup does it for any chr; pickup message send sends nothing). | Gun Game hand-outs |
| 0x79e344 | data | reported hit flag | 1 while the game takes a reported hit. | Player Health |
| 0x79e360 | data | coin message flag | Word the coin message handler sets to 1. | Setbacks (XSBRX) |
| 0x7a7204 | data | is Xbox Live | 1 = Xbox Live (not LAN). | Return to Lobby |
| 0x7a7208 | data | OWNCLIENT | Pointer to this console's own network client. | Packet sends (armouries, Gun Game, Wrong Way Bag) |
| 0x7a7220 | data | HOSTINFO / SINFO | The host's match info (packets 44 / 45 / 59, 0x144 bytes): +0x14 setup byte 72, +0x58 level, +0x9d match number, +0xac weapon slots, +0x134 Ban Small Characters, +0x138 Music, +0x13c host-in-level. | Gun Game, Showdown, disc-version new match, setup bytes |
| 0x7a7358 | data | match info +0x138 | SINFO+0x138: the host's Music. | Music fix (XNMS) |
| 0x7a735c | data | match info +0x13c | SINFO+0x13c: the host-is-in-a-level flag. | Disc-version new match |
| 0x7a7380 | data | network clients | The game's 16 network clients (0x314 each: +0 id, +0x1c state, +0x20 players on it). | Disc-version new match, Player Drops Gun |
| 0x7a739c | data | client state | Network client +0x1c: its state (host's view), per client every 0x314. | Armouries |
| 0x7a73b4 | data | client spawned flags | Network client field whose bit 0x10 says that console has spawned (as the ranking checks). | Team Elimination / Team Vampire |
| 0x7aa4c0 | data | network player table | LAN players (0x124 each, 16): +4 owner client, +0x4c flags (0x10 prefs received), +0x104 character, +0x105 head. | Weapon switch prefs, Coin Rush, kill messages, Manage Players |
| 0x7aa4c4 | data | network player table owner | network player table +4: the player's owner client (its console). | Setbacks, Gun Game drops, start of match |
| 0x7aa508 | data | network player table previous team | network player table +0x48, read as the previous team. | Team skip (skip.s) |
| 0x7aa50c | data | network player table +0x4c flags | network player table flags (bit 2 tested). | Spawn Rule, mc.s |
| 0x7b72b4 | data | MapMaker map buffer pointer | Pointer to the MapMaker map temp buffer. | MapMaker maps on LAN |
| 0x7bc79c | data | pause block bits 2 | Per-player bits that make the pause tabs bail. | Project notes |
| 0x7bc8e0 | data | pause block bits | Per-player bits that make the pause tabs bail; the confirm No clears it. | Return to Lobby |
| 0x7bdfc0 | data | setup | The host's match setup (+0 = setup id, e.g. 17). | Return to Lobby, setup data path |
| 0x7bdfcc | data | menu context | Setup +0xc: menu context (LAN 0xb / 0xc / 0xd). | Mode list, start of match, team modules |
| 0x7bdfec | data | arena list index | The selected arena's list index. | Story-level test build |
| 0x7bdff8 | data | menu parms | Setup +56 (menu parms): copied into SINFO+4; character types +20, character heads +68. | Random Characters, setup bytes |
| 0x7bdffa | data | setup byte 58 | Setup byte read as the number of bots. | Random Characters |
| 0x7bdffb | data | setup byte 59 (team count) | Team list count. | Team list modules (bal.s, lan.s, lh.s) |
| 0x7bdffc | data | setup bytes 60-63 (team ids) | Team list ids. | Team list (lh.s) |
| 0x7bdfff | data | setup byte 63 | Last team list id slot. | Team list (lh.s) |
| 0x7be000 | data | setup byte 64 | Setup byte 64 (0xE0 \| Respawn Delay); start of bytes 64-75. | Respawn Delay, host-has-patch markers |
| 0x7be001 | data | setup byte 65 | 0x80 \| Red \| Blue<<3 respawn delays. | Respawn Delay per team |
| 0x7be002 | data | setup byte 66 | 0x80 \| Yellow \| Green<<3 respawn delays. | Respawn Delay per team |
| 0x7be003 | data | setup byte 67 | 0x90 \| Player Health \| Spectate<<2. | Player Health, Spectate |
| 0x7be004 | data | setup bytes 68-71 | Setup bytes 68-71. | Host-has-patch setup bytes |
| 0x7be008 | data | setup byte 72 | 0xB0 \| Spawn Rule \| Overtime bit 2 \| Gun Game bit 3. | Gun Game, Spawn Rule, Overtime |
| 0x7be009 | data | setup byte 73 | 0xD0 \| Multikill (bit 3 = Showdown match). | Multikill, Showdown |
| 0x7be00a | data | setup byte 74 | 0xC0 \| Zone interval \| King of the Hill / coin bits. | Zone Interval, King of the Hill, Coin Rush |
| 0x7be00b | data | setup byte 75 | 0xA0 \| disabled-team mask. | Team icons / disabled teams |
| 0x7be00c | data | setup character types | Per-player character types in the setup. | Random Characters |
| 0x7be01c | data | setup per-player team | Per-player bytes 16 past character types, read and written as a player's team by the team-balance module. | Team balance (bal.s) |
| 0x7be03c | data | setup character heads | Per-player heads in the setup. | Random Characters |
| 0x7be04c | data | menu level | The menu's selected level (0x64 = MapMaker map). | MapMaker maps, map list |
| 0x7be04d | data | menu game type | The menu's game type byte. | Showdown, start of match |
| 0x7be04e | data | MODMENU | The mode being picked on the menu. | Advanced Settings, mode-dependent menus |
| 0x7be050 | data | menu game flags | Setup game flags (bit 1 Teamplay, 0x100 Infinite Ammo, 0x4 One Shot Kill ...). | Gun Game, Showdown, team balance |
| 0x7be058 | data | menu time limit | Setup time limit (frames, 0 = none). | Catch-Up period |
| 0x7be05c | data | menu kill limit | Setup kill / score limit. | Gun Game: no score limit |
| 0x7c3bec | data | current level | The level (0x65 = front end). | Advanced Settings custom-match gate, story test |
| 0x7c3bf0 | data | NPLAYERS | Number of players. | Gun Game, Coin Rush, weapon switch, Manage Players |
| 0x7f0ee0 | data | pickup respawn timers | 75-entry pickup respawn timer table. | Project notes (keep resends few) |
| 0x7f1758 | data | bot count | Number of bots. | Manage Players, Showdown, Team Elimination |
| 0x7f19c8 | data | FSTAT flame status | Infected / burning bitmask by chr id. | Flame Pass, Infection, Flame Tag |
| 0x7f19e4 | data | team bag props | Bag prop per team (8 bytes each). | Wrong Way Bag |
| 0x7f1a64 | data | DROPS zone list | Zone list (8 bytes each: prop; pad at -4). | King of the Hill, Wrong Way Bag |
| 0x7f2380 | data | active characters | Active chr list. | Gun Game, Catch-Up, Team VIP, Flame Tag |
| 0x7f4f60 | data | HUD message rings | Per-player HUD message rings (0x177c each: +0x30 next, +0x38 16 entries of 0x16c). | Spectate "Spectating <name>" |
| 0x7f4f98 | data | HUD message ring entries | 0x7f4f60 +0x38: the ring's entries. | Spectate |
| 0x7ffa48 | data | PLAYERS | Players pointer (stride 0x1584: +0 player num, +4 local number, -1 = another console's; +0x14 prop). | Most features |
| 0x7ffa7c | data | local player | A local player pointer drawn each frame (name tags). | Spectate |
| 0x7ffb20 | data | dropped pickup data | Dropped pickups' data (0xd8 each, +0 prop). | Gun Game drops |
| 0x801480 | data | dropped pickup times | Gameframe each dropped pickup slot was filled at (oldest recycled). | Gun Game drops |
| 0x801500 | data | dropped pickup slots | 30 dropped pickup slots in use (dword each). | Gun Game drops, Coin Rush |
| 0x803dac | data | prop count | Number of level props. | Armouries, Gun Game |
| 0x8053c0 | data | placement pad count | Number of placement pads. | Armouries |
| 0x805464 | data | pad count | Number of level pads. | Armouries, Switch Spawns, Coin Rush |
| 0x808e38 | data | canvas factor | Menu units to pixels factor. | Manage Players, Team icons |
| 0x809048 | data | last menu item made | The last menu item made. | Advanced Settings one-page list |
| 0x8097e0 | data | menu player index | Index of the player whose menu is open (into the menu contexts). | Return to Lobby, Manage Players |
| 0x809fd4 | data | scrolled part | Scrolled part state (+0x54 / +0x58 first / last item). | Advanced Settings one-page list |
| 0x809fd8 | data | scroll item | Item used when finishing a scrolled list. | Advanced Settings one-page list |
| 0x809fe0 | data | construct state | Menu construct state (+0x28 item flags, +0x3c scrollable height). | Advanced Settings layout |
| 0x809fe8 | data | current menu | Menu being built (+0x178 items, +0x5c content height). | Advanced Settings, Manage Players, Team icons |
| 0x80a000 | data | last item | Last item of the list being built. | Advanced Settings one-page list |
| 0x82d10c | data | game state | Game state (5 zones tick check, 6 / 7 in the level, 7 = being played, 8 = ended). | Most in-match features |
| 0x82d118 | data | GFRAME | Gameframe counter. | Timers (Gun Game, Overtime, Team VIP, Multikill ...) |
| 0x82d120 | data | Gladiator prop | The Gladiator (VIP) prop. | Team VIP |
| 0x82d140 | data | next match parms | Next match's parameters (setup copied here before the level). | Setup data path |
| 0x82d148 | data | next match bytes 64-67 | Next match setup bytes 64-67. | Host setup bytes |
| 0x82d14c | data | next match bytes 68-71 | Next match setup bytes 68-71. | Host setup bytes |
| 0x82d150 | data | next match bytes 72-75 | Next match setup bytes 72-75. | Host setup bytes |
| 0x82d200 | data | match parms | Match parameters (setup byte N = 0x82d200 + (N-56)). | Setup data path |
| 0x82d203 | data | match team count | Match setup byte 59: number of team colours. | Manage Players, team skip |
| 0x82d208 | data | match bytes 64-67 | Match setup bytes 64-67 (64 = Respawn Delay). | Respawn Delay |
| 0x82d209 | data | match byte 65 | Match setup byte 65 (+ team index for 66). | Respawn Delay per team |
| 0x82d20b | data | match byte 67 | Setup byte 67 as received from the host (0x90 \| Player Health \| Spectate<<2). | Player Health, Spectate |
| 0x82d20c | data | match bytes 68-71 | Match setup bytes 68-71. | Host setup bytes |
| 0x82d210 | data | match byte 72 | Setup byte 72 as received from the host. | Gun Game, Overtime, Spawn Rule |
| 0x82d211 | data | match byte 73 | Setup byte 73 as received from the host. | Multikill, Showdown |
| 0x82d212 | data | match byte 74 | Team-list byte 74 as received from the host. | King of the Hill, Coin Rush, Zone Interval, Switch Spawns |
| 0x82d213 | data | match byte 75 | Setup byte 75 (disabled-team mask) as received. | Disabled teams |
| 0x82d254 | data | match level | Match parms level byte. | Project notes |
| 0x82d255 | data | GMODE game type | Match game type byte (1 Bag Tag ... 10 Story). | Most mode-dependent features |
| 0x82d256 | data | MODIN mode | Match mode byte (3 DM ... 19 Monkey Assistant). | Most mode-dependent features |
| 0x82d258 | data | match game flags | Game flags (1 Teamplay, 4 One Shot Kill, 0x40 Arcade League, 0x8000000 Challenges ...). | Teamplay checks, Showdown, custom-match gate |
| 0x82d260 | data | time left | Time left in the match (the host's, kept up to date). | Overtime, Catch-Up, Time Bonus |
| 0x82d274 | data | match lives | The match's number of lives (0 = none). | Showdown, Team Lives, Return to Lobby |
| 0x82d300 | data | team scores | Per-team scores, 4 words (for lives modes the team's lives left). | Team Elimination / Team Lives, team Bag Tag (bt.s) |
| 0x836064 | data | font height | Current font height (float). | Manage Players, Spectate hints |
| 0x83a654 | data | Team Spawns setting | Word whose bit 1 means Team Spawns Off (this console's setting). | Team Spawns, Switch Spawns, zs.s |
| 0x83a658 | data | disabled colours | This console's disabled team colours mask. | Disabled teams, Manage Players, team modules |
| 0x83a65c | data | team balance setting | On/off word toggled from a menu item by the team-balance module. | Team balance (bal.s) |
| 0x83a660 | data | np.s setting | On/off word toggled from a menu item by the np.s module. | np.s module |

## PS2

| Address | Kind | Name | What it is | Used for |
|---|---|---|---|---|
| 0x104b28 | function | get text by id | Returns a game text by id (a0 = text id; the confirm page title and question go through it). | Manage Players kick confirm page (MPTT / MPTB) |
| 0x10a328 | function | set text size | Sets the text size (f12-f14; the mod starts it from 1). | Manage Players option rows |
| 0x10a8a8 | function | fit text to width | Scales text to a width (a0 text, a1 0 = only smaller, a2 1 = only across, f12 width). | Manage Players option rows |
| 0x10aaa8 | function | set font | Selects a font (a0); returns the previous one. | Manage Players, Spectate hints, Team icons |
| 0x10b208 | function | text width | Returns a text's width (a0 = text). | Manage Players rows (MPATW), Team icons |
| 0x10d158 | function | draw button hint text | Draws a hint text line (f12 x, f13 y). | Spectate on-screen button hints |
| 0x10e760 | function | pad held buttons | Returns a pad's held buttons (R2 held = the game's bit 2). | Spectate free cam speed-up |
| 0x10e7e8 | function | pad new presses | Returns a pad's newly pressed buttons. | Spectate controls, LAN host auto second A on Select Team (HBTN) |
| 0x10eb18 | function | stick with dead zone | Called with the 0.25 dead zone the game's own look sets (f12). | Spectate camera |
| 0x10eb90 | function | read stick axis | Reads a stick axis (a0 player number, a1 axis) -> f0. | Spectate camera |
| 0x10f408 | function | button name | Returns a button's display name. | Spectate button hints |
| 0x111a00 | function | play sound | Plays a sound from a 48-byte sound parameter buffer (a0). | Overtime, Setbacks, King of the Hill, Multikill sounds |
| 0x111b00 | function | sound parms init | Initialises a 48-byte sound parameter buffer (a0). | Overtime "Text Sweep", Setbacks laugh, King of the Hill |
| 0x1123d8 | function | sound loader decision (hook site) | Sound loader decision point (a0 = sound id, t7 = table entry); the mod forces the multikill and Setbacks laugh sounds to load (SNDLD). | Multikill, Setbacks |
| 0x1123e0 | function | sound loader decision (resume) | Resume point after the sound loader hook. | Setbacks, Multikill |
| 0x139d88 | function | save end-of-match scores | End-of-level step called from the end-of-level code at 0x13C994. | Weapon switch overrides restored (PFALL), Team Lives (TLSV) |
| 0x13a090 | function | kill count routine | Counts a chr's kills (a0 = chr). | Showdown kills (GGADD) |
| 0x13a118 | function | kill count routine before adjustments (hook site) | Point in kill count routine before the lives / suicide adjustments (s0 = kills, s1 = chr). | Multikill (mk.py MKADD) |
| 0x13a120 | function | kill count routine (resume) | Resume point in kill count routine after the score hooks. | Gun Game / Showdown score (GGADD), Multikill |
| 0x13a12c | function | kill count routine score store | Point in kill count routine the mod jumps to with the Gun Game level as the score. | Gun Game score = level |
| 0x13a208 | function | add team score | Adds points to a team (a0 = team, a1 = points). | Catch-Up (CUTA), Team VIP points |
| 0x13a210 | function | add team score (resume) | Resume point after the Catch-Up hook. | Catch-Up |
| 0x13a6f0 | function | add points | Adds points to a chr (a0 = chr record, a1 = points). | Catch-Up (CUSC), Coin Rush scoring |
| 0x13a6f8 | function | add points (resume) | Resume point after the Catch-Up hook. | Catch-Up |
| 0x13a774 | function | add points tail call (hook site) | Add points' tail call to add team score. | Catch-Up (CUTAR) |
| 0x13a7c4 | function | add kills (hook site) | Add kills entry check (s0 = killer, s2 = victim id). | Gun Game level-up (GGK) |
| 0x13a7cc | function | add kills (resume) | Resume point after the Gun Game hook. | Gun Game |
| 0x13a7f0 | function | add kills Gladiator check (hook site) | Gladiator check in add kills (s0 = killer data, s2 = victim id). | Team VIP (VIPK) |
| 0x13a7f8 | function | add kills Gladiator check (resume) | Resume point after the VIP check. | Team VIP |
| 0x13a8a4 | function | add kills no team points | Add kills path that skips team points. | Showdown team kills, Team VIP |
| 0x13a90c | function | death lives (hook site) | Where a death reads the victim's lives (lhu t6,2664(s1)). | Team Lives (TLDEC) |
| 0x13a940 | function | after kill counted (hook site) | Point in add kills after the kill is counted (s0 = killer, s1 = victim), before the multikill code. | Infect On Kill (INFK), Multikill (mk.py MKH) |
| 0x13a948 | function | after kill counted (resume) | Resume point after the multikill hook. | Multikill (mk.py) |
| 0x13a954 | function | kill team points (hook site) | Where kills add team points (lw t7,108(s2)). | Showdown team kills (SDTS) |
| 0x13a960 | function | kill team points (continue) | Path that adds team points. | Showdown |
| 0x13a9f0 | function | add kills end | Add kills continue / end point the Gun Game code jumps to. | Gun Game |
| 0x13acc0 | function | rank players | Ranks players / teams (a0; the mod calls it with 0 for one more pass). | Team Lives ranking, Team VIP timer, Gun Game frame tick |
| 0x13ad98 | function | ranking lives check (hook site) | Ranking reads the match lives (lw t6,108(t7)). | Showdown ranks by score (SDRK) |
| 0x13ada4 | function | ranking lives check (continue) | Continue point in the ranking. | Showdown |
| 0x13adbc | function | ranking survival time (hook site) | Ranking reads survival time (lw t7,2676(s0)). | Team Elimination / Team Vampire (TLAGE) |
| 0x13add8 | function | ranking sets lives left | Ranking code that sets lives left. | Showdown |
| 0x13ade0 | function | ranking mode step | Ranking step taking 3*FPS off in Elimination / Vampire. | Showdown |
| 0x13ae10 | function | ranking after mode step | Ranking point after the 3*FPS step. | Showdown |
| 0x13b1f0 | function | ranking team step (hook site) | Ranking chooses team or own score. | Team Elimination / Team Vampire (TLRK) |
| 0x13b204 | function | ranking team score | Ranking path using the team score. | Team Elimination / Team Vampire |
| 0x13b214 | function | ranking own score | Ranking path using the player's own score. | Team Elimination / Team Vampire |
| 0x13b5d0 | function | weapon allowed check | Checks if a gun can be picked (a0 = menu mode, a1 = gun id). | Gun Game / Showdown weapon bans (GGBAN, SDDRW) |
| 0x13c8b8 | function | level done | Ends the level / match (a0 = 1). | Gun Game / Showdown end, Zones end |
| 0x13c980 | function | end-of-level code | End-of-level code every mode's end goes through. | Weapon switch overrides restored |
| 0x13c994 | function | end-of-level save call (hook site) | Call to save end-of-match scores. | PFALL |
| 0x13d048 | function | lives match end (hook site) | Lives end check in the game tick (s2 = players with lives left). | Showdown with Teamplay (SDEND) |
| 0x13d054 | function | lives match end | The match end path. | Showdown |
| 0x13d060 | function | lives match continue | Path when more than one player has lives. | Showdown |
| 0x13dda0 | function | zones tick (hook site) | Zones tick. | King of the Hill (KHT) |
| 0x13e3dc | function | match frame tick (hook site) | Per-frame call to the ranking. | Team VIP timer (VIPT) |
| 0x13e53c | function | time limit check (hook site) | Time limit check (t6 = time left). | Capture the Bag Overtime (OTH) |
| 0x13e544 | function | time up | The game's time-up path. | Overtime |
| 0x13e578 | function | time up scoring (hook site) | Time-up call to the Zones last-score code. | Zones last score (NCZE) |
| 0x13e58c | function | time not up | Path while time is not up. | Overtime |
| 0x13e660 | function | mode tick call site | Call site of the jal 0x388DB0 that every mode's tick goes through (the PS2 equivalent of Xbox 0x239360's calls). | Mercy Rule check placement |
| 0x13fcfc | function | start-of-level wait (hook site) | Start wait's call to ready start. | Gun Game / Showdown map gun removal (GGRDY) |
| 0x143dc8 | function | give gun | Gives a gun to a chr. | Gun Game hand-outs |
| 0x1440c0 | function | level setup by map | Returns a map's level setup. | Spawn Rule |
| 0x1441d8 | function | level setup | Returns a level's setup. | Switch Spawns, Coin Rush |
| 0x144270 | function | pickup subtype | Weapon of a map pickup's weapon-set slot (a0 type, a1 slot); -1 = not made. | Showdown empty weapon set, weapon switch |
| 0x144898 | function | spawn point picker team flag (hook site) | spawn point picker's team spawn points read the chr's team (lw t7,132(s7)). | Switch Spawns (SWTM) |
| 0x1448c0 | function | spawn point picker Assault path | spawn point picker Assault path word restored after an old Switch Spawns hook was removed. | Switch Spawns (removed hook) |
| 0x14498c | function | spawn point picker random pick (hook site) | spawn point picker's jal to rand. | Spawn Rule (SRN), King of the Hill spawns |
| 0x145a58 | function | mode allows pad | Checks a spawn pad's create flags fit this match (as spawn point picker checks; a0 = pad flags). | Switch Spawns, Spawn Rule |
| 0x147700 | function | level pickups subtype call (hook site) | Level pickups' jal to pickup subtype (type, slot 0-5). | Showdown / Gun Game empty weapon set (NWPST) |
| 0x14df50 | function | menu start scroll | Starts a scrolling list (f12 height, a0 items). | Advanced Settings one-page list, Manage Players |
| 0x14e008 | function | menu end scroll | Ends a scrolling list. | Advanced Settings, Manage Players |
| 0x14e8f0 | function | add menu text item | Adds a text item (a0 text, a1 id, a2 flags, f12 height, a3 select, t0 draw). | Every Advanced Settings item, weapon set page (SDSLOT) |
| 0x14ea80 | function | menu get text | Returns a menu text as drawn (text, option flags, 0), upper case applied. | Manage Players, Team icons |
| 0x14f0b8 | function | add menu option | Adds an option (a0 = text) to the current item. | Every Advanced Settings item |
| 0x14f118 | function | add menu option with id | Adds an option text with an id (a0 text, a1 id). | Manage Players rows (team names, "Kick") |
| 0x14f3f8 | function | menu gap | Adds the gap below a page heading, as the in-match pages. | Manage Players page |
| 0x14f430 | function | menu divider | Adds a divider / break (a0 index). | Advanced Settings layout |
| 0x1508a8 | function | menu finish item | Finishes the last item (its height counted), as the end of a scrolled list does. | Advanced Settings one-page list |
| 0x150f88 | function | menu option shown | Sets / gets the option an item shows (a0 = item). | Manage Players rows |
| 0x151020 | function | get menu item by id | Returns a menu item by id (a0 page, a1 id). | Advanced Settings, match settings greying |
| 0x151568 | function | menu page setting | Menu page builder call with a0 = 1 (Manage Players page build). | Manage Players page |
| 0x1516f0 | function | menu text margins | Sets text margins. | Advanced Settings layout, Manage Players |
| 0x151740 | function | menu item flags | Sets item flags (assigns). | Advanced Settings layout, Manage Players |
| 0x151c98 | function | menu page begin | Page begin: flags, title, back. | Manage Players page |
| 0x153938 | function | option text colour | Option text colour (a0 menu, a1 item, a2 &colour, a3). | Manage Players waiting move greyed (MPTCOL) |
| 0x158030 | function | menu refresh | Called with the current menu (0x643674) when rebuilding the Manage Players page. | Manage Players |
| 0x1584d8 | function | menu state | Returns the menu's state (3, 4 or 6: no labels drawn). | Manage Players |
| 0x159008 | function | close menu | Closes a menu (ctx, 0); closing the kick confirm with it softlocked the pause menu. | Manage Players |
| 0x159190 | function | menu back a page | Back a page (a0 = item). | Confirm page No |
| 0x1591b8 | function | menu back | Menu back / close path the Manage Players code jumps to. | Manage Players |
| 0x159588 | function | open menu page | Opens a menu page. | Manage Players, Return to Lobby-style pages |
| 0x159b80 | function | add arrow-select options | Makes an item an arrow-select option list (a0 flags). | Advanced Settings items, Manage Players rows |
| 0x15aa20 | function | option text draw | Draws an option's text (a0 menu, a1 item, a2 option, f12 x, f13 y, f14 0). | Manage Players centred text (MPTXT) |
| 0x15aa84 | function | option text colour call (hook site) | Call to option text colour inside the option text draw. | Manage Players (MPTCOL) |
| 0x15ac68 | function | option arrows draw | Draws an option's arrows (s1 = item), placed from its end (+0xdc). | Manage Players rows |
| 0x15ad7c | function | option arrows end (hook site) | Arrow draw loads the option end (lwc1 f0,220(s1)). | Manage Players (MPADC) |
| 0x15ade0 | function | option arrows text width (hook site) | Arrow draw's jal to text width. | Manage Players (MPATW) |
| 0x15aebc | function | option text draw call (hook site) | Call to the option text draw. | Manage Players (MPTXT) |
| 0x1620b0 | function | icon height | Returns an icon's height (a0 icon). | Team icons |
| 0x162100 | function | draw icon | Draws an icon (a0 icon, a1 colour, x, y). | Team icons |
| 0x16ed18 | function | room trace | Finds the room along a way from a point (room trace). | Spectate camera |
| 0x16f360 | function | camera collision test | The game's camera test along a way (t3 = -7: all but rooms and doors left out). | Spectate camera |
| 0x185d78 | function | pad number | Returns a pad number / index for a level pad (-1 = none). | Switch Spawns, Coin Rush, Spawn Rule |
| 0x185e20 | function | pad from big index | Pad lookup used for large pad numbers when scoring spawn candidates. | Spawn Rule |
| 0x185f38 | function | pad pointer | Pad from number (a0) -> v0 (0 = not a pad in use). | Gun Game drops, armouries, King of the Hill, Spawn Rule |
| 0x188c10 | function | closest pad | Closest pad (a0 pos, f12 min distance) -> v0 pad. | Gun Game drops, Player Drops Gun |
| 0x18f328 | function | free prop | Frees a prop (a0), as the game's own collect frees a taken pickup. | Gun Game hand-outs |
| 0x1af484 | function | One Shot Kill check (hook site) | Damage code loads the game flags for the One Shot Kill test. | Showdown one-hit kills (SDOS) |
| 0x1af538 | function | hit slowdown (hook site) | Hit slowdown jal; the mod's hook (to 0xFE3E4) spares burning characters offline in Flame Tag only. | Flame Tag (offline only) |
| 0x1b04fc | function | Thief death coin (hook site) | Kill code's jal that spawns the victim's coin. | Coin Rush / Coin Drop (CDK) |
| 0x1b18d0 | function | damage routine | The game's damage routine (a0 = the hit). | Player Health (PHDA) |
| 0x1b18d8 | function | damage routine (resume) | Resume point after the Player Health hook. | Player Health |
| 0x1b1968 | function | damage hit report (hook site) | Damage routine's jal that sends the hit report. | Player Health (PHNH) |
| 0x1b6000 | function | show pickup | Makes a pickup come back. | Gun Game / Showdown pickups never return (GGVIS) |
| 0x1b6008 | function | show pickup (resume) | Resume point after the hook. | Gun Game |
| 0x1b6a80 | function | pickup taken | Marks a pickup prop as taken. | Gun Game hand-outs, armouries |
| 0x1b79d8 | function | bag pickup handler | Bag pickup handler. | Project notes (bag modes) |
| 0x1b7a58 | function | bag touched, no bag (hook site) | Bag touched by a chr with no bag. | Wrong Way Bag (WWA) |
| 0x1b7a68 | function | bag pick up | Picks up the touched bag (t7 = 2). | Wrong Way Bag |
| 0x1b7c88 | function | own bag touched | Returns a dropped own bag / nothing. | Wrong Way Bag |
| 0x1b80b0 | function | base handler | Bag base handler. | Project notes (bag modes) |
| 0x1b8118 | function | zone beam code | Zone code words restored after zone beams were removed (sllv / sw). | King of the Hill (removed zone beams) |
| 0x1b815c | function | base touch: nothing | Base touch path that does nothing (v0 = 0). | Wrong Way Bag |
| 0x1b81b4 | function | base touched carrying bag (hook site) | Base touched while carrying a bag. | Wrong Way Bag (WWC) |
| 0x1b81c4 | function | capture check | Own-base capture check. | Wrong Way Bag |
| 0x1b81d0 | function | capture check past home test | Capture check after the "your bag must be home" test. | Wrong Way Bag, Bag Must Be Home |
| 0x1b83d8 | function | chr picks up pickup | A chr picks up a pickup, the game's own path (a0 pickup, a1 chr prop). | Gun Game hand-outs |
| 0x1b857c | function | collect pickup | The game's own collect. | Referenced for FREEPROP use |
| 0x1b9120 | function | capture | Bag capture code. | Project notes (bag modes) |
| 0x1b9194 | function | bag capture check (hook site) | Capture: base must be own; own bag carried returns it, else score. | Wrong Way Bag (WWD) |
| 0x1b91b0 | function | bag capture score | Scores a capture. | Wrong Way Bag |
| 0x1b9230 | function | capture message loop (hook site) | Capture message loop (lw t4,28(s2)). | Wrong Way Bag (WWM) |
| 0x1b9238 | function | capture message loop (resume) | Resume point in the capture message loop. | Wrong Way Bag |
| 0x1b9358 | function | capture: wrong base | Capture path for a base that is not the chr's own. | Wrong Way Bag |
| 0x1b9424 | function | return carried own bag | Returns the carried own bag. | Wrong Way Bag |
| 0x1b9b18 | function | prop placing routine | Puts / drops a prop (prop, chr, chr gun); the zone drops use it with the forced pad 0x6E6494. | Gun Game drops, King of the Hill, Player Drops Gun |
| 0x1c0ef8 | function | set view camera | Sets a view's camera (a0 view, a1 mode: 1 death view, 0 first person, a2 prop). | Spectate |
| 0x1c1814 | function | camera code (continue) | Rest of the game's camera code after the mod sets the spectate look. | Spectate |
| 0x1c2010 | function | first-person camera (hook site) | First-person camera code (s2 = this view's player). | Spectate (SPFP) |
| 0x1c205c | function | first-person camera branch | Camera code word checked before patching. | Spectate |
| 0x1c8160 | function | start pad | Places a player at a spawn point (a0 = player) -> v0 its pick. | Switch Spawns (SWSP) |
| 0x1c81ec | function | start pad net check (hook site) | Start pad's jal to the LAN check (s0 = player). | Spawn Rule (SRP) |
| 0x1c83e8 | function | place own player (hook site) | A console placing its own player (jal start pad). | Switch Spawns (SWSP) |
| 0x1c9594 | function | respawn code (old hook site) | Respawn code words restored after the Gun Game respawn hook moved. | Gun Game respawn (GGPR) |
| 0x1c95a4 | function | respawn can-respawn test (hook site) | Respawn's "can it respawn" test. | Gun Game weapon on respawn (GGPR) |
| 0x1c95ac | function | respawn (resume) | Resume point after the test. | Gun Game |
| 0x1c9950 | function | respawn bail | Respawn path when the player cannot respawn. | Gun Game |
| 0x1cc2a0 | function | death spawn pick | The game's death spawn pick, which sends it to the player's console (a0 = player). | Spawn Rule re-pick (LAN host) |
| 0x1cc378 | function | host spawn pick (hook site) | The host's pick for a player (jal start pad). | Switch Spawns (SWSP) |
| 0x1cc768 | function | at death (hook site) | Point at a death (t6 = player). | Respawn Delay (PRDT) |
| 0x1ce4d8 | function | gondola code (old hook) | Words restored after the removed Venice gondola hooks (v5.45-v5.47). | Removed gondola sync |
| 0x1d4ddc | function | death drop (hook site) | Death drop jal to prop placing routine. | Player Drops Gun / Gun Game (GGPD) |
| 0x1d4e34 | function | death drop 2 (hook site) | Second death drop jal. | Player Drops Gun / Gun Game (GGPD) |
| 0x21e2e8 | function | all emitters off | Turns every flame (particle emitter) of a prop off (a0 = prop). | King of the Hill zone flames |
| 0x232798 | function | set-on-fire routine | Sets a chr alight. | Infection: no spreading by touch |
| 0x2327a0 | function | set-on-fire routine (resume) | Resume point after the hook. | Infection |
| 0x248cc0 | function | HUD message | Shows a HUD message (type 4 = centre main message). | Overtime, Setbacks, King of the Hill, Multikill |
| 0x2491e0 | function | HUD kill message entry | Adds a kill-message style HUD entry (text, then name in team colour). | Spectate "Spectating <name>" |
| 0x249238 | function | kill message made (hook site) | Kill message entry stores the chr id (sw s2,360(s1)). | Kill messages keep the victim's colour (KMC) |
| 0x2492e8 | function | kill message made 2 (hook site) | The other kill message adder (type 12). | Kill messages (KMC) |
| 0x24a610 | function | kill message draw | Draws kill messages, colouring the name from the chr's team every frame. | Kill messages keep the victim's colour |
| 0x24a84c | function | kill message team read (hook site) | Draw reads the chr's team (lw t6,132(s1)). | Kill messages (KMD1) |
| 0x24ab98 | function | kill message team read 2 (hook site) | Second team read (lw t5,132(s1)). | Kill messages (KMD2) |
| 0x24bc00 | function | HUD message draw | The game's HUD message draw (a0 = 0). | Spectate HUD |
| 0x254330 | function | radar | The radar (its zone blips read the zone count at 0x254638 / 0x2546C0). | King of the Hill radar (KHRAD) |
| 0x254638 | function | radar zone count read | Radar reads the zone count. | King of the Hill |
| 0x2546c0 | function | radar zone count read 2 | Radar reads the zone count. | King of the Hill |
| 0x25e174 | function | HUD draw (hook site) | The HUD (s3 = player's HUD, s0 = 11). | Spectate (SPHUD) |
| 0x25e180 | function | HUD draw (resume) | Resume point. | Spectate |
| 0x25e714 | function | radar call (hook site) | HUD call to the radar. | King of the Hill (KHRAD) |
| 0x25eb2c | function | HUD draw skip | HUD path for state 11. | Spectate |
| 0x25ec70 | function | name tags draw call (hook site) | Per-frame call of the name tags draw. | Spectate (HATW) |
| 0x262048 | function | name tags draw | Draws name tags per local player and decides who is in sight. | Spectate (HATW) |
| 0x2620dc | function | name tags Teamplay check | Name tags' Teamplay check (restored to the game's own). | Spectate crash fix |
| 0x262178 | function | name tags team-mate test (hook site) | Name tags team-mate test. | Spectate (HTSK) |
| 0x26219c | function | name tags (continue) | Continue point in the name tags draw. | Spectate |
| 0x262964 | function | name tags skip | Name tags path skipping a chr. | Spectate |
| 0x262974 | function | name tags no Teamplay | Name tags path taken without Teamplay. | Spectate |
| 0x265230 | function | Zones score bar | The Zones score bar (reads the zone count at 0x2652A4 / 0x2654CC / 0x2655A4 / 0x2655C8 / 0x2656B8). | King of the Hill (KHZB) |
| 0x266428 | function | Zones score bar address load (hook site) | Loads the score bar's address (lui / addiu at 0x266428 / 0x266430). | King of the Hill (KHZB) |
| 0x266430 | function | Zones score bar address load 2 (hook site) | Second half of the address load. | King of the Hill (KHZB) |
| 0x277e40 | function | rand | Random number. | Spawn Rule, Random Weapon, Coin Rush, Flame Pass |
| 0x278288 | function | cos | Cosine (f12 -> f0; uses t0-t2, f0-f9). | Spectate camera look |
| 0x2d19d0 | function | screen rectangle call | Takes an integer screen rectangle (a0 left, a1 top, a2 right, a3 bottom); the mod calls it before drawing Manage Players row boxes. | Manage Players rows |
| 0x2d1e90 | function | draw corner-colour quad | Draws a quad with corner colours (f12-f15 rect, then colours). | Manage Players rows |
| 0x2e7a88 | function | take gun | Takes a gun away (a0 chr data, a1 gun id). | Gun Game level change |
| 0x2e7c48 | function | switch gun | Switches to a gun (a0 chr data, a1 gun id). | Gun Game hand-outs, armouries |
| 0x3071d8 | function | local player count | Returns the number of local players. | Manage Players layout, Overtime / King of the Hill messages |
| 0x36f270 | function | gondola code (old hook) 2 | Word restored after the removed Venice gondola hooks. | Removed gondola sync |
| 0x375bf8 | function | complete objective | Completes an Assault objective (f12 = 0.0). | Auto-Complete Phase (Assault) |
| 0x3772fc | function | Assault tick call (hook site) | Objectives update's call to the Assault tick. | Auto-Complete Phase / Time Bonus (ASK) |
| 0x383ee8 | function | current Assault phase | Returns the current Assault phase (v0). | Auto-Complete Phase, Time Bonus |
| 0x384718 | function | Assault spawn re-pick return | Return address of Assault's re-pick of spawn points. | Spawn resends / Respawn Delay |
| 0x384d20 | function | Assault tick | The Assault tick. | Auto-Complete Phase / Time Bonus (ASK) |
| 0x388db0 | function | mode tick | Called from every mode's tick (Mercy Rule's check goes on to it). | Mercy Rule (NCMC) |
| 0x394db0 | function | MapMaker gun item build (hook site) | Level builder reads a MapMaker gun item's "always available" (lw t5,0(s2)). | MapMaker no factories (MMGUN) |
| 0x3d3fa8 | function | bag is home | Returns 1 if the chr's team bag is home. | Wrong Way Bag, Bag Must Be Home |
| 0x3d4160 | function | team bag | Returns a team's bag (a0 = team). | Wrong Way Bag |
| 0x4185ec | function | AI mode-5 check | AI check hard-wired to mode 5. | Project notes (Virus AI) |
| 0x4197e4 | function | bot respawn send (hook site) | Arcade bot respawn's jal to the bot respawn send (a0 = chr record). | Gun Game bot weapons (GGBR) |
| 0x419b3c | function | AI mode-5 check 2 | AI check hard-wired to mode 5. | Project notes (Virus AI) |
| 0x41aaa8 | function | first infected pick | Match-start pick of the first infected player (do not bypass). | Project notes (Virus) |
| 0x41cdf0 | function | AI mode-5 check 3 | AI check hard-wired to mode 5. | Project notes (Virus AI) |
| 0x41f480 | function | spawn pickup prop at pad | Spawns a pickup prop at a pad (a0 prop, a1 pad). | Coin Rush / Coin Drop (CDF), mid-match joiner coins |
| 0x41f668 | function | spawn death pickup | Spawns the victim's Thief death coin (a0 = victim prop). | Coin Rush / Coin Drop (CDK) |
| 0x41f988 | function | remove pickup prop | Removes a pickup prop (a0 chr id, a1 pad). | Coin Rush (CRNR) |
| 0x42bd18 | function | mode team colours | Returns the mode's number of team colours (2 or 4). | Respawn Delay per team |
| 0x42d550 | function | weapon set slot drawing (hook site) | Weapon set page slot drawing call (a0 menu mode, a1 gun id). | Showdown slot greying (SDDRW) |
| 0x42ddf0 | function | weapon set page construct | Weapon set page construct code (checked). | Showdown (SDSLOT) |
| 0x42ddfc | function | weapon set slot add (hook site) | Weapon set page's jal to add its 6 slots. | Showdown (SDSLOT) |
| 0x42e46c | function | weapon picker check (hook site) | Weapon picker's jal to the weapon allowed check. | Gun Game / Showdown weapon bans (GGBAN) |
| 0x43a2e8 | function | match settings refresh: Always Start With Gun (hook site) | Refresh call for item 1. | Gun Game / Random Weapon (GGSGI) |
| 0x43a334 | function | match settings refresh: Friendly Fire (hook site) | Refresh call for item 4. | Friendly Fire greyed (FFI) |
| 0x43a380 | function | match settings refresh: Score Limit (hook site) | Refresh call for item 7. | Gun Game (GGSLI) |
| 0x43a39c | function | match settings refresh: Score Method (hook site) | Refresh call for item 8. | Gun Game / Showdown (GGSMI) |
| 0x43a3b4 | function | match settings refresh: One Shot Kill (hook site) | Refresh call for item 9. | Showdown (SDOSI) |
| 0x43ad2c | function | match settings page top (hook site) | Top of the match settings page (a0 = item flags). | Advanced Settings layout (ADV) |
| 0x43b59c | function | divider before Weapon Set (hook site) | Divider before Weapon Set (a0 = 1). | Advanced Settings link (ADVL) |
| 0x43e39c | function | mode list LAN check (hook site) | Mode list check for context 13. | Mode list: Assault only with an Assault map (LM13) |
| 0x43e3ac | function | mode list LAN branch | Original branch target of the context 13 check. | Mode list |
| 0x43e4d8 | function | mode not listed | Mode list path that leaves the mode out. | Mode list |
| 0x43e520 | function | mode listed | Mode list path that lists the mode. | Mode list |
| 0x43f020 | function | map list mode check (hook site) | Map list check for a map not made for the mode. | Map list: Assault only (MAPA) |
| 0x43f028 | function | map list (resume) | Continue point. | Map list |
| 0x43f128 | function | map list next | Map list next map. | Map list |
| 0x44cbe4 | function | setup builder return (hook site) | Match setup builder's return. | Random Characters (RCEND) |
| 0x44d300 | function | setup builder flags (hook site) | Setup builder's flag call (Infinite Ammo / No Punch). | Advanced Settings flags (IAFLAG) |
| 0x44d8f8 | function | match info copied | Called after the host's match info (45) is copied into the setup. | Setup bytes 64-75 (HPZ2) |
| 0x461df8 | function | in-match menu buttons | Handles a player's buttons while its in-match menu is open (a0 = player). | Spectate |
| 0x4677d4 | function | score text lives check (hook site) | Score text's branch on the match lives. | Showdown shows kills (SDFMT) |
| 0x467844 | function | score text no lives | Score text path for no lives. | Showdown |
| 0x46da4c | function | pause menu code (old hook) | Word restored after Return to Lobby was removed on PS2. | Return to Lobby (removed on PS2) |
| 0x46de20 | function | confirm page title call (hook site) | Confirm page title text. | Manage Players kick (MPTT) |
| 0x46de60 | function | confirm page question call (hook site) | Confirm page question text. | Manage Players kick (MPTB) |
| 0x46df38 | function | open confirm page | Opens the confirm page (a0 title text, a1 1, a2 Yes callback, a3 No 0x46E050, t0 0). | Manage Players kick |
| 0x46e050 | function | confirm page No | Back to the previous page as the page's No does (a0 kept). | Manage Players kick |
| 0x46e7e0 | function | open Players page | How the game opens its in-match Players page. | Manage Players (model) |
| 0x46ecb4 | function | pause Options before Leave Match (hook site) | Options tab's network game flag call just before Leave Match (s2 = page). | Manage Players item (MPOP) |
| 0x46ecd0 | function | pause Options text call | Text call in the Options tab (checked). | Manage Players |
| 0x46ecf8 | function | pause menu code (old hook) 2 | Word restored after Return to Lobby was removed on PS2. | Return to Lobby (removed on PS2) |
| 0x471c5c | function | Select Team second A (hook site) | Select Team reads the pad for the second A press. | LAN host auto ready (HBTN) |
| 0x473f08 | function | Players page back | The Players page's back. | Manage Players back (model) |
| 0x474010 | function | in-match Players page builder | The game's in-match Players page builder. | Manage Players layout (model) |
| 0x47477c | function | in-match page heading | In-match pages' heading code. | Manage Players heading (model) |
| 0x475028 | function | Scores page player rows (hook site) | Scores page player rows. | Team Elimination / Team Vampire (PERS) |
| 0x475038 | function | Scores rows Team Deathmatch number | Shows the Team Deathmatch number (kills of other teams). | Deathmatch with Teamplay (PERS) |
| 0x4750e8 | function | Scores rows lives / time | Shows "N Lives" or the time. | Team Elimination / Team Vampire |
| 0x475424 | function | Scores team row call (hook site) | Scores page team rows' Bag Tag team row call. | Team Elimination / Vampire team time (PSTSC) |
| 0x47759c | function | pause menu code (old hook) 3 | Word restored after Return to Lobby was removed on PS2. | Return to Lobby (removed on PS2) |
| 0x47f8b8 | function | MapMaker map-full flag | MapMaker code that sets the map-full flag (patched never to set it). | MapMaker no map size limit |
| 0x489b20 | function | MapMaker count links | Counts a tile's links (a0 tile). | MapMaker maps on LAN |
| 0x4c7eb0 | function | MapMaker count plugs | Counts a tile's plugs (a0 tile). | MapMaker maps on LAN |
| 0x4f08d0 | function | client name | Returns a player's name (a0). | Manage Players rows |
| 0x4f12bc | function | scores-to-clients timer (hook site) | Host scores-to-clients timer (lw FPS / slt). | Flame Tag score sync (SCTIM) |
| 0x4f2fc4 | function | joiner start send | Mid-match joiner start code (checked). | Showdown joiner (NW59) |
| 0x4f2fe4 | function | joiner start send (hook site) | The other mid-match joiner's start (j NSEND). | Showdown empty weapon set (NW59) |
| 0x4f326c | function | match info 44 copied (hook site) | Host's match info 44 just copied into the setup. | Setup bytes 64-75 (HPZ1) |
| 0x4f33b0 | function | match info 45 copied (hook site) | Match info 45 copied. | Setup bytes 64-75 (HPZ2) |
| 0x4f33b8 | function | match info copied (continue) | Continue point after the match info copies. | HPZ3 |
| 0x4f3458 | function | match info 59 copied (hook site) | Match info 59 copied. | Setup bytes 64-75 (HPZ3) |
| 0x4f3470 | function | SEND | Sends data (a0 client, 0 = every player; a1 type, a2 data, a3 size, t0 reliable). | Match info sends, MapMaker, weapon switch |
| 0x4f3d30 | function | SENDTO | Sends a packet to a client (a0 client, a1 type, a2 packet with 8-byte header, a3 size, t0 reliable, t1 in game). | Gun Game joiner, armouries, Coin Rush, weapon switch |
| 0x4f3fd0 | function | game message send routine | Sends a game packet (a0 from client, a1 type, a2 buffer with 8-byte header, a3 size, t0 guaranteed, t1 in game). | Armouries, Gun Game drops, Wrong Way Bag |
| 0x4f4130 | function | send packet from client | Sends a packet from this console's client. | Showdown kills, Player Health, Manage Players |
| 0x4f462c | function | packet decode not-in-match (hook site) | Packet decode's "not in the match" test. | Weapon switch prefs kept (PFGATE) |
| 0x4f4634 | function | packet decode (in match) | Continue point when in the match. | PFGATE |
| 0x4f4664 | function | packet decode skip | Path where a packet is thrown away. | PFGATE |
| 0x4f4910 | function | packet 15 received (hook site) | Packet 15 received: jal to read prefs. | Weapon switch prefs kept (PFRCV) |
| 0x4f5550 | function | is network game | Returns network game flag (the LAN check). | Spawn Rule (SRP), Manage Players (MPOP) |
| 0x4f5858 | function | host check | Is LAN host. | Most host-decided features |
| 0x4f61c4 | function | send tile set | MapMaker tile set send code (checked). | MapMaker maps on LAN |
| 0x4f61e8 | function | send tile set tail (hook site) | Tile set send's tail jump to SEND (a0 client, a1 48, a2 map, a3 0x8000, t0 1). | MapMaker no factories (MMSEND) |
| 0x4f6314 | function | joiner start send | Mid-match joiner start code (checked). | Showdown joiner |
| 0x4f6324 | function | joiner match info send (hook site) | Mid-match joiner's start: SEND (client, 59, SINFO, 312, 1). | Showdown empty weapon set (NW59) |
| 0x4f64b8 | function | match start send | Match start code (checked). | Showdown |
| 0x4f64dc | function | match start send (hook site) | End of match start: SEND (0, 45, SINFO, 312, 1). | Showdown only slot 1 (NW45) |
| 0x4f6c18 | function | is connected | Is a player connected (a0 = player). | Weapon switch, King of the Hill, Manage Players, Showdown |
| 0x4f8254 | function | score sync write (hook site) | LAN host's score sync stores the rank score it sends. | Showdown players out (SDSS) |
| 0x4f88c0 | function | ready start | Returns 1 once every player has loaded (offline: always). | Gun Game start, start of a match |
| 0x4f8960 | function | ready start code | Ready start words restored (the game's own 5-second limit). | Start of a match |
| 0x4f8aa8 | function | forced pad given | Called for another console's player at a respawn to tell if a forced pad was given. | Spawn Rule |
| 0x4f9168 | function | Thief collect message (hook site) | Read collect's jal to remove pickup prop. | Coin Rush (CRNR) |
| 0x4f92c8 | function | coin message receive | Coin message (type 35) receive. | Setbacks signal (SBRX) |
| 0x4f9320 | function | coin message own player (hook site) | Coin message arriving (t7 = the player's local number). | Setbacks (SBRX) |
| 0x4f9328 | function | coin message (resume) | Resume point. | Setbacks |
| 0x4f933c | function | death coin arriving (hook site) | A LAN player's death coin arriving. | Coin Rush / Coin Drop (CDF) |
| 0x4f9348 | function | coin message (continue) | Continue point after the coin message. | Setbacks |
| 0x4f9418 | function | damage report decode (hook site) | Damage report decode at the amount. | Player Health (PHRX) |
| 0x4f9728 | function | send hit report | Sends a hit this console decides. | Player Health |
| 0x4fa898 | function | send kill message (hook site) | Kill sender's jal to send if local. | Showdown / Player Health (SDKL) |
| 0x4fa8d8 | function | team message receive | Applies a team message on this console (a1 = data after the 8-byte header, a2 = size, a3 = type); also sends the spawn point. | Manage Players moves (MPMOVE) |
| 0x4fa95c | function | team write (hook site) | Team message writes the chr's team (sw t3,132(t1)). | Manage Players kill banking (MPTW1) |
| 0x4fa9f0 | function | spawn request handler return | Return address of send spawn pad from the spawn request handler. | Gun Game resends after first spawn request |
| 0x4faf18 | function | bot respawn send | Arcade bot respawn send (a0 = chr record). | Gun Game bot weapons |
| 0x4fb328 | function | pickup message send | Sends "picked up" for a pickup (a0 pickup, a1 chr prop). | Gun Game hand-outs, Wrong Way Bag replays |
| 0x4fb5f8 | function | read drop message | Runs a drop message on this console (a0 = message: kind, network setup value, ...). | Gun Game drops on pads |
| 0x4fb93c | function | read drop message (continue) | Continue point in the drop message handler. | Armouries (LKDEC) |
| 0x4fb980 | function | drop message other branch (hook site) | DROPMSG_OTHER branch's jal to the LAN entity lookup. | Armouries (LKDEC) |
| 0x4fc7a4 | function | state packet team write (hook site) | State packet writes the team (sw t5,132(s6)). | Manage Players (MPTW2) |
| 0x4fc884 | function | gondola code (old hook) 3 | Word restored after the removed Venice gondola hooks. | Removed gondola sync |
| 0x4fcae0 | function | dead player spawn resend (hook site) | Host's 1.5 s resend of a dead LAN player's spawn point. | Spawn Rule (SRRS) |
| 0x4fe738 | function | read prefs | Reads a player's prefs from packet 15 (a0 = slot byte, then 128 bytes). | Weapon switch for unpatched players |
| 0x4fea70 | function | send all prefs | Sends every prefs to a client: first host step for a joiner. | Gun Game joiner |
| 0x4fed90 | function | send restarting | Restart / rematch send. | Showdown slot-1 set again (NWRS1) |
| 0x4fed98 | function | send restarting (resume) | Resume point after the hook. | NWRS1 |
| 0x4fee20 | function | send if local | Sends a message if the prop is this console's. | Showdown kills, Player Health |
| 0x4ff4a0 | function | leaver loop same-team skip (hook site) | Leaver loop's same-team skip. | Manage Players kill banking (MPLVS) |
| 0x4ff4cc | function | leaver loop next | Leaver loop past its body. | Manage Players |
| 0x4ff770 | function | return to lobby | The game's own return to the lobby (as packet 11 runs it). | Notes (no Return to Lobby on PS2) |
| 0x4ff858 | function | LAN entity lookup | Prop from a network setup value (a0) -> v0, 0 = none (leaf: t4-t7). | Armouries |
| 0x4ffe20 | function | bag sync decode | Bag sync decode. | Project notes (bag modes) |
| 0x500130 | function | joiner lives | Fewest lives left of the other players, given to a joiner (a0 client). | Showdown (SDMIN) |
| 0x50024c | function | greet joiner (hook site) | Host greets a mid-match joiner (jal send all prefs). | Gun Game / King of the Hill joiner (GGJOIN) |
| 0x500294 | function | joiner lives call (hook site) | Call to the joiner lives function. | Showdown (SDMIN) |
| 0x500338 | function | bag sync send | Bag sync send. | Project notes (bag modes) |
| 0x500d88 | function | zone beam code 2 | Word restored after zone beams were removed. | King of the Hill |
| 0x500dc0 | function | send spawn pad | Sends a player's spawn pad and the zone owners. | Spawn Rule, King of the Hill, start of match |
| 0x500dd4 | function | send spawn pad host check (hook site) | Host check inside send spawn pad. | Start of a match (LRDYSP) |
| 0x506de0 | function | kick player | Called with a player's number to carry out a kick. | Manage Players kick |
| 0x53f2d8 | function | map-send reset | The map-send screen sender's reset. | MapMaker maps on LAN (MMPREP) |
| 0x5418b8 | function | Players row draw | The game's Players row draw. | Manage Players rows (model) |
| 0x552538 | function | map-send screen start (hook site) | Start of the map-send screen. | MapMaker (MMPREP) |
| 0x5d9a18 | function | format text | Formats text (a0 buffer, a1 format, a2, a3 values), sprintf style. | Team Elimination / Vampire team time text |
| 0x615dd8 / PAL 0x615ed8 | data | font height | Option font height (float). | Manage Players rows |
| 0x627e38 / PAL 0x627f38 | data | team scores | The game's team scores (index team - 1). | Team Elimination / Team Lives |
| 0x628294 / PAL 0x628394 | data | team colours | Team colour table. | Manage Players |
| 0x6283dc / PAL 0x6284dc | data | mode table team game | Mode table (32 per mode) team game: 0 none, 1 teams, 2 optional. | Advanced Settings hide, Spawn Rule |
| 0x6284a0 / PAL 0x6285a0 | data | mode table Bag Tag team spawns | Bag Tag entry: team spawn points used (patched to 1). | Team Bag Tag spawns |
| 0x6284bc / PAL 0x6285bc | data | mode table Elimination teams | Elimination entry: Teamplay possible (2). | Team Elimination |
| 0x6284c0 / PAL 0x6285c0 | data | mode table Elimination team spawns | Elimination entry: team spawn points (1). | Team Elimination |
| 0x6284e0 / PAL 0x6285e0 | data | mode table Shrink team spawns | Shrink entry: team spawn points (already 1). | Notes |
| 0x6284fc / PAL 0x6285fc | data | mode table Vampire teams | Vampire entry: Teamplay possible (2). | Team Vampire |
| 0x628500 / PAL 0x628600 | data | mode table Vampire team spawns | Vampire entry: team spawn points (1). | Team Vampire |
| 0x628520 / PAL 0x628620 | data | mode table Thief team spawns | Thief entry: team spawn points (already 1). | Notes |
| 0x628e50 / PAL 0x628f50 | data | match parms | Match parameters (setup byte N = 0x628E58 + (N-64)); +77 game type, +78 mode. | Setup data path, most features |
| 0x628e53 / PAL 0x628f53 | data | match team count | Match setup byte 59: the match's team colours (at most 4). | Manage Players |
| 0x628e58 / PAL 0x628f58 | data | match setup byte 64 | Match setup bytes from 64 (the host's mod settings, cleared until the host is known to be patched). | Host-has-patch setup bytes |
| 0x628e60 / PAL 0x628f60 | data | match setup byte 72 | Setup byte 72 (0xB0 \| Spawn Rule \| Overtime \| Gun Game marker bits). | Armouries, Spawn Rule, Gun Game |
| 0x628e63 / PAL 0x628f63 | data | match setup byte 75 | Setup byte 75: the host's disabled team colours under its 0xA0 marker. | Disabled teams (team settings) |
| 0x628e9d / PAL 0x628f9d | data | game type byte | Match game type (+77). | Most mode-dependent features |
| 0x628e9e / PAL 0x628f9e | data | mode byte | Match mode (+78). | Most mode-dependent features |
| 0x628ea0 / PAL 0x628fa0 | data | match flags | Match game flags (bit 0 = teams on). | Manage Players, Teamplay checks |
| 0x628ef0 / PAL 0x628ff0 | data | next match setup byte 64 | The next match's setup bytes from 64. | Host-has-patch setup bytes |
| 0x628f80 / PAL 0x629080 | data | gameframe | Gameframe counter. | Timers |
| 0x628f8c / PAL 0x62908c | data | game state | Game state (7 = in the level, every player loaded). | Armouries, Coin Rush, Gun Game, Spawn Rule |
| 0x643670 / PAL 0x643770 | data | menu player index | Index of the player whose menu is open (into the menu contexts). | Manage Players back |
| 0x643674 / PAL 0x643774 | data | current menu | Current menu pointer (+88 content height, +372 items). | Advanced Settings, Manage Players |
| 0x643e1c / PAL 0x643f1c | data | construct state | Menu construct pointer (+60 scroll height). | Advanced Settings layout |
| 0x643e24 / PAL 0x643f24 | data | last menu item made | The last menu item made. | Advanced Settings one-page list |
| 0x643e30 / PAL 0x643f30 | data | scrolled part | Scrolled part state (+84 / +88 first / last item). | Advanced Settings one-page list |
| 0x645104 / PAL 0x645204 | data | canvas factor | Menu units to pixels factor. | Manage Players rows |
| 0x64a188 / PAL 0x64a288 | data | level pads pointer | Pointer to the level's pads (32 bytes: +4 flags, +0xC position). | Armouries |
| 0x64a190 / PAL 0x64a290 | data | placement pads pointer | Pointer to the placement pads. | Armouries |
| 0x64a1c4 / PAL 0x64a2c4 | data | pad count | Number of level pads. | Armouries |
| 0x64a1cc / PAL 0x64a2cc | data | placement pad count | Number of placement pads. | Armouries |
| 0x64a4d4 / PAL 0x64a5d4 | data | level props pointer | Pointer to level props (768 each: +0x20 type, +0x28 flags, +0x7C ...). | Armouries |
| 0x64aeb4 / PAL 0x64afb4 | data | prop count | Number of level props. | Armouries |
| 0x6515b8 / PAL 0x6516b8 | data | dropped pickup data | Dropped pickups' data (216 each, +0 prop). | Gun Game drops |
| 0x652f08 / PAL 0x653008 | data | dropped pickup slots | 30 dropped pickup slots in use (word each). | Gun Game drops, Coin Rush |
| 0x652f80 / PAL 0x653080 | data | dropped pickup times | Gameframe each slot was filled at. | Gun Game drops |
| 0x653aac / PAL 0x653bac | data | PLAYERS | Players pointer (stride 5168: +0 num, +4 local number). | Manage Players, Spectate, Spawn Rule |
| 0x653ab0 / PAL 0x653bb0 | data | local player | Local player pointer the name tags draw uses each frame. | Spectate |
| 0x653b00 / PAL 0x653c00 | data | chr records pointer | Pointer to chr 0's record (characters follow). | Manage Players kill banking |
| 0x662908 / PAL 0x662a08 | data | HUD message rings | HUD message rings (6012 per local player: +48 next, +56 16 entries of 364). | Spectate |
| 0x669388 / PAL 0x669488 | data | frame ticks | This tick's frames (0 while paused), divided by FPS for the frame time. | Spectate camera |
| 0x66b940 / PAL 0x66ba40 | data | zone count | Number of zones (max 20). | King of the Hill |
| 0x66b95c / PAL 0x66ba5c | data | Assault phase list | The Assault phase list. | Auto-Complete Phase, Time Bonus |
| 0x66b96c / PAL 0x66ba6c | data | flame status | Infected / burning bitmask by chr id. | Flame Pass, Infection |
| 0x66ba00 / PAL 0x66bb00 | data | bot count | Number of non-player characters (added to NPLAYERS for all characters). | Manage Players |
| 0x66bcb8 / PAL 0x66bdb8 | data | zone list | Zone list (8 bytes each: +0 pad, +4 prop). | King of the Hill |
| 0x66eba8 / PAL 0x66eca8 | data | FPS | Frames per second (int). | Timers |
| 0x682f2c / PAL 0x68302c | data | gun info table pointer | Pointer to the gun info table (668 per gun type; +20 main ammo type). | Gun Game ammo |
| 0x6834a8 / PAL 0x6835a8 | data | gun id table | gun id table (60 each, +16 gun type). | Gun Game / Showdown |
| 0x687670 / PAL 0x687770 | data | current level | The level (0x65 = front end). | Advanced Settings custom-match gate |
| 0x687674 / PAL 0x687774 | data | NPLAYERS | Number of players. | Many features |
| 0x6b0f50 / PAL 0x6b1050 | data | coin pickup count | Number of coin pickups. | Coin Rush / Coin Drop |
| 0x6b1fc0 / PAL 0x6b20c0 | data | character select table | 150-character select list (48 bytes each: +1 head, +4 character type). | Random Characters |
| 0x6b4d80 / PAL 0x6b4e80 | data | setup | The match setup (parms the builder writes). | Gun Game setup (GGSET), setup data path |
| 0x6b4db8 / PAL 0x6b4eb8 | data | setup menu parms | Setup part copied into SINFO+4 (character types +20, character heads +62). | Random Characters |
| 0x6b4e06 / PAL 0x6b4f06 | data | menu modifier byte | Menu modifier byte. | Project notes |
| 0x6b6bb8 / PAL 0x6b6cb8 | data | pause block word | Cleared by the confirm page's No. | Manage Players kick |
| 0x6bb528 / PAL 0x6bb628 | data | MapMaker tiles | MapMaker tiles (0x140 each). | MapMaker maps on LAN |
| 0x6c3eac / PAL 0x6c3fac | data | MapMaker map buffer pointer | Pointer to the MapMaker map temp buffer (32 KB). | MapMaker maps on LAN |
| 0x6e3d24 / PAL 0x6e3e24 | data | network game flag | Network game word. | Most host-decided features |
| 0x6e3d2c / PAL 0x6e3e2c | data | in-game traffic flag | Set while this console is in the match; packet 15 is dropped before. | Weapon switch prefs |
| 0x6e3ea0 / PAL 0x6e3fa0 | data | gone online flag | 1 once the game has gone online. | Manage Players |
| 0x6e41b0 / PAL 0x6e42b0 | data | network clients | The game's 8 network clients (0x30C each: +0 id, +0x1C state, +0x20 players). | Player Drops Gun, Team Elimination |
| 0x6e5a10 / PAL 0x6e5b10 | data | network player table | LAN players (296 each, 8: +4 owner client, +76 flags). | Weapon switch, Manage Players |
| 0x6e5a14 / PAL 0x6e5b14 | data | network player table owner | network player table +4: owner client. | Armouries, Coin Rush, Setbacks |
| 0x6e6350 / PAL 0x6e6450 | data | OWNCLIENT | This console's own client. | Packet sends |
| 0x6e6358 / PAL 0x6e6458 | data | HOSTINFO / SINFO | Host's match info (312 bytes): +0x14 setup byte 72, +0x50 level, +0x95 match number, +0xA4 weapon slots, +0x130 host-in-level. | Gun Game, Showdown, Manage Players |
| 0x6e6494 / PAL 0x6e6594 | data | forced drop pad | prop placing routine's forced pad (-1 = none). | King of the Hill zone drops |
| 0x74e4ec / PAL 0x74e5ec | data | menu text margins | Text margins the title sets for the Advanced items. | Advanced Settings layout |
| 0x74e4f0 / PAL 0x74e5f0 | data | menu item flags | Item flags the title sets for the Advanced items. | Advanced Settings layout |
| 0x7bb3d8 | data | spawn candidate list | spawn point picker's candidate list. | Spawn Rule |
| 0x82bb00 | data | pickup props | Coin pickup props. | Coin Rush / Coin Drop |
| 0x82bb78 | data | pickup pads | Coin pickup pads. | Coin Rush / Coin Drop |
| 0x82e9d0 | data | menu contexts | Menu context per player. | Manage Players |
| 0x82ea54 | data | confirm Yes callback | The confirm page's Yes callback. | Manage Players kick |
| 0x836460 | data | host flag | 1 = host. | Manage Players, Team Elimination |
| 0x836470 | data | reported hit flag | 1 while the game takes a reported hit. | Player Health |
| 0x836478 | data | pickup forced flag | 1 while a pickup another console reported is done here. | Gun Game hand-outs |

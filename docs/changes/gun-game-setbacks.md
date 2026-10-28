# Gun Game: Setbacks

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00046041 | 036041 | 5 | `8b 41 08 a8 20` | `e8 fe 13 8a 00` | sound loader: the Setbacks laugh too \| sound loader decision (call at 0x46041, was call mk.s XMKLD: mov 8(%ecx),%eax; test $0x20,%al): always load the multikill \| sound loader decision (call at 0x46041, replaces mov 8(%ecx),%eax; test $0x20,%al): always load the multikill sound \| sound loader decision (call at 0x46041, was call mk.s XMKLD: mov 8(%ecx),%eax; test $0x20,%al): always load the multikill jingle (3455) and the Setbacks laugh at level start | v5.3 · 2026-10-16 |
| 00354DF1 | 344DF1 | 8 | `bf f8 df 7b 00 50 f3 a5` | `50 e8 46 24 59 00 90 90` | the host's match info into the setup: bytes 64-75 \| the host's match info into the setup (call at 0x354df2 / 0x354ee5 / 0x354f1f, was mov $0x7bdff8,%edi / rep movsl; esi = the \| the host's match info into the setup (call at 0x354df2 / 0x354ee5 / 0x354f1f, was mov $0x7bdff8,%edi / rep movsl; esi = the match info + 4, ecx = 0x28): copied as before, then setup bytes 64-75 cleared, and in the lobby the match's too (until the host says it has the patch, XHPRX); keeps all but esi / edi / ecx (as the copy leaves them) | v5.70 · 2026-10-23 |
| 00354EE5 | 344EE5 | 7 | `bf f8 df 7b 00 f3 a5` | `e8 53 23 59 00 90 90` | cleared until the host says it has the patch \| the host's match info into the setup (call at 0x354df2 / 0x354ee5 / 0x354f1f, was mov $0x7bdff8,%edi / rep movsl; esi = the \| the host's match info into the setup (call at 0x354df2 / 0x354ee5 / 0x354f1f, was mov $0x7bdff8,%edi / rep movsl; esi = the match info + 4, ecx = 0x28): copied as before, then setup bytes 64-75 cleared, and in the lobby the match's too (until the host says it has the patch, XHPRX); keeps all but esi / edi / ecx (as the copy leaves them) | v5.70 · 2026-10-23 |
| 00354F1F | 344F1F | 7 | `bf f8 df 7b 00 f3 a5` | `e8 19 23 59 00 90 90` | the host's match info into the setup (call at 0x354df2 / 0x354ee5 / 0x354f1f, was mov $0x7bdff8,%edi / rep movsl; esi = the \| the host's match info into the setup (call at 0x354df2 / 0x354ee5 / 0x354f1f, was mov $0x7bdff8,%edi / rep movsl; esi = the match info + 4, ecx = 0x28): copied as before, then setup bytes 64-75 cleared, and in the lobby the match's too (until the host says it has the patch, XHPRX); keeps all but esi / edi / ecx (as the copy leaves them) | v5.70 · 2026-10-23 |
| 0035C22F | 34C22F | 16 | `5f 85 db c7 05 60 e3 79 00 01 00 00 00 5b 7d 1c` | `e9 bc b1 58 00 90 90 90 90 90 90 90 90 90 90 90` | coin message: the host's Setbacks message for this game's own player \| coin message arriving (jmp at 0x35c22f, was pop %edi / test %ebx,%ebx / movl $1,0x79e360 / pop %ebx / jge 0x35c25b; ebx = the \| coin message arriving (jmp at 0x35c22f, was pop %edi / test %ebx,%ebx / movl $1,0x79e360 / pop %ebx / jge 0x35c25b; ebx = the player's local number, eax its slot, cx the pad): another game's player's coin as before; for this game's own player (which the game ignores) pad 0xFFFE is the host's Setbacks message: "Humiliation!" (XSBHUM); 0xFF01 .. 0xFF45 Gun Game's hand-out (XGGTELL) | v5.8 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E70E4 | 184 bytes | xbreadfail_sp | ---------------- Setbacks (Advanced Settings, Gun Game: Off / One Kill / One Weapon), decided by the host (offline: this game) A player killed unarmed (a melee hit, bullet type 0, by a killer holding the fists: not a gun melee hit) or by themselves (own weapons, falls, anything that is not another chr) goes back: One Kill = one kill fewer (with none on this weapon: the previous weapon, one kill short of this one); One Weapon = the previous weapon with no kills on it (on the first weapon: its kills go). The level is the Gun Game score everyone sees, and the respawn hands out the level's weapon, so players without the patch get it too. Greyed out, and Off, with a Weapon Mode other than Gun Game. With 1 Kill To Advance One Kill is the same as One Weapon, so it is not offered: scrolling skips it, and a One Kill already chosen shows as One Weapon. XSBK: from XGGK (Gun Game applies, offline / host) after its pushal: 0x24.. = XGGK's registers (0x28 = esi at add-kill routine' entry: the damage info when character death routine counts the kill), 0x44 = add-kill routine' return, 0x48 = killer chr, 0x4c = victim id | v5.13 · 2026-10-16 |
| 008E719C | 161 bytes | xbreadfail_sp | XSBHUM(chr id), cdecl, keeps all: a player set back gets "Humiliation!" (centre text, as the multikill messages) and a laugh on their own screen: on this game when it is one of its own players; a LAN host sends another game's player's game message 35 (the coin message) with that player's own slot and pad 0xFFFE. A game ignores a coin message for its own player, so a game without the patch does nothing with it and a game with the patch (XSBRX) shows it. Bots: nothing | v5.8 · 2026-10-16 |
| 008E723D | 80 bytes | xbreadfail_sp | the host's match info into the setup (call at 0x354df2 / 0x354ee5 / 0x354f1f, was mov $0x7bdff8,%edi / rep movsl; esi = the match info + 4, ecx = 0x28): copied as before, then setup bytes 64-75 cleared, and in the lobby the match's too (until the host says it has the patch, XHPRX); keeps all but esi / edi / ecx (as the copy leaves them) | v5.70 · 2026-10-23 |
| 008E728D | 61 bytes | xbreadfail_sp | ---- A LAN player's game uses the host's team settings, never its own (old header code, base exe): the disabled colours (Select Team 0x11590, the per-player team cycling 0x11302 / 0x11329) and Team Spawns (spawn pick 0x112ea, Switch Spawns) edx = the disabled colours to use: offline / host: this game's (0x83a658); LAN player: the host's (setup byte 75 under its 0xA0 marker), else none; keeps the others (call at 0x11595, was mov 0x83a658,%edx) | v5.70 · 2026-10-23 |
| 008E72CA | 10 bytes | xbreadfail_sp | ebx = the same (call at 0x11305 / 0x1132c, was mov 0x83a658,%ebx); keeps the others | v5.70 · 2026-10-23 |
| 008E72D4 | 37 bytes | xbreadfail_sp | ZF clear when this game's Team Spawns Off applies: offline / host, and it is on (call at 0x112ef, was testb $1,0x83a654; and in XSWSP); keeps all registers | v5.89 · 2026-10-27 |
| 008E72F9 | 72 bytes | xbreadfail_sp | pad 0xFFFD arrived (from XSBRX): on a LAN player's game, the match's bytes 64-75 from the host's match info (SINFO+12); keeps all | v5.70 · 2026-10-23 |
| 008E7341 | 86 bytes | xbreadfail_sp | XHPSEND(ebx = player number), LAN host: pad 0xFFFD to that player's game (another game's player only); keeps all | v5.70 · 2026-10-23 |
| 008E7397 | 65 bytes | xbreadfail_sp | every frame (XGGT), LAN host: once a second, pad 0xFFFD to every other game's player; keeps all | v5.70 · 2026-10-23 |
| 008E73D8 | 4 bytes | xbreadfail_sp | Data: XHPLAST | v5.3 · 2026-10-16 (approx.) |
| 008E73DC | 1 bytes | xbreadfail_sp | (XRDH's own pick under way) | v5.3 · 2026-10-16 (approx.) |
| 008E73DD | 3 bytes | xbreadfail_sp | XENTER: its player is a joiner (for XGGLATE, which keeps it in +1 and clears it) | v5.3 · 2026-10-16 (approx.) |
| 008E73E0 | 16 bytes | xbreadfail_sp | coin message arriving (jmp at 0x35c22f, was pop %edi / test %ebx,%ebx / movl $1,0x79e360 / pop %ebx / jge 0x35c25b; ebx = the | v5.70 · 2026-10-23 |
| 008E73F0 | 84 bytes | xbreadfail_sp | coin message arriving (jmp at 0x35c22f, was pop %edi / test %ebx,%ebx / movl $1,0x79e360 / pop %ebx / jge 0x35c25b; ebx = the player's local number, eax its slot, cx the pad): another game's player's coin as before; for this game's own player (which the game ignores) pad 0xFFFE is the host's Setbacks message: "Humiliation!" (XSBHUM); 0xFF01 .. 0xFF45 Gun Game's hand-out (XGGTELL) | v5.70 · 2026-10-23 |
| 008E7444 | 28 bytes | xbreadfail_sp | sound loader decision (call at 0x46041, was call mk.s XMKLD: mov 8(%ecx),%eax; test $0x20,%al): always load the multikill jingle (3455) and the Setbacks laugh at level start | v5.8 · 2026-10-16 |
| 008E7460 | 17 bytes | xbreadfail_sp | eax = Setbacks (1 One Kill, 2 One Weapon), 0 when Off (ZF set); keeps the others (with 1 Kill To Advance both do the same) | v5.3 · 2026-10-16 |
| 008E7471 | 101 bytes | xbreadfail_sp | refresh (from XGGKR, esi = page): value; Kills To Advance's changefn greys it out with 1 Kill | v5.3 · 2026-10-16 |
| 008E74D6 | 35 bytes | xbreadfail_sp | apply (from XGGKA, esi = page) | v5.3 · 2026-10-16 |
| 008E74F9 | 121 bytes | xbreadfail_sp | XSBGR(page): Setbacks greyed out unless the page's Weapon Mode is Gun Game; with its Kills To Advance at 1 Kill a One Kill choice becomes One Weapon; keeps all | v5.3 · 2026-10-16 |
| 008E7572 | 74 bytes | xbreadfail_sp | Setbacks changefn (menu, item; cdecl): with 1 Kill To Advance One Kill is skipped, on to One Weapon or back to Off, whichever way the player is scrolling; keeps all | v5.3 · 2026-10-16 |
| 008E75BC | 16 bytes | xbreadfail_sp | Kills To Advance changefn (menu, item; cdecl) | v5.70 · 2026-10-23 |
| 008E7A29 | 9 bytes | xbreadfail_sp | Menu / message text "Setbacks" | v5.3 · 2026-10-16 |
| 008E7A32 | 9 bytes | xbreadfail_sp | Menu / message text "One Kill" | v5.3 · 2026-10-16 |
| 008E7A3B | 13 bytes | xbreadfail_sp | Menu / message text "One Weapon" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 004F9320 / PAL 004F93C8 | 05E30009 | 0803B422 | bgezl t7,0x4f9348 | j 0xed088 | Hook: coin message: the host's Setbacks message for this game's own player (was bgezl t7,0x4F9348 / sw zero,25724(s0)) | v5.8 · 2026-10-16 |
| 004F9324 / PAL 004F93CC | AE00647C | 00000000 | sw zero,25724(s0) | nop | Hook: coin message: the host's Setbacks message for this game's own player (was bgezl t7,0x4F9348 / sw zero,25724(s0)) | v5.8 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E705C-000E718F | 77 | SBK: ---------------- Setbacks (Advanced Settings, Gun Game: Off / One Kill / One Weapon), decided by the host (offline: this game) A player killed unarmed (a melee hit, bullet type 0, by a killer holding the fists, gun id 1, or no gun: not a gun melee hit) or by themselves (own weapons, falls, anything that is not another chr) goes back: One Kill = one kill fewer (with none on this weapon: the previous weapon, one kill short of this one); One Weapon = the previous weapon with no kills on it (on the first weapon: its kills go). The level is the Gun Game score everyone sees, and the respawn hands out the level's weapon, so players without the patch get it too. Greyed out, and Off, with a Weapon Mode other than Gun Game. With 1 Kill To Advance One Kill is the same as One Weapon, so it is not offered: scrolling skips it, and a One Kill already chosen shows as One Weapon. Port of the Xbox version (gg.s XSB*). jal from GGK at add-kill routine' hook (s0 = killer chr or 0, s1 = the caller's s1: character death routine's damage info, s2 = victim id; add-kill routine' return address at 48 in its frame = 64(sp) here); uses t0-t9, v0, v1 | v5.13 · 2026-10-16 |
| 000E8508-000E8607 | 64 | SBHUM: a0 = chr id: a player set back gets "Humiliation!" (centre text, as the multikill messages) and a laugh on their own screen: on this game when it is one of its own players; a LAN host sends another game's player's game message | v5.8 · 2026-10-16 |
| 000EAC9C-000EAD53 | 46 | SBGR: a0 = page: Setbacks greyed out unless the page's Weapon Mode is Gun Game (option 1: the item is only there when it can be played); with Kills To Advance at 1 Kill (option 0) a One Kill choice becomes One Weapon | v5.3 · 2026-10-16 |
| 000EAD54-000EAE07 | 45 | SBREF: a0 = page, a1 = 0 refresh / 1 apply (tail of GGKREF): Setbacks value; refresh also makes Kills To Advance grey it out with 1 Kill, and greys it now | v5.3 · 2026-10-16 |
| 000ED088-000ED103 | 31 | SBRX: coin message arriving (j at 0x4F9320, was bgezl t7,0x4F9348 / sw zero,25724(s0); t7 = the player's local number, t3 its slot, a1 the pad): another game's player's coin as before; for this game's own player (which the game | v5.70 · 2026-10-23 |
| 000EDC80-000EDCEB | 27 | SBCH: Setbacks changefn (a0 = page, a1 = item): with 1 Kill To Advance One Kill is skipped, on to One Weapon or back to Off, whichever way the player is scrolling | v5.3 · 2026-10-16 |
| 000EFF08-000EFF2B | 9 | SNDLD: sound loader decision (j from 0x1123D8, was j mk.py's MKLD; a0 = sound id, t7 = table entry): always load the multikill jingle (3455) and the Setbacks laugh at level start | v5.8 · 2026-10-16 |
| 000F0294-000F02A3 | 4 | LHUM: text | v5.8 · 2026-10-16 |
| 000F03F8-000F0403 | 3 | LSB: text | v5.3 · 2026-10-16 (approx.) |
| 000F0404-000F040F | 3 | LSB1: text | v5.3 · 2026-10-16 (approx.) |
| 000F0410-000F041B | 3 | LSB2: text | v5.3 · 2026-10-16 |
| 000F0424-000F042B | 2 | SBKCH: Kills To Advance changefn (a0 = page, a1 = item) | v5.3 · 2026-10-16 (approx.) |

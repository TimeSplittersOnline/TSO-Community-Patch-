# Advanced Settings menu & shared hooks (used by several features)

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00068C2F | 058C2F | 5 | `e8 bc c5 ff ff` | `e8 0d 0c 88 00` | every frame (via 0x8e9841, call at 0x68c2f): then the Team VIP timer, which goes on to the game's own tick \| Team VIP timer: per frame (call at 0x68c2f via 0x8e9841, replaces call 0x651f0; its argument is already pushed). | v5.3 · 2026-10-16 |
| 00068E27 | 058E27 | 5 | `a1 58 d2 82 00` | `e8 27 59 86 00` | Zones' last score at time up (ze.s XZEND): the call goes through XZENC first, so it only happens in custom arcade matches and on LAN (not Story, Arcade League or Challenges). | v5.3 · 2026-10-16 |
| 002C7832 | 2B7832 | 5 | `e8 69 ae da ff` | `e8 c9 97 d4 ff` | Match settings page: after the game's item-flags call, run the mod's page code (0x8E8BA3) through header code 0x11000. | v5.3 · 2026-10-16 |
| 002C7C3A | 2B7C3A | 2 | `75 4e` | `eb 4e` | Match settings page: the extra text line (game text 0x3BE) that the original added for some modes is always skipped, making room for the Advanced Settings link. (Reason inferred from the code; not written down at the time.) | v5.3 · 2026-10-16 |
| 002C7F6F | 2B7F6F | 5 | `e8 ec 21 db ff` | `e8 dd 9d d4 ff` | XADVL (call at 0x2c7f6f, was call 0x7a160 with arg 1: the divider before Weapon Set): "Advanced Settings" as the first big link, just above Weapon Set \| XADVL (call at 0x2c7f6f, was call 0x7a160 with arg 1: the divider before Weapon Set): "Advanced Settings" as the first big link, just above Weapon Set | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 00011000 | 18 bytes | XBE header | Wrapper (called from 0x2C7832): the game's item-flags call 0x726A0, then the mod's page code 0x8E8BA3. | v5.3 · 2026-10-16 |
| 00011030 | 942 bytes | XBE header | Menu helpers: add a text line / an On-Off option list to a menu page. | v5.70 · 2026-10-23 |
| 00011505 | 21 bytes | XBE header | XFL (jmp at 0x116b5, end of our pages' title line): items use the match settings page's flags (small font, upper case) | v5.3 · 2026-10-16 |
| 00011680 | 292 bytes | XBE header | Advanced Settings pages: title line and item layout. | v5.3 · 2026-10-16 |
| 00011B46 | 250 bytes | XBE header | Code: _start (see the code shown) | v5.3 · 2026-10-16 |
| 00011C40 | 33 bytes | XBE header | eax = 1 if the menu mode can have teams (mode table team game, or Gladiator: Team VIP) | v5.3 · 2026-10-16 |
| 00011C61 | 15 bytes | XBE header | Team Spawns item (jmp from XTS2 at 0x8e8e7e): only in modes that can have teams | v5.3 · 2026-10-16 |
| 00011C70 | 57 bytes | XBE header | folder links (call at 0x8e8f52, then jmp *%eax): eax = where to continue | v5.3 · 2026-10-16 |
| 00011CA9 | 20 bytes | XBE header | Mercy Rule labels (call at 0x11dfe, replaces mov $KILLS,%esi): Thief counts coins | v5.3 · 2026-10-16 |
| 00011CBD | 27 bytes | XBE header | end of every Advanced Settings page (jmp at XTAIL 0x8e8eb9): the Team Settings page adds its mod items (Team VIP) | v5.3 · 2026-10-16 |
| 00011CD8 | 80 bytes | XBE header | Menu / message text "10 Coins","15 Coins","20 Coins","25 Coins","30 Coins","35 Coins","40 Coins","45 Coins","50 Coins" | v5.3 · 2026-10-16 |
| 00011D30 | 16 bytes | XBE header | Menu / message text "Team Settings >" | v5.3 · 2026-10-16 |
| 00011D40 | 17 bytes | XBE header | Menu / message text "Spawn Settings >" | v5.3 · 2026-10-16 |
| 00011D51 | 62 bytes | XBE header | XADVL (call at 0x2c7f6f, was call 0x7a160 with arg 1: the divider before Weapon Set): "Advanced Settings" as the first big link, just above Weapon Set | v5.3 · 2026-10-16 |
| 008CE680 | 35 bytes | xbreadfail_sp | ---- Advanced Settings only in custom arcade matches and on LAN: not in Story (game type 10), Arcade League (match flag 0x40) or Challenges (0x8000000). Their setups never reach the mod's setup code (the builder's other cases), so only the in-match checks need it: each setting's effective value is Off there. The match's parms keep the last match's values in the front end (level 0x65), so there it counts as custom (menus as before) ZF set = a custom match (or the front end): the settings apply; ZF clear = Story, League or Challenge; keeps all registers | v5.89 · 2026-10-27 |
| 008CE6A3 | 14 bytes | xbreadfail_sp | the gates, called first thing in a setting's function (nothing on the stack yet but its return): not custom -> that function returns at once with its "off" value eax = 0 (ZF set) | v5.89 · 2026-10-27 |
| 008CE6B1 | 14 bytes | xbreadfail_sp | edx = 0 (XRDOPT: no delay) | v5.89 · 2026-10-27 |
| 008CE6BF | 14 bytes | xbreadfail_sp | ZF set, registers kept (XTSPN: Team Spawns Off doesn't apply) | v5.89 · 2026-10-27 |
| 008CE6CD | 16 bytes | xbreadfail_sp | XGGPD: the gun dropped, as the game does | v5.89 · 2026-10-27 |
| 008CE6DD | 16 bytes | xbreadfail_sp | XASK: the game's own Assault tick only | v5.89 · 2026-10-27 |
| 008CE6ED | 18 bytes | xbreadfail_sp | the older modules' checks (calls from xgg_patch.py over their first 7-byte instruction, +2 nops): as that instruction, or its "off" (0) when not custom; keep the other registers ia.s, Reverse Scoring (0x8e9a76, was cmpb $0,WWVAR: ZF set = Off) | v5.89 · 2026-10-27 |
| 008CE6FF | 18 bytes | xbreadfail_sp | ia.s, Score With Bag Away (0x8e9c43, was cmpb $0,HOMEVAR) | v5.89 · 2026-10-27 |
| 008CE711 | 18 bytes | xbreadfail_sp | ia.s / vip.s, Team VIP (0x8e9dd5, 0x8e959e, was cmpb $0,VIPVAR) | v5.89 · 2026-10-27 |
| 008CE723 | 24 bytes | xbreadfail_sp | all.s, Number of Flames (0x8e8284, was movzbl FLAMES,%eax: 0 = one flame); flags kept | v5.89 · 2026-10-27 |
| 008CE73B | 24 bytes | xbreadfail_sp | zi.s, Zone Scoring Interval (0x8e8c42, was movzbl ZVAR,%eax: 0 = 15 seconds); flags kept | v5.89 · 2026-10-27 |
| 008CE765 | 18 bytes | xbreadfail_sp | mc3.s XCHK, Mercy Rule (header 0x11ea8, was cmpl $7,GSTATE; then jne = no check) | v5.89 · 2026-10-27 |
| 008DF000 | 256 bytes | xbreadfail_sp | Mod variables area (reserved, starts as zero). | v5.3 · 2026-10-16 (approx.) |
| 008E7860 | 64 bytes | xbreadfail_sp | Data: XGGCT | v5.15 · 2026-10-16 |
| 008E81C0 | 20 bytes | xbreadfail_sp | Data: PLIST | v5.3 · 2026-10-16 (approx.) |
| 008E81D4 | 20 bytes | xbreadfail_sp | Data: SLIST | v5.3 · 2026-10-16 (approx.) |
| 008E81E8 | 24 bytes | xbreadfail_sp | ---------------- helpers | v5.3 · 2026-10-16 (approx.) |
| 008E8200 | 22 bytes | xbreadfail_sp | ---------------- helpers nchars16: eax = min(character count,16) | v5.3 · 2026-10-16 |
| 008E84B3 | 70 bytes | xbreadfail_sp | ---------------- menu: add item helper. args: eax=label, edx=id, ecx=option list ptr, ebx=count | v5.3 · 2026-10-16 |
| 008E84F9 | 210 bytes | xbreadfail_sp | XPH (jmp at 0x8e8ecc): phase 2 skips Number of Flames / Zone Scoring Interval | v5.3 · 2026-10-16 |
| 008E85CB | 38 bytes | xbreadfail_sp | value address for id in ecx -> edx = address (uses MODMENU) | v5.3 · 2026-10-16 |
| 008E85F1 | 58 bytes | xbreadfail_sp | page refresh (jmp from 0x11e7a), esi=page; ends with pop ebp,ebx,edi,esi; ret | v5.3 · 2026-10-16 |
| 008E862B | 56 bytes | xbreadfail_sp | apply (jmp from 0x11e7f): original mercy store then ours; esi=page | v5.3 · 2026-10-16 |
| 008E87C0 | 32 bytes | xbreadfail_sp | Settings bytes for several features (Multikill window at 0x8E87D4, others). | v5.3 · 2026-10-16 (approx.) |
| 008E8CB4 | 88 bytes | xbreadfail_sp | XMG0 (XCH page 0, was je 0x11960): XAFTM in phase 1 first (Number of Flames, Zone Scoring Interval, mode items) | v5.3 · 2026-10-16 (approx.) |
| 008E8E00 | 25 bytes | xbreadfail_sp | page builders: set page + title, then the shared Advanced Settings builder (cdecl page argument untouched) | v5.3 · 2026-10-16 |
| 008E8E19 | 25 bytes | xbreadfail_sp | Code: XBT (see the code shown) | v5.3 · 2026-10-16 |
| 008E8E32 | 25 bytes | xbreadfail_sp | page title (call at 0x110a9) | v5.3 · 2026-10-16 |
| 008E8E4B | 14 bytes | xbreadfail_sp | page title (call at 0x110a9) | v5.3 · 2026-10-16 |
| 008E8E59 | 11 bytes | xbreadfail_sp | title line (call at 0x1168e, replaces push $-1; push $0x113f7) | v5.3 · 2026-10-16 (approx.) |
| 008E8E64 | 17 bytes | xbreadfail_sp | Teamplay item only on the Team page (call at 0x11104) | v5.3 · 2026-10-16 |
| 008E8E75 | 15 bytes | xbreadfail_sp | Team Spawns only on the Spawn page (call at 0x11133) | v5.3 · 2026-10-16 |
| 008E8E84 | 17 bytes | xbreadfail_sp | colour items only on the Team page (call at 0x1115a) | v5.3 · 2026-10-16 |
| 008E8E95 | 35 bytes | xbreadfail_sp | rest of the items (jmp at 0x1118f) | v5.3 · 2026-10-16 |
| 008E8EB8 | 1 bytes | xbreadfail_sp | end of the Respawn Delay items (jmp at 0x8e85bf) | v5.3 · 2026-10-16 (approx.) |
| 008E8EB9 | 11 bytes | xbreadfail_sp | after Mercy (jmp at 0x11e42): Number of Flames, Zone Scoring Interval, then the folder links | v5.3 · 2026-10-16 (approx.) |
| 008E8EC4 | 210 bytes | xbreadfail_sp | after Mercy (jmp at 0x11e42): Number of Flames, Zone Scoring Interval, then the folder links | v5.3 · 2026-10-16 |
| 008E8F96 | 20 bytes | xbreadfail_sp | folder links: open the sub-page | v5.3 · 2026-10-16 |
| 008E8FAA | 20 bytes | xbreadfail_sp | first selected item (call at 0x111a3, replaces add $4,%esp; push $id): first existing id of the page's list (esi = page) | v5.3 · 2026-10-16 |
| 008E8FBE | 78 bytes | xbreadfail_sp | first selected item (call at 0x111a3, replaces add $4,%esp; push $id): first existing id of the page's list (esi = page) | v5.3 · 2026-10-16 |
| 008E900C | 16 bytes | xbreadfail_sp | Data: DTEAM | v5.3 · 2026-10-16 (approx.) |
| 008E901C | 16 bytes | xbreadfail_sp | Data: DSPAWN | v5.3 · 2026-10-16 (approx.) |
| 008E902C | 12 bytes | xbreadfail_sp | Data: CTAB | v5.3 · 2026-10-16 |
| 008E9038 | 14 bytes | xbreadfail_sp | Menu / message text "Team Settings" | v5.3 · 2026-10-16 |
| 008E9046 | 15 bytes | xbreadfail_sp | Menu / message text "Spawn Settings" | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 001B7A58 | 8E6E0084 | 0803FF1C | lw t6,132(s3) | j 0xffc70 | new[0x1B7A58]=j(SYM['WWA']); new[0x1B7A5C]=NOP | v5.3 · 2026-10-16 |
| 001B7A5C | 8E4F001C | 00000000 | lw t7,28(s2) | nop | new[0x1B7A58]=j(SYM['WWA']); new[0x1B7A5C]=NOP | v5.3 · 2026-10-16 |
| 001B81B4 | 8D6E001C | 0803FF5C | lw t6,28(t3) | j 0xffd70 | new[0x1B81B4]=j(SYM['WWC']); new[0x1B81B8]=NOP | v5.3 · 2026-10-16 |
| 001B81B8 | 8E2F0084 | 00000000 | lw t7,132(s1) | nop | new[0x1B81B4]=j(SYM['WWC']); new[0x1B81B8]=NOP | v5.3 · 2026-10-16 |
| 001B9194 | 8E8E0084 | 0803FB00 | lw t6,132(s4) | j 0xfec00 | new[0x1B9194]=j(SYM['WWD']); new[0x1B9198]=NOP | v5.3 · 2026-10-16 |
| 001B9198 | 8D4F001C | 00000000 | lw t7,28(t2) | nop | new[0x1B9194]=j(SYM['WWD']); new[0x1B9198]=NOP | v5.3 · 2026-10-16 |
| 001B9230 | 8E4C001C | 0803FFC8 | lw t4,28(s2) | j 0xfff20 | delay slot (lw t7,20(t5)) kept | v5.3 · 2026-10-16 |
| 0043B59C | 0C053D0C | 0C03F9B3 | jal 0x14f430 | jal 0xfe6cc | new[0x43B59C]=jal(ADVL) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FD010-000FDF9F | 592 | new code, page descriptor, label text and settings in free low memory (0x000FD000-0x000FDFA0) | v5.70 · 2026-10-23 |
| 000FDC80-000FDCD7 | 22 | "Advanced Settings" page: same layout as the match settings page (title line + match settings text style) at 0x000FDC80 | v5.3 · 2026-10-16 |
| 000EE148-000EE1A7 | 24 | NCFL: j at 0xFCC5C in the flame function (was lui t0,0x10 / lbu s1,-12512(t0): Number of Flames, 0 = one): custom arcade and LAN only, else one; then on at 0xFCC64 | v5.89 · 2026-10-27 |
| 000EE1A8-000EE207 | 24 | NCZI: j at 0xFBBD0, the zone interval's start (was lui t9,0x10 / lbu t8,-16552(t9): Zone Scoring Interval, 0 = 15 s): custom arcade and LAN only, else the default; then on at 0xFBBD8 | v5.89 · 2026-10-27 |
| 000EE824-000EE87B | 22 | NCZE: jal at 0x13E578 (time up, was jal 0xFB9E0: ze.py, Zones scores the held zones once more, then 0x13C8B8 with a0 = 0, set in the delay slot): custom arcade and LAN only; else straight to 0x13C8B8 | v5.95 · 2026-10-27 |
| 000EE87C-000EE8D3 | 22 | NCMC: jal at 0x13E660 (was jal 0xFC2A4, Mercy Rule's check, which goes on to 0x388DB0): custom arcade and LAN only | v5.89 · 2026-10-27 |
| 000EF6F8-000EF733 | 15 | NCWW: leaf for ia.py (jalr t9,t8; link t9, uses t8 only): t8 = Reverse Scoring (WWVAR) in a custom arcade match or on LAN, else 0 (Story, Arcade League, Challenge); in a match only | v5.89 · 2026-10-27 |
| 000EF734-000EF76F | 15 | NCHM: leaf for ia.py (jalr t9,t8; link t9, uses t8 only): t8 = Score With Bag Away (HOMEVAR) in a custom arcade match or on LAN, else 0 (Story, Arcade League, Challenge); in a match only | v5.89 · 2026-10-27 |
| 000EFA48-000EFA7B | 13 | NCJ: leaf for ia.py (jalr t9,t8; link t9, uses t8 only): t8 = 0 in a custom arcade match or on LAN, else non-zero (Story, game type 10; Arcade League, flag 0x40; Challenge, flag 0x8000000); in a match only | v5.89 · 2026-10-27 |
| 000EFBD8-000EFC07 | 12 | GGCT: text | v5.15 · 2026-10-16 |
| 000F00DC-000F00EB | 4 | LWWA: text | v5.3 · 2026-10-16 |
| 000F02F4-000F02FB | 2 | RGNT: chain step before Respawn Delay (j at 0xFBE14 in sub.py's RG, was j 0xFBE30 = the end of the chain): the end of the chain as before (Spawn Rule and the Respawn Delay items are added by OPT in every mode) | v5.3 · 2026-10-16 (approx.) |
| 000FE640-000FE663 | 9 | LTEAML=lstr('Team Settings >',16); LSPAWNL=lstr('Spawn Settings >',20) | v5.3 · 2026-10-16 |
| 000FE664-000FE677 | 5 | LSCORE=lstr('Score With Bag Away',20) | v5.3 · 2026-10-16 |
| 000FE678-000FE6B3 | 15 | a.w[ZR_]=addiu('t7','t7',lo(a.lab['ZRET'])); FLRET=a.lab['FLRET']; place(a) | v5.3 · 2026-10-16 |
| 000FE6B4-000FE737 | 33 | place(a) | v5.99 · 2026-10-28 |
| 000FE800-000FE89B | 39 | for _i,_x in enumerate(_w): new[0xFE800+4*_i]=_x | v5.3 · 2026-10-16 |
| 000FEBA8-000FEBFB | 21 | for _i,_x in enumerate(_m): new[0xFEBA8+4*_i]=_x | v5.3 · 2026-10-16 |
| 000FEBFC-000FEBFF | 1 | the rest of the old block written as zeros (no stale words) | v5.3 · 2026-10-16 (approx.) |
| 000FF800-000FF81F | 8 | for i,n in enumerate(JT): new[BASE+8*i]=j(SYM[n]); new[BASE+8*i+4]=NOP | v5.3 · 2026-10-16 (approx.) |
| 000FF850-000FF883 | 13 | IAITEM_A=a; emit(a) | v5.3 · 2026-10-16 |
| 000FF884-000FF88B | 2 | new[w0]=lui('a0',((LWWA+0x8000)>>16)&0xffff); new[w0+4]=addiu('a0','a0',LWWA&0xffff) | v5.3 · 2026-10-16 (approx.) |
| 000FF88C-000FF8CB | 16 | IAITEM_A=a; emit(a) | v5.3 · 2026-10-16 |
| 000FF8CC-000FF8D3 | 2 | new[w1]=lui('a0',0x10); new[w1+4]=addiu('a0','a0',lo(LSCORE)) | v5.3 · 2026-10-16 (approx.) |
| 000FF8D4-000FF927 | 21 | IAITEM_A=a; emit(a) | v5.3 · 2026-10-16 |
| 000FF928-000FF92F | 2 | new[w2]=lui('a0',((LVIP+0x8000)>>16)&0xffff); new[w2+4]=addiu('a0','a0',LVIP&0xffff) | v5.3 · 2026-10-16 (approx.) |
| 000FF930-000FFA4F | 72 | IAITEM_A=a; emit(a) | v5.3 · 2026-10-16 |
| 000FFA50-000FFB27 | 54 | apply routine('IAN1',False) | v5.3 · 2026-10-16 |
| 000FFB30-000FFC1B | 59 | apply routine('IAN2',True) | v5.3 · 2026-10-16 |
| 000FFF30-000FFF43 | 5 | emit(a) | v5.3 · 2026-10-16 (approx.) |

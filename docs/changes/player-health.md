# Player Health

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 000BC1A0 | 0AC1A0 | 5 | `a1 c4 c8 4e 00` | `e9 f2 73 82 00` | damage routine: Player Health (host / offline, hits it decides) \| the game's damage routine (jmp at 0xbc1a0, was mov 0x4ec8c4,%eax; [esp+4] = the hit; cdecl): host / offline, a hit it decides \| the game's damage routine (jmp at 0xbc1a0, was mov 0x4ec8c4,%eax; [esp+4] = the hit; cdecl): host / offline, a hit it decides here (not one reported by another game: PKDMGF): the amount by Player Health, for the routine (it takes it here and sends it on); put back after, as callers use the same hit again (an explosion, for each character in it) | v5.67 · 2026-10-23 |
| 000BC1FA | 0AC1FA | 5 | `e8 c1 22 2a 00` | `e8 18 75 82 00` | damage routine, the hit's report: was call 0x35e4c0 (Player Health, LAN player's own copy) \| the hit's report (call at 0xbc1fa in the damage routine, was call 0x35e4c0: sends a hit this game decides, [esp+4] = the hit; \| the hit's report (call at 0xbc1fa in the damage routine, was call 0x35e4c0: sends a hit this game decides, [esp+4] = the hit; eax: 1 = this game takes it now): LAN player, a hit of its own going through XPHDA's LAN player path (XPHGF) and sent: from here on the amount by the host's Player Health, for this game's own copy only (XPHDA puts it back after) | v5.3 · 2026-10-16 |
| 0035C2E4 | 34C2E4 | 9 | `8b b4 24 88 00 00 00 8b ce` | `e8 48 73 58 00 90 90 90 90` | damage report decode: Player Health (host, reports it passes on) \| the damage report decode (call at 0x35c2e4, was mov 0x88(%esp),%esi / mov %esi,%ecx: the buffer, at the amount): the host \| the damage report decode (call at 0x35c2e4, was mov 0x88(%esp),%esi / mov %esi,%ecx: the buffer, at the amount): the host passing on another game's report (packet 17): the amount by Player Health, in the report itself, so that the host takes it and sends it on so (every other game takes the amount it gets) | v5.67 · 2026-10-23 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E3485 | 3 bytes | xbreadfail_sp | the setting: the menu option (0 = Default) | v5.3 · 2026-10-16 (approx.) |
| 008E3488 | 16 bytes | xbreadfail_sp | by XPHVAR: Default, 75, 50, 25% | v5.67 · 2026-10-23 |
| 008E3498 | 71 bytes | xbreadfail_sp | Code: XPHITEM (see the code shown) | v5.67 · 2026-10-23 |
| 008E34DF | 32 bytes | xbreadfail_sp | Code: XPHR (see the code shown) | v5.68 · 2026-10-23 |
| 008E34FF | 31 bytes | xbreadfail_sp | Code: XPHA (see the code shown) | v5.68 · 2026-10-23 |
| 008E351E | 14 bytes | xbreadfail_sp | Menu / message text "Player Health" | v5.67 · 2026-10-23 |
| 008E352C | 32 bytes | xbreadfail_sp | eax = target prop, edx = attacker prop, cl = bullet type -> ZF clear if Player Health changes this hit (a setting other than | v5.79 · 2026-10-26 |
| 008E354C | 75 bytes | xbreadfail_sp | eax = target prop, edx = attacker prop, cl = bullet type -> ZF clear if Player Health changes this hit (a setting other than Default (XPHEFF), not Leech; a character hit by another character; its guns and melee, not fire, explosions, the explosives' own hits (rockets, grenades, mines, TNT, bricks) or the energy beam); keeps every register | v5.78 · 2026-10-26 |
| 008E3597 | 154 bytes | xbreadfail_sp | the game's damage routine (jmp at 0xbc1a0, was mov 0x4ec8c4,%eax; [esp+4] = the hit; cdecl): host / offline, a hit it decides here (not one reported by another game: PKDMGF): the amount by Player Health, for the routine (it takes it here and sends it on); put back after, as callers use the same hit again (an explosion, for each character in it) | v5.78 · 2026-10-26 |
| 008E3631 | 108 bytes | xbreadfail_sp | the damage report decode (call at 0x35c2e4, was mov 0x88(%esp),%esi / mov %esi,%ecx: the buffer, at the amount): the host passing on another game's report (packet 17): the amount by Player Health, in the report itself, so that the host takes it and sends it on so (every other game takes the amount it gets) | v5.67 · 2026-10-23 |
| 008E369D | 74 bytes | xbreadfail_sp | kill message (from XSDKL, which jumps here when not a Showdown shot: the call at 0x35eaa1 in kill message, was call local-send routine; esi = the prop it goes by, ebx = size, edi = reliable; stack: type as host (18), type as player (19), data; the damage info at 0x124(%esp)): LAN host, Player Health on, a character killed by another: the host's copy reached no health first, so the host sends the kill to every console (message send routine from this console's client), whoever fired it, and goes on with it here (eax = 1) | v5.67 · 2026-10-23 |
| 008E36E7 | 1 bytes | xbreadfail_sp | > 0 while a LAN player's own hit goes through the damage routine (XPHDA) | v5.3 · 2026-10-16 (approx.) |
| 008E36E8 | 47 bytes | xbreadfail_sp | eax = the Player Health setting that applies to this game's hits (offline / LAN host: the setting; LAN player: the host's, setup byte 67 bits 0-1 under its 0x90 marker, so only from a host with the patch; else Default); keeps ecx/edx | v5.89 · 2026-10-27 |
| 008E3717 | 96 bytes | xbreadfail_sp | the hit's report (call at 0xbc1fa in the damage routine, was call 0x35e4c0: sends a hit this game decides, [esp+4] = the hit; eax: 1 = this game takes it now): LAN player, a hit of its own going through XPHDA's LAN player path (XPHGF) and sent: from here on the amount by the host's Player Health, for this game's own copy only (XPHDA puts it back after) | v5.78 · 2026-10-26 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 001B18D0 | 27BDFFE0 | 08039705 | addiu sp,sp,-32 | j 0xe5c14 | Hook: damage routine: Player Health (host / offline, hits it decides); its delay slot lui t7,0x67 kept | v5.67 · 2026-10-23 |
| 001B1968 | 0C13E5CA | 0C03B2A8 | jal 0x4f9728 | jal 0xecaa0 | Hook: damage routine, the hit's report: was jal 0x4F9728 (Player Health, a LAN player's own copy); delay slot kept | v5.78 · 2026-10-26 |
| 004F9418 / PAL 004F94C0 | 8FCF0088 | 0C03B2CC | lw t7,136(fp) | jal 0xecb30 | Hook: damage report decode: Player Health (host, reports it passes on); its delay slot kept | v5.67 · 2026-10-23 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E5C14-000E5D9F | 99 | PHDA: j at 0x1B18D0 in the game's damage routine (its delay slot lui t7,0x67 done; a0 = the hit): host / offline, a hit it decides here (not one reported by another game: PKDMGF): the amount by Player Health, for the routine (it takes | v5.89 · 2026-10-27 |
| 000E7D20-000E7E33 | 69 | PHOK: t0 = target prop, t1 = attacker prop, t2 = bullet type -> v1 = 0, or the setting * 4 (PHM) if Player Health changes this hit (the setting that applies here, phef, not Default; not Leech; a character hit by another character; its guns and | v5.89 · 2026-10-27 |
| 000EB940-000EB9E3 | 41 | PHKL: kill message (from SDKL, when not a Showdown shot: the jal at 0x4FA898 in kill message, was jal local-send routine: a0 the prop it goes by, a1 type as host (18), a2 type as player (19), a3 data, t0 size, t1 reliable; s0 = damage info): LAN host, | v5.67 · 2026-10-23 |
| 000EC0B4-000EC14F | 39 | PHITEM: Advanced page (every mode but Leech): Player Health (Default / Low / Weakling / Pathetic (75% / 50% / 25%)) | v5.67 · 2026-10-23 |
| 000ECAA0-000ECB2F | 36 | PHNH: jal at 0x1B1968 in the damage routine (was jal 0x4F9728, the hit's report: sends a hit this game decides; its delay slot daddu a0,s0 = the hit kept; v0: 1 = this game takes it now): LAN player, a hit of its own going through PHDA's LAN | v5.78 · 2026-10-26 |
| 000ECB30-000ECBBF | 36 | PHRX: jal at 0x4F9418 in the damage report decode (was lw t7,136(fp): the buffer, at the amount; its delay slot kept; fp = its frame: +0 target, +8 attacker; s3 = packet type): the host passing on another game's report (packet 17): | v5.67 · 2026-10-23 |
| 000EF634-000EF67F | 19 | PHRA: a0 = page, a1 = 0 refresh / 1 apply: Player Health (stored as the option) | v5.68 · 2026-10-23 |
| 000F06A8-000F06B7 | 4 | PHM: by PHVAR: Default, 75, 50, 25% | v5.67 · 2026-10-23 |
| 000F0728-000F0737 | 4 | LPH: text | v5.67 · 2026-10-23 |
| 000F07C4-000F07CF | 3 | PHORIG: the damage routine's own start (PHDA's tail; its first word, then on at 0x1B18D8) | v5.67 · 2026-10-23 |
| 000F0884-000F088F | 3 | LPH25: text | v5.67 · 2026-10-23 (approx.) |
| 000F0890-000F089B | 3 | LPH50: text | v5.67 · 2026-10-23 (approx.) |
| 000F0948-000F094F | 2 | LPH100: text | v5.67 · 2026-10-23 (approx.) |
| 000F09CC-000F09CF | 1 | LPH75: text | v5.67 · 2026-10-23 (approx.) |

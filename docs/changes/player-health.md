# Player Health

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 000BC1A0 | 0AC1A0 | 5 | `a1 c4 c8 4e 00` | `e9 82 73 82 00` | damage routine: Player Health (host / offline, hits it decides) \| the game's damage routine (jmp at 0xbc1a0, was mov 0x4ec8c4,%eax; [esp+4] = the hit; cdecl): host / offline, a hit it decides \| the game's damage routine (jmp at 0xbc1a0, was mov 0x4ec8c4,%eax; [esp+4] = the hit; cdecl): host / offline, a hit it decides here (not one reported by another game: PKDMGF): the amount by Player Health, for the routine (it takes it here and sends it on); put back after, as callers use the same hit again (an explosion, for each character in it) | v5.67 · 2026-10-23 |
| 000BC1FA | 0AC1FA | 5 | `e8 c1 22 2a 00` | `e8 a8 74 82 00` | damage routine, the hit's report: was call 0x35e4c0 (Player Health, LAN player's own copy) \| the hit's report (call at 0xbc1fa in the damage routine, was call 0x35e4c0: sends a hit this game decides, [esp+4] = the hit; \| the hit's report (call at 0xbc1fa in the damage routine, was call 0x35e4c0: sends a hit this game decides, [esp+4] = the hit; eax: 1 = this game takes it now): LAN player, a hit of its own going through XPHDA's LAN player path (XPHGF) and sent: from here on the amount by the host's Player Health, for this game's own copy only (XPHDA puts it back after) | v5.3 · 2026-10-16 |
| 0035C2E4 | 34C2E4 | 9 | `8b b4 24 88 00 00 00 8b ce` | `e8 d8 72 58 00 90 90 90 90` | damage report decode: Player Health (host, reports it passes on) \| the damage report decode (call at 0x35c2e4, was mov 0x88(%esp),%esi / mov %esi,%ecx: the buffer, at the amount): the host \| the damage report decode (call at 0x35c2e4, was mov 0x88(%esp),%esi / mov %esi,%ecx: the buffer, at the amount): the host passing on another game's report (packet 17): the amount by Player Health, in the report itself, so that the host takes it and sends it on so (every other game takes the amount it gets) | v5.67 · 2026-10-23 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E3414 | 4 bytes | xbreadfail_sp | the setting: the menu option (0 = Default) | v5.3 · 2026-10-16 (approx.) |
| 008E3418 | 16 bytes | xbreadfail_sp | by XPHVAR: Default, 75, 50, 25% | v5.67 · 2026-10-23 |
| 008E3428 | 71 bytes | xbreadfail_sp | Code: XPHITEM (see the code shown) | v5.67 · 2026-10-23 |
| 008E346F | 32 bytes | xbreadfail_sp | Code: XPHR (see the code shown) | v5.68 · 2026-10-23 |
| 008E348F | 31 bytes | xbreadfail_sp | Code: XPHA (see the code shown) | v5.68 · 2026-10-23 |
| 008E34AE | 14 bytes | xbreadfail_sp | Menu / message text "Player Health" | v5.67 · 2026-10-23 |
| 008E34BC | 32 bytes | xbreadfail_sp | eax = target prop, edx = attacker prop, cl = bullet type -> ZF clear if Player Health changes this hit (a setting other than | v5.79 · 2026-10-26 |
| 008E34DC | 75 bytes | xbreadfail_sp | eax = target prop, edx = attacker prop, cl = bullet type -> ZF clear if Player Health changes this hit (a setting other than Default (XPHEFF), not Leech; a character hit by another character; its guns and melee, not fire, explosions, the explosives' own hits (rockets, grenades, mines, TNT, bricks) or the energy beam); keeps every register | v5.78 · 2026-10-26 |
| 008E3527 | 154 bytes | xbreadfail_sp | the game's damage routine (jmp at 0xbc1a0, was mov 0x4ec8c4,%eax; [esp+4] = the hit; cdecl): host / offline, a hit it decides here (not one reported by another game: PKDMGF): the amount by Player Health, for the routine (it takes it here and sends it on); put back after, as callers use the same hit again (an explosion, for each character in it) | v5.78 · 2026-10-26 |
| 008E35C1 | 108 bytes | xbreadfail_sp | the damage report decode (call at 0x35c2e4, was mov 0x88(%esp),%esi / mov %esi,%ecx: the buffer, at the amount): the host passing on another game's report (packet 17): the amount by Player Health, in the report itself, so that the host takes it and sends it on so (every other game takes the amount it gets) | v5.67 · 2026-10-23 |
| 008E362D | 74 bytes | xbreadfail_sp | kill message (from XSDKL, which jumps here when not a Showdown shot: the call at 0x35eaa1 in kill message, was call local-send routine; esi = the prop it goes by, ebx = size, edi = reliable; stack: type as host (18), type as player (19), data; the damage info at 0x124(%esp)): LAN host, Player Health on, a character killed by another: the host's copy reached no health first, so the host sends the kill to every console (message send routine from this console's client), whoever fired it, and goes on with it here (eax = 1) | v5.67 · 2026-10-23 |
| 008E3677 | 1 bytes | xbreadfail_sp | > 0 while a LAN player's own hit goes through the damage routine (XPHDA) | v5.3 · 2026-10-16 (approx.) |
| 008E3678 | 47 bytes | xbreadfail_sp | eax = the Player Health setting that applies to this game's hits (offline / LAN host: the setting; LAN player: the host's, setup byte 67 bits 0-1 under its 0x90 marker, so only from a host with the patch; else Default); keeps ecx/edx | v5.89 · 2026-10-27 |
| 008E36A7 | 96 bytes | xbreadfail_sp | the hit's report (call at 0xbc1fa in the damage routine, was call 0x35e4c0: sends a hit this game decides, [esp+4] = the hit; eax: 1 = this game takes it now): LAN player, a hit of its own going through XPHDA's LAN player path (XPHGF) and sent: from here on the amount by the host's Player Health, for this game's own copy only (XPHDA puts it back after) | v5.78 · 2026-10-26 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 001B18D0 | 27BDFFE0 | 080394F9 | addiu sp,sp,-32 | j 0xe53e4 | Hook: damage routine: Player Health (host / offline, hits it decides); its delay slot lui t7,0x67 kept | v5.67 · 2026-10-23 |
| 001B1968 | 0C13E5CA | 0C03B13D | jal 0x4f9728 | jal 0xec4f4 | Hook: damage routine, the hit's report: was jal 0x4F9728 (Player Health, a LAN player's own copy); delay slot kept | v5.78 · 2026-10-26 |
| 004F9418 / PAL 004F94C0 | 8FCF0088 | 0C03B161 | lw t7,136(fp) | jal 0xec584 | Hook: damage report decode: Player Health (host, reports it passes on); its delay slot kept | v5.67 · 2026-10-23 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000E53E4-000E556F | 99 | PHDA: j at 0x1B18D0 in the game's damage routine (its delay slot lui t7,0x67 done; a0 = the hit): host / offline, a hit it decides here (not one reported by another game: PKDMGF): the amount by Player Health, for the routine (it takes | v5.89 · 2026-10-27 |
| 000E7BE4-000E7CF7 | 69 | PHOK: t0 = target prop, t1 = attacker prop, t2 = bullet type -> v1 = 0, or the setting * 4 (PHM) if Player Health changes this hit (the setting that applies here, phef, not Default; not Leech; a character hit by another character; its guns and | v5.89 · 2026-10-27 |
| 000EBC1C-000EBCB7 | 39 | PHITEM: Advanced page (every mode but Leech): Player Health (Default / Low / Weakling / Pathetic (75% / 50% / 25%)) | v5.67 · 2026-10-23 |
| 000EC4F4-000EC583 | 36 | PHNH: jal at 0x1B1968 in the damage routine (was jal 0x4F9728, the hit's report: sends a hit this game decides; its delay slot daddu a0,s0 = the hit kept; v0: 1 = this game takes it now): LAN player, a hit of its own going through PHDA's LAN | v5.78 · 2026-10-26 |
| 000EC584-000EC613 | 36 | PHRX: jal at 0x4F9418 in the damage report decode (was lw t7,136(fp): the buffer, at the amount; its delay slot kept; fp = its frame: +0 target, +8 attacker; s3 = packet type): the host passing on another game's report (packet 17): | v5.67 · 2026-10-23 |
| 000EEF40-000EEF8B | 19 | PHRA: a0 = page, a1 = 0 refresh / 1 apply: Player Health (stored as the option) | v5.68 · 2026-10-23 |
| 000EFF4C-000EFF5B | 4 | PHM: by PHVAR: Default, 75, 50, 25% | v5.67 · 2026-10-23 |
| 000EFFCC-000EFFDB | 4 | LPH: text | v5.67 · 2026-10-23 |
| 000F005C-000F0067 | 3 | PHORIG: the damage routine's own start (PHDA's tail; its first word, then on at 0x1B18D8) | v5.67 · 2026-10-23 |
| 000F0110-000F011B | 3 | LPH25: text | v5.67 · 2026-10-23 (approx.) |
| 000F011C-000F0127 | 3 | LPH50: text | v5.67 · 2026-10-23 (approx.) |
| 000F01D4-000F01DB | 2 | LPH100: text | v5.67 · 2026-10-23 (approx.) |
| 000F0258-000F025B | 1 | LPH75: text | v5.67 · 2026-10-23 (approx.) |
| 000FC95C-000FC9FF | 41 | PHKL: kill message (from SDKL, when not a Showdown shot: the jal at 0x4FA898 in kill message, was jal local-send routine: a0 the prop it goes by, a1 type as host (18), a2 type as player (19), a3 data, t0 size, t1 reliable; s0 = damage info): LAN host, | v5.67 · 2026-10-23 |

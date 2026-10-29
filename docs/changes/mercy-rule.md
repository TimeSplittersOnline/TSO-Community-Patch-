# Mercy Rule

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00068F7C | 058F7C | 5 | `e8 df 03 1d 00` | `e8 27 8f fa ff` | Each mode's end-of-match check now goes through the Mercy Rule check (header code 0x11EA8), which ends the match early when a side is far enough ahead, then calls the original check 0x239360. | v5.3 · 2026-10-16 |
| 00068F92 | 058F92 | 5 | `e8 c9 03 1d 00` | `e8 11 8f fa ff` | Same Mercy Rule check for another mode. | v5.3 · 2026-10-16 |
| 00068FA8 | 058FA8 | 5 | `e8 b3 03 1d 00` | `e8 fb 8e fa ff` | Same Mercy Rule check for another mode. | v5.3 · 2026-10-16 |
| 00068FBE | 058FBE | 5 | `e8 9d 03 1d 00` | `e8 e5 8e fa ff` | Same Mercy Rule check for another mode. | v5.3 · 2026-10-16 |
| 00068FD4 | 058FD4 | 5 | `e8 87 03 1d 00` | `e8 cf 8e fa ff` | Same Mercy Rule check for another mode. | v5.3 · 2026-10-16 |
| 00069000 | 059000 | 5 | `e8 5b 03 1d 00` | `e8 a3 8e fa ff` | Same Mercy Rule check for another mode. | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 00011B03 | 67 bytes | XBE header | Mercy Rule tables: which limit each mode uses, and the texts "10 Points" ... "50 Points". | v5.89 · 2026-10-27 |
| 00011DB0 | 157 bytes | XBE header | Code: XMADD (see the code shown) | v5.3 · 2026-10-16 |
| 00011E4D | 50 bytes | XBE header | Code: XMEXT1 (see the code shown) | v5.3 · 2026-10-16 |
| 00011E7F | 41 bytes | XBE header | Code: XMEXT2 (see the code shown) | v5.3 · 2026-10-16 |
| 00011EA8 | 319 bytes | XBE header | Code: XCHK (see the code shown) | v5.89 · 2026-10-27 |
| 008E78EC | 27 bytes | xbreadfail_sp | Mercy Rule times (mc3.s, header 0x11e1c: mov $LMIN,%esi; were "1 Min" .. "5 Min") | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0013E660 | 0C0E236C | 0C03BA7B | jal 0x388db0 | jal 0xee9ec | Mercy Rule (Advanced Settings, set per mode): host ends the match when 1st place leads 2nd by the limit (kills; coins in Thief) | v5.89 · 2026-10-27 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FC000-000FC91B | 342 | Mercy Rule (Advanced Settings, set per mode): host ends the match when 1st place leads 2nd by the limit (kills; coins in Thief) | v5.89 · 2026-10-27 |
| 000EFD18-000EFD47 | 12 | LMIN: text | v5.3 · 2026-10-16 |

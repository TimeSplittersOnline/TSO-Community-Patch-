# Infinite Ammo, Disable Unarmed (No Punch)

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002D823D | 2C823D | 5 | `a1 cc df 7b 00` | `e8 cd 15 61 00` | setup builder (call at 0x2d823d): Infinite Ammo -> FLAG_INFAMMO (0x100), then the No Punch flag code | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 00011960 | 176 bytes | XBE header | Disable Unarmed item: add, refresh and store it (text "Disable Unarmed" at 0x119F7). | v5.3 · 2026-10-16 |
| 008E9800 | 80 bytes | xbreadfail_sp | Advanced Settings items: Wrong Way Bag (Capture the Bag menu), Infinite Ammo (all modes; not offered in LAN/online matches, where the game always uses up ammo) | v5.3 · 2026-10-16 |
| 008E9850 | 74 bytes | xbreadfail_sp | Advanced Settings items: Wrong Way Bag (Capture the Bag menu), Infinite Ammo (all modes; not offered in LAN/online matches, where the game always uses up ammo) | v5.3 · 2026-10-16 |
| 008E98DB | 193 bytes | xbreadfail_sp | the mode's own items (first on the Advanced page): Capture the Bag: Reverse Scoring, Score With Bag Away; Virus: Spread By Kills (LAN) | v5.3 · 2026-10-16 |
| 008E999C | 49 bytes | xbreadfail_sp | refresh (esi = page): show each stored value | v5.3 · 2026-10-16 |
| 008E99CD | 61 bytes | xbreadfail_sp | apply (esi = page): store each chosen value | v5.3 · 2026-10-16 |
| 008E9A0A | 44 bytes | xbreadfail_sp | setup builder (call at 0x2d823d): Infinite Ammo -> FLAG_INFAMMO (0x100), then the No Punch flag code | v5.3 · 2026-10-16 (approx.) |
| 008E9A36 | 60 bytes | xbreadfail_sp | setup builder (call at 0x2d823d): Infinite Ammo -> FLAG_INFAMMO (0x100), then the No Punch flag code | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FDFA0-000FE31F | 62 | Advanced Settings: "No Punch" On/Off (sets the game's own no-punch match flag in the setup the host sends, so it applies to every player) | v5.3 · 2026-10-16 |
| 000FF820-000FF82F | 4 | LIA=D0; putb(LIA,b'Infinite Ammo\0'.ljust(16,b'\0')) | v5.3 · 2026-10-16 |
| 000FF830-000FF833 | 1 | OOFF=D0+16; putb(OOFF,b'Off\0') | v5.3 · 2026-10-16 (approx.) |
| 000FF834-000FF837 | 1 | OON=D0+20; putb(OON,b'On\0\0') | v5.3 · 2026-10-16 (approx.) |
| 000FF840-000FF84F | 4 | LINF=D0+32; putb(LINF,b'Spread By Kills\0') | v5.3 · 2026-10-16 |

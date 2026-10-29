# LAN: MapMaker maps use the host's weapon set

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 004DB288 / PAL 004DB330 | 28AF000A | 0C03BFA9 | slti t7,a1,10 | jal 0xefea4 | Hook: MapMaker weapon items: was slti t7,a1,10 / beq t7,zero,0x4DB2C4 (on LAN: the host's set) | v5.102 · 2026-10-29 |
| 004DB28C / PAL 004DB334 | 11E0000D | 00000000 | beq t7,zero,0x4db2c4 | nop | Hook: MapMaker weapon items: was slti t7,a1,10 / beq t7,zero,0x4DB2C4 (on LAN: the host's set) | v5.102 · 2026-10-29 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000EFEA4-000EFECB | 10 | MMWCHK: LAN: MapMaker maps take their weapons from the host's weapon set jal at 0x4DB288 (0x4DB28C now a nop) in the MapMaker weapon item lookup 0x4DB220, was slti t7,a1,10 / beq t7,zero, 0x4DB2C4 (a1 = this console's own saved Weapon Set choice, s0 = slot). The game takes the set the host sent for a | v5.102 · 2026-10-29 |

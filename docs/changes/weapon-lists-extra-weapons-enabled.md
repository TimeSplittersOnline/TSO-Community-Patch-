# Weapon lists (extra weapons enabled)

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 006838C0 / PAL 006839C0 | 00000000 | 00000001 | nop | .word 0x00000001 | mod: weapon list - enable Minigun (starts in alt fire) | v5.3 · 2026-10-16 |
| 00683ADC / PAL 00683BDC | 00000000 | 00000001 | nop | .word 0x00000001 | mod: weapon list - enable Sci-fi handgun (starts in alt fire) | v5.3 · 2026-10-16 |
| 00683B54 / PAL 00683C54 | 00000000 | 00000001 | nop | .word 0x00000001 | mod: weapon list - enable Sci-fi handgun secondary mode | v5.3 · 2026-10-16 |
| 00683D70 / PAL 00683E70 | 00000000 | 00000001 | nop | .word 0x00000001 | mod: weapon list - enable Mag Charger (starts in alt fire) | v5.3 · 2026-10-16 |
| 00683E60 / PAL 00683F60 | 00000000 | 00000001 | nop | .word 0x00000001 | mod: weapon list - enable Time Grenade | v5.3 · 2026-10-16 |
| 00683FC8 / PAL 006840C8 | 00000000 | 00000001 | nop | .word 0x00000001 | mod: weapon list - enable TNT | v5.3 · 2026-10-16 |
| 00684040 / PAL 00684140 | 00000000 | 00000001 | nop | .word 0x00000001 | mod: weapon list - enable KSMG (starts in alt fire) | v5.3 · 2026-10-16 |
| 006841E4 / PAL 006842E4 | 00000000 | 00000001 | nop | .word 0x00000001 | mod: weapon list - enable Temporal Uplink | v5.3 · 2026-10-16 |

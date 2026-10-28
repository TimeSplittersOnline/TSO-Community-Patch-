# Virus on Siberia

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 0043E484 / PAL 0043E4D4 | 122F0014 | 00000000 | beq s1,t7,0x43e4d8 | nop | Virus allowed on Siberia (level 0x35) | v5.3 · 2026-10-16 |
| 0043EFC8 / PAL 0043F018 | 11CF0056 | 00000000 | beq t6,t7,0x43f124 | nop | Virus on Siberia: show Siberia in the offline level list too | v5.3 · 2026-10-16 |

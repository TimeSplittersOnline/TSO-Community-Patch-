# Multikill, Multikill Window

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E4D46 | 33 bytes | xbreadfail_sp | eax = the window in seconds to show (1-5); keeps ecx/edx | v5.3 · 2026-10-16 |
| 008E4D67 | 37 bytes | xbreadfail_sp | mk.s's effective setting (jmp at 0x8e9100, its first 9 bytes: push %ecx / push %edx / movzbl MKVAR,%eax): Off in a Gun Game or Showdown match | v5.89 · 2026-10-27 |
| 008E4D8C | 174 bytes | xbreadfail_sp | Advanced page (jne at 0x8e8aeb, was to mk.s's item step): Multikill, Multikill Window | v5.3 · 2026-10-16 |
| 008E4E3A | 107 bytes | xbreadfail_sp | refresh (jmp at 0x8e8d4a, was to mk.s's refresh step; esi = page) | v5.3 · 2026-10-16 |
| 008E4EA5 | 73 bytes | xbreadfail_sp | (menu, 1 when Gun Game is chosen for the menu's mode; cdecl): Multikill greyed out with Gun Game, Multikill Window greyed out with Gun Game or while Multikill is Off | v5.3 · 2026-10-16 |
| 008E4EEE | 44 bytes | xbreadfail_sp | Multikill changefn (menu, item; cdecl): Multikill Window only selectable with Multikill On | v5.3 · 2026-10-16 |
| 008E4F1A | 140 bytes | xbreadfail_sp | apply (jmp at 0x8e8d8f, was to mk.s's apply step; esi = page): the window kept, MKVAR = window when On, else 0 | v5.3 · 2026-10-16 |
| 008E7AAE | 10 bytes | xbreadfail_sp | Menu / message text "Multikill" | v5.3 · 2026-10-16 |
| 008E7AB8 | 17 bytes | xbreadfail_sp | Menu / message text "Multikill Window" | v5.3 · 2026-10-16 |
| 008E9100 | 106 bytes | xbreadfail_sp | eax = effective setting for the match being played (0 = off); keeps other registers | v5.3 · 2026-10-16 |
| 008E916A | 308 bytes | xbreadfail_sp | add-kill routine after the kill is counted (call at 0x64fb4): esi killer, edx victim chr | v5.16 · 2026-10-17 |
| 008E929E | 76 bytes | xbreadfail_sp | kill count routine before the lives / suicide adjustments (call at 0x64afc): esi chr, edi kills | v5.16 · 2026-10-17 |
| 008E92EA | 136 bytes | xbreadfail_sp | Advanced Settings item (call at 0x8e8f30, replaces the folder group's text-margin call) | v5.3 · 2026-10-16 |
| 008E9372 | 45 bytes | xbreadfail_sp | refresh tail (jmp at 0x8e8d4a), esi = page | v5.3 · 2026-10-16 |
| 008E939F | 72 bytes | xbreadfail_sp | apply tail (jmp at 0x8e8d8f), esi = page: store, and put both settings in the setup sent to LAN players | v5.3 · 2026-10-16 |
| 008E93E7 | 18 bytes | xbreadfail_sp | sound loader decision (call at 0x46041, replaces mov 8(%ecx),%eax; test $0x20,%al): always load the multikill sound | v5.3 · 2026-10-16 |
| 008E93F9 | 6 bytes | xbreadfail_sp | Data: SECS | v5.3 · 2026-10-16 (approx.) |
| 008E93FF | 21 bytes | xbreadfail_sp | Data: OK | v5.3 · 2026-10-16 |
| 008E9414 | 64 bytes | xbreadfail_sp | Code: KMSG (see the code shown) | v5.3 · 2026-10-16 |
| 008E9454 | 23 bytes | xbreadfail_sp | Menu / message text "Multikill Bonus Window" | v5.3 · 2026-10-16 |
| 008E946B | 4 bytes | xbreadfail_sp | Menu / message text "Off" | v5.3 · 2026-10-16 (approx.) |
| 008E946F | 9 bytes | xbreadfail_sp | Menu / message text "1 Second" | v5.3 · 2026-10-16 |
| 008E9478 | 10 bytes | xbreadfail_sp | Menu / message text "2 Seconds" | v5.3 · 2026-10-16 |
| 008E9482 | 10 bytes | xbreadfail_sp | Menu / message text "3 Seconds" | v5.3 · 2026-10-16 |
| 008E948C | 10 bytes | xbreadfail_sp | Menu / message text "4 Seconds" | v5.3 · 2026-10-16 |
| 008E9496 | 10 bytes | xbreadfail_sp | Menu / message text "5 Seconds" | v5.3 · 2026-10-16 |
| 008E9600 | 512 bytes | xbreadfail_sp | Multikill state: last kill frame, bonus, chain count, message text (32 players). | v5.3 · 2026-10-16 (approx.) |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 001123D8 | 8DED0008 | 0803C05D | lw t5,8(t7) | j 0xf0174 | Multikill Bonus Window (Advanced Settings: Off / 1 / 2 / 3 / 4 / 5 Seconds) for Deathmatch, Team Deathmatch, Shrink, Regeneration, Leech, Gladiator, Monkey Assistant: from a triple kill (each kill within the time of the last), the kill scores 2, then 3, then 4 points. Host decides scores on LAN; patched players get a centre-screen "<name> - Triple Kill!" message and the monkey-curling score jingle (always loaded at level start) (setting sent in a spare setup byte) | v5.16 · 2026-10-17 |
| 001123DC | 31AE0020 | 00000000 | andi t6,t5,0x20 | nop | Multikill Bonus Window (Advanced Settings: Off / 1 / 2 / 3 / 4 / 5 Seconds) for Deathmatch, Team Deathmatch, Shrink, Regeneration, Leech, Gladiator, Monkey Assistant: from a triple kill (each kill within the time of the last), the kill scores 2, then 3, then 4 points. Host decides scores on LAN; patched players get a centre-screen "<name> - Triple Kill!" message and the monkey-curling score jingle (always loaded at level start) (setting sent in a spare setup byte) | v5.16 · 2026-10-17 |
| 0013A118 | 25EF8E50 | 0803FD50 | addiu t7,t7,-29104 | j 0xff540 | Multikill Bonus Window (Advanced Settings: Off / 1 / 2 / 3 / 4 / 5 Seconds) for Deathmatch, Team Deathmatch, Shrink, Regeneration, Leech, Gladiator, Monkey Assistant: from a triple kill (each kill within the time of the last), the kill scores 2, then 3, then 4 points. Host decides scores on LAN; patched players get a centre-screen "<name> - Triple Kill!" message and the monkey-curling score jingle (always loaded at level start) (setting sent in a spare setup byte) | v5.16 · 2026-10-17 |
| 0013A11C | 8DEE006C | 00000000 | lw t6,108(t7) | nop | Multikill Bonus Window (Advanced Settings: Off / 1 / 2 / 3 / 4 / 5 Seconds) for Deathmatch, Team Deathmatch, Shrink, Regeneration, Leech, Gladiator, Monkey Assistant: from a triple kill (each kill within the time of the last), the kill scores 2, then 3, then 4 points. Host decides scores on LAN; patched players get a centre-screen "<name> - Triple Kill!" message and the monkey-curling score jingle (always loaded at level start) (setting sent in a spare setup byte) | v5.16 · 2026-10-17 |
| 0013A940 | 26728E50 | 0803FAC0 | addiu s2,s3,-29104 | j 0xfeb00 | Multikill Bonus Window (Advanced Settings: Off / 1 / 2 / 3 / 4 / 5 Seconds) for Deathmatch, Team Deathmatch, Shrink, Regeneration, Leech, Gladiator, Monkey Assistant: from a triple kill (each kill within the time of the last), the kill scores 2, then 3, then 4 points. Host decides scores on LAN; patched players get a centre-screen "<name> - Triple Kill!" message and the monkey-curling score jingle (always loaded at level start) (setting sent in a spare setup byte) | v5.16 · 2026-10-17 |
| 0013A944 | 240F0009 | 00000000 | addiu t7,zero,9 | nop | Multikill Bonus Window (Advanced Settings: Off / 1 / 2 / 3 / 4 / 5 Seconds) for Deathmatch, Team Deathmatch, Shrink, Regeneration, Leech, Gladiator, Monkey Assistant: from a triple kill (each kill within the time of the last), the kill scores 2, then 3, then 4 points. Host decides scores on LAN; patched players get a centre-screen "<name> - Triple Kill!" message and the monkey-curling score jingle (always loaded at level start) (setting sent in a spare setup byte) | v5.16 · 2026-10-17 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FBB44-000FF76B | 339 | Multikill Bonus Window (Advanced Settings: Off / 1 / 2 / 3 / 4 / 5 Seconds) for Deathmatch, Team Deathmatch, Shrink, Regeneration, Leech, Gladiator, Monkey Assistant: from a triple kill (each kill within the time of the last), the kill scores 2, then 3, then 4 points. Host decides scores on LAN; patched players get a centre-screen "<name> - Triple Kill!" message and the monkey-curling score jingle (always loaded at level start) (setting sent in a spare setup byte) | v5.16 · 2026-10-17 |
| 000E8474-000E8577 | 65 | MKITEM2: Advanced page step (address loaded at 0xFBE44, was mk.py's MKA): Multikill, Multikill Window, then MKA's tail | v5.3 · 2026-10-16 |
| 000E9928-000E99FF | 54 | MKAP2: apply (j at 0xFBB98, was to mk.py's MKE2; s0 = page): window kept, MKVAR = window when On, else 0; then the Infinite Ammo / Weapon Mode apply, byte 73 for LAN players (Off when the match will be Gun Game), MKE2's tail | v5.3 · 2026-10-16 |
| 000EBEE0-000EBF7B | 39 | MKR2: refresh (j at 0xFBB44, was to mk.py's MKE1; s0 = page): values, changefn, greying; then MKE1's tail | v5.3 · 2026-10-16 |
| 000ECEE0-000ECF5F | 32 | MKEFF2: j from mk.py's MKEFF (its first two words): Off in a Gun Game or Showdown match, else on with MKEFF; uses t5,t6,t8,t9 | v5.89 · 2026-10-27 |
| 000ED7A8-000ED81F | 30 | MKGR: a0 = page, a1 = 1 when Gun Game is chosen for the menu's mode: Multikill greyed out with Gun Game, Multikill Window greyed out with Gun Game or while Multikill is Off | v5.3 · 2026-10-16 |
| 000EF754-000EF797 | 17 | MKCH: Multikill changefn (a0 = page, a1 = item): Multikill Window only selectable with Multikill On | v5.3 · 2026-10-16 |
| 000EF820-000EF85F | 16 | MKLF: mk.py (built into the base pnach) and its new-match checks (t2 = gameframe, t1 = that chr's last kill frame, t8 = the gameframe below it), as everywhere only in the match's first 20 seconds: leaf, the kill chain (jal at 0xFF3FC, was bne t8,zero,new; returns to beq t0,zero,new): a gameframe that stepped back later is not a new match: t1 = the gameframe (no time passed, the chain goes on); in the first 20 seconds t0 = 0 | v5.16 · 2026-10-17 |
| 000EF920-000EF95B | 15 | MKWS: leaf: v0 = the window in seconds to show (1-5): MKVAR if set, else the last window, else 3; uses t6,t7 | v5.3 · 2026-10-16 |
| 000F03B4-000F03C7 | 5 | LMKW: text | v5.3 · 2026-10-16 |
| 000F0644-000F064F | 3 | LMKO: text | v5.3 · 2026-10-16 |
| 000FCEC4-000FCEFF | 15 | MKCMP: leaf, kill count routine' bonus kills (jal at 0xFF56C, was beq t8,zero,keep; returns to their clearing): cleared only when the gameframe went back into the first 20 seconds, else on at keep; uses t8, t9 | v5.16 · 2026-10-17 |

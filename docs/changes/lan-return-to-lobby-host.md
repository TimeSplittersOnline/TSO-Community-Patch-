# LAN: Return to Lobby (host)

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 002D7647 | 2C7647 | 5 | `be bc e3 4e 00` | `e9 6c 73 5f 00` | Menus rebuilt after a match with the lost-connection flag set (cable check failed or host lost): jumps to XFELB, which clears the flag (as the Xbox Live / System Link choice page does when it opens; the mod skips that page, so it used to stay set), then sends a console still hosting its running System Link session to its lobby and anything else to the System Link match list 0x4ee66c instead of the choice page 0x4ee3bc. Xbox only. | v5.94 · 2026-10-27 |
| 002ED385 | 2DD385 | 5 | `e9 26 ff ff ff` | `e9 81 9b 5f 00` | leave-confirm page: Yes \| its Yes (jmp at 0x2ed385, was jmp 0x2ed2b0: leave the match) \| its Yes (jmp at 0x2ed385, was jmp 0x2ed2b0: leave the match) | v5.3 · 2026-10-16 |
| 002ED418 | 2DD418 | 5 | `e8 53 0d d5 ff` | `e8 cb 9a 5f 00` | leave-confirm page: its question \| the leave-confirm page's question (call at 0x2ed418, was call 0x3e170 for text 0x1a7e) \| the leave-confirm page's question (call at 0x2ed418, was call 0x3e170 for text 0x1a7e) | v5.3 · 2026-10-16 |
| 002F407A | 2E407A | 5 | `e8 b1 c5 06 00` | `b8 01 00 00 00` | End-of-match menu, host branch: the update's "Return to Lobby" item now shows on LAN too (was: call 0x360630, the Xbox Live check; now mov $1,%eax). | v5.21 · 2026-10-17 |
| 002F4095 | 2E4095 | 5 | `68 30 d5 2e 00` | `68 16 70 8e 00` | End-of-match menu: that item's callback is XRLCB (LAN: the game's own return to the lobby; Xbox Live: the update's 0x2ed530 as before) (was: push $0x2ed530). | v5.3 · 2026-10-16 |
| 002F6BA5 | 2E6BA5 | 5 | `a1 e0 97 80 00` | `e8 32 02 5f 00` | match-over pause page: Return to Lobby (LAN host) \| pause menu (call at 0x2f6ba5, was mov 0x8097e0,%eax; esi = page): the host's first player gets "Return to Lobby" on LAN \| pause menu (call at 0x2f6ba5, was mov 0x8097e0,%eax; esi = page): the host's first player gets "Return to Lobby" on LAN | v5.21 · 2026-10-17 |
| 002F706D | 2E706D | 5 | `e8 9e d7 05 00` | `e8 06 fe 5e 00` | in-match pause menu (Options tab): Manage Players just above Leave Match \| in-match pause menu, Options tab (call at 0x2f706d just before its Leave Match, was call 0x354810; ebp = page): the LAN host's \| in-match pause menu, Options tab (call at 0x2f706d just before its Leave Match, was call 0x354810; ebp = page): the LAN host's first player gets "Manage Players" there when someone can be managed; eax = network game flag as before | v5.3 · 2026-10-16 |
| 002F70A0 | 2E70A0 | 5 | `e8 6b d7 05 00` | `e8 8a fd 5e 00` | in-match pause menu (Options tab): Return to Lobby after Leave Match \| in-match pause menu, Options tab (builder 0x2f6e30; call at 0x2f70a0 after its Leave Match, was call 0x354810; ebp = page): the \| in-match pause menu, Options tab (builder 0x2f6e30; call at 0x2f70a0 after its Leave Match, was call 0x354810; ebp = page): the host's first player gets "Return to Lobby" on LAN; eax = network game flag as before | v5.3 · 2026-10-16 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008CE9B8 | 75 bytes | xbreadfail_sp | ---------------- Manage Players: a kick during a Weapon Mode hand-out | v5.94 · 2026-10-27 |
| 008E6D78 | 100 bytes | xbreadfail_sp | pause menu (call at 0x2f6ba5, was mov 0x8097e0,%eax; esi = page): the host's first player gets "Return to Lobby" on LAN | v5.99 · 2026-10-28 |
| 008E6DDC | 83 bytes | xbreadfail_sp | pause menu (call at 0x2f6ba5, was mov 0x8097e0,%eax; esi = page): the host's first player gets "Return to Lobby" on LAN | v5.21 · 2026-10-17 |
| 008E6E2F | 73 bytes | xbreadfail_sp | in-match pause menu, Options tab (builder 0x2f6e30; call at 0x2f70a0 after its Leave Match, was call 0x354810; ebp = page): the host's first player gets "Return to Lobby" on LAN; eax = network game flag as before | v5.25 · 2026-10-17 |
| 008E6E78 | 75 bytes | xbreadfail_sp | in-match pause menu, Options tab (call at 0x2f706d just before its Leave Match, was call 0x354810; ebp = page): the LAN host's first player gets "Manage Players" there when someone can be managed; eax = network game flag as before | v5.106 · 2026-10-29 |
| 008E6EC3 | 37 bytes | xbreadfail_sp | its callback (both pause items): the leave-confirm page (0x529b90) with our question, as Leave Match opens it (0x2ed5a0) | v5.21 · 2026-10-17 |
| 008E6EE8 | 35 bytes | xbreadfail_sp | the leave-confirm page's question (call at 0x2ed418, was call 0x3e170 for text 0x1a7e) | v5.37 · 2026-10-19 |
| 008E6F0B | 49 bytes | xbreadfail_sp | its Yes (jmp at 0x2ed385, was jmp 0x2ed2b0: leave the match) | v5.37 · 2026-10-19 |
| 008E6F3C | 127 bytes | xbreadfail_sp | Manage Players kick, confirmed (XRLYES, 4(%esp) = the page's item): if the row's player is still there and still the one asked about, the game's drop (network player entry, reason 2 kicked); then back to the Manage Players page as the page's No does (0x2ed372) | v5.106 · 2026-10-29 |
| 008E6FBB | 91 bytes | xbreadfail_sp | end-of-match menu, the host's "Return to Lobby" (push at 0x2f4095, was push $0x2ed530; shown on LAN too: the Live check at 0x2f407a is now mov $1,%eax): Xbox Live as before, LAN ours the Scores page's player rows (jmp at 0x2f2072, was cmp $9,%al / jne 0x2f209e / testb $1,0x82d258 / je 0x2f209e; al = the game type): Deathmatch with Teamplay shows the Team Deathmatch number (kills of other teams); Team Elimination / Vampire with lives (also Deathmatch with Teamplay) the game's own lives / time instead (0x2f209e: "N Lives" for a player still in, else the time) | v5.99 · 2026-10-28 |
| 008E7016 | 18 bytes | xbreadfail_sp | Code: XRLCB (see the code shown) | v5.21 · 2026-10-17 |
| 008E7028 | 50 bytes | xbreadfail_sp | Menu / message text "Return everyone to the lobby? The match will end." | v5.21 · 2026-10-17 |
| 008E705A | 46 bytes | xbreadfail_sp | ---- Score page, team rows (0x2f22a0, drawn on consoles where Bag Tag has Teamplay, so only with the patch): each team's score | v5.99 · 2026-10-28 |

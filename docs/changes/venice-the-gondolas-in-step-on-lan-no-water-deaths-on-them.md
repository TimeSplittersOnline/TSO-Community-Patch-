# Venice: the gondolas in step on LAN, no water deaths on them

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E6F84 | 240 bytes | xbreadfail_sp | ---- Score page, team rows (0x2f22a0, drawn on consoles where Bag Tag has Teamplay, so only with the patch): each team's score goes through sprintf (text, "%d", score) into an 8-byte stack buffer just under the function's return address. The XBE this mod started from sends that call (0x2f2353) to its own 0x11aa0, which in Bag Tag writes the team's bag time with the game's time text (0x65a20, e.g. "148.5 secs"): longer than 7 characters, it ran over the return address and the console crashed when the score page was shown. Here (call at 0x2f2353, was call 0x11aa0; cdecl text, format, score): Bag Tag: the time as the Results page shows it, m:ss.t ("2:28.5", at most "99:59.9", 7 characters); otherwise sprintf as before | v5.86 · 2026-10-27 |
| 008E7074 | 12 bytes | xbreadfail_sp | ---------------- Manage Players (LAN host, during a match): move a player to another team, or kick a player off another console. | v5.29 · 2026-10-18 |

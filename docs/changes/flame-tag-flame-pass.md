# Flame Tag: Flame Pass

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 008E29D4 | 48 bytes | xbreadfail_sp | eax = setting (1 Kill / 2 Touch Or Kill) when Flame Pass applies (Flame Tag, LAN host), else 0; keeps other registers | v5.3 · 2026-10-16 |
| 008E2A04 | 23 bytes | xbreadfail_sp | every frame (XGGT): Kill only -> the touch check never passes (distance^2 limit 0); else the normal 1.2 m | v5.3 · 2026-10-16 |
| 008E2A1B | 78 bytes | xbreadfail_sp | kills (XINFK's exit, then jmp 0x8e916a multikill; esi = killer or 0, edx = victim): Kill / Touch Or Kill: a burning player who kills a player not on fire passes the flame to them | v5.3 · 2026-10-16 |
| 008E2A69 | 84 bytes | xbreadfail_sp | Flame Tag menu, LAN only: Flame Pass | v5.3 · 2026-10-16 |
| 008E2ABD | 36 bytes | xbreadfail_sp | refresh / apply (esi = page) | v5.3 · 2026-10-16 |
| 008E2AE1 | 35 bytes | xbreadfail_sp | ---------------- Coin Rush / Coin Drop (Advanced Settings, Thief), decided by the host (offline: this game) | v5.3 · 2026-10-16 |
| 008E79D4 | 11 bytes | xbreadfail_sp | Menu / message text "Flame Pass" | v5.3 · 2026-10-16 |
| 008E79DF | 6 bytes | xbreadfail_sp | Menu / message text "Touch" | v5.3 · 2026-10-16 (approx.) |
| 008E79E5 | 5 bytes | xbreadfail_sp | Menu / message text "Kill" | v5.3 · 2026-10-16 (approx.) |
| 008E79EA | 14 bytes | xbreadfail_sp | Menu / message text "Touch Or Kill" | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000EB05C-000EB10F | 45 | FPK: kills (INFK's exit, then j 0xFF370 multikill; s0 = killer data or 0, s1 = victim data): Flame Pass Kill / Touch Or Kill: a burning player who kills a player not on fire passes the flame to them | v5.3 · 2026-10-16 |
| 000EC4E4-000EC57B | 38 | FPITEM: Flame Tag menu, LAN only: Flame Pass | v5.3 · 2026-10-16 |
| 000EEF48-000EEF9B | 21 | FPRA: a0 = page, a1 = 0 refresh / 1 apply: Flame Pass value | v5.3 · 2026-10-16 |
| 000F0480-000F048F | 4 | LFP2: text | v5.3 · 2026-10-16 |
| 000F05CC-000F05D7 | 3 | LFP: text | v5.3 · 2026-10-16 |
| 000F06A4-000F06AB | 2 | LFP0: text | v5.3 · 2026-10-16 (approx.) |
| 000F06AC-000F06B3 | 2 | LFP1: text | v5.3 · 2026-10-16 (approx.) |
| 000FC040-000FC11F | 56 | FPT: Flame Tag touch passing (j at 0xFCD1C, the start of the host's touch check; delay slot harmless; s2 = who is on fire among the players there, s1 = how many flames there should be): more than that (a player not on fire left), one is put | v5.69 · 2026-10-23 |

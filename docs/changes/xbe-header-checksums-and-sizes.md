# XBE header (checksums and sizes)

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00010394 | 000394 | 20 | `12 2e b5 1f 81 fb 61 2e 40 65 cd 5b 5c 2d 23 e4 11 16 9a 60` | `39 7d 6d de 67 30 e4 f1 3f dc 2f ba 8b 6c 41 e6 63 57 71 38` | SHA-1 digest of section .text (recalculated so the Xbox accepts the changed file) | v5.98 · 2026-10-28 |
| 00010570 | 000570 | 1 | `74` | `7c` | virtual size of section .data (RAM after the file data, used by mod variables) | v5.3 · 2026-10-16 |
| 0001058C | 00058C | 20 | `32 81 c1 b2 ef 63 8d 3b 01 c1 1d 7d 3a af 84 83 af 93 94 8f` | `0d b0 57 df 4a 65 ea e9 bd 6d 93 e9 c1 a9 80 7a 5f da 45 d7` | SHA-1 digest of section .data (recalculated so the Xbox accepts the changed file) | v5.40 · 2026-10-19 |
| 0001082C | 00082C | 20 | `1c 9c 13 e6 62 f4 bf fc c1 82 70 09 9e 60 63 99 36 cd 38 da` | `4f dd 13 c0 90 36 76 b0 fe 22 00 dd 25 68 90 31 78 39 ee 26` | SHA-1 digest of section xbreadfail_sp (recalculated so the Xbox accepts the changed file) | v5.98 · 2026-10-28 |

## Xbox: added code

| Address | Size | Where | Purpose | Since |
|---|---|---|---|---|
| 00011D9C | 20 bytes | XBE header | Leftover copy of the PC (PE) section table, not used when the game runs: cleared. | v5.3 · 2026-10-16 (approx.) |
| 00011FF4 | 4 bytes | XBE header | Leftover copy of the PC (PE) header, not used when the game runs: cleared. | v5.3 · 2026-10-16 (approx.) |
| 008DE001 | 3071 bytes | xbreadfail_sp | Leftover copy of the PC (PE) header, not used when the game runs: cleared. | v5.3 · 2026-10-16 (approx.) |

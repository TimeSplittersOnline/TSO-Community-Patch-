# MapMaker limits and story maps

## Xbox: changes to the game's own code and data

| Address | File offset | Bytes | Original | New | Purpose | Since |
|---|---|---|---|---|---|---|
| 00529D0C | 51A32C | 1 | `20` | `ff` | MapMaker item limit (was 32) raised to 255. | v5.3 · 2026-10-16 |
| 00529D54 | 51A374 | 1 | `3c` | `ff` | MapMaker item limit (was 60) raised to 255. | v5.3 · 2026-10-16 |
| 00529D6C | 51A38C | 1 | `3c` | `ff` | MapMaker item limit (was 60) raised to 255. | v5.3 · 2026-10-16 |
| 00529D84 | 51A3A4 | 1 | `78` | `ff` | MapMaker item limit (was 120) raised to 255. | v5.3 · 2026-10-16 |
| 00529DE4 | 51A404 | 1 | `78` | `ff` | MapMaker item limit (was 120) raised to 255. | v5.3 · 2026-10-16 |
| 00529DFC | 51A41C | 1 | `78` | `ff` | MapMaker item limit (was 120) raised to 255. | v5.3 · 2026-10-16 |
| 00529E14 | 51A434 | 1 | `78` | `ff` | MapMaker item limit (was 120) raised to 255. | v5.3 · 2026-10-16 |
| 00529E2C | 51A44C | 1 | `78` | `ff` | MapMaker item limit (was 120) raised to 255. | v5.3 · 2026-10-16 |
| 00529E44 | 51A464 | 1 | `0a` | `ff` | MapMaker item limit (was 10) raised to 255. | v5.3 · 2026-10-16 |
| 00529E5C | 51A47C | 1 | `0a` | `ff` | MapMaker item limit (was 10) raised to 255. | v5.3 · 2026-10-16 |
| 00529E8C | 51A4AC | 1 | `0a` | `ff` | MapMaker item limit (was 10) raised to 255. | v5.3 · 2026-10-16 |
| 00529EA4 | 51A4C4 | 1 | `0a` | `ff` | MapMaker item limit (was 10) raised to 255. | v5.3 · 2026-10-16 |
| 00529ED4 | 51A4F4 | 1 | `78` | `ff` | MapMaker item limit (was 120) raised to 255. | v5.3 · 2026-10-16 |
| 00529EEC | 51A50C | 1 | `78` | `ff` | MapMaker item limit (was 120) raised to 255. | v5.3 · 2026-10-16 |
| 00529F04 | 51A524 | 1 | `01` | `ff` | MapMaker item limit (was 1) raised to 255. | v5.3 · 2026-10-16 |
| 00529F4C | 51A56C | 1 | `64` | `ff` | MapMaker item limit (was 100) raised to 255. | v5.3 · 2026-10-16 |
| 00529F64 | 51A584 | 1 | `64` | `ff` | MapMaker item limit (was 100) raised to 255. | v5.3 · 2026-10-16 |
| 00529F7C | 51A59C | 1 | `20` | `ff` | MapMaker item limit (was 32) raised to 255. | v5.3 · 2026-10-16 |
| 00529F94 | 51A5B4 | 1 | `20` | `ff` | MapMaker item limit (was 32) raised to 255. | v5.3 · 2026-10-16 |
| 00529FAC | 51A5CC | 1 | `20` | `ff` | MapMaker item limit (was 32) raised to 255. | v5.3 · 2026-10-16 |

## PS2: changes to the game's own code and data

NTSC address first; the PAL address follows where it differs.

| Address | Original | New | Original (instruction) | New (instruction) | Purpose | Since |
|---|---|---|---|---|---|---|
| 00481F68 / PAL 00482008 | 24150028 | 241500FF | addiu s5,zero,40 | addiu s5,zero,255 | mod: MapMaker item limit 40 -> 255 | v5.3 · 2026-10-16 |
| 004823C0 / PAL 00482460 | 2415001E | 241500FF | addiu s5,zero,30 | addiu s5,zero,255 | mod: MapMaker item limit 30 -> 255 | v5.3 · 2026-10-16 |
| 006B6BD4 / PAL 006B6CD4 | 00000020 | 000000FF | .ascii " \0\0\0" | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6BEC / PAL 006B6CEC | 00000020 | 000000FF | .ascii " \0\0\0" | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6C04 / PAL 006B6D04 | 00000010 | 000000FF | mfhi zero,zero,zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6C1C / PAL 006B6D1C | 00000001 | 000000FF | .word 0x00000001 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6C34 / PAL 006B6D34 | 00000001 | 000000FF | .word 0x00000001 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6C4C / PAL 006B6D4C | 00000001 | 000000FF | .word 0x00000001 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6C64 / PAL 006B6D64 | 00000004 | 000000FF | sllv zero,zero,zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6C7C / PAL 006B6D7C | 00000001 | 000000FF | .word 0x00000001 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6C94 / PAL 006B6D94 | 00000020 | 000000FF | .ascii " \0\0\0" | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6CAC / PAL 006B6DAC | 00000020 | 000000FF | .ascii " \0\0\0" | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6CC4 / PAL 006B6DC4 | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6CDC / PAL 006B6DDC | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6CF4 / PAL 006B6DF4 | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6D0C / PAL 006B6E0C | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6D24 / PAL 006B6E24 | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6D3C / PAL 006B6E3C | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6D54 / PAL 006B6E54 | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6D6C / PAL 006B6E6C | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6D84 / PAL 006B6E84 | 00000002 | 000000FF | srl zero,zero,0 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6D9C / PAL 006B6E9C | 00000010 | 000000FF | mfhi zero,zero,zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6DB4 / PAL 006B6EB4 | 00000010 | 000000FF | mfhi zero,zero,zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6DCC / PAL 006B6ECC | 0000000C | 000000FF | .word 0x0000000C | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6DE4 / PAL 006B6EE4 | 00000001 | 000000FF | .word 0x00000001 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6DFC / PAL 006B6EFC | 00000010 | 000000FF | mfhi zero,zero,zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6E14 / PAL 006B6F14 | 00000032 | 000000FF | .ascii "2\0\0\0" | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6E2C / PAL 006B6F2C | 00000014 | 000000FF | .word 0x00000014 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6E44 / PAL 006B6F44 | 00000014 | 000000FF | .word 0x00000014 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6E5C / PAL 006B6F5C | 00000008 | 000000FF | jr zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6E74 / PAL 006B6F74 | 00000008 | 000000FF | jr zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6E8C / PAL 006B6F8C | 00000008 | 000000FF | jr zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6EA4 / PAL 006B6FA4 | 0000000A | 000000FF | movz zero,zero,zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6EBC / PAL 006B6FBC | 00000020 | 000000FF | .ascii " \0\0\0" | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6ED4 / PAL 006B6FD4 | 00000014 | 000000FF | .word 0x00000014 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6EEC / PAL 006B6FEC | 00000042 | 000000FF | srl zero,zero,1 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6F04 / PAL 006B7004 | 00000042 | 000000FF | srl zero,zero,1 | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6F1C / PAL 006B701C | 00000004 | 000000FF | sllv zero,zero,zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 006B6F34 / PAL 006B7034 | 00000004 | 000000FF | sllv zero,zero,zero | .word 0x000000FF | MapMaker: per-item limits -> 255 (all 37 item types) | v5.3 · 2026-10-16 |
| 004823E4 / PAL 00482484 | 24150064 | 241500FF | addiu s5,zero,100 | addiu s5,zero,255 | MapMaker: placement limit 100 -> 255 | v5.3 · 2026-10-16 |
| 006D19D4 / PAL 006D1AD4 | 00000004 | 00000007 | sllv zero,zero,zero | srav zero,zero,zero | mod: option record 4 -> 7 (MapMaker story character select) | v5.3 · 2026-10-16 |
| 00439C78 | 15CF0080 | 10000080 | bne t6,t7,0x439e7c | beq zero,zero,0x439e7c | mod: MapMaker story maps - always build character select list | v5.3 · 2026-10-16 |
| 0043898C | 11CF0250 | 00000000 | beq t6,t7,0x4392d0 | nop | mod: MapMaker story maps - keep chosen character | v5.3 · 2026-10-16 |
| 0043E37C / PAL 0043E3CC | 122F0056 | 0C03F86C | beq s1,t7,0x43e4d8 | jal 0xfe1b0 | LAN: Story and Monkey Assistant removed from the mode list (not supported over LAN) | v5.3 · 2026-10-16 |

## PS2: added code (memory the game never uses)

| Addresses | Words | Purpose | Since |
|---|---|---|---|
| 000FE1B0-000FE203 | 21 | LAN: Story and Monkey Assistant removed from the mode list (not supported over LAN) | v5.3 · 2026-10-16 |

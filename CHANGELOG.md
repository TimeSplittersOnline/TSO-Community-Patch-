# TSFP mod changelog

Entries before 14 Oct 2026 were rebuilt from the dates of the working files, so times are approximate and small fixes inside a day are folded together. From 14 Oct on, every delivered build adds an entry here. Versions: v<major>.<minor>, shown in-game on the Advanced Settings title.

## v5.103 · 2026-10-29 · LAN: the Temporal Uplink is taken out of the weapon set the host sends, so MapMaker maps don't get it either

*v5.103 · UplinkLanSet* · Xbox, PS2 NTSC, PS2 PAL

- Since v5.102 the Temporal Uplink can be in weapon sets again offline, so a custom set saved with it could be used to host a LAN game. The match's own list already left it out, but MapMaker maps take their guns straight from the host's weapon set, so their Uplink spots could still appear on LAN, where the Uplink crashes the game.
- A patched host now takes the Uplink out of the weapon set it sends to everyone (and keeps for itself). Every console, with or without the patch, then builds the map from the same set and leaves out the same gun spots, so the map stays in step. Offline nothing changes.
- Xbox, MapMaker maps on LAN: a host with a custom weapon set saved built the map's guns from its own copy of that set, while its clients use the set it sent (unlike PS2, the Xbox game already does that for clients). Both held the same guns until now; with the Uplink taken out of the sent set they could differ, so on LAN the Xbox host now also uses the set it sent, as PS2 does since v5.102.

## v5.102 · 2026-10-29 · PS2 MapMaker maps on LAN: weapons, zones and bags in step with the host; Temporal Uplink back offline

*v5.102 · MapMakerLanWeapons* · Xbox, PS2 NTSC, PS2 PAL

- PS2, MapMaker maps on LAN (a bug in the original game): a console whose own saved Weapon Set choice was a custom set built the map without any of its gun items, because it looked for that custom set on its own console, where a LAN player's game doesn't have it. The map's items were then numbered differently from the host's, so on that console guns didn't appear, armour and health didn't disappear when taken, zones didn't change colour (or didn't show), and bags and the HUD were wrong.
- With the patch, a PS2 console on LAN always builds a MapMaker map's guns from the weapon set the host sends, whatever it has saved itself, so it matches the host. Offline play is unchanged, and it works with an unpatched host.
- Players without the patch still have the original bug. Workaround: on that console pick a built-in weapon set (Recommended, Assorted, Plasma, Conventional, Neon, Retro, Rockets, Doubles or Explosives), start any match so the choice is saved, then join. The host can use any set.
- Temporal Uplink: since v5.99 it was taken out of every weapon list and every match. It is now only taken out on LAN, where it crashes the game. Offline it is back in the weapon lists and in weapon sets as in the original game (Xbox and PS2).

## v5.101 · 2026-10-28 · Spectate on LAN players' consoles: a joiner placed out no longer counts as still in

*v5.101 · SpectateJoinerLives* · Xbox, PS2 NTSC, PS2 PAL

- Team Elimination / Team Vampire on LAN: a player who joined mid-match onto a team with nobody still in is placed out by the host with no lives (since v5.98), but the other consoles kept the lives that player joined with. On those consoles Spectate counted them as still in. With Teamplay their team-mates couldn't switch to watching the other teams (they were left on their own death view), and from v5.100 free cam stayed off for that team for the rest of the match.
- Spectate on a LAN player's console now also goes by the lives the host sends every console (the number every game keeps a player dead by), so it agrees with the host. The host and offline play are unchanged.

## v5.100 · 2026-10-28 · Spectate: with Teamplay, free cam only once your team is out

*v5.100 · FreecamTeamOut* · Xbox, PS2 NTSC, PS2 PAL

- Spectate (Elimination / Vampire) with Teamplay: free cam can't be turned on while anyone on your team is still in (alive, or waiting to respawn with lives left), so a player who is out can't scout the other teams for team-mates who are still playing. You can still watch your team-mates as before. Once your whole team is out, free cam works as before.
- While free cam isn't available, the spectate button hints leave out "Freecam". If a team-mate is back in while you're in free cam (moved to your team, or a player joining), free cam ends and you go back to watching a team-mate. Turning free cam off always works. Without Teamplay nothing changes.

## v5.99 · 2026-10-28 · Bug fixes: team rows, kicks, Showdown setting, score rows, Temporal Uplink

*v5.99 · BugFixRound599* · Xbox, PS2 NTSC, PS2 PAL

- Scores page, Team Elimination / Team Vampire with team lives: a team's row showed your own lives instead of the team's (and changed once you were out). It now shows the team's lives while it has any.
- Team Elimination / Team Vampire: the team time no longer counts a player who isn't in the ranking (still choosing a team), or one who just joined and hasn't been placed on a team yet.
- Manage Players: a kick still waiting at the end of the match (or when the host used Return to Lobby on Xbox) now happens then, instead of being dropped.
- Manage Players: a kick confirmed less than half a second after the player's own weapon switch setting was sent back to them now also waits half a second, so that setting can still be resent before their connection closes.
- Advanced Settings: applying the page for a mode without Showdown no longer forgets a Showdown setting you'd chosen for Elimination / Vampire.
- Scores page, Thief / Team VIP with Teamplay: player rows show the mode's own score again, instead of a kills number. The kills number now only shows in the modes scored by kills.
- Random Characters (Xbox): only the host's (or offline) game picks the characters. A LAN player's game no longer runs the pick on its own copy of the setup, as on PS2.
- PS2 online: the Advanced Settings link no longer shows on the online search filter page.
- Temporal Uplink: the game lists it twice in its weapon tables. Neither entry shows in the weapon lists any more, in any menu (offline or LAN); before, only the first was hidden, and only on LAN. A weapon set saved with the uplink in it (possible in earlier versions) has that slot emptied when the match starts (on consoles with the patch), and the PS2 weapon list flag an early version switched on is back to the game's own value. Gun Game and Random Weapon already never handed it out.

## v5.98 · 2026-10-28 · Team Elimination: late joiners and leavers no longer change team times; free cam faster with RT / R2

*v5.98 · JoinerTimeFreecamBoost* · Xbox, PS2 NTSC, PS2 PAL

- Team Elimination / Team Vampire: a player who joined mid-match on a team with nobody still in (so they spectate with no lives) counted towards their team's time as if they had just been knocked out, so a finished team could jump above a team that really outlasted it. They now don't count towards the team's time at all.
- Team Elimination / Team Vampire: a player who was knocked out and then left the match still counts towards their team's time, so a team no longer drops below a team it beat because its longest-lasting player quit afterwards.
- Spectate free cam: hold the right trigger (Xbox) / R2 (PS2) to move the camera twice as fast, whatever your controller layout; while free cam is on, the spectate button hints show "Speed up" for it. Only your own camera moves; nothing is sent to other consoles.

## v5.97 · 2026-10-28 · Manage Players in PS2 online play

*v5.97 · ManagePlayersOnline* · PS2 NTSC, PS2 PAL

- PS2: Manage Players now also shows for the host in online matches (revived servers). Kicks use the game's own drop, as when a player leaves, so the server's player and slot counts stay right and the kicked console goes back to the online menus.
- Online, all players on one console stay on one team (as the game keeps them at Select Team): moving or cancelling a move for one of them does the same for the others on that console, each switching at their own next death. LAN works as before.
- Online, cancelling a move after a guest on that console has already switched sends the guest back to the team shown, so the console stays together.
- Xbox: no change (it has no online play with the mod); version number only.

## v5.96 · 2026-10-28 · Manage Players: a kick during a Weapon Mode hand-out waits for the player's own setting

*v5.96 · KickWaits* · Xbox, PS2 NTSC, PS2 PAL

- v5.95 sent a kicked player's own weapon change on pickup back just before the kick, but the kick closes their connection at once, so if that one packet was lost they still kept "Always". Now their setting goes back at once and the kick happens half a second later (the setting is sent once more first), so a lost packet can be resent in time.
- The kick is skipped if by then it is a new match, this console is no longer the host, or someone else is in that player's place.
- While a kick waits, that player gets no new "Always" (e.g. a Gun Game level-up in that half second), so the setting sent back stays.

## v5.95 · 2026-10-27 · Fixes: Switch Spawns with Team Spawns off, kicks during a Weapon Mode hand-out, Zones in League / Challenges

*v5.95 · ThreeFixes* · Xbox, PS2 NTSC, PS2 PAL

- Capture the Bag on LAN with Switch Spawns On and Team Spawns Off: Switch Spawns looked greyed out but the host still sent it, so patched players often spawned at the other team's base (unpatched players didn't). The host now only sends it with Team Spawns on.
- Manage Players kick in Gun Game, Random Weapon or Showdown: a player kicked just after a hand-out could be left with their weapon change on pickup set to "Always". Their own setting is now sent back to their console before the kick.
- Zones: the last score of the held zones at time up now only happens in custom matches and on LAN, not in Story, Arcade League or Challenges (which play as the game made them).

## v5.94 · 2026-10-27 · Return to Lobby: the host back in its lobby, not the match list

*v5.94 · LobbyAfterMatch* · Xbox

- Xbox host: Return to Lobby after a match could land on the System Link match list while the lobby's countdown ran for everyone else, and then kept doing it on every later return until a restart. The game keeps a lost-connection flag that only the Xbox Live / System Link choice page cleared, and the mod skips that page, so once set it stayed set. Now the flag is cleared on the way back, and a host whose session is still running goes to its lobby.
- A client that really lost its host, or a console whose network cable was pulled, still goes to the match list as before.
- PS2: no change (no Return to Lobby on PS2); version number only.

## v5.93 · 2026-10-27 · Spectate: names and icons seen from the camera

*v5.93 · SpectateCameraSight* · Xbox, PS2 NTSC, PS2 PAL

- Watching another player or in free cam (Elimination / Vampire with Teamplay): names and icons over other players now show as if you were standing at the camera. Other teams' names and icons appear when the camera can see them, team-mates' names when the camera is close, the same rules as normal play. Before, the game still judged sight from your own knocked-out player, so other teams' names never showed.
- Only while spectating; normal play is unchanged. Without Teamplay there are still no names while spectating (as the game draws them).

## v5.92 · 2026-10-27 · Crash fix: running out of lives in Elimination / Vampire without Teamplay

*v5.92 · SpectateFFACrash* · Xbox, PS2 NTSC, PS2 PAL

- Elimination / Vampire with Teamplay off: the game crashed on a patched console as soon as its player ran out of lives (any host, offline too). v5.90 drew the names over other players while spectating without Teamplay, but the game only sets up what that drawing needs (the names' fade-in) with Teamplay on. Names while spectating are back to Teamplay matches only, as the game draws them; without Teamplay there are none, as before v5.90.
- Tests: the name tags' Teamplay check is the game's own on both platforms.

## v5.91 · 2026-10-27 · Spectate: other teams' names only when in sight

*v5.91 · SpectateTagsInSight* · Xbox, PS2 NTSC, PS2 PAL

- Spectate (Elimination, Vampire): while you watch someone, other teams' names and icons show only when they are in sight, as the game normally draws them (v5.90 showed them through walls, which a team-mate on split screen or voice chat could use). Your own team's show as before, the player you watch has none, and without Teamplay names still show (when in sight).

## v5.90 · 2026-10-27 · Spectators see every player's name; Team Lives at 1 is the last life; PS2 Scores page player rows; Manage Players names

*v5.90 · ScoresRowsPS2* · Xbox, PS2 NTSC, PS2 PAL

- Spectate (Elimination, Vampire): while you watch someone, every other player's name and icon is shown, every team's, as a team-mate's is (always, not only when in sight), and also without Teamplay. The player you are watching has none, as before; your own as before.
- Team Lives: the team's lives now work as the HUD shows them. At 1 everyone still in is on their last life: each player's next death knocks that player out, and the others play on until their own. Before, the death that took the team's last life brought the player back once more with 1 life (so at 1 everyone got one extra death). At 2 or more a death takes one off the team and the player comes back.
- PS2: on the Scores page in Team Elimination / Team Vampire, every player's score showed 0 (the Team Deathmatch number). It now shows the game's own lives ("N Lives") for a player still in and the time a player was knocked out, as on the Xbox since v5.86.
- Manage Players with 3 or 4 players on one console (Xbox and PS2): a name too long for its row is now shrunk evenly instead of squeezed sideways, so it keeps its shape.
- Tests: names while spectating, Team Lives at 1, the PS2 Scores page player rows, the even fit.

## v5.89 · 2026-10-27 · Advanced Settings stay out of Story, Arcade League and Challenges; King of the Hill LAN fix; other fixes

*v5.89 · CustomOnlySettings* · Xbox, PS2 NTSC, PS2 PAL

- Advanced Settings now only apply to custom arcade matches and LAN. Story, Arcade League and Challenge matches play exactly as the game made them: before, settings chosen for custom arcade carried over into them (for example Player Drops Gun Off stopped Story enemies dropping their guns, Player Health scaled Story damage, and Weapon Mode, Showdown, Catch-Up, Respawn Delay, Spawn Rule, Multikill, King of the Hill, Coin Rush, Overtime, Switch Spawns, Team Lives, Team Spawns, Reverse Scoring, Score With Bag Away, Team VIP, Number of Flames, Zone Scoring Interval, Assault's phase settings and Mercy Rule could change League and Challenge matches). Menus and settings are unchanged.
- King of the Hill (LAN): until someone first captured the Hill, the host re-dropped every zone and sent a burst of messages to every console every frame (lag, stutter and flickering zone beams at the start of a match). The host's zone-owner sends are no longer taken as players entering the match.
- LAN, weapon switch for players without the patch: a copy of a player's settings the host kept from earlier is only used for a player on the same console it came from, so a player with the same name on another console can no longer be sent someone else's settings (such as Invert Look).
- Showdown: Infinite Ammo no longer applies (one bullet means one bullet); the Infinite Ammo item is greyed out while Showdown is on.
- Mercy Rule removed from Vampire (it never ended a Team Vampire match, and Vampire is a survival mode like Elimination, which never had it).
- Tests (Xbox and PS2): King of the Hill sends, kept settings by console, Showdown flags, and every setting's custom-only check.

## v5.88 · 2026-10-27 · Patched Xbox players follow a host on the original disc build into the next match; PS2 Scores page team rows fixed

*v5.88 · DiscHostMatchInfo* · Xbox, PS2 NTSC, PS2 PAL

- LAN (Xbox): with a host running the original disc version of the game (no title update), a patched Xbox stayed on the old match's results screen when the host started the next match (any mode). The disc version's match info is 4 bytes shorter, so the title update read the wrong field as the host-in-level flag and dropped it. A patched Xbox now moves the disc host's match info into the title update's layout first (Music, the host-in-level flag and headsets one field later, Ban Small Characters off), so it loads the new match with everyone else. The host's Music choice is also read right now, not as Ban Small Characters. Title-update and patched hosts are unchanged.
- PS2 (v5.86 regression): the Scores page team rows (pause and end of match, every team mode) could show a wrong number or junk instead of the team score, and Team Bag Tag team rows lost their times. The knocked-out team time added in v5.86 took the score from the wrong place and skipped the existing Bag Tag row code. Team scores, Bag Tag team times and the knocked-out team time (Team Elimination / Vampire) all show correctly again.
- Tests: disc-sized and update-sized match info (Xbox); the Scores page team row called as the game calls it (PS2), and the build now checks the set-up it relies on.

## v5.87 · 2026-10-27 · Team Elimination / Vampire no longer ends before the host has picked a team

*v5.87 · TeamElimStartFix* · Xbox, PS2 NTSC, PS2 PAL

- Team Elimination / Team Vampire: v5.86 left players who hadn't picked a team yet out of the one-team-left check, so a match could end at once (the host shown DNF) while the host was still on Select Team. A player who hasn't picked counts with its own team again, and on the PS2 the check waits while the host is still on Select Team.
- Tests (Xbox and PS2): players who haven't picked; the host on Select Team.

## v5.86 · 2026-10-27 · Team Elimination / Vampire and Spectate fixes; knocked-out times on the Scores page

*v5.86 · TeamElimFixes-SpectateFixes-ScoresTimes* · Xbox, PS2 NTSC, PS2 PAL

- Spectate: the player you're watching has no name tag over them in your view (every screen size, free cam too); everyone else keeps theirs. "Spectating <name>" stays while you follow a player.
- Spectate: the camera stays on the player you're watching when they die with lives left (it holds where it was until they respawn), and only moves on once they're out or gone; in free cam it never switches by itself.
- Spectate: buttons used in the pause menu or the Scores tab no longer also switch who you watch or toggle free cam.
- Spectate: everything is cleared when a new match starts (the camera no longer sits at the old player's spot while the next level loads); another kill message no longer waits about 2 seconds behind "Spectating <name>" (ours fades straight away and comes back after); free cam isn't offered where the camera has no room; a player who comes back to life gets their hands and gun drawn again.
- Team Lives: the death that empties a team's pool no longer puts that player out; once the pool is empty each player's next death does (Lives 5 with 2 players: 7 deaths), as the setting was described.
- Team Elimination / Vampire, time limit: teams still in are ranked by lives left (the team with more lives wins) instead of every team tying.
- Team Elimination / Vampire: the one-team-left end only happens while the match is being played (not while players are still picking on Select Team) and only counts teams 1-4; a mid-match joiner still loading or picking can't hold a decided match open.
- Mid-match joiners (host): a player who joins and picks a team that has nobody left in (knocked out, or empty) while another team is still in gets no lives and spectates, so a knocked-out team can't come back (also when the pick is the team its slot had before); with Team Lives a joiner on a team still in gets the team's lives.
- Team time and ranks: a joiner who hasn't spawned yet no longer counts toward its team's time.
- End-of-match / pause Scores page (consoles with the patch): Xbox player rows in Team Elimination / Vampire show lives or the time the player was knocked out (they showed Team Deathmatch kills); on Xbox and PS2 a knocked-out team's row shows the time it was knocked out instead of 0. Consoles without the patch draw this page themselves and are unchanged.
- Tests (Xbox and PS2): all of the above.

## v5.85 · 2026-10-26 · Team Elimination / Vampire Scores tab for players who joined mid-match; Manage Players and Spectate on a quarter screen

*v5.85 · TeamRowsJoiners-ManagePlayersQuarter-SpectateTag* · Xbox, PS2 NTSC, PS2 PAL

- Team Elimination / Team Vampire, pause Scores tab: a player counts as still in for v5.84's team rows only once the game includes them in the ranking (on LAN, their console has spawned). A team whose only player still in had just joined mid-match was counted as in while the game left that player out of the ranking, so the team's row was an out player with a meaningless time. That team now counts as out until the player spawns, and every team-mate shows the team's time, as before v5.84.
- Manage Players on a quarter screen (3 or 4 players on one console): the team options show R / B / Y / G (Kick stays), and a name too long for the room left of them is drawn narrower to fit, so names and teams no longer overlap. One or two players on a console: as before. (v5.84's smaller font alone made no visible difference.)
- Spectate on a quarter screen: the name tag over the head of the player you're watching isn't drawn in your view ("Spectating <name>" already says who it is). In free cam, with one or two players on a console, and for everyone else's tags: as before.
- Tests (Xbox and PS2): teams with a player not spawned yet; the quarter-screen Manage Players rows; the watched player's name tag.

## v5.84 · 2026-10-26 · Spectate once your team is out, a working camera when watching stops, team lives on the Scores tab, Manage Players in split screen

*v5.84 · SpectateAnyone-ScoresLives-ManagePlayersSplit* · Xbox, PS2 NTSC, PS2 PAL

- Spectate (Elimination / Vampire with teams): once nobody on your own team is still in, you can watch any player still in. Before, a player whose whole team was out, or who was moved to a team with nobody else on it, had nobody to watch.
- Spectate: when watching stops (nobody left to watch), the camera goes back to where it was when you started watching (your death view). It used to restart from your body's eyes, which had gone down with the body, and could leave the screen black.
- Spectate at the end of a match: you keep watching the player you were watching and get the game's whole end-of-match HUD (before, nobody counted as in the match any more, so the view went black, and only the messages were drawn).
- Team Elimination / Team Vampire, pause Scores tab: while two or more teams still have players in, a player who is out ranks below every team, so each team's row is one of its players still in and shows the lives left (not a time). Team ranks are unchanged. Decided by the host, so consoles without the patch show it too. Before the end scores are saved the host ranks once more without this, so a match that ends on its time limit saves every player with their team's time and rank.
- Manage Players with more than one player on a console (split screen): the rows use the game's smaller font (as its own Players page), so names no longer run into the team.
- Tests (Xbox and PS2): Spectate's team fallback, the end of the match and the kept camera; the out-player rank and the re-rank before the end scores; the split-screen font.

## v5.83 · 2026-10-26 · Team Elimination results for every console; Coin Rush and match starts for consoles that get in late; the weapon switch setting put back

*v5.83 · TeamElimRanks-CoinsLate-SelectTeamHold-SwitchRestore* · Xbox, PS2 NTSC, PS2 PAL

- Team Elimination / Team Vampire: consoles without the patch showed every player finishing 1st. On the last frame the host ranked the teams before it noted the team just knocked out, so both teams had the same time. A player still in now counts up to this frame, so the surviving team ranks first on every console. Scores shown are unchanged.
- Thief Coin Rush: a console that got into the match after the first coins had dropped never saw them (a console only takes coin messages once it is in the match). The coins already out now go to every console as it enters, not only to players who join mid-match.
- PS2: while the host is still on Select Team, another console waiting for its spawn point isn't in the match yet; the start-of-match hand-outs (Weapon Mode), the first coins (Coin Rush) and the Hill (King of the Hill) now wait until the host has left Select Team, so that console doesn't miss them.
- Weapon switch for players without the patch: the message that puts a player's own weapon change setting back at the end of a match can arrive after their console has left the match and be thrown away, leaving them on "Always". The host now notes each setting it put back; when that player's console next enters a match and the host's copy of their settings still says "Always", their own setting is sent once more (once per put-back, so a player who really chose "Always" keeps it).
- Tests (Xbox and PS2): the end-frame team ranking, coins for a console that started late, the Select Team hold, the setting sent again on entry.

## v5.82 · 2026-10-26 · Weapon Mode: unpatched players' settings no longer lost when their console gets into the match before the host

*v5.82 · WeaponSwitch-EarlyPrefs* · Xbox, PS2 NTSC, PS2 PAL

- A console sends its players' settings once at the start of a match (and whenever they change), but the game only takes them while it is already in the match itself. If the other console got in first (the host still loading or on its start screen), the host threw them away and they were never sent again, so the weapon switch didn't work for that player. This could happen in any match, including the first one.
- Settings that arrive at that moment are now kept (the same kept copy as v5.81) instead of being lost, as long as they came from the console that owns that player's slot, and the host uses them at the first weapon hand-out. Nothing else about how the game takes them changes.
- Tests (Xbox and PS2): settings arriving before the match kept, other packets untouched, settings from a console that doesn't own the slot not kept, in the match the game's own path, then used at the hand-out.

## v5.81 · 2026-10-26 · Weapon Mode: the weapon switch for unpatched players works after the host reconnects

*v5.81 · WeaponSwitch-KeptPrefs* · Xbox, PS2 NTSC, PS2 PAL

- Every console now keeps a copy of each other console's player's settings when it receives them, labelled with the player's name.
- When the host has no settings for an unpatched player (after the host reconnected to the network, the other console may not send them again until something in them changes, such as their character), it uses the copy it kept, so the switch to the handed-out weapon and the setting put back afterwards work as before.
- A real change still wins: a console sends its settings whenever they change, and the new ones replace the kept copy. If two players in the game have the same name, no copy is kept or used for that name (it can't be told whose it is). The copies last until the console is switched off.
- Tests (Xbox and PS2): kept by name, our own override coming back not kept as the player's own setting, full table, two players with the same name, names compared on the game's 30 characters, the kept copy used for the override at a match start.

## v5.80 · 2026-10-26 · Spectate: no "Spectating <name>" message in free cam

*v5.80 · Spectate-FreecamNoMessage* · Xbox, PS2 NTSC, PS2 PAL

- Free cam removes the "Spectating <name>" message at once; it comes back when the camera goes back behind the player (Activate again, or switching player).
- Tests (Xbox and PS2): the message gone in free cam and back after it.

## v5.79 · 2026-10-26 · Spectate: aim the camera, free cam, button prompts, no HUD or hands; players who left skipped. Player Health names

*v5.79 · Spectate-Controls-Freecam* · Xbox, PS2 NTSC, PS2 PAL

- Spectate camera: the right stick turns the camera round the player you watch and up / down, still anchored behind them (walls and doors pull it in as before). It starts facing their way each time you pick someone. It follows your own controls: your stick layout (southpaw too), Invert Look, the game's look speed and frame time (still while paused).
- Free cam: Activate (A on Xbox, X on PlayStation) frees the camera where it is; the left stick flies it along the way you look and sideways, the right stick turns it. Walls and doors stop it and it stays inside the level. Activate again, or switching player, puts it back behind the player.
- Button prompts bottom left, the same as the game's autogun / camera ones: "<button> Freecam" ("Exit freecam" while free) and "<D-pad> Switch player".
- "Spectating <name>" is now a kill message at the bottom (the name in its team colour) that stays on screen while you watch; the big centre text is gone. Any message it would hold back (another kill message, pick-ups and the like) still comes through: it steps aside and comes back after.
- While you are out with Spectate the in-match HUD is hidden (the Vampire bar, score, timer, ammo ...); messages and the prompts still show. Your own first-person hands and gun are not drawn in the spectate camera.
- A player who left the match (the game keeps their body) is no longer someone to watch: no more "Spectating" with no name at a fixed spot.
- Player Health options renamed: Default / Low / Weakling / Pathetic (75% / 50% / 25%).
- Only the watching player's own console changes and nothing is sent, so players without the patch, and other spectators watching the same player, are unaffected.
- New tests (Xbox and PS2): the stick turning (speed, frame time, pause, Invert Look, the player's control slots, limits), free cam on / off, its moving, walls and rooms, the free cam view, the hidden hands, the prompts, the hidden HUD, the kept kill message stepping aside for other messages, players who left.

## v5.78 · 2026-10-26 · Spectate in Elimination and Vampire (third person, always on). Player Health: kills on time for patched LAN players

*v5.78 · Spectate-PlayerHealthGuests* · Xbox, PS2 NTSC, PS2 PAL

- Spectate (Elimination and Vampire, always on: no setting). A player who is out of lives watches a player still in from just behind them (third person): the camera follows their position and the way they face and look up or down, in their part of the map. D-pad right / left picks the next / previous player; with Teamplay on, only team-mates. When the player watched is out, the view moves to the next one; "Spectating <name>" shows on each change. With nobody left to watch, the game's own out-of-lives view comes back.
- It works on every console with the patch, whoever hosts, because only the watching player's own view changes and nothing is sent. Players without the patch keep the game's normal out-of-lives view, and the match plays exactly as before.
- Walls and doors pull the camera in (the game's own camera wall test), so it never ends up on the other side of a wall. Right up against one, it moves to the watched player's eyes, and they aren't drawn on that screen so their head doesn't block the view.
- Player Health on LAN: a LAN player with the patch now counts their own hits at the host's Player Health setting, so their own screen shows the kill on the same hit as everyone else (before, lag could make it show one hit late). The hit they report to the host keeps the normal amount, so the host still multiplies it exactly once. Players without the patch are unchanged: their hits do the same boosted damage through the host as before.
- The host's Player Health goes to LAN players with the patch in setup byte 67 (0x90 | Player Health), the same way as the mod's other settings.
- New tests (Xbox and PS2): who can be watched (alive, lives left, team-mates with Teamplay), next / previous round the list, the view switching to the camera and back to the death view, the camera behind the watched player along their look, pulled in by a wall, at their eyes against one, the room traced from their eyes, split screen; Player Health on a LAN player (report at the normal amount, own copy at the host's setting, put back after, never twice on the host).

## v5.77 · 2026-10-25 · Weapon Mode: the weapon switch for unpatched players waits for the gun in hand; Showdown one-hit kills only for player hits

*v5.77 · SwitchAndCredit* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game, Random Weapon and Showdown on LAN: for a player on an unpatched console, the host sets their "weapon change on pickup" to Always just before handing them a weapon, then puts their own setting back. It used to put it back once the host's own copy of that player had the weapon, which is at once, so a console that took the weapon a moment later (the weapon landing a step away, or a console running behind) had its setting back to Never or Keep Current by then and didn't switch. The setting now goes back once the player is seen holding the new weapon (or when the usual time runs out).
- Showdown: only a player shooting another player is a one-hit kill. Other damage (a crate, barrel or other object hitting someone, an explosion's own blast, a hit with no attacker) does its normal amount. Those deaths could be turned into kills credited to whoever last hurt the player, even someone who hadn't killed anyone.

## v5.76 · 2026-10-24 · Weapon Mode fixes: a left-over Showdown setting, hand-outs left on the floor, joiners, PS2 armouries and Select Team

*v5.76 · GunGameFixes* · Xbox, PS2 NTSC, PS2 PAL

- A Showdown setting no longer switches Weapon Mode off in other modes. Showdown is one setting shared by every mode, so turning it on in Elimination and then changing the mode to Deathmatch on the match settings page (without opening Advanced Settings again) left it on: the match played plain Deathmatch while the menu still showed Gun Game. Weapon Mode now follows the mode chosen: Showdown in Elimination and Vampire, Weapon Mode's own setting everywhere else, and Showdown comes back if the mode is changed back.
- A hand-out still lying on the floor is taken away on every console when its player is given the next one (a respawn, a new Gun Game level). Before, nothing removed it any more, and it stayed there for anyone until the game's own 12 seconds ran out: in Showdown, a spare bullet. It is left to those 12 seconds, as before, while anyone (alive or dead) is standing by it, while a console has joined since it was dropped, or while the host has 25 or more dropped weapons on the map.
- The host no longer hands out a second Showdown bullet (or a second Random Weapon gun) to a player on another console who is already holding the weapon, whatever the host's own copy of that player shows.
- A player joining mid-match into the slot of someone who just left now always starts Gun Game at level 1 with no kills and no owed Showdown bullets. Before, if the host had no character for that slot yet, they kept the leaver's level and kills.
- Gun Game: an unpatched player stuck on their fists early in a match is given their gun again once in that life, as intended. A record left over from the previous match (one that ended with someone finishing the ladder, or with Return to Lobby) could skip it until their first death.
- PS2 hosts now resend the weapon locker moves every 10 seconds in Gun Game and Showdown, as Xbox hosts do. This was listed for v5.55 but the PS2 part had been left out, so a console that missed the moves at the start of a PS2-hosted match kept working lockers all match.
- PS2 hosts hold the other players at the start of a Teamplay match until the host's own players have picked a team, as Xbox hosts do. The check looked for a Select Team game state that PS2 never uses. It is limited to the first 20 seconds of the match so it can never hold anyone for good.
- PS2 hosts now only count a player's console as in the match once the game has actually respawned them (after the game's own "can this player spawn" check, as on Xbox), not on calls the game then turned down.
- PS2: two words left in memory by very old builds (v5.3 to v5.15) are now cleared when the patch is reloaded.

## v5.75 · 2026-10-24 · Weapon Mode hand-outs for players on other consoles: only once their game can take them

*v5.75 · HandoutTiming* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game, Random Weapon and Showdown on LAN. A console only takes the host's hand-out once it is in play: in its 3-2-1 countdown it numbers the dropped weapon itself and throws the host's "you picked it up" away, so the player got nothing, and the host, which gives its own copy of the player the weapon too, never gave it again. The start-of-match weapons now go out a second after the host is in play (they used to go 2 seconds into the level, during the countdown), and a player whose console has just entered the match (late, or joining mid-match) gets theirs once their countdown is over, 4.5 seconds after they enter.
- No hand-out for a player whose console isn't in the match yet. It used to lie on the floor where that player's copy stood, for anyone to take, and came back every 12 seconds: an extra Showdown bullet on a spawn pad, or a higher Gun Game gun. Their first spawn gives them one. Showdown bullets they earn meanwhile are kept until they can be given.
- A hand-out for a player on another console now lands a few steps away (the nearest point 3 or more units away) instead of under their feet. The host's "you picked it up" still gives it to them; their own console can no longer take it as well by walking over it, which gave the weapon twice (2 bullets in Showdown).
- The host now also notes a console as in the match whenever it respawns that console's player, so a console that entered just before the new match started still gets its hand-outs.
- Xbox: the mod's code now has a second block in the unused Spanish "disc can't be read" picture (the mod already kept tables there). A Spanish-language Xbox that can't read the disc shows a garbled picture instead of that message.

## v5.74 · 2026-10-24 · Gun Game can't be combined with Teamplay

*v5.74 · NoTeamGunGame* · Xbox, PS2 NTSC, PS2 PAL

- Shrink, Regeneration and Leech: choosing Gun Game with Teamplay On now stores Weapon Mode as Off, as Showdown already did. The match never played Gun Game with teams, so the menu no longer suggests it does. Random Weapon with Teamplay is unchanged.

## v5.73 · 2026-10-24 · Weapon Mode: players without the patch get their hand-outs again

*v5.73 · HeldStartHandouts* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game, Showdown and Random Weapon on LAN: players without the patch could get no weapon at the start or after respawning. Since v5.70 the host only puts a hand-out straight into another console's player's hands once that console is in the match, which it notes when it sends the player's spawn point. At the start of a match the host holds those spawn points until it leaves its start screen, and the new match's clear-out came after that note, so it was lost and never made again for those players. The host now notes it when the held spawn points go out as well.

## v5.72 · 2026-10-24 · Weapon Mode start: weapons handed out a little apart instead of all in one frame

*v5.72 · SpreadStartHandouts* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game, Showdown and Random Weapon: at the start of a match the host used to hand every player and bot their weapon in the same frame, the frame it also clears the map's weapons. Each player now gets theirs 2 frames after the one before (by player slot, so with 16 players the last is about half a second after the first). This is meant to stop the frame drops at the start of these matches.

## v5.71 · 2026-10-23 · Joining a match in progress, restarting after a Weapon Mode change, PS2 fixes

*v5.71 · JoinFixes* · Xbox, PS2 NTSC, PS2 PAL

- A player joining mid-match into the slot of someone who left while dead is now treated as entering the match, not respawning. In Gun Game / Showdown they get the removed map guns and armouries taken away as everyone else has, and hand-outs dropped while they were loading are no longer moved under them (a move for a pickup a game doesn't have could crash a PS2 without the patch).
- A joiner no longer inherits the previous player's Catch-Up extra kills, Multikill bonus kills and chain, Team VIP points or Respawn Delay record in that slot (the host's scores, which decide the match). Before, they could start with an unearned score. Other patched consoles may still show the old Multikill bonus in their own count for that slot until the next match.
- Restart after changing Weapon Mode at the end of a Showdown match: every game now reloads with the full weapon set, so nobody is handed a gun their game didn't load. (Changing to Showdown and restarting keeps the full set and the map's pickups until the next new match.)
- PS2: the "host has the patch" settings are kept during the countdown as well as in play (PS2 has no separate Select Team state). A value the mod uses while sending the held start-of-match spawn points moved to memory PCSX2 doesn't rewrite every frame.

## v5.70 · 2026-10-23 · Fixes from the exploit check: stale host settings, Respawn Delay for every player, team settings, Gun Game hand-outs

*v5.70 · HostDecidesFixes* · Xbox, PS2 NTSC, PS2 PAL

- Leftover settings from a patched host are no longer trusted. A patched console that joins a host keeps the mod's extra match settings only after that host has said it has the patch (once a second, and as each player enters the match). From a host without the patch, a patched player now plays exactly as that host's game does, even if it was in a patched lobby before. For the first second of a match, and in the lobby, a patched player falls back to the normal game until the host's message arrives.
- Respawn Delay now applies to every player, patched or not. The host holds back a dead player's spawn point until their delay is over, whichever way the game asks for it: its own pick, the 1.5 second resend, Spawn Rule's re-pick or Manage Players. Assault's re-pick when the objective moves on no longer gives a living player on a team with a delay a spawn point they could use straight away at their next death. Each death's delay is timed once, so the game's own 3 second timer running out no longer restarts it. If the delay is over and the player's console asks again with no spawn point picked yet, the host picks one then instead of sending an empty one.
- Players on another console use the host's Disable [colour] Team and Team Spawns settings, never their own. Before, a patched player's own settings could change their team choices and spawn picks. The host's settings apply once its "has the patch" message has arrived, so on Select Team a patched player sees no colours disabled, the same as a player without the patch.
- Gun Game / Showdown hand-outs: a player whose console is still loading the level is no longer handed a weapon directly (it was lost); it is handed out when they enter. The weapon switch set to Always no longer ends too early right after the host hands the player a weapon.
- PS2: settings the pnach never sets now start Off at boot, as they do on Xbox.

## v5.69 · 2026-10-23 · Flame Tag: extra flames are put out when a player leaves

*v5.69 · FlamesTrim* · Xbox, PS2 NTSC, PS2 PAL

- Number of Flames never puts everyone on fire: there is always at least one fewer flame than there are players (bots included). Until now the host only ever added flames. If a player who wasn't on fire left, the flames stayed, and everyone left could end up burning with nobody to pass to. Now the host puts out one at random, down to the right number. When more players join, the flames come back up to the setting as before.
- Decided by the host (offline: this game) and sent with the game's own who-is-on-fire status, so players without the patch see it too.

## v5.68 · 2026-10-23 · Player Health options run Default, 75%, 50%, 25%; Return to Lobby removed on PS2

*v5.68 · PlayerHealthOrderNoPS2Lobby* · Xbox, PS2 NTSC, PS2 PAL

- The Player Health list starts at Default, and pressing right steps down through 75%, 50% and 25%. The damage at each setting is unchanged.
- PS2 (NTSC and PAL): Return to Lobby is gone from the pause menu and the end-of-match menu. On PS2 the game's own return to the lobby restores the network side, but the menus then load the Network Menu and wait on "Finish Network Game" for the session to end, which never happens. The game gets stuck there, on a real console and in PCSX2, and players without the patch would be stuck the same way. The Xbox keeps Return to Lobby. Manage Players and its Kick Player confirmation are unchanged.

## v5.67 · 2026-10-23 · New Advanced Setting, every mode but Leech: Player Health (25% / 50% / 75% / Default)

*v5.67 · PlayerHealth* · Xbox, PS2 NTSC, PS2 PAL

- Player Health: how much damage players take from each other's guns and melee. Default is the game's normal damage. 75% is a third more, 50% double and 25% four times. It covers bullets, slow projectiles, harpoons, darts, lasers and melee.
- Unchanged: explosions and the explosives' own hits (rockets, grenades, mines, TNT, bricks), fire, the energy beam, remote-controlled devices, falls and a player's own damage. Not offered in Leech, where each console heals the shooter by the damage it applies.
- The host decides, and it works for players without the patch. The host passes every hit on with the extra damage, so the victim's console shows the right health. When the host's copy reaches no health, it sends the kill to every console itself, the shooter's included, the same way Showdown's one-hit kills reach everyone.
- Only more damage, not less. A console without the patch kills at the normal number of hits, and a kill can't be taken back, so settings above 100% can't be made to work.

## v5.66 · 2026-10-23 · Gun Game / Random Weapon / Showdown: a handed-out weapon goes straight into the player's hands

*v5.66 · DirectHandout* · Xbox, PS2 NTSC, PS2 PAL

- A handed-out weapon is still dropped at the player's feet, and is now picked up by them at once, on every console, through the game's own pickup. For another console's player the host reports it as picked up by them, as it does for a pickup a client reports, so their console (with or without the patch) puts it in their hands with its ammo and their weapon-change setting, and every other console takes it off the floor. The host's own players and bots pick theirs up straight away too. No walking to it, nobody else can take it, and in Showdown it can't add a bullet.
- Players without the patch still switch to it: their weapon-change setting is set to Always just before the drop and the report, on the same channel, so it is in place when they pick it up.
- If a player can't take it (they already have that gun with full ammo), it stays on the floor and is followed as before (v5.65). If the host's own copy of another console's player doesn't take it after the report has gone out, it is never moved again, since the other consoles may no longer have it.
- Xbox: the MapMaker item table (2 KB) moved out of the full code block into the data area, leaving about 2 KB free.

## v5.65 · 2026-10-23 · Gun Game / Random Weapon / Showdown: a handed-out weapon no longer runs away from the player going to get it

*v5.65 · Settle* · Xbox, PS2 NTSC, PS2 PAL

- A handed-out weapon still on the floor follows its player: every half second the host moves it to the pad nearest where it sees them. The host sees another console's player a little late, so while that player moved towards it, it kept landing on a pad they had just passed and trailed behind them, out of reach. Now, once it lands near its player (within 12 units across and 2.5 up or down, so on their floor; floors are 2.5 to 5 apart), it stays put for 3 seconds so they can walk over it.
- It only waits while its player is the closest living player to it (players on another floor don't count). If anyone else gets closer, if its player is further away or on another floor, or if they still haven't taken it after 3 seconds, it follows as before.
- Xbox: three more Weapon Mode tables moved out of the full code block into the data area set up in v5.64.

## v5.64 · 2026-10-22 · Gun Game safety net and late kills; Spawn Rule picks from the host for everyone; Overtime capped at a minute; boot and lobby resets

*v5.64 · Checks* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game: a player holding their level's gun with no ammo left in it or in reserve for 2 seconds is given it again, with full ammo (ammo loaded in a hand counts only while that hand holds a gun, as the game counts it). Another console's player left on fists gets their level's gun again once per level each life, so it can't be used to refill ammo on demand; the host's own player on fists is left alone (they switch themselves).
- Gun Game: a kill made just after the killer died (a grenade or rocket landing within 5 seconds) counts if it was made with the gun they held at their level while alive. Before, a dead killer's kills never counted.
- Showdown: a hand-out gone from the floor is given again only if it timed out (12 seconds since it was last put down). Gone sooner means someone took it, and a second one would have put an extra bullet in the match.
- Gun Game / Random Weapon / Showdown: taking away a dead player's hand-out uses any living player on the host's console (in Showdown its first player may be out for good), instead of waiting for the first one. Offline it is simply removed. PS2: this now covers characters 8-15 too (bots offline), as on Xbox.
- Flame Tag: a dead flame holder no longer passes the flame by touch, and a dead player is no longer tagged.
- Coin Rush: coins only start once every player has loaded (the first 3 seconds after that) and stop when the match ends.
- PS2: after the console boots, every mod option starts Off and every per-match table starts empty. PS2 memory isn't cleared at boot, so a leftover value could switch an option on without the host choosing it, or add old points in the first match.
- Return to Lobby: King of the Hill, Catch-Up, Auto-Complete Phase and Team VIP also start fresh in the next match (Team VIP points from a match left in its first seconds were carried over). Coin Drop's record of deaths waiting for a coin is cleared at a new match. Xbox: the Capture the Bag hold and Team VIP values now start at 0 in the XBE.
- Offline Gun Game / Random Weapon / Showdown: a dead player's hand-out still on the floor is taken away after a second, as on LAN, so a bot doesn't pick it up.
- Team Lives + Manage Players: a moved player takes the new team's lives (at least their last life), instead of the old team's. A player already out stays out.
- Spawn Rule (Away From Enemies / Near Teammates): the host picks a waiting player's spawn point again every 1.5 seconds from where everyone is now, and every console's player spawns at the host's latest pick. Before, consoles with the patch picked at respawn time while consoles without it used the host's pick from the moment of death, several seconds older. A player out of lives isn't picked for, so they don't keep others off a point.
- Capture the Bag Overtime ends after one minute at most, bag carried or not.

## v5.63 · 2026-10-22 · Showdown hand-outs that time out are given again; coin safety; dropped-gun pads freed

*v5.63 · PickupTimers* · Xbox, PS2 NTSC, PS2 PAL

- Showdown: a dropped gun disappears 12 seconds after it lands, on every console. A hand-out that wasn't moved in that time (frozen after a console came in, the pickup slots nearly full, or someone standing by it) vanished and the player had no weapon for the rest of that life. If a hand-out is gone from the floor and its player doesn't have that gun, another is handed out half a second later. It is gone on every console by then, so there is never a second bullet. (Gun Game and Random Weapon already gave one again.)
- Thief: the coins already out are sent only to a console that joined mid-match (its level loaded after the greeting). A console that only started late got every coin since it loaded, and a second copy of each could take it past the 30 coins its coin list holds, which breaks the list on a console without the patch. At most 24 are sent.
- Coin Rush spawns only while 8 or more of the 30 dropped-pickup slots are free (was 6): with 2 or fewer free the game starts timing out the oldest dropped pickups, coins first, and a few guns dropped at deaths could take it there.
- Each time a handed-out weapon follows its player, the pad it leaves loses the game's "dropped item here" mark (as when a pickup is taken or fades). The host skips marked pads when choosing where a dropped gun lands, so every pad a hand-out passed through stayed out for the rest of the match and death drops landed further away.

## v5.62 · 2026-10-22 · A console entering late or joining gets everything it missed, in every feature

*v5.62 · Entering* · Xbox, PS2 NTSC, PS2 PAL

- One place on the host now handles a console entering the match: when another console's player asks for its spawn point while its character is alive on the host or has none yet (it loaded late, e.g. left on the profile prompt, or joined mid-match; not a respawn, not a spawn point held at the start), its level has loaded, so everything a feature sent before then (and that console missed) goes to it again.
- A mid-match joiner's players are marked at the greeting, so their first spawn request counts as entering even if their slot still holds a leaver's dead character.
- King of the Hill: the zones go to the Hill at once and again 3 seconds later. Before, a late loader saw them at their own places until the Hill moved, and a joiner for the first 5 seconds.
- Thief: the coins already out are sent to that console when it enters, instead of at the greeting while it is still loading, and only once a match per console (a console with two players asks twice; coins sent twice would show twice there and score).
- The weapon switch for players without the patch: an "Always" still on is sent again.
- Gun Game / Random Weapon / Showdown: the console's own handed-out weapon (which it never had) is taken away on every console once nobody, the entering player included, has been within 4 units of it for a second, and a new one is handed out. Map guns and armouries were already handled. A dead player's hand-out now also waits while the host's player has no character yet, instead of being left.
- Test fixes only: an Xbox test's hard-coded order, and test consoles marked as booted.

## v5.61 · 2026-10-22 · Gun Game / Showdown: the weapon switch lasts up to 12 s while the hand-out is still on the floor; a dead player's hand-out is taken away

*v5.61 · FloorExtend* · Xbox, PS2 NTSC, PS2 PAL

- Players without the patch get "Always" for 4 seconds when a weapon is handed out. In Gun Game and Showdown, if their weapon is still lying on the floor when the 4 seconds are up (not picked up yet), the host adds half a second at a time while it stays there, 12 seconds in all at most; it goes back as soon as they hold it or it's gone. Random Weapon keeps its 1 second.
- When a player dies with their handed-out weapon still on the floor, the host takes it away on every console once nobody else has been within 4 units of it for a second: the game's own "picked up" message, sent as the host's player, and the pickup freed on the host as the game's own pickup does. Not while a console came in since the drop, while 25 or more dropped-pickup slots are in use, or while the host's own player is dead. So a killer can't take the victim's Showdown bullet (or a higher Gun Game weapon).
- Test fix only: an Xbox test passed its registers in a way the compiler could break.

## v5.60 · 2026-10-22 · Gun Game / Showdown: hand-outs followed with a full pickup table; no late-player handling at the match start; PS2 boot clear

*v5.60 · GunGameFixes3* · Xbox, PS2 NTSC, PS2 PAL

- With all 30 dropped-pickup slots in use, a hand-out takes over the oldest slot instead of a free one, and the host didn't know which pickup was the player's, so it was never followed. The host now notes the slots' times before the drop and follows the one whose time changed.
- When a drop fills a slot, any other player's follow record for that same slot is dropped (that pickup was taken over, or the slot was freed and filled again in one frame), so two players can't follow the same pickup.
- At the match start the host sends out the spawn points it held during the start screen. Each one went through the late-player check, so every start sent the map guns' "picked up" once per waiting player, moved armouries again and froze every hand-out's follow. Those spawn points now skip the check (the start's own removal and its 3-second resend cover them).
- PS2: Weapon Mode, Player Drops Gun, Kills To Advance and the handed-out gun record are cleared once after the console boots (low RAM isn't zero on real hardware), like Team Lives and the others.

## v5.59 · 2026-10-21 · Gun Game / Showdown: a late console's map guns cleared at once, not 3 seconds later

*v5.59 · LateNow* · Xbox, PS2 NTSC, PS2 PAL

- When a console comes into the match late, the host now sends the map guns' "picked up" to it straight away (it is asking for a spawn point, so its level has loaded), as well as 3 seconds later as before. That closes the few seconds in which a quick player could still grab a map gun. Its armouries were already moved at once (v5.57).

## v5.58 · 2026-10-21 · Gun Game / Showdown: late loaders caught whichever way the host answers their spawn request

*v5.58 · LateEntering2* · Xbox, PS2 NTSC, PS2 PAL

- The host answers a spawn-point request in two ways: straight away if that player already has a pad, or by picking a pad first. Only the first way reached the late-loader check, and a console coming in late from the profile prompt takes the second, so its map guns were never cleared. Every spawn-point answer to another console's player now goes through the check (still only when that player's character is alive on the host or has none, so respawns after a death are left alone; the host's own player never).

## v5.57 · 2026-10-21 · Gun Game / Showdown: a console left on the profile prompt gets the map guns cleared when it enters

*v5.57 · LateEntering* · Xbox, PS2 NTSC, PS2 PAL

- A console left on the profile prompt asks for its spawn point when the match starts (that answer is lost) and asks again when it finally loads in. The host only acted on the first request, so the map guns stayed on that console until picked up. Now any spawn-point request made while that player's character is alive on the host (a console entering, not a respawn after a death) sends the "picked up" messages again 3 seconds later and moves its weapon lockers at once. Works for players without the patch.

## v5.56 · 2026-10-21 · Xbox: after a match, the menus go back to the System Link match list

*v5.56 · StraightToSystemLink2* · Xbox

- After a System Link match the game rebuilt its menus with the Xbox Live / System Link choice page; it now goes back to the System Link match list, as the main menu item does since v5.54. Xbox only (the PS2 files only change version).

## v5.55 · 2026-10-21 · Gun Game / Showdown: a late loader's weapon lockers are moved at once

*v5.55 · LateLockers* · Xbox, PS2 NTSC, PS2 PAL

- A console that loaded in late missed the start-of-match moves that put the weapon lockers (armouries) out of reach, and only got them on the host's 10-second resend, so for a moment its player could take a locker's gun and full ammo. The host now sends that console the moves the moment it asks for its first spawn point. Works for players without the patch.

## v5.54 · 2026-10-21 · Gun Game: late loaders get the map guns cleared again; Xbox: main menu straight to the System Link match list

*v5.54 · StraightToSystemLink* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game / Showdown: a player whose console loads in late (for example left on the profile prompt) could still see and pick up map guns. The host counted them as already in because their character exists on the host before their console has loaded, so their first spawn didn't send the "picked up" messages again. Now only a player's first spawn point counts, kept for the whole match.
- Selecting "Xbox Live / System Link" on the main menu now opens the System Link match list directly, skipping the Xbox Live / System Link choice. The game's own checks still run (no cable attached, signed in to Xbox Live). B goes back to the main menu.
- Xbox only: on PS2 that step is where the network settings are chosen, so the PS2 menus are unchanged.

## v5.53 · 2026-10-21 · Safer joins, early Return to Lobby, PS2 boot memory

*v5.53 · SaferResets* · Xbox, PS2 NTSC, PS2 PAL

- When someone joins or a slower console first enters the match, handed-out weapons on the floor stop moving but stay tracked, so the safety nets don't hand out a second copy.
- A joiner's "first spawn" marker is now cleared by its network slot, the same number used to set it.
- Return to Lobby makes the next match count as new from its first frame, so Team Lives, Overtime, Coin Rush, Multikill / Catch-Up and Weapon Mode state can't carry over after a very early return.
- PS2: the weapon-switch override table is cleared after the console boots, as the option values already are.

## v5.52 · 2026-10-21 · Weapon Mode fixes: joiners, late loaders, leftover state; PS2 options start Off

*v5.52 · WeaponModeFixes* · Xbox, PS2 NTSC, PS2 PAL

- A handed-out weapon is no longer moved after someone joins, or after a slower console first enters the match: those consoles never had it, and a move for a weapon a console doesn't have could freeze a PS2 without the patch.
- A player who rejoins (or takes a free slot) mid-match now gets the map guns' "picked up" sent again at their first spawn, so they can't grab leftover map guns in Gun Game or Showdown.
- A mid-match joiner starts with fresh safety-net state instead of the previous player's.
- A "picked up" resend left over from the last match no longer fires in the next one.
- The 4-second "Always" weapon-change override for players without the patch is put back on Return to Lobby and when the next match isn't a Weapon Mode match.
- PS2: Team Lives, Setbacks and Random Characters now start Off after the console boots (their memory wasn't cleared, so they could start On).

## v5.51 · 2026-10-21 · Gun Game: a patched player no longer loses their gun by picking up someone else's hand-out

*v5.51 · GunGameOwnGun* · Xbox, PS2 NTSC, PS2 PAL

- A patched player's console switched them to any of the match's guns they picked up and took the others away, so grabbing another player's hand-out cost them their own level's gun for a couple of seconds.
- The host now tells a patched player's console which gun it handed them (a message only that console reads; consoles without the patch ignore it). The console switches only to that gun, once the player has it. Other guns they pick up are just kept, as for players without the patch.
- When a patched player has their level's gun but is holding another one (for example a map gun left on a slower console), the host's safety net now tells their console to switch to it.
- The safety net no longer switches anyone off their fists (a punch can set someone back with Setbacks); before, the host's own players were switched back to their gun every few seconds.
- Nothing changes for players without the patch.

## v5.50 · 2026-10-20 · Advanced Settings: no health / armour arcs over the page in the pause menu

*v5.50 · NoArcs* · Xbox, PS2 NTSC, PS2 PAL

- In a match, the pause menu drew the player's health and armour arcs over the Advanced Settings page (Change Game Type). The page now carries the game's own page flag for hiding them (as the game's confirm page does), so they aren't drawn while it is on screen.
- Only this console's menu changes; nothing is sent to other players.

## v5.49 · 2026-10-20 · Gun Game, Random Weapon, Showdown: a handed-out weapon follows the player until it is picked up (PS2 too)

*v5.49 · DropFollow* · Xbox, PS2 NTSC, PS2 PAL

- The host can only hand a weapon to a player without the patch by dropping it on the map pad nearest to where it sees them. A player who is running, or whose position the host sees a little late, could end up with the weapon lying on a pad beside them and never get it.
- The host now moves that weapon to the pad nearest the player every half second until they pick it up (before: for 2 seconds, and only on an Xbox host). PS2 hosts now do it too. It uses the game's own "dropped" message, so players without the patch see the same.
- Moving a weapon never uses up one of the game's 30 dropped-pickup slots. While 25 or more are in use, the host stops moving it, so every console keeps the same pickups even near the limit.
- While any player is within a short distance of the weapon, the host doesn't move it that half second: that player may have just picked it up on their own console, and moving a weapon a console no longer has could crash a PS2 without the patch.
- A new hand-out replaces the one being followed, even when the game made no new pickup for it.
- The Gun Game and Random Weapon safety nets no longer drop a second weapon while the last one is still on the floor (it is on its way to the player).
- The 4-second "Always" weapon change on pickup for players without the patch is unchanged.

## v5.48 · 2026-10-20 · Gun Game: map guns cleared on slower consoles; missed hand-outs given again

*v5.48 · GunGameClear* · Xbox, PS2 NTSC, PS2 PAL

- The host's "picked up" messages for the map's guns and ammo went out once, on the first frame everyone had loaded. A console still starting its level (a slower one, or a player left on a menu such as the profile prompt) dropped them, and the guns stayed on its map. Players could pick them up, then already held a later ladder gun, so the host's hand-out didn't switch them and they were stuck until they died.
- The host now sends them again 3 seconds after the start, and 3 seconds after a player's console first asks for its spawn point (however late it loaded). Works for players without the patch.
- Gun Game safety net: a player not holding their level's gun for 2 seconds (setbacks included) is given it again when they don't have it (a drop they never got) or are out of its ammo; one who has it with ammo is switched to it on the host's own console and left alone on other consoles (no drops pile up). Then 3 seconds before the next look.
- Random Weapon: 2 seconds after a weapon is handed out, a player who doesn't have it is given one again (twice at most). Not in Showdown: a second drop could give an extra bullet.

## v5.47 · 2026-10-20 · Venice: the gondola changes removed

*v5.47 · VeniceRevert* · Xbox, PS2 NTSC, PS2 PAL

- The v5.45 / v5.46 gondola changes are taken out: in testing, the gondolas on consoles without the patch looked further out of step while the host had them. Venice is back as in v5.44 (the game's own behaviour).
- PS2: the changed words are written back to the game's own, so Reload Cheats/Patches is enough.

## v5.46 · 2026-10-20 · Venice: no false water deaths on the gondolas (LAN host)

*v5.46 · VeniceWater* · Xbox, PS2 NTSC, PS2 PAL

- The host decides water deaths. Between a player's position updates it moves its own copy of them, and where the host's gondola isn't under a rider (players without the patch keep their own gondolas), that copy sank and the host killed them.
- The host now keeps each player's last reported height and doesn't apply a water death to another console's player whose own console had them above the floor within the last 1.25 seconds. A real fall into the water still kills them (at most about a second later).

## v5.45 · 2026-10-20 · Venice: the gondolas in step on LAN

*v5.45 · VeniceBoats* · Xbox, PS2 NTSC, PS2 PAL

- Each console used to move Venice's gondolas on its own from when it finished loading, so on LAN they were in different places on different screens (riders fell in the water on the host's).
- Now the host's gondolas run as before, and the host tells every patched console how far along they are (every 5 seconds, sooner when it changes); those consoles put their gondolas in the same place. Players joining mid-match get it too.
- Consoles without the patch keep their own gondolas, exactly as before (the host's are unchanged). Xbox Live / PS2 online keep the game's own timing.

## v5.44 · 2026-10-19 · King of the Hill: the Hill visits every place

*v5.44 · HillEveryPlace* · Xbox, PS2 NTSC, PS2 PAL

- The Hill now goes to every zone place on the map once, in a random order, before it repeats any; it never stays where it is.
- Xbox: the move used the low bits of the game's random number, which repeat in short cycles, so on some maps the Hill could keep returning to the same few places. It now uses the top bits (PS2 too).

## v5.43 · 2026-10-19 · LAN team games: the host spawns as soon as it picks a team

*v5.43 · HostAutoSpawn* · Xbox, PS2 NTSC, PS2 PAL

- On the LAN host, Select Team no longer waits for a second A press after the team is picked: the host spawns straight away, so the other players (who wait for the host) aren't held up by an away host.
- Clients still press A to confirm as before. The host can no longer back out of its team pick with B.

## v5.42 · 2026-10-19 · Team Elimination / Team Vampire: team-mates share their result

*v5.42 · TeamSurvivalTime* · Xbox, PS2 NTSC, PS2 PAL

- With Teamplay on in Elimination or Vampire, every player's time is now their team's time: the longest any of its players survived. Team-mates rank together on the Results and Scores pages instead of being placed separately (2nd / 3rd on the same team).
- The host sends that time, so players without the patch see the same team times.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.41 · 2026-10-19 · Team Lives: the scores show each team's lives left

*v5.41 · TeamLivesScores* · Xbox, PS2 NTSC, PS2 PAL

- With Team Lives on, a team's score is now its shared lives left (the pool); once the pool is empty, the number of its players still in. Before, it was the pool plus the players still in (Red 12 with Lives 10 and two players).
- Teams with nobody in them (or nobody left) show 0 instead of the full pool.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.40 · 2026-10-19 · Team Elimination and Team Vampire, with Team Lives

*v5.40 · TeamElimination* · Xbox, PS2 NTSC, PS2 PAL

- Elimination and Vampire now have Teamplay (Advanced Settings > Team Settings), with team spawn points and the team colour options. With teams, the match ends when everyone with lives left is on one team.
- New option Team Lives (Off / On), under Teamplay and greyed out while Teamplay is Off. Off: everyone has their own lives and a team is out when all its players are. On: each team shares one pool of lives equal to the Lives setting (not multiplied by the team's size); every death takes one, and once the pool is empty a player's next death puts them out.
- The host decides it all and sends the lives left as the game already does, so players without the patch keep the right lives and are removed when out. Their results screen shows players individually, as with Team Bag Tag; patched consoles show team results (team score = lives left).
- Showdown and Teamplay can't be combined: each greys the other out, and a match never plays Showdown with Teamplay on.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL; new Team Lives tests on both platforms.

## v5.39 · 2026-10-19 · Bag Tag teams use their own spawn points

*v5.39 · BagTagTeamSpawns* · Xbox, PS2 NTSC, PS2 PAL

- With Teamplay On, Bag Tag teams now start at their own team spawn points when Team Spawns is On (the default). Before, the game marked Bag Tag as a mode without team spawns, so teams always spawned anywhere, whatever the setting showed. Team Spawns Off still lets everyone spawn anywhere.
- Shrink and Thief already used team spawns; this brings Bag Tag in line. It's the host's setting, so players without the patch get it too.

## v5.38 · 2026-10-19 · Manage Players: kick no longer locks the menu; fainter row tint

*v5.38 · KickConfirmFix* · Xbox, PS2 NTSC, PS2 PAL

- Yes on "Are you sure you want to kick this player?" left the pause menu stuck on its closing screen. Yes now kicks the player and goes back to the Manage Players list, the same way No does.
- The team-coloured tint across each player's row is now much fainter: at most 16 of the game's 128 alpha on the left (was 40), fading out to the right. The colour bar on the left is as before.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.37 · 2026-10-19 · Manage Players: names in capitals, kick confirmation, team-coloured rows

*v5.37 · ManagePlayersPolish* · Xbox, PS2 NTSC, PS2 PAL

- The options read RED, BLUE, YELLOW, GREEN and KICK, matching the game's other menus. Player names stay as written.
- Kick now asks first, on the game's own confirm page: "Are you sure you want to kick this player?" (PS2 page title "Kick Player"). No goes back to the list. Yes closes the menu and kicks the player, if they're still in that slot.
- Each player's row has a faint tint of their current team's colour, fading out to the right, drawn with the game's own gradient (as its menu backgrounds). The colour bar on the left is as before.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.36 · 2026-10-19 · Kill messages keep the victim's team colour after a Manage Players move

*v5.36 · KillMessageColour* · Xbox, PS2 NTSC, PS2 PAL

- The "Killed <name>" message (and "Killed by <name>" on the victim's screen) keeps only who was killed, and the game coloured the name from that player's team every frame. A Manage Players move happens the frame after the death, so the name turned to the new team's colour while the message was still showing.
- The message now keeps the colour of the team the player was on when killed. On consoles with the patch; a console without it still recolours its own message.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.35 · 2026-10-18 · MapMaker: no map size limit again on PS2 (as on Xbox)

*v5.35 · MapMakerNoLimit* · PS2 NTSC, PS2 PAL

- The game's map-full limit restored on PS2 in v5.34 is lifted again, as the community patch had it, so MapMaker maps can be as big as the maker likes. A very large map can still overrun the game's 32 KB save space or run out of memory loading; that is left to the maker.
- Correction to v5.34: Xbox was never limited either. The Xbox file the mod started from already skips the map-full flag and leaves the placed tiles out of the memory estimate, so both consoles now match.

## v5.34 · 2026-10-18 · Crash review fixes; Manage Players: no A button, team lined up with the right edge

*v5.34 · CrashReview* · Xbox, PS2 NTSC, PS2 PAL

- A full check for crashes like the Bag Tag one (text running past its space, missing players or objects, unchecked numbers, Xbox instructions the real console lacks, PS2 timing and memory pitfalls) on both consoles.
- Xbox: the pause menu's match info panel showed team Bag Tag times through the same old code as the score page; past a minute it overran its 16-byte space (no crash, but it wrote over spare memory and showed the wrong format). It now uses the same safe m:ss.t text.
- PS2: the community patch lifted every MapMaker size limit, so a very large map could overrun its 32 KB save space (a crash) or run out of memory loading (a hang). The game's own map-full limit is back; per-item limits stay at 255 (lifted again in v5.35).
- Team VIP (Xbox): if the VIP left mid-match, the 5-second scoring tick could read their missing character. It now skips that tick.
- King of the Hill: Xbox's zone colour resend now skips a player with no character; PS2 no longer trusts leftover memory at the first Zones match after starting the game.
- Manage Players: the A button is gone (the prompt at the bottom already says it). The team and its arrows now end as far from the row's right edge (6 pixels) as the colour bar starts from its left.
- Checked and clean: the PS2 score page (its buffer fits the Bag Tag time), every buffer and packet the mod writes, indices from the network, SSE2 on Xbox, PS2 delay slots and RAM the patch rewrites.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.33 · 2026-10-18 · Fix: a player who joins into a leaver's slot no longer inherits old kills

*v5.33 · LeaverKills* · Xbox, PS2 NTSC, PS2 PAL

- When a player leaves a LAN match, the game moves the kills other teams made of them into those players' totals and clears them, but it left the kills by their own team. If someone then joined into that slot on another team, those old entries started counting as kills.
- After a Manage Players move this could count kills twice: a moved player who then left kept kills that had already been counted when they changed team. The kills by the leaver's own team are now cleared as well. Nothing that was counted changes.
- This also fixes the base game's smaller version of the same leak (old team kills counting as kills against the new joiner).
- Host and patched consoles. Tests updated on PS2 NTSC and PS2 PAL; the Xbox change is a one-byte branch change checked against the retail code.

## v5.32 · 2026-10-18 · Manage Players: a queued team is locked until A cancels it; kill counts kept on every patched console

*v5.32 · ManagePlayersLock* · Xbox, PS2 NTSC, PS2 PAL

- While a move is queued (the option greyed out), left and right no longer change the team. Press A on it to cancel the move, then choose again.
- The kill-count fix from v5.31 now runs on every patched console, not just the host. Each one adjusts its own counts when the game applies a team change during a match (the host's team message, or another console reporting its players' teams), so mid-match counts and the results screen match the host.
- Unpatched consoles still work out kills the game's way: after a move, the personal kill counts of the moved player and the players they fought before the move show re-labelled numbers on those consoles (mid-match and on their results screen). Team scores and the winner are right on every console.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.31 · 2026-10-18 · Manage Players: kills stay with the right team after a move; A button after the arrows; clearer grey

*v5.31 · ManagePlayersKills* · Xbox, PS2 NTSC, PS2 PAL

- Fix: moving a player no longer re-labels their past kills. The game counts each player's kills against whoever is on another team right now, so after a move a kill of them by their new team counted as a team kill. Each move now banks the difference, as the game already does when a player leaves: totals stay as they were, and later kills count on the new team.
- The A button (cross on PS2) now shows to the right of the highlighted row's right arrow instead of before the team; the arrows sit a little further left to make room.
- A queued team is now a clearly darker grey (the game's own greyed-out prompt colour).
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.30 · 2026-10-18 · Manage Players: centred options, A button shown, queued moves greyed and cancellable

*v5.30 · ManagePlayersConfirm* · Xbox, PS2 NTSC, PS2 PAL

- The team (or Kick) now sits in the middle between its arrows.
- The highlighted row shows the game's A button (cross on PS2) before its option, e.g. "(A) Red", to show that A picks it.
- Pressing A on a team queues the move for the player's next death, and that option goes grey.
- Pressing A on the grey option again cancels the move, and the row goes back to the player's current team. Picking another team and pressing A queues that one instead.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.29 · 2026-10-18 · Manage Players: arrows line up, no star or respawn note

*v5.29 · ManagePlayersArrows* · Xbox, PS2 NTSC, PS2 PAL

- The arrows either side of each player's team option now sit in the same place on every row, whatever team or Kick is shown.
- A move waiting for the player's next death now just shows the team they will move to (e.g. "Red"). The colour bar on the left keeps their current team, so a Blue player being moved to Red shows a blue bar and "Red".
- The star and the "* Team changes on respawn" line under the list are gone.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.28 · 2026-10-17 · Manage Players: boxed rows, team colour bars, waiting moves marked

*v5.28 · ManagePlayersLook* · Xbox, PS2 NTSC, PS2 PAL

- Each player row now sits in its own faint box (a small gap between rows), with a small bar at its left in the player's current team colour. The selected row keeps the game's highlight.
- A team waiting for the player's next death is marked with a star, e.g. "Blue *", and a small line under the list reads "* Team changes on respawn" (only when teams are on).
- Drawn with the same calls as the game's own in-match Players rows, so it works in a level on both consoles.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.27 · 2026-10-17 · Manage Players: shorter option names so long player names fit

*v5.27 · ManagePlayersShort* · Xbox, PS2 NTSC, PS2 PAL

- The options are now "Red", "Blue", "Yellow", "Green" and "Kick" (were "Red Team" ... "Kick Player"): the box is narrow, and a long name ran into a long option.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.26 · 2026-10-17 · Manage Players: team moves happen when the player dies; list cleaned up

*v5.26 · ManagePlayersOnDeath* · Xbox, PS2 NTSC, PS2 PAL

- Picking a team for a player now waits for that player's next death: they respawn on the new team, at its spawn points. The row shows the team they are waiting to move to; picking their own team again cancels it. Kick still happens straight away.
- The move is sent the frame after the death is scored, so it never counts as a team kill. A player already on the death camera (including a fall the host doesn't score) moves straight away. Their next spawn point is picked again for the new team.
- A waiting move is dropped at a new match, if the colour gets disabled, or if the player leaves (so someone joining in their slot isn't moved).
- The list now shows only players who are actually there (LAN always has 16 player slots; the empty ones showed as blank rows). PS2 checks its 8 slots.
- Rows are laid out like the Advanced Settings list: name on the left, team on the right (they overlapped before).
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.25 · 2026-10-17 · Manage Players moved to just above Leave Match

*v5.25 · ManagePlayersPlace* · Xbox, PS2 NTSC, PS2 PAL

- In the in-match pause menu (Options tab), Manage Players now sits just above Leave Match instead of below Return to Lobby. The order is now ... Audio/Video Options, Manage Players, Leave Match, Return to Lobby.
- Who sees it is unchanged: the LAN host only (not offline, not Xbox Live / PS2 online), and only when there is someone to manage.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL (the new place, when it shows, and Return to Lobby on its own after Leave Match).

## v5.24 · 2026-10-17 · Manage Players: player names show, heading inside the box

*v5.24 · ManagePlayersFix* · Xbox, PS2 NTSC, PS2 PAL

- The player rows were there but drew no text (they used the Xbox Live player list's row style, which leaves the text to its own drawing). They now show each player's name and their team / Kick Player.
- "Manage Players" is now the first line inside the box with the game's gap below it, as on the game's own in-match pages, instead of sitting on the box's top edge.
- Tests updated on Xbox, PS2 NTSC and PS2 PAL.

## v5.23 · 2026-10-17 · Manage Players: the host can move a player to another team or kick a player during a LAN match

*v5.23 · ManagePlayers* · Xbox, PS2 NTSC, PS2 PAL

- New "Manage Players" item in the in-match pause menu (Options tab), under Return to Lobby, for the LAN host. It shows only when there is someone to manage.
- Its page lists the players with their team. Left / right picks a team (only the colours playing; disabled colours are left out) or "Kick Player" (only for players on other consoles); confirm does it.
- Moving a player uses the game's own team message, the same one the disabled-colour redirect already sends, so players without the patch (Xbox original disc and title update, PS2) change team too. The player switches team where they stand; their next spawn uses the new team's spawn points.
- Kick uses the game's own kick: that console leaves the match for the menu (all players on it). They can join again.
- With Teamplay off only Kick Player is offered. If a player leaves while the page is open, the page closes instead of acting on the wrong player.
- Not tested yet in play: moving a player who is carrying a bag, and how team scores look after a move.
- Tests added on Xbox, PS2 NTSC and PS2 PAL (when the item shows, the rows and options, moving, kicking, refusing disabled colours and changed players).

## v5.22 · 2026-10-17 · Return to Lobby in the in-match pause menu

*v5.22 · ReturnToLobbyPause* · Xbox, PS2 NTSC, PS2 PAL

- Return to Lobby now shows in the pause menu during a LAN match (the Options tab: Continue, Controls, Audio/Video Options, Leave Match), right under Leave Match, for the host. v5.21 had put it on a different page, so it didn't appear there.
- It asks first, as before ("Return everyone to the lobby? The match will end."). The end-of-match menu item is unchanged.
- Tests added on Xbox, PS2 NTSC and PS2 PAL for the new place (when it shows, the item, the registers the menu code relies on).

## v5.21 · 2026-10-17 · LAN: Return to Lobby (host)

*v5.21 · ReturnToLobby* · Xbox, PS2 NTSC, PS2 PAL

- The LAN host can now send everyone back to the lobby, during a match or after it; the session stays up. The host chooses Return to Lobby: in the pause menu (after Change Game Type) it asks to confirm first, and in the end-of-match menu it goes straight away.
- It uses the game's own return to the lobby. The host runs it, then the game tells every console to follow, so players without the patch and on the original Xbox disc go back too. A match in progress is recorded as the game does.
- Only the host sees the option, the same as Change Game Type; other players are taken along. Not shown online (Xbox Live keeps the update's own option).
- Xbox shows the update's own (translated) "Return to Lobby"; PS2 shows the mod's own text. The confirm page uses the game's Leave Match page with its own question.
- Tests added on Xbox, PS2 NTSC and PS2 PAL: when the item shows, the confirm page and its texts, Yes and No, Leave Match unchanged, the end-of-match item on LAN and on Xbox Live.

## v5.20 · 2026-10-17 · Assault: Time Bonus After Phase; Auto-Complete Phase times as the game's own

*v5.20 · TimeBonusAfterPhase* · Xbox, PS2 NTSC, PS2 PAL

- New Assault setting, Time Bonus After Phase: Off / 1 Min / 2 Mins / 3 Mins (Advanced Settings, Modifiers, after Auto-Complete Phase).
- Each time a phase is completed and another one follows, the host adds that much to the match clock. It works whether the attackers complete the phase or Auto-Complete Phase does. Completing the last phase ends the match as before, and two phases completed at once give one bonus.
- Every console shows the host's clock, so LAN players without the patch get the extra time too. Only the host adds it.
- Greyed out when the match has no Time limit, since there is no clock to add to.
- With Auto-Complete Phase on as well, the next phase's timer starts after the bonus, so the bonus never counts toward it.
- Auto-Complete Phase's times now read 1 Min to 10 Mins, in the same style as the game's own Time limit (was 1 Minute to 10 Minutes).
- Tests added on Xbox, PS2 NTSC and PS2 PAL: every value, each later phase, none for the first phase, after the last phase or in a new match, no time limit, LAN players, PAL's 50 FPS, Auto-Complete together, and the menu item.

## v5.19 · 2026-10-17 · Advanced Settings cleanup: options greyed out when they can't apply

*v5.19 · AdvancedCleanup* · Xbox, PS2 NTSC, PS2 PAL

- Disable [colour] Team On greys out that colour's Respawn Delay; it comes back when the colour is enabled again.
- At least one team always stays pickable: once every other colour is disabled, the last one's Disable item is greyed out.
- Capture the Bag: Switch Spawns is greyed out while Team Spawns is Off (it swaps the teams' own spawn points, which Team Spawns Off doesn't use).
- Capture the Bag: Overtime is greyed out when the match has no Time limit (time never runs out, so it can't start).
- Catch-Up with no Time limit: Catch-Up Period is greyed out and Catch-Up runs all match. Before, Last Minute with no time limit meant Catch-Up never switched on.
- Greying is decided on each console's own menu, and the Catch-Up rule by the host, so players without the patch are not affected.
- Tests added on Xbox, PS2 NTSC and PS2 PAL for every rule (team colours and their delays, the last colour, Switch Spawns, Overtime, Catch-Up Period and Catch-Up with no time limit).

## v5.18 · 2026-10-17 · Advanced Settings inside a level: every option reachable, no colour bars

*v5.18 · InLevelAdvanced* · Xbox, PS2 NTSC, PS2 PAL

- Advanced Settings opened inside a level (End of match > New game) now shows 11 options at a time, not 15, and scrolls through the rest. The in-level panel is smaller: the list ran past its bottom edge, and the options below it could not be seen or reached.
- Inside a level the team icons next to Disable [colour] Team and the team Respawn Delay items are left out. The icon isn't loaded there, so it was drawn as a bar of the team's colour across the row. The front-end page is unchanged (15 at a time, with the icons).
- A level counts as "inside" the same way the game decides its own "in a level" flag: any level but the front end's.
- Tests added on Xbox, PS2 NTSC and PS2 PAL: the scroll height for 11 options in a level (and all of them when there are fewer), and no icon drawn in a level.

## v5.17 · 2026-10-17 · Gold Rush: an unpatched player's own death coin is removed

*v5.17 · SuicideCoinRemoval* · Xbox, PS2 NTSC, PS2 PAL

- Gold Rush / Coin Drop Player Kills: when an unpatched LAN player dies without a kill, their console makes a death coin only it has. The host already ignored it; now the host also tells that console the coin was collected (naming the host's player), so it disappears, and then re-sends any of the host's real coins on that spawn point.
- This fixes two things on the unpatched console: the private coin filled its pickup slots so it could stop seeing the host's real coins, and picking the private coin up could still score through Coin Rush (correcting the v5.16 note, which said it never counted).
- Side effect: on that unpatched console only, the host's player may briefly get 1 point counted locally for each removed coin. The scoreboard there comes from the host's score sync, so it should not show; to be checked in play.
- Only the dying player's console gets these messages; the host's coins and every other console are unchanged. Patched players reach this only when the host saw the death differently, and then get the same result.
- Tests added on Xbox, PS2 NTSC and PS2 PAL for the removal message, the re-sent coins and every skip case. An independent review found no problems.

## v5.16 · 2026-10-17 · Fixes: new-match detection, Catch-Up in Overtime, Spawn Rule bots, Showdown on LAN

*v5.16 · ConsistencyFixes* · Xbox, PS2 NTSC, PS2 PAL

- New-match detection is the same everywhere: a new match is only seen when the game clock goes back into its first 20 seconds (as King of the Hill already did). Gun Game, Gold Rush, Assault, Catch-Up, Overtime, Team VIP and Multikill used to treat any step back as a new match, which could wipe their state mid-match on a LAN player's console when the host corrects its clock (Multikill bonus kills and chains).
- A new match now also clears every player's Catch-Up extra kills and Multikill state, not only for the players who kill or score in its first 20 seconds: a player joining later no longer starts with the previous match's Multikill bonus or chain.
- Catch-Up with Catch-Up Period Last Minute stays on while Overtime holds a Capture the Bag match after time runs out (it switched off when the clock reached 0).
- Spawn Rule in team games: bots now spawn on the level's bot spawn points and players on player spawn points, as the game picks them (bots used player spawn points). As before, when fewer than 2 fit, the game's own pick is used.
- Showdown on LAN: the host now says it is a Showdown match in setup byte 73 (bit 3, with Multikill off), so patched LAN players show kills as the score for certain instead of guessing from the weapon set. With a host on an older version they guess as before only when it has no marker; host and players should use the same version.
- Gold Rush / Coin Drop Player Kills, checked: an unpatched player's own death coin only exists on their screen. The host ignores both the coin and its pickup, so the real score is never affected. Nothing changed.
- Tests added on Xbox, PS2 NTSC and PS2 PAL for every change (new-match checks in each feature, the per-player clear, Catch-Up in Overtime, Spawn Rule kinds for bots and players, byte 73 written and read). An independent review found two problems in the first version (Spawn Rule on PS2 when the game falls back to its full list; stale Multikill state for late joiners), both fixed before release.

## v5.15 · 2026-10-16 · Integrity review: 15 fixes from a full check of the mod

*v5.15 · IntegrityReview* · Xbox, PS2 NTSC, PS2 PAL

- PS2: the LAN host's team-pick check still wrote old debug counters into memory that now holds Switch Spawns code. A team pick arriving could break that code until the next frame (a possible host crash on a respawn in Capture the Bag). The counters are gone.
- PS2: a PS2 host sent the wrong setup byte 74 to LAN players. King of the Hill (Zones) and Switch Spawns (Capture the Bag) were read from its Gold Rush / Coin Drop settings, so patched players could see the Hill display with it off, miss it with it on, or spawn in the wrong base. It now sends the same byte as Xbox.
- Gun Game / Random Weapon: a weapon due to a player who had just died (a rocket that killed both players, a spawn kill) was dropped at their body, where anyone could take it. A patched LAN player who walked over it lost their own level weapon. It now waits for the respawn, as Showdown already did.
- Weapon switch for players without the patch: an "Always" given in the last seconds of a match stayed on that player's console after the match. This happened every time a Showdown match ended on a kill. It is now put back when the match ends. A player who changes their own setting to Always between matches also no longer gets their old setting put back.
- Random Weapon: the host's own players and bots no longer lose a map gun they picked up just before their random weapon arrives. Other consoles' players already kept theirs.
- Xbox: consoles with the title update heard track 1 (Scotland the Brave) after a Showdown restart, or after a new match started from inside a level, when the host's music was the level's own. They now get the host's music.
- Capture the Bag Overtime: with no time limit, patched LAN players saw "Overtime!" 1.5 seconds into every match. Fixed.
- Multikill: the setting LAN players get is now set at the start of every match. Changing the mode or Teamplay after leaving the Advanced page no longer leaves it out of date.
- Gladiator with Team VIP: a LAN player whose own Team VIP setting differed from the host's got the wrong Respawn Delay. Teams now follow the host's match.
- King of the Hill: the host's 10-second zone colour resend could give a player who had just respawned their old spawn point again. It now skips players whose spawn point is still pending.
- Start of a LAN match: other consoles could start their countdown up to 1.5 seconds after the host's player. The host now sends every spawn point it held back the moment it leaves Select Team.
- PS2: Switch Spawns now does nothing with Team Spawns Off, as on Xbox. Random Characters no longer re-randomises a LAN player's own copy of the setup; only the host decides, as on Xbox.
- Gold Rush: its fallback spawn points (used only when no navigation pad is usable) now skip MapMaker placement pads, which it could not place a coin on correctly.
- The Advanced Settings page opens on its top item again; in team modes it opened on Teamplay at the bottom.
- Tests: the Xbox Gun Game test had been stopping part-way since Setbacks was added, so its Coin Rush, MapMaker and Showdown sections were not running. It now runs to the end, and the build flags any test that does not finish. Every fix above has new tests on Xbox, PS2 NTSC and PS2 PAL. Unused code and stale comments were removed.

## v5.14 · 2026-10-16 · Fix: the host crashed starting a LAN Gun Game or Showdown match on a MapMaker map

*v5.14 · MapMakerGunGameCrash* · Xbox, PS2 NTSC, PS2 PAL

- Fixed: on LAN, pressing Start for Gun Game or Showdown on a MapMaker map crashed the host (Xbox: at "Game starts in 0"; the other consoles then showed the network error).
- Cause: before the map is sent, the host reads it to turn its weapon factories into normal gun pickups. Reading a map tile uses the game's tile tables, and in the lobby the game has only set up the first layer of each tile; it sets up the rest when it builds the map. A map with any two-layer tile made the host read from address 0. It only worked if the host had already been in MapMaker since switching on. PS2 read the same uninitialised entries.
- Now the host fills in the missing layer entries exactly as the game's own MapMaker set-up does before reading the map, and a tile number outside the game's 45 tiles counts as an unreadable map (sent as it is) instead of being read.
- Showdown on a MapMaker map went through the same step and is fixed the same way. Nothing else in the mod reads MapMaker data from the lobby.
- New tests (Xbox, PS2 NTSC and PAL): the real map from the crash, run through the game's own tile code in the lobby state: no crash, the same 8 gun items found on every platform, only those turned off, layer entries as the game makes them, bad tile numbers refused.

## v5.13 · 2026-10-16 · Fixes: Setbacks One Weapon starts the older weapon at 0 kills; LAN lobby no longer stuck on Assault maps

*v5.13 · SetbacksOneWeapon-LANAssaultMaps* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game Setbacks, One Weapon: a player set back now starts the previous weapon with no kills on it. Before, they kept the kills they had on the weapon they lost, so they could be one kill from moving up again. On the first weapon their kills still go. One Kill is unchanged.
- LAN lobby: when the host's match came up as Assault, the map list only showed Assault maps, so there was no way to change to another mode without backing out. On LAN the map is picked first and the mode after it, and the mode list already leaves Assault out on maps without it, so the map list now shows every map again on LAN. Change Game Type still only lists Assault's own maps for Assault.
- Tests updated (Xbox, PS2 NTSC and PAL): One Weapon from a later weapon, from the first weapon, and with no kills; the map list on LAN and offline.

## v5.12 · 2026-10-16 · Fix: Xbox players without the title update joining a match that hasn't started

*v5.12 · LobbyEarlyJoinFix* · Xbox

- Fixed a game bug: a player on an Xbox without the title update could be sent to Select Team while the host was still in the lobby or match settings. It happened whenever the host's Music setting was anything other than the level's own music.
- Cause: the title update added one setting to the match info the host sends. A console without the update reads the host's Music value where it expects the "host is in a match" flag, so it took the lobby for a match in progress.
- Now, while the host is in the lobby, the lobby updates go out with that value at 0. The host keeps its Music setting, and the match start and mid-match joins still send it, so consoles with the update still play the chosen music.
- Decided by the host; works with consoles without the patch. Xbox only (the title update is Xbox only; PS2 only gets the new version number).
- New Xbox test: lobby and in-match sends, Music 0 / set, arguments and saved registers.

## v5.11 · 2026-10-16 · New: Assault Auto-Complete Phase (Off / 1-10 Minutes)

*v5.11 · Assault-AutoCompletePhase* · Xbox, PS2 NTSC, PS2 PAL

- Assault has a new Modifiers item, Auto-Complete Phase: Off, or 1 to 10 Minutes. It is only shown for Assault.
- When a phase has gone on that long, the host completes it as if the attackers had done it, and the match moves on to the next phase. The time is counted from the start of each phase on the match clock, so it pauses when the clock does. With no time limit, game time is used.
- The last phase is never completed this way: players must finish it themselves.
- Match time is not changed: completing a phase never adds time, so a match can still run out right after an auto-completed phase.
- Decided by the host (offline: this console). Every console, including those without the patch, follows through the game's own phase sync, so they get the same objective text, spawn points and doors as after a normal completion.
- New tests (Xbox, PS2 NTSC and PAL): timing per phase, the timer restarting each phase and each match, the clock stopping, no time limit, never the last phase, Off / not Assault / LAN player / one phase, 1 and 10 minutes, menu item, refresh and apply.

## v5.10 · 2026-10-16 · Fix: Random Characters no longer hands out characters Ban Small Characters bans

*v5.10 · RandomCharacters-BanSmall* · Xbox

- Random Characters picks every player's character when the match setup is built, after the game's own Ban Small Characters step (which switches banned picks to Harry Tipper), so it could still give someone a small character. Each pick is now checked with the game's own character check (the one its character select uses) and picked again if banned (up to 40 tries).
- Checked: the game's own lobby ban step (the host switches banned picks when it builds the setup; consoles with the update do it again when they receive it) still runs with the mod.
- Xbox only: Ban Small Characters is a title update setting, and PS2 has no title update. The PS2 files only change version.
- New tests (Xbox): banned picks are picked again; it gives up after 40 tries.

## v5.9 · 2026-10-16 · Fix (game bug): Xbox players without the title update heard Scotland the Brave instead of the level's music

*v5.9 · DiscMusicFix* · Xbox

- The title update added a field to the match info the host sends: the host's Ban Small Characters setting (consoles with the update only test it for on / off). A console without the update has no such field, so it reads its Music setting one field early, from that one. With Ban Small Characters on, it played track 1, Scotland the Brave, on every map.
- The host now fills that field so both work. Ban Small Characters off: 0 (as before; Music 0 is the level's own music). On: the host's Music when it is a track, else a non-zero value that the music table lookup on consoles without the update turns back into entry 0, the level's own music. Consoles with the update still see Ban Small Characters exactly as before.
- Consoles without the update now hear the level's music, or the host's chosen track when Ban Small Characters is on. With it off they still get the level's music rather than a track the host picked (the field has to stay 0 there).
- Xbox only: PS2 has no title update. The PS2 files only change version.
- New tests (Xbox): the value sent for each case, and that registers are kept.

## v5.8 · 2026-10-16 · Gun Game Setbacks: "Humiliation!" and a laugh for the player set back; LAN players use the host's Respawn Delay

*v5.8 · Humiliation-HostRespawnDelay* · Xbox, PS2 NTSC, PS2 PAL

- Setbacks (Gun Game): the player who is set back sees "Humiliation!" in the centre of their screen (like the multikill messages) and hears a crow's cackle (sound 5659). Only the victim gets it.
- On LAN the host sends it only to the victim's console, as a coin message that names one of that console's own players with pad 0xFFFE. Every console ignores a coin message for its own player, so unpatched consoles are unaffected; patched consoles show the message.
- The cackle is loaded at level start, the same way as the multikill jingle.
- Respawn Delay (everyone's and Red / Blue / Yellow / Green) now comes from the host: the host writes the mode's delays into setup bytes 64-66 (byte 64 = 0xE0 | everyone's, 65 = 0x80 | Red | Blue << 3, 66 = 0x80 | Yellow | Green << 3). Before this, patched LAN players used their own console's menu values.
- A patched LAN player with an unpatched host gets no delay, the same as the host's own players.
- Audit: every other patch setting a LAN player's console uses already comes from the host (setup bytes 72-75 or the match info), or the host decides it.
- New tests (Xbox, PS2 NTSC and PAL): the message, the laugh and the coin message, the receive side, sound loading, and Respawn Delay on host, LAN player and with an unpatched host.

## v5.7 · 2026-10-16 · Fix: Switch Spawns works (the game numbers teams 1-4, Red 1 / Blue 2)

*v5.7 · SwitchSpawns-TeamNumbers* · Xbox, PS2 NTSC, PS2 PAL

- Switch Spawns still didn't work: it took Red and Blue to be teams 0 and 1, but the game numbers teams 1-4 (Red 1, Blue 2). So it swapped Red with 'no team' (which can spawn at any spawn point) and left Blue alone, and the first-spawn check never found a point to move. Red and Blue (1 and 2) are now swapped, and the spawn point check uses their real flags (Red bit 2, Blue bit 3).
- Tests (Xbox, PS2 NTSC and PAL) now use the game's real team numbers and spawn point flags (the spawn flag plus Red / Blue / both / none / team 3).

## v5.6 · 2026-10-16 · Fixes: Switch Spawns now also covers the first spawn and LAN players; a Gold Rush joiner sees the coins; Catch-Up last in Modifiers

*v5.6 · SwitchSpawns-FirstSpawn-GoldRush-Join* · Xbox, PS2 NTSC, PS2 PAL

- Switch Spawns: the first spawn of a match (and the spawn points the host picks for other games' players) came from the game's fixed start points, which the team swap didn't see, so you started at your own base and LAN players kept spawning by their own bag. Every spawn point picked for a player is now checked: if it is one of their own team's, a random usable one of the other team's is used instead. Points already at the other team's base, shared points and other teams are left alone.
- Gold Rush (Coin Rush): someone who joined a match in progress saw no coins, because coins now stay until taken and their game never received the ones already out. The host now sends that player's game each coin already on the map (the same message the game uses for a dropped coin, to that game only), so it works for consoles without the patch too.
- Advanced Settings: Catch-Up and Catch-Up Period are now always last in Modifiers.
- Tests (Xbox, PS2 NTSC and PAL): the spawn check for each team, shared / other-team points, Switch Spawns off, no Teamplay, team spawn points off, a LAN player following the host's setting; the coins sent to a joiner (host only, Thief only, the host's player and each coin's pad).

## v5.5 · 2026-10-16 · Advanced Settings: Respawn Delay in General Settings; mode-style modifiers first in Modifiers

*v5.5 · Settings-Order* · Xbox, PS2 NTSC, PS2 PAL

- Respawn Delay (the one for everyone, not the per-team delays) moves from Team Settings to General Settings, right after Spawn Rule. Modes without teams no longer show a Team Settings section just for it.
- Modifiers that turn a mode into its own game come first in Modifiers: Gold Rush, Team VIP, King of the Hill, Showdown, Weapon Mode (with Kills To Advance and Setbacks). The rest follow in their old order.
- Tests (Xbox, PS2 NTSC and PAL): the section order in every mode checked, and the page height with one header fewer.

## v5.4 · 2026-10-16 · Builds have version numbers; the version is shown on the Advanced Settings title

*v5.4 · Version-Numbers* · Xbox, PS2 NTSC, PS2 PAL

- Every build now has a version number (v<major>.<minor>): a big new feature bumps the first number, everything else the second. Past builds are numbered in order: v1 the starting point and the first options, v2 Weapon Mode, v3 King of the Hill, v4 Showdown, v5 the Advanced Settings sections. Each one keeps its date and old name.
- The Advanced Settings page title shows the build, e.g. "Advanced Settings (v5.4)", so you can check which version a console is running (Xbox, PS2 NTSC and PAL).
- Builds are kept in the project folder under builds/<version> <date>/ from v5.3 on (older build files weren't kept).
- Tests (Xbox, PS2 NTSC and PAL): the title shows the version and the page's own title is put back afterwards.

## v5.3 · 2026-10-16 · Showdown: players who are out show "--" on consoles without the patch, not their kills as a time

*v5.3 · Showdown-Dash-Unpatched* · Xbox, PS2 NTSC, PS2 PAL

- A console without the patch shows a player who has no lives left as a time made from the score the host sends (kills read as seconds, e.g. 0:-3.0). In a Showdown match the LAN host now sends 0 for those players, which that game shows as "--". The order is still the host's ranking (by kills).
- A patched LAN player's game no longer takes the score from that sync for Showdown: the score text counts that player's kills itself (kill count routine), so patched consoles still show the kills for everyone, out or not.
- Host-decided: only the host's own Showdown setting changes what is sent; nothing changes outside Showdown.
- Tests (Xbox, PS2 NTSC and PAL): the sync sends 0 only for a Showdown player with no lives left (host / offline, Elimination and Vampire, lives on), the score text's own kill count on a LAN player's game in a Showdown match, registers kept.

## v5.2 · 2026-10-16 · Fixes: Switch Spawns now swaps spawns; Showdown score shows kills (not kills - 180); clearer section headers

*v5.2 · Fix-SwitchSpawns-SDScore-Headers* · Xbox, PS2 NTSC, PS2 PAL

- Switch Spawns didn't work: the hook was on Assault's attacker / defender spawn lists (game type 3 is Assault), not Capture the Bag. Capture the Bag uses the team spawn points, which the game picks by the team's pad flag (bit team + 1). The swap (Red <-> Blue) is now there; the Assault hook is removed (PS2: its original word written back).
- Showdown score showed kills - 180 (-176 for 4 kills): in Elimination and Vampire the game takes 3 seconds' worth (3 x 60) off every rank score as a sorting trick for their lives / time scores. A Showdown match (host / offline, and a patched LAN player's game) now skips it, so the score is the kills.
- Section headers stand out from the settings: further left (left margin 2 instead of 5) and the menu's other text style (item flag 0x200 in place of 0x100). They still can't be selected.
- Tests (Xbox, PS2 NTSC and PAL): the team swap for every team at the new place, the Assault path untouched; the ranking's mode step in and out of Showdown (and for a LAN player in a Showdown match); the headers' margins and style, then the items' back.

## v5.1 · 2026-10-15 · Capture the Bag: Switch Spawns (Red spawns at Blue's base, Blue at Red's)

*v5.1 · CTB-Switch-Spawns* · Xbox, PS2 NTSC, PS2 PAL

- New Capture the Bag setting in Advanced Settings > Modifiers (after Overtime): Switch Spawns, Off / On. On: each team spawns at the other team's base. The bags stay at their own bases.
- How: the game picks a Capture the Bag spawn from the team's own base spawn list; with Switch Spawns the team it goes by is swapped.
- LAN: the host decides. It picks every player's spawn point when they die and sends it, so players without the patch spawn switched too. A patched player's console that picks its own spawn (Spawn Rule on) gets the setting from the host in byte 74 (bit 2 in Capture the Bag; the Thief coin bits there are unchanged).
- Tests (Xbox, PS2 NTSC and PAL): when it applies (Capture the Bag; offline / host setting; LAN player from byte 74 with its marker; other modes never); the team swap for every team, registers kept; byte 74 in Capture the Bag and Thief; the item only in Capture the Bag; refresh / apply; the menu's item order.

## v5.0 · 2026-10-15 · Advanced Settings in sections (General Settings, Modifiers, Team Settings); Showdown Lives code removed

*v5.0 · Settings-Sections* · Xbox, PS2 NTSC, PS2 PAL

- Advanced Settings is now grouped under three headers. General Settings: Spawn Rule, Player Drops Gun, Random Characters, Disable Unarmed, Infinite Ammo, Mercy Rule. Modifiers: Weapon Mode, Kills To Advance, Setbacks, Showdown, Gold Rush, Coin Drop, Catch-Up, Catch-Up Period, Multikill, Multikill Window, Reverse Scoring, Score With Bag Away, Overtime, King of the Hill, Number of Flames, Flame Pass, Spread By Kills, Zone Scoring Interval, Team VIP. Team Settings: Teamplay, Team Spawns, the Disable [colour] Team items, Respawn Delay and the team Respawn Delay items.
- Each mode shows only the settings it has, and a section with none of them has no header. Headers can't be selected (the cursor skips them). Anything not in the list goes at the end of General Settings. The settings on the normal page are unchanged.
- How: the page is built as before, then the items are put in section order, each row keeping its height, with its option text moved with it, and the list relinked. The scrolling (15 options at a time) counts the new order.
- The leftover Showdown Lives code (its item, value, apply and greying; Showdown now uses the mode's own Lives) is removed on all three builds.
- Tests (Xbox, PS2 NTSC and PAL): the order for every page kind (Bag Tag, Team Deathmatch, Capture the Bag, Assault, Deathmatch, Zones, Gladiator, Flame Tag); headers (labels, can't be selected, none for an empty section); rows laid out in the new order with their option texts; the links; the scrolled part's first / last item; the scroll height with the headers; registers kept.

## v4.14 · 2026-10-15 · Showdown moves to Elimination and Vampire; kills shown as the score on patched LAN consoles

*v4.14 · Showdown-Elimination-Vampire* · Xbox, PS2 NTSC, PS2 PAL

- Showdown is now offered in Elimination and Vampire (teams or not), in place of Deathmatch, Shrink, Regeneration and Leech. It plays the same way: slot 1's gun, one bullet each life and one more per kill, one-hit shots, no map weapons or armouries, and kills are the score that decides the match.
- Lives come from the mode's own Lives setting (1, 2, 3, 4, 5, 10 and up), so the separate Showdown Lives item is gone. Because these are the game's own lives modes, consoles without the patch already handle lives, elimination and the end of the match natively.
- Mid-match joiners: in these modes the game gives a joiner the fewest lives of anyone, counting players who are already out, so a joiner could start with 0 and die at once. In Showdown the host now skips the players who are out (and uses the Lives setting if nobody else has any). The earlier join fix for the old modes is replaced by this.
- Score display on a patched LAN player's console: it recognises a Showdown match from the host's match info (lives, Elimination or Vampire, only weapon-set slot 1 filled). The score then shows kills, and the ranking uses them, as on the host. Consoles without the patch still show lives.
- Tests (Xbox, PS2 NTSC and PAL): every Showdown test moved to Elimination / Vampire; menus (Showdown item only in those modes, no Showdown Lives); setup leaves the lives alone; joiner lives through the game's own call; the LAN player's detection (lives, mode, slot 1 only, not the host) for the score text, ranking and score.

## v4.13 · 2026-10-15 · Fix: a player joining a Showdown match in progress died straight away

*v4.13 · Fix-Showdown-Join-Death* · Xbox, PS2 NTSC, PS2 PAL

- Cause: when someone joins mid-match, the game gives them lives only in its own lives modes (Elimination-style modes). Showdown runs in Deathmatch, Shrink, Regeneration and Leech, so a joiner started with 0 lives, and the LAN host's lives check killed them at once.
- Fix (Xbox, PS2 NTSC and PAL; host-decided, so joiners on unpatched consoles are covered too): a Showdown joiner now gets the fewest lives left among the players still in. If nobody else has lives left, they get the match's Showdown Lives setting. This is how the game handles its own lives modes, except that players who are already out are skipped. That means a joiner can never start with more lives than anyone still playing.
- Tests (Xbox, PS2 NTSC and PAL): the fewest lives of the others still in; players who are out, not connected, or on the joiner's own console are skipped; the Showdown Lives setting is used when nobody else has lives; nothing changes outside Showdown, on a LAN client, or with no lives set; registers are kept.

## v4.12 · 2026-10-15 · Fix: the LAN host's player kept dying in Showdown; Showdown score shown as kills

*v4.12 · Fix-Showdown-LAN-Deaths* · Xbox, PS2 NTSC, PS2 PAL

- Cause: in a match with lives, the LAN host regularly checks each player's lives left and keeps anyone with none dead. To rank Showdown by kills, the mod had stopped the game filling in that lives-left value, so it stayed at 0 and the host killed its own player at every check (no attacker, a few seconds after each spawn, until its lives ran out). Offline never runs that check. Found with a debug build that logged every kill on Jake's xemu host.
- Fix (Xbox, PS2 NTSC and PAL): Showdown still ranks by kills, and the lives-left value is filled in again as the game does.
- Showdown with lives showed the score as a time (the lives-mode format). The host and offline games now show kills, as in Deathmatch. Other consoles still use the game's lives format.
- Tests (Xbox, PS2 NTSC and PAL): the ranking keeps lives left in and out of Showdown; the score text path in and out of Showdown.

## v4.11 · 2026-10-15 · Showdown back to weapon slot 1; LAN armouries moved out of reach in Gun Game and Showdown

*v4.11 · Showdown-Slot1-ArmouryMove* · Xbox, PS2 NTSC, PS2 PAL

- Showdown hands out the weapon set's slot 1 gun again (was slot 6). On the weapon set page, slots 2-6 are greyed out and can't be picked while Showdown is on. LAN Showdown sends only slot 1 in its weapon set, so no console builds pickups, ammo or armouries for slots 2-6.
- LAN, Gun Game and Showdown: at the start of the match the host moves every armoury out of reach on every console, including consoles without the patch. It uses the game's own "dropped" message to send each armoury's base to a pad at least 3.5 units above or below the armoury, with no pad within 2.5 units across at the armoury's height. The game only gives an armoury's gun to a player standing within 1 unit of the base at the armoury's original height, so nobody can use it there or where it was. On every stock map with armouries, one or two such pads take them all (the bases sit on top of each other). Players who join mid-match get the same moves.
- Consoles without the patch still show the floating gun model where the armoury was, but it gives nothing. The host and consoles with the patch hide armouries completely. Gun Game keeps its full 6-weapon ladder (the real weapon set), so every console still has every gun loaded.
- This also closes the armoury gap in LAN Gun Game: a player with the patch who took one of the ladder's guns from an armoury was switched to it and lost the gun they had.
- Edge case (no stock map has it): an armoury with no pad 3.5 units above or below it is hidden on the host only and stays usable on the other consoles.
- Tests (Xbox, PS2 NTSC and PAL): pad choice at every limit (3.5 / 2.5 / 3.0), pads not in use, both pad lists, several armouries, more than 31, the joiner, host only; 600 random maps against the rule written out separately; the exact message bytes; the message through the retail decoder (and the retail drop on PS2) and the patched decoder. Every instruction of the new code was broken one at a time; the tests caught every change that alters behaviour. An independent review found no crash or desync risk for consoles without the patch.

## v4.10 · 2026-10-15 · Showdown uses weapon slot 6; no slot 1-5 armouries on LAN; MapMaker armouries off in Gun Game and Showdown; ammo boxes collected

*v4.10 · Showdown-Slot6-MapMaker* · Xbox, PS2 NTSC, PS2 PAL

- Showdown now hands out the weapon set's slot 6 gun (was slot 1). On the weapon set page, slots 1-5 are greyed out and can't be picked while Showdown is on. A set whose slot 6 is empty or Unarmed gives no gun, so pick one for slot 6.
- LAN Showdown: the match goes out with only slot 6 in its weapon set, so no console builds weapon pickups, ammo or armouries for slots 1-5, including consoles without the patch. The host leaves them out of its own map the same way. Slot 6 stays in the set, so every console still has that gun loaded (the countdown crash fix holds). Slot 6's armouries remain; on the stock arcade maps only Virtua (an Assault map) has one in a deathmatch-style mode.
- MapMaker maps on LAN, Gun Game and Showdown: gun items set to "always available" (the ones that become armouries) reach every console as normal gun pickups. They ride in the map the game already sends when the host presses Start; its map-send screen waits until every console has it. The host builds its own map the same way. They are then normal map guns: collected at the start, never back. The host's saved map is unchanged.
- Gun Game and Showdown: map ammo boxes are now collected at the start and stay hidden, like map guns.
- Removed: sending the full weapon set again during a match and to mid-match joiners (left over from the empty-set approach). Restart still sends Showdown's slot-6-only set first.
- Fixed (PS2, found in review): the restart resend went over 16 network clients, but the PS2 game has 8, so it could send to memory past the client list. It only ran on LAN Showdown restarts.
- Redundant code removed (Xbox and PS2): a flag every caller set, a tile-count limit the map's size checks already cover, a rounding step that never changed an item's size, reloads of registers that already held the value, and a value saved around a call that keeps it.
- Tests (Xbox, PS2 NTSC and PAL): slot 6 hand-out and greying; the slot-6-only match packet for starts, joiners and restarts; the MapMaker walk, turn-off and put-back with damaged and edge-case maps; the Start decision; ammo boxes; PS2's 8 clients. Every instruction of the new PS2 code was changed one at a time (removed, branch flipped, constant changed): only changes that can't alter the result went unnoticed. The Xbox changes had the same kind of check.

## v4.9 · 2026-10-15 · Fix: original Xbox players crashed at the countdown in Gun Game and Showdown

*v4.9 · Fix-LAN-WeaponSet* · Xbox, PS2 NTSC, PS2 PAL

- Cause: each console preloads the guns (models and animations) of the weapon set it loads the map with. Gun Game and Showdown sent the match out with an empty weapon set, to keep armouries and pickups off every map. So a console without the patch had none of the match's guns loaded, and crashed at the countdown once guns were handed out. Jake's three test builds found it: only the one that started with the normal weapon set didn't crash.
- Fix: LAN matches always go out with the real weapon set (Xbox, PS2 NTSC and PAL). Map guns are still taken away at the start for everyone, as before. Offline Gun Game and Showdown still build the map without weapon, ammo and armoury pickups.
- Side effect: on LAN, armouries and ammo boxes are back in Gun Game and Showdown, for everyone. The host can't remove an armoury once the map has one; that's why the empty set was used. The empty-set code is left in place but unused.
- Tests updated (Xbox, PS2 NTSC and PAL): the match-start packet keeps the real set in Gun Game, Showdown and on MapMaker maps.

## v4.8 · 2026-10-15 · Showdown is its own Off / On item; team items unavailable with Teamplay Off; Gladiator team respawn delays; no scrolling with 15 options or fewer

*v4.8 · Showdown-Toggle-TeamItems* · Xbox, PS2 NTSC, PS2 PAL

- Showdown is now its own item (Off / On) below the Gun Game items, with Showdown Lives below it. Weapon Mode is back to Off, Gun Game, Random Weapon. With Showdown On, Weapon Mode, the Gun Game items, Catch-Up, Multikill and Player Drops Gun are greyed out. Weapon Mode keeps its own setting for when Showdown is turned Off. Showdown is still in Deathmatch, Shrink, Regeneration and Leech.
- Spawn Rule: Near Teammates can't be picked while Teamplay is Off; scrolling skips it. Turning Teamplay Off changes a Near Teammates setting to Default. Modes without teams already didn't offer it.
- New order at the bottom of Advanced Settings: the Disable [colour] Team items, then Respawn Delay (everyone), then the team Respawn Delays.
- Friendly Fire (match settings page) is greyed out while Teamplay is Off. The game linked it to its own Teamplay item, which the mod had moved off that page. Team Spawns, the team Respawn Delays, the Disable colours and Near Teammates were already unavailable with Teamplay Off.
- Gladiator now has the team Respawn Delays as well as Respawn Delay. Team VIP is its team toggle. With Team VIP On, the team delays, Team Spawns and Disable colours apply and Respawn Delay is greyed out. With Team VIP Off it's the other way round. At a death the delay is the team's when Team VIP is On.
- Fixed: lists with 15 or fewer options could still scroll a little. The last item's height wasn't counted in the scroll height, because the game only counts an item once it's finished. The last item is now finished first, as the game's own end of a scrolling list does.
- Tests updated and added (Xbox, PS2 NTSC and PAL): Showdown item (menu, refresh, apply, changefn), the new order, Gladiator delays and greying, Near Teammates, Friendly Fire, the last item finished first.

## v4.7 · 2026-10-15 · Mercy Rule times: 1 Min, 2 Mins, 3 Mins, 5 Mins

*v4.7 · Mercy-Mins* · Xbox, PS2 NTSC, PS2 PAL

- Mercy Rule times read 1 Min, 2 Mins, 3 Mins, 5 Mins (were 1 Minute .. 5 Minutes in the last build).

## v4.6 · 2026-10-15 · Showdown in kill modes with Showdown Lives; Team Spawns under Teamplay; Team VIP 6 units; units on every value

*v4.6 · Showdown-Kills-Lives* · Xbox, PS2 NTSC, PS2 PAL

- Showdown is now in Deathmatch, Shrink, Regeneration and Leech (teams allowed; not Team Deathmatch), and no longer in Elimination or Vampire. In those modes Weapon Mode lists Off, Gun Game, Random Weapon, Showdown. Gun Game is listed whatever Teamplay is set to, but still only plays with Teamplay Off.
- Showdown Lives (1 Life to 5 Lives, default 3 Lives), below the Gun Game items. It uses the game's own lives, as Elimination does: a player with no lives left doesn't respawn. The match ends when one player is left, or with Teamplay when one team is left, or on the score or time limit. Kills are the score that decides the match, not lives left. The host keeps that score; players without the patch see their lives on their HUD.
- With Showdown chosen, the Gun Game items, Catch-Up, Multikill and Player Drops Gun are greyed out (and One Shot Kill, Score Method and Always Start With Gun on the match settings page, as before). Catch-Up and Multikill are off in a Showdown match.
- The weapon switch for players without the patch was already used for every Showdown hand-out (each life's bullet and each bullet for a kill).
- Order at the top of Advanced Settings: Teamplay, then Team Spawns, then Spawn Rule.
- Mercy Rule times now read 1 Minute, 2 Minutes, 3 Minutes, 5 Minutes (were 1 Min .. 5 Min). Every other option value already had its word.
- Team VIP (Gladiator): the VIP has to move 6 units between scoring ticks again (was 8).
- Tests updated and added (Xbox, PS2 NTSC and PAL): Showdown modes and menus, Showdown Lives (menu, setup, score, team points, ranking, the end), Catch-Up / Multikill off, Mercy Rule times, 6 units.

## v4.5 · 2026-10-15 · Advanced Settings: new order, one Spawn Rule, Respawn Delay in every mode, scrolling past 15 options

*v4.5 · Advanced-Order-RespawnDelay* · Xbox, PS2 NTSC, PS2 PAL

- Order: Teamplay (where the mode has it) at the top, then Spawn Rule and Team Spawns, then the mode's Advanced items, then the Respawn Delay items, then the Disable [colour] Team items. The first selected item is the top one.
- Fixed: Deathmatch and every other mode without teams showed Spawn Rule twice on Xbox (the no-team spawn items were added, then the Spawn part ran again). Each item is now added once on both consoles.
- Fixed: items added after the mode's Advanced items had different text margins, so they weren't lined up. Every group now uses the margins and item flags the title sets.
- The list scrolls only when it has more than 15 options, and then shows 15 at a time.
- Respawn Delay in every mode. Modes without teams get "Respawn Delay". Modes that always have teams get the team items. There's one per team colour the mode has (2 or 4); Assault keeps Attacker / Defender. Modes with a Teamplay option get both. "Respawn Delay" is greyed out while Teamplay is On, and the team items, Team Spawns and Disable colours are greyed out while it is Off. This updates as Teamplay is changed.
- At a death the delay is the team's when the match has teams (a mode that always has them, or Teamplay On), otherwise the everyone setting. Where the delay is applied hasn't changed.
- Team icons: drawn at whole pixels (icon and shadow), so the figure isn't blurred.
- Tests rewritten for the new order, greying and death delay (Xbox, PS2 NTSC and PAL).

## v4.4 · 2026-10-15 · Gun Game and Showdown: MapMaker maps without weapon factories, pickups or ammo

*v4.4 · MapMaker-NoArmoury* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game and Showdown on a MapMaker map now load without its gun pickups, weapon factories (gun items with the locker option, which become armouries) or ammo boxes, like normal maps. MapMaker items take their weapon from the weapon set's slots like any map, so the match-start packet's empty weapon set covers them on every console, original disc included. The real set follows once the match is running, as on normal maps.
- Only the "not on a MapMaker map" check was removed (Xbox XNMS, PS2 NW45). Untested on a MapMaker map over LAN: whether resending the real set mid-match makes a console reload or ask for the map again needs checking.
- Tests updated (Xbox, PS2 NTSC and PAL): MapMaker map with Gun Game / Showdown gets the empty set; MapMaker map without them is unchanged.

## v4.3 · 2026-10-15 · Team icons: Xbox fixed, Assault Attacker / Defender added

*v4.3 · Team-Icons-2* · Xbox, PS2 NTSC, PS2 PAL

- Xbox: the previous build's XBE didn't have the team icons. The patcher stopped at the hook in the XBE header (0x11176) and the build went on with the older XBE. Fixed; the build now stops on any patcher error.
- Assault's "Attacker Respawn Delay" and "Defender Respawn Delay" get the team icon too: red for attackers, blue for defenders.
- Tests added: the Attacker / Defender hooks (Xbox, PS2 NTSC and PAL).

## v4.2 · 2026-10-15 · Team icons on the Disable Team and team Respawn Delay items

*v4.2 · Team-Icons* · Xbox, PS2 NTSC, PS2 PAL

- "Disable Red / Blue / Yellow / Green Team" and "Red / Blue / Yellow / Green Respawn Delay" (Advanced Settings) now show the game's own figure icon just after the text, in that team's colour, with the same shadow the bot / team display on the match settings page gives it. It is the game's icon 22 from its files, drawn the way the game draws it; nothing new was made. Attacker / Defender Respawn Delay (Assault) have none: the sides aren't one colour. Only the menu on a patched game changes.
- Removed (in the build before this one): the Flame Tag LAN change that spared the flame holder from the hit slowdown. Each console slows its own player, so patched players would have had an advantage. It will not be added again.
- Tests added (Xbox, PS2 NTSC and PAL): where the icon goes (after the text and a space, in the middle of the row), its colour and shadow, the font put back, and the hooks on the colour and team Respawn Delay items.

## v4.1 · 2026-10-15 · Fix: guns missing in every mode; Advanced Settings on one page; Score Method greyed

*v4.1 · Advanced-OnePage* · Xbox, PS2 NTSC, PS2 PAL

- Fix: weapon pickups, ammo and armouries were missing in every mode (and could crash a player on the original disc at the start). The "is this Gun Game" check read the wrong byte of the match info, so every match went out with an empty weapon set. It now reads setup byte 72 (match info +0x14) on Xbox, PS2 NTSC and PAL.
- Advanced Settings is one page: the Team Settings and Spawn Settings items follow the Advanced items (no folder links). With more than 15 items the list scrolls with the game's own scroll bar and arrows. This also fixes the title and text being misaligned after visiting a sub-page.
- PS2 PAL: the Advanced Settings builder now reads the menu mode at PAL's address (it read the NTSC one).
- Score Method is greyed out with Gun Game (and Showdown, where the game doesn't list it).
- Checked: a Setback on the first Gun Game weapon always keeps that weapon (the level never goes below the first weapon).
- Tests added: one-page builder (parts per mode, scroll height, no links), Score Method greying (Xbox, PS2 NTSC and PAL); empty weapon set regression for non-Gun Game modes.

## v4.0 · 2026-10-15 · Showdown: a new Weapon Mode for Elimination and Vampire

*v4.0 · Showdown* · Xbox, PS2 NTSC, PS2 PAL

- Weapon Mode (Advanced Settings) has a new option, Showdown, in Elimination and Vampire, with or without teams. The number of lives comes from the game's own Number of Lives option. The host decides everything, so players without the patch can play it too.
- Everyone gets the weapon in slot 1 of the weapon set, with one bullet, at the start of each life (handed out the way Gun Game hands out weapons). Each kill gives the killer one more bullet; suicides and team-mate kills don't. Bullets left over don't carry into the next life.
- On the weapon set page, slots 2 to 6 are greyed out and can't be picked while Showdown is chosen. The weapon picker greys out weapons Showdown can't hand out (grenades and other weapons that can't be dropped).
- Shots kill in one hit; melee and flames do their normal damage. Each console works out its own damage, so the host takes every shot as a one-hit kill on its own copy and sends the kill to every console, the shooter's included. Shots from mounted or remote guns keep their normal damage. One Shot Kill and Always Start With Gun are greyed out with Showdown, and the setup turns both off.
- Like Gun Game, the map loads with no weapon pickups, ammo boxes or armouries on every console (the empty weapon set at match start, for mid-match joiners and on restart), and nobody drops a gun on death. Player Drops Gun is greyed out with Showdown. MapMaker maps aren't covered.
- Fix: Weapon Mode now updates the Player Drops Gun greying as you change it in every mode that lists it (before, only where Gun Game was listed).
- Tests added (Xbox, PS2 NTSC and PAL): the option list and its settings, the hand-out (one bullet, nothing loaded counted, everything put back), kill bullets (suicide, team-mate, dead killer, respawn, joiner), the one-hit check (shots, melee, flames, remote guns, One Shot Kill on), the host's kill message, the weapon set page slots, the greyed items, the setup flags and the empty weapon set.

## v3.34 · 2026-10-15 · Gun Game: no armouries, weapon pickups or ammo boxes for anyone

*v3.34 · GG-NoArmoury* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game on a normal map (not MapMaker) now loads with no armouries (the weapon spawns that never run out), weapon pickups or ammo boxes on any player's game, players without the patch included. The host can't take an armoury away once it exists, so the match-start packet goes out with every weapon-set slot empty: each game only builds those pickups for slots that hold a weapon. The host leaves them out of its own map the same way.
- The real weapon set goes back to every game half a second and 1.5 seconds into the match, before the first weapons are handed out at 2 seconds, without reloading anything (each game needs the gun in its set to make the hand-out). Players on the original Xbox disc get the flag where their build reads it.
- Players joining mid-match load with the same empty set (or their map's items would be numbered differently from everyone else's) and get the real one as soon as they are in. Restart / rematch empties the set again first, then puts it back the same way. Each game is sent the match number it already has, so nothing reloads.
- Offline Gun Game also builds the map without those pickups. Health and armour pickups are not affected.
- Tests added (Xbox, PS2 NTSC and PAL): the match-start packet (Gun Game, not Gun Game, MapMaker map, in a level), both mid-match start packets, the real-set packets and their timing, which games get them, the match numbers, restart, and which pickups each game's map leaves out.

## v3.33 · 2026-10-15 · Setbacks with 1 Kill To Advance; one Advanced page for modes without teams

*v3.33 · SB1-OnePage* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game Setbacks is no longer greyed out with 1 Kill To Advance. There One Kill and One Weapon do the same thing, so One Kill is not offered: scrolling goes Off / One Weapon, and a One Kill choice turns into One Weapon when Kills To Advance is set to 1 Kill.
- Modes without teams (Deathmatch, Elimination, Vampire, Flame Tag, Virus, Monkey Assistant) have every Advanced setting on the one page: Spawn Rule and the Respawn Delay items now sit on the Advanced page, and there is no Spawn Settings link. Modes that can have teams, and Gladiator (Team VIP), keep their Team / Spawn Settings pages.
- Tests added (Xbox, PS2 NTSC and PAL): Setbacks scrolling both ways with 1 Kill and with more kills, Kills To Advance changed to 1 Kill, refresh and apply; the Advanced page of every mode (items on the page or the folder links).

## v3.32 · 2026-10-14 · King of the Hill starts on the middle zone; Team VIP needs 8 units; PAL Team VIP fix

*v3.32 · KotH-Middle-VIP8* · Xbox, PS2 NTSC, PS2 PAL

- King of the Hill: the Hill's first place is now the middle zone of the map, the one with the shortest total distance to all the other zones (height counts; on a tie, the zone listed first). From there it moves every 30 / 60 / 90 seconds as before.
- Team VIP: the VIP now has to move at least 8 units (was 10) between the 5-second ticks to score the point.
- PS2 PAL fix: Team VIP's movement check read the last VIP from the wrong address, so on PAL the VIP almost certainly never scored its 5-second point. The check had been placed over the last word of the code before it, and the PAL conversion then shifted that word as if it belonged to the earlier code. The check now has its own space on both PS2 versions, and the earlier code has its last word back.
- Tests added: the middle place on Xbox and PS2 (zones in a line, a plus with the centre listed last, height, an unknown spawn point, 2 and 20 zones, ties, no random number at the start), and the 8-unit check on PS2 NTSC and PAL.

## v3.31 · 2026-10-14 · Gun Game: Setbacks

*v3.31 · GG-Setbacks* · Xbox, PS2 NTSC, PS2 PAL

- New Gun Game option, listed under Kills To Advance: Setbacks: Off (the default) / One Kill / One Weapon. It is greyed out, and treated as Off, when Kills To Advance is 1 Kill or Weapon Mode is not Gun Game.
- A player is set back when another player kills them unarmed (with their fists; a melee hit with a gun does not count), or when they die with no other player as the killer (their own weapons, falls).
- One Kill takes one kill off their progress; with none on their current weapon, they drop to the previous weapon one kill short of this one. One Weapon puts them back on the previous weapon with the same kills; on the first weapon, its kills go.
- The host (or the game offline) decides. The level is the Gun Game score everyone sees, and the respawn hands out that level's weapon, so players without the patch are set back too.
- Tests added (Xbox, PS2 NTSC and PAL): unarmed and gun melee kills, other weapons, suicides from every place the game counts them, each Kills To Advance value and setting, after a win, before the start, Random Weapon, LAN player and LAN host, menu items, refresh, apply, greying and both changefn handlers.

## v3.30 · 2026-10-14 · King of the Hill on PS2

*v3.30 · PS2-KotH* · PS2 NTSC, PS2 PAL

- King of the Hill is now on PS2 (NTSC and PAL), the same as on Xbox: Zones Advanced Settings > King of the Hill: Off / 30 / 60 / 90 Second Hill, listed after Zone Scoring Interval.
- The host (or the game offline) gathers every zone onto one Hill with the game's own zone drop, so players without the patch see it too, and moves it every 30 / 60 / 90 seconds with "The Hill has moved!" and a sting. 2 seconds after each move the zones are dropped again, their colours are resent every 10 seconds, and a player joining mid-match is resynced 5 seconds after joining. The host's own character slot is used for the drops while it has not spawned or is dead.
- Patched consoles draw the Hill as one zone: one beam and flame, one radar blip, one circle on the zone bar. LAN players with the patch get the setting in byte 74 (bits 2-3 in Zones; Thief keeps its Coin Rush bits there) and show the message when they see the Hill fly to its new place, at most once every 5 seconds.
- Tests added (NTSC and PAL): setting per role, start, moves, settle, colour resend, held and unheld zones, late joiner, host without a character, LAN player messages, unpatched host, new match, menu, byte 74, and the zones tick running through the game's own code.

## v3.29 · 2026-10-14 · Temporal Uplink: not on LAN, never in Gun Game

*v3.29 · No-Uplink-LAN* · Xbox, PS2 NTSC, PS2 PAL

- The Temporal Uplink (enabled in the weapon lists by an earlier change) crashes the game on LAN. It can no longer be picked in the weapon picker or the custom weapon set list on LAN; offline it can still be picked.
- Gun Game and Random Weapon never hand it out.

## v3.28 · 2026-10-14 · Gun Game: patched players only have the gun they are on

*v3.28 · GG-Current-Gun* · Xbox, PS2 NTSC, PS2 PAL

- The game keeps several weapon entries for one gun (single, a pair, alternate fire), and a picked-up gun can sit under any of them. Gun Game looked for the exact entry it handed out, so some old guns (the K-SMG, the rifle) were never recognised and stayed in the weapon slots, even on the host. It now goes by the gun.
- When a patched player (host, offline, or a LAN player with the patch) moves up the ladder, every other gun they hold goes, not only earlier ladder guns: they only have the gun they are on (and their fists). All entries of the current gun stay.
- Players without the patch are unchanged and keep their guns.

## v3.27 · 2026-10-14 · Gun Game: patched LAN players only hold the gun they are on

*v3.27 · GG-LAN-Players* · Xbox, PS2 NTSC, PS2 PAL

- Only the host runs Gun Game, and it can only take weapons away from players on its own console, so patched LAN players kept every gun they had been given. The host now marks a Gun Game match in the match setup (byte 72, bit 3), and each patched player's console takes its own player's old gun away when the next one is picked up, switching to the new one.
- Players without the patch are unchanged: they keep their old guns, as before. Random Weapon is unchanged.

## v3.26 · 2026-10-14 · LAN lobby: Assault only on maps that have it

*v3.26 · Assault-Maps-2* · Xbox, PS2 NTSC, PS2 PAL

- In the original game's LAN lobby, the mode list only offers modes that the selected map supports, so Assault doesn't appear on a map without an Assault setup. The XBE this mod started from (and the PS2 version, which copied it) skips the LAN mode checks in the lobby so more modes are allowed, which also dropped that map check. Assault is listed again only when the selected map has it; every other mode is unchanged.
- The Assault-Maps change to the map list stays, so a map without Assault still can't be picked after choosing Assault, including in Change Game Type.

## v3.25 · 2026-10-14 · Assault only lists its own maps

*v3.25 · Assault-Maps* · Xbox, PS2 NTSC, PS2 PAL

- On LAN and in Change Game Type the game lists every map for any mode, so Assault could be picked on maps with no Assault setup. Assault now only lists the maps made for it, in the lobby and in Change Game Type. Other modes are unchanged and still list every map on LAN, as the original game does.

## v3.24 · 2026-10-14 · Overtime and King of the Hill messages for patched LAN players

*v3.24 · Client-Messages-1* · Xbox, PS2 NTSC, PS2 PAL

- Overtime: a patched LAN player only showed "Overtime!" when its own game saw someone carrying a bag at time-up, which misses other players carrying it. It now also shows it (with the sound) once the host's time has run out and the match has gone on for 1.5 seconds.
- King of the Hill (Xbox): a patched LAN player now also shows "The Hill has moved!" (with the sting) when it sees the Hill fly to its new place, as well as on its own count of the Hill's period; at most one every 5 seconds, and none for the gathering at the start.

## v3.23 · 2026-10-14 · Multikill byte change withdrawn

*v3.23 · MK-LAN-Fix-Withdrawn* · Xbox, PS2 NTSC, PS2 PAL

- Multikill already worked for patched LAN players, so the MK-LAN-Fix change is undone. This build is the same as Gold-Rush-Stay.

## v3.22 · 2026-10-14 · Multikill messages and sounds for patched LAN players

*v3.22 · MK-LAN-Fix* · Xbox, PS2 NTSC, PS2 PAL

- Patched LAN players take the host's Multikill setting from the match setup, but the host only wrote it there when its Advanced Settings page was applied. If the host never opened that page in a session, other patched players had Multikill Off: no multikill messages, sounds or bonus points on their screens.
- The host now writes it at the start of every match (Off in a Gun Game match, as before).

## v3.21 · 2026-10-14 · Spawn-point hold back on in Assault

*v3.21 · Assault-Fix-Withdrawn* · Xbox, PS2 NTSC, PS2 PAL

- The Assault crash could not be reproduced on the build with the spawn-point hold, so it was most likely a one-off rather than caused by the hold. Assault holds spawn points again like every other mode, so everyone counts down together. This build is the same as Gold-Rush-Stay.

## v3.20 · 2026-10-14 · Assault loads again with other players

*v3.20 · Assault-Fix* · Xbox, PS2 NTSC, PS2 PAL

- Assault crashed the host while loading when another player was in the match (seen on Mars Prison), since Start-Wait-5/6. In Assault the game picks spawn points from the current Assault phase, and holding them back made the host read phase data that was not set up yet.
- The spawn-point hold (everyone counts down together) is now off in Assault; every other mode keeps it.

## v3.19 · 2026-10-14 · Gold Rush coins stay until someone takes them

*v3.19 · Gold-Rush-Stay* · Xbox, PS2 NTSC, PS2 PAL

- Gold Rush coins used to vanish after 15 seconds. Only the mod removed them, so players on the original disc (e.g. Series X) kept coins the host no longer had, and their coins and scores drifted out of sync, including the host's pickups not matching for them.
- Coins now stay until someone picks one up, on every console. At most 24 are out at once (about as many as before), and a new one appears 5/8 second after one is taken.

## v3.18 · 2026-10-14 · Spawn-point hold now also covers the host's start screen; earlier start-wait changes removed

*v3.18 · Start-Wait-6* · Xbox, PS2 NTSC, PS2 PAL

- Start-Wait-5 only held spawn points while the host was on Select Team (game state 6). A player who picked a team during the start screen (state 4) still got their spawn point at once and started early, so it made no difference. The host now holds other players' spawn points through its start screen as well, in every mode.
- That also covers the case the earlier changes were for (the host loading last while others started early), so those are removed and the game's own start code is back: the host again waits up to 5 seconds for consoles still loading (the game's own limit) and says everyone has loaded as soon as they have (PS2: the original words are written back). A console still loading after 5 seconds starts a little late, as in the unmodified game; nobody can start before the host.

## v3.17 · 2026-10-14 · Team modes: everyone leaves Select Team together

*v3.17 · Start-Wait-5* · Xbox, PS2 NTSC, PS2 PAL

- In team modes each console waits on its own Select Team screen and starts its 3-2-1 once the host sends it a spawn point. A player who picked a team straight away counted down and was moving while the host was still picking.
- The host now holds other players' spawn points until it has left Select Team itself. Their games keep asking and get one as soon as the host moves on, so everyone counts down together. Works with players on unpatched games; respawns and mid-match joins are unchanged.

## v3.16 · 2026-10-14 · Every console starts the countdown together; load limit back to 15 seconds

*v3.16 · Start-Wait-4* · Xbox, PS2 NTSC, PS2 PAL

- Each console starts its 3-2-1 (or team select) once the host says everyone has loaded and it has itself been on the start screen for 5 seconds. The game's host said it the moment the last console reported in, so the last console to load (often the host on xemu or an original Xbox) still had its 5 seconds to wait while consoles that loaded early (Series X) counted down straight away.
- The host now says everyone has loaded only once every console has been loaded for 7 seconds, so they all start together. The limit for a console that never loads is back to 15 seconds (was 30 in Start-Wait-3; the game's own is 5). Works with players on unpatched games.

## v3.15 · 2026-10-14 · Match start waits up to 30 seconds for slower-loading consoles

*v3.15 · Start-Wait-3* · Xbox, PS2 NTSC, PS2 PAL

- The host now waits up to 30 seconds (was 20 in Start-Wait-2; the game's own limit is 5) for every console to load before it starts everyone's countdown. A console that never finishes loading is left out after 30 seconds.

## v3.14 · 2026-10-14 · Match start waits up to 20 seconds for slower-loading consoles

*v3.14 · Start-Wait-2* · Xbox, PS2 NTSC, PS2 PAL

- The host now waits up to 20 seconds (was 15 in Start-Wait-1; the game's own limit is 5) for every console to load before it starts everyone's countdown. A console that never finishes loading is left out after 20 seconds.

## v3.13 · 2026-10-14 · The match start waits up to 15 seconds for slower-loading consoles

*v3.13 · Start-Wait-1* · Xbox, PS2 NTSC, PS2 PAL

- At the start of a match the host waits for every console to load, then tells everyone to start their 3-2-1 countdown. The game gave up waiting after 5 seconds, so a console that loads more slowly (an original Xbox reading the disc, a real PS2) started its countdown late, while fast-loading consoles (Xbox Series, emulators with fast loading) were already moving.
- The host now waits up to 15 seconds (Xbox ready-start routine 0x35BED0, PS2 0x4F88C0). It points the check at the mod's own 15.0 instead of changing the game's 5.0, which other code may use. Only the host's game decides this, so it works with players on the original disc.
- If a console never finishes loading, the match starts without it after 15 seconds instead of 5.
- Not changed: each console still counts its own 3-2-1. An emulator running below full speed counts more slowly in real time, and the host can shorten other consoles' countdowns but cannot hold them back.

## v3.12 · 2026-10-14 · Change Game Type after a match works for players on the original disc

*v3.12 · X-Compat-1* · Xbox

- Fixed: after a match, Change Game Type on the host left players on the original disc in the old match, and the host dropped them about a minute later.
- Cause: the mod is built on a later Xbox build of the game (19 May 2005, version 0x201) than the original disc (28 Feb 2005, version 1). The later build's match-start packet has one extra field, so everything after it sits 4 bytes later. A player on the original disc reads the "host is in a level" flag 4 bytes too early, sees 0, and ignores the new match. Starting from the lobby was never affected, because the flag is 0 there anyway.
- The host now also writes that flag where the original build reads it, whenever it starts a new match from inside a level. A player on the later build (a patched console) takes that 1 as one minor menu setting for that match.
- Checked while doing this: the original build understands packets 1 to 70 (the later build adds 71, which it does not need here), and its player-settings packet (15) has the same layout as the later build's, so the Gun Game / Random Weapon weapon switch reaches it correctly.

## v3.11 · 2026-10-14 · Fix: weapon switch sent a misaligned settings packet on Xbox

*v3.11 · GG-Switch-3 (experimental)* · Xbox

- Fixed: on Xbox the host's settings packet was laid out wrongly. The game's send function puts a 4-byte packet header in front of the data (sendprefs at 0x359F10 leaves room for it), and the mod's packet had no room for it, so the player's console read every byte 4 places off: the wrong player slot, and controls, aim settings and the rest from the wrong offsets. This changed the client's aim scheme and crashed their game. The packet now matches the game's own layout.
- PS2 was not affected: its packets already left the game's 8-byte header in front of the data.
- The Xbox test harness now writes the 4-byte header the way the game does and checks the size, and it fails on the previous build.

## v3.10 · 2026-10-14 · Random Weapon: players without the patch switch to the weapon they are given

*v3.10 · GG-Switch-2 (experimental)* · Xbox, PS2 NTSC, PS2 PAL

- The weapon switch from GG-Switch-1 now also works in Random Weapon, but only for the weapon the host hands out when a player spawns. The host sets the player's console to "Always" just before dropping it at their feet, and puts their own setting back as soon as it sees them holding it.
- Random Weapon keeps the map's weapons, so its limit is 1 second instead of 4: if the pickup is not seen, the setting goes back after 1 second, and a map gun is the only other weapon they could switch to in that time. Gun Game keeps its 4 seconds.
- Tests added on both platforms: Random Weapon override, restore on pickup and after 1 second; Gun Game still 4 seconds.

## v3.9 · 2026-10-14 · Gun Game: players without the patch switch to each new weapon

*v3.9 · GG-Switch-1 (experimental)* · Xbox, PS2 NTSC, PS2 PAL

- Experimental. A player's own console decides whether they switch to a weapon they pick up, using their "weapon change on pickup" setting. The default, "If New And Best", only switches to a better weapon, so players without the patch often kept their old gun when Gun Game gave them the next one.
- Now, just before the LAN host hands another console's player their next weapon, it sends that player's own settings back to their console with the weapon option set to "Always". The game takes these settings for any player slot (packet 15). Once the host sees them holding the weapon, or after 4 seconds at most, it sends their own setting back. Only that one option changes: controls, sensitivity and handicap are the player's own.
- The setting is put back on the winning kill (before the match ends) and when a new match starts. If a player leaves, what was saved for their slot is forgotten, so a new player in that slot gets their own setting saved. Because "Always" usually lasts well under a second, a player leaving or the host dropping almost never leaves it changed; if it does happen, it stays "Always" until the player changes it in their settings.
- Each settings packet goes only to the console that owns that player. Gun Game only (not Random Weapon), LAN host only; offline play is unchanged.
- Tests added on both platforms: override and restore on pickup, after 4 seconds, on the win and on a new match; their console's own "Always" echo arriving late; the player changing their setting between weapons; a player leaving and another joining in the slot; weapon already held; Random Weapon, offline, settings not received yet and unknown values left alone.

## v3.8 · 2026-10-14 · Multikill and Multikill Window as two options; never in Gun Game

*v3.8 · Multikill-Split* · Xbox, PS2 NTSC, PS2 PAL

- Advanced Settings: "Multikill" (Off / On), and below it "Multikill Window" (1 / 2 / 3 / 4 / 5 Seconds), which is greyed out while Multikill is Off. They replace the single "Multikill Bonus Window" option. The window is remembered while Multikill is Off (first time: 3 seconds).
- Gun Game: both options are greyed out when Weapon Mode is Gun Game for a mode that can play it, and a Gun Game match never gives multikill bonuses, whatever the setting. LAN players with the patch are told Off by the host for a Gun Game match.
- PS2 PAL fix: applying Advanced Settings wrote the LAN team-list byte (Zone Scoring Interval, Coin Rush, Player Kills) 256 bytes below where PAL keeps it (since the 13 Oct afternoon build). It now goes to the right place. NTSC was not affected, and match setup itself already wrote it correctly.
- Register: Xbox code in gg.s is now matched to its feature by the section headings, so a few Spawn Rule, Overtime and Random Characters lines that were listed under the neighbouring feature are now listed correctly.
- Tests added on both platforms: menu items per mode, greying (Off, Gun Game, Gun Game not playable), apply (window kept, bad values, modes without Multikill), LAN byte 73, and the effective setting in Gun Game.

## v3.7 · 2026-10-14 · Things the host does before it has a character

*v3.7 · GG-Spawn-1 / X-KotH-6* · Xbox, PS2 NTSC, PS2 PAL

- Gun Game (Xbox and PS2): the host removes the map guns on the first frame everyone has loaded and tells the other players they were picked up. That message is sent as the host's character, so when the host had not spawned yet the guns vanished only on the host and stayed on everyone else's screen. Now the host remembers and sends it as soon as its character exists.
- King of the Hill (Xbox): the zone drop now uses the host's own character slot when the host has not spawned or is dead, instead of the made-up stand-in from X-KotH-5. The drop message carries the character's slot number, so it should always name a real slot.
- Checked and left as they are: Coin Rush coins only appear once the host has a character (sending them as anyone else would make that player's console ignore the coin or crash it); Spawn Rule, Respawn Delay, Flame Tag, Team VIP, Catch-Up, Overtime and Random Characters do not need the host's character.
- Tests added on both platforms: host without a character at the removal, still without one, then spawned (sent once); offline unchanged.

## v3.6 · 2026-10-14 · Network menu name back to the original

*v3.6 · X-Menu-1* · Xbox

- The main menu item and the network menu's title and header read "Xbox Live / System Link" again (game text 92), instead of "Xlink Kai". The original bytes are back at 0x1A3B90, 0x1A62F0 and 0x2D0D09, and the mod's "Xlink Kai" text is gone.
- The "Xbox Live" option stays removed from that menu.

## v3.5 · 2026-10-14 · King of the Hill: zones gathered at the very start of a LAN match

*v3.5 · X-KotH-5* · Xbox

- Fixed: at the start of a LAN match players saw the zones in their own places, and they only flew to the Hill once the host spawned. The host's zone drop needed the host's own character, which does not exist until the host spawns, so the first gather did nothing.
- The drop now uses a stand-in character when the host has none (not spawned yet, or dead when the Hill moves), so the zones go to the Hill on the first frame the match is played.
- Tests added: host not spawned at the start, host dead at a move, host spawned again.

## v3.4 · 2026-10-14 · Change register and changelog

*v3.4 · R1* · Xbox, PS2 NTSC, PS2 PAL

- No game changes. Added this register: every byte (Xbox) and word (PS2) that differs from the original files, with the original code, the code that replaced it and what it is for.
- Project folder kept on Jake's PC (Desktop\TimeSplitters\TSFP Mod Project) with the files, build scripts, tests, original files and this register.

## v3.3 · 2026-10-13 · King of the Hill: zones settle for unpatched players

*v3.3 · X-KotH-4* · Xbox

- Host drops every zone on the Hill again 2 seconds after each move, and resends the zones' colours every 10 seconds, so a late or out-of-order message on an unpatched console is corrected.
- A player joining mid-match gets the zones resynced 5 seconds after joining.
- Status: waiting for Jake's test on the original Xbox client (one zone was seen floating apart with a stale blue streak).

## v3.2 · 2026-10-13 · King of the Hill: all zones gathered on the Hill

*v3.2 · X-KotH-3* · Xbox

- New design: every zone is dropped onto the Hill's spot (the game's own zone drop, which the host sends to everyone), so unpatched players no longer see white flames elsewhere on the map.
- Patched consoles draw the Hill as one zone; the radar and zone bar count it once.
- Scoring is the game's normal 1 point per zone per tick on every console.
- Fixed: non-Hill zones being captured, and the Hill being re-picked mid-match after a game-frame glitch (new match only within the first 20 seconds).

## v3.1 · 2026-10-13 · King of the Hill: crash fix

*v3.1 · X-KotH-2* · Xbox

- Fixed the freeze (Xbox kernel error 0x1E at 0xC36F3): the Hill-move code kept a value in a register that the game's random-number call overwrites. Tests now overwrite those registers on every game call.

## v3.0 · 2026-10-13 · King of the Hill (Zones Advanced Settings: Off / 30 / 60 / 90 Second Hill)

*v3.0 · X-KotH-1* · Xbox

- Only one zone is live at a time and it moves every 30/60/90 seconds with "The Hill has moved!" and a sting. Host decides. Xbox first; PS2 after it is confirmed.

## v2.2 · 2026-10-13 · Catch-Up, Overtime, Random Characters, Xlink Kai name

*v2.2 · 13 Oct evening* · Xbox, PS2 NTSC, PS2 PAL

- Catch-Up (per mode, Off / On) with Catch-Up Period (All Match / Last Minute): the last-placed player or team scores double. Greyed out in Gun Game.
- Capture the Bag Overtime: the match goes on while a bag is carried at time-up, with "Overtime!" and the Text Sweep sound.
- Random Characters (every mode): every player and bot gets a random character each match; the host's picks reach everyone.
- Xbox: the network menu item reads "Xlink Kai".
- Lockers added for a test, then removed again.

## v2.1 · 2026-10-13 · Spawn Rule, Flame Pass, Gold Rush / Coin Drop, Team VIP update

*v2.1 · 13 Oct afternoon* · Xbox, PS2 NTSC, PS2 PAL

- Spawn Rule (Spawn Settings, per mode): Default / Away From Enemies / Near Teammates.
- Flame Pass (Flame Tag, LAN): Touch / Kill / Touch Or Kill.
- Thief: Gold Rush (coins appear on spawn points instead of dropping) and Coin Drop (Any Death / Player Kills).
- Team VIP: the VIP must have moved at least 10 units for the 5-second point.
- PS2 PAL pnach made from the NTSC one (address translation) for every feature so far.

## v2.0 · 2026-10-13 · Weapon Mode and Player Drops Gun

*v2.0 · 13 Oct morning* · Xbox, PS2 NTSC

- Weapon Mode: Off / Gun Game / Random Weapon, with Kills To Advance (1 / 3 / 5 / 10). Gun Game removes the map guns and hands out the ladder weapons.
- Player Drops Gun (every mode, On / Off).
- Always Start With Gun and Score Limit greyed out where they do not apply.

## v1.3 · 2026-10-12 · Infinite Ammo, Capture the Bag options, Virus, Team VIP, menu layout

*v1.3 · 12 Oct evening* · Xbox, PS2 NTSC

- Infinite Ammo (offline and split-screen).
- Capture the Bag: Reverse Scoring and Score With Bag Away (host-decided, works for unpatched players).
- Virus: Spread By Kills (LAN), no spreading by touch.
- Team VIP (Gladiator): the Gladiator's team scores every 5 seconds.
- Advanced Settings hides what a mode can never use; layout matches the match settings page; Team Settings / Spawn Settings folders.

## v1.2 · 2026-10-12 · Mercy Rule, Respawn Delay, Zones options, Multikill

*v1.2 · 12 Oct day* · Xbox, PS2 NTSC

- Mercy Rule (per mode): the host ends the match when first place leads by the limit.
- Respawn Delay (Off / 1-5 seconds, per team where it applies).
- Yellow and Green get their own spawn areas on maps without them; Team Spawns hidden in Assault, colour options hidden in Capture the Bag / Assault.
- Zones: Zone Scoring Interval (10 / 15 / 20 s) and a last score at time-up.
- Multikill Bonus Window (Off / 1-5 seconds).
- An early King of the Hill attempt was shelved.

## v1.1 · 2026-10-12 · No Punch, Flame Tag, team Bag Tag, LAN mode list

*v1.1 · 12 Oct night* · Xbox, PS2 NTSC

- Disable Unarmed (No Punch).
- Flame Tag re-enabled with LAN play, offline flame passing, Number of Flames and burn-time scoring for every burning player.
- Team Bag Tag: bag time counts for the whole team; scoreboard shows team times.
- LAN mode list: Story and Monkey Assistant removed.

## v1.0 · 2026-10-11 · Starting point, 4 teams, team colours

*v1.0 · Start* · Xbox, PS2 NTSC

- Started from Jake's Xbox build (default.xbe) and the TSO Community Patch pnach (team play in more modes, 4 teams, MapMaker limits, extra weapons).
- Xbox: 4-team patch (team counts and checks for 4 teams, Zones included); yellow / green zone flames.
- Advanced Settings page: Teamplay, Team Spawns, Disable Red / Blue / Yellow / Green Team; the LAN host's colours apply to everyone.

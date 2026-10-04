# Commands and Permissions


The main command is `/vc` (aliases `/valocraft`, `/valo`).

## Player commands

| Command | Description |
|---|---|
| `/vc join [map]` | Join a game (menu without argument) |
| `/vc leave` | Leave the game |
| `/vc list` | List games |
| `/vc shop` | Buy-phase shop (or key F) |
| `/vc lobby` | Back to the lobby |
| `/vc boutique` | Collection shop (in the lobby) |
| `/vc radianite` | Your Radianite balance |
| `/vc pass` | Battle pass |
| `/vc missions` | Daily missions |
| `/vc resume` | Your last match summary |
| `/vc rang [player]` | Ranked rank |
| `/vc party invite\|accept\|deny\|leave\|kick\|chat\|list` | Party |
| `/vc ff [non]` | Vote to surrender (from round 5) |
| `/vc remake [non]` | Cancel the game if a teammate left early |
| `/vc pack send` / `remove` | (Re)receive / remove the resource pack |
| `!message` (in match) | Team chat |

`/vc buyfor` is used internally by the **[Buy for …]** button of weapon requests.

## Admin commands

| Command | Description |
|---|---|
| `/vc setlobby` | Set the lobby at your position |
| `/vc wand` | Selection wand (left click = pos1 / point A, right click = pos2 / point B) |
| `/vc start <map>` | Force a game to start (2 players minimum) |
| `/vc forcestart [map]` | Start **even with a single player** (no map: the game you're in). Doesn't count for ranked. |
| `/vc stop <map>` | Force a game to stop |
| `/vc ult add\|set <player> [points]` | Ult points (`set` without a number = full ult) |
| `/vc pass addxp <player> <xp>` | Give battle pass XP |
| `/vc leaderboard set <type>` / `remove` / `list` | Lobby leaderboards ([Progression](page:progression)) |
| `/vc give <weapon\|knife\|spike> [player]` | Give a weapon, the knife or the spike |
| `/vc reload` | Reload `config.yml`, `weapons.yml` and `abilities.yml` |
| `/vc pack send\|remove <player\|all>` | Send / remove the resource pack |
| `/vc pack info` / `reload` | Pack mode and link / reload it |
| `/vc radianite give\|take\|set <player> <amount>` | Manage a player's Radianite |
| `/vc radianite voir <player>` | Check a player's balance |
| `/vc import list` / `<name>` | Catalog / download a map ([Importing Maps](page:importing-maps)) |

## Map commands (admin)

See [Map Setup](page:map-setup) for the walkthrough.

| Command | Description |
|---|---|
| `/vc map create <id>` / `delete <id>` | Create / delete a map |
| `/vc map list` / `info <id>` | List / see what's missing |
| `/vc map setname <id> <name>` | Display name |
| `/vc map setwaiting <id>` | Waiting room = your position |
| `/vc map addspawn <id> <attack\|defend>` | Add a spawn at your position |
| `/vc map clearspawns <id> <attack\|defend>` | Clear spawns |
| `/vc map addsite <id> <A\|B\|C...>` / `removesite <id> <site>` | Spike site (selection) / remove it |
| `/vc map addwall <id> [block]` / `removewall <id> <n>` / `walls <id>` | Pre-round walls |
| `/vc map previewwalls <id>` | Show / hide walls |
| `/vc map setplayers <id> <min> <max>` | Player limits |
| `/vc map setmode <id> <mode>` | Default mode (`unrated`, `competitive`, `swiftplay`, `replication`, `spike_rush`, `deathmatch`, `team_deathmatch`, `escalation`) |
| `/vc map setmusic <id> <sound\|none>` | Map music |
| `/vc map addorb <id>` / `clearorbs <id>` | Ult orbs |
| `/vc map setminimap <id>` / `clearminimap <id>` | Tactical map area |
| `/vc map addzipline <id>` / `ziplines <id>` / `removezipline <id> <n>` | Ziplines |
| `/vc map enable\|disable <id>` | Enable / disable |
| `/vc map tp <id>` | Go to the map (loads its world if needed) |

## Permissions

| Permission | Default | Description |
|---|---|---|
| `valocraft.play` | Everyone | Play Valocraft |
| `valocraft.admin` | Operators | Admin commands |
| `valocraft.agents.all` | Nobody | Unlock every agent (already the case by default with `default-agents: [ALL]`) |
| `valocraft.skins.all` | Nobody | Unlock every weapon skin |

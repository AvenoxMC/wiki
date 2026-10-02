# Commands and Permissions


The main command is `/vc`.

## Player commands

| Command | Description |
|---|---|
| `/vc join [map]` | Join a game (opens a menu with no argument) |
| `/vc leave` | Leave the game |
| `/vc list` | List games |
| `/vc shop` | Open the shop |
| `/vc lobby` | Return to the lobby |
| `/vc pack send` | (Re)receive the resource pack |
| `/vc pack remove` | Remove the resource pack |

## Admin commands

| Command | Description |
|---|---|
| `/vc setlobby` | Set the lobby at your position |
| `/vc wand` | Get the selection wand (left click = pos1 / point A, right click = pos2 / point B) |
| `/vc start <map>` | Force a match to start |
| `/vc stop <map>` | Force a match to stop |
| `/vc give <weapon\|knife\|spike> [player]` | Give a weapon, the knife or the spike |
| `/vc reload` | Reload `config.yml` and `weapons.yml` |
| `/vc pack send <player\|all>` | Send the resource pack |
| `/vc pack remove <player\|all>` | Remove the resource pack |
| `/vc pack info` | Pack mode and link |
| `/vc pack reload` | Reload the pack after editing it |
| `/vc import list` | Show the map catalog |
| `/vc import <name>` | Download and install a map ([Importing Maps](page:importing-maps)) |

## Map commands (admin)

See [Map Setup](page:map-setup) for the workflow.

| Command | Description |
|---|---|
| `/vc map create <id>` | Create a map |
| `/vc map setname <id> <name>` | Set the display name |
| `/vc map setwaiting <id>` | Waiting room = your position |
| `/vc map addspawn <id> <attack\|defend>` | Add a spawn at your position |
| `/vc map addsite <id> <A\|B\|C...>` | Spike site from your wand selection |
| `/vc map addwall <id> [block]` | Pre-round wall from your wand selection |
| `/vc map previewwalls <id>` | Show / hide the walls |
| `/vc map setplayers <id> <min> <max>` | Player limits |
| `/vc map setmusic <id> <sound>` | Map music |
| `/vc map addorb <id>` | Add an ultimate orb at your position |
| `/vc map clearorbs <id>` | Remove all orbs |
| `/vc map addzipline <id>` | Zipline between the two wand points |
| `/vc map ziplines <id>` | List ziplines |
| `/vc map removezipline <id> <n>` | Remove a zipline |
| `/vc map info <id>` | Show what is missing for the map to be playable |
| `/vc map enable <id>` | Enable the map |

## Permissions

| Permission | Default | Description |
|---|---|---|
| `valocraft.play` | Everyone | Play Valocraft |
| `valocraft.admin` | Ops | Admin commands |

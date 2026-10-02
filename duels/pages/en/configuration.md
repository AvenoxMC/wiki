# Configuration

Configuration files are stored in `plugins/Duels/`.

## Files

| File | Contents |
|---|---|
| `config.yml` | Lobby, lobby items, worlds, match rules, parties and feature settings. |
| `messages.yml` | All plugin messages, in French by default, with `&` color codes. |
| `kits.yml` | Kit definitions, also editable with `/dkit`. |
| `arenas.yml` | Arena definitions, written by arena commands. |
| `lobby.yml` | Lobby location. |
| `stats.yml` | Player statistics. |
| `schematics/` | Schematic files discovered by the plugin. |

## Notable settings

| Setting | Purpose |
|---|---|
| `lobby-server` | Server to send players to when they use `/lobby` or `/hub`; empty returns them to the Duels lobby. |
| `worlds.max-loaded-instances` | Maximum total loaded match instances across the server. |
| Arena `max-instances` | Maximum simultaneous copies for one arena. |
| `schematics.folders` | Directories searched for schematic files. |
| `schematics.paste-y` | Y coordinate used to center a pasted map (default 64). |
| `schematics.ms-per-tick` | Limits schematic block writing per tick to reduce server stalls. |
| `devine` | Guess! time limits, attempts, colors, duplicates and board layout. |

Run `/duels reload` after editing configuration or `kits.yml` manually.

## Admin permission

`duels.admin` is granted to operators by default. It provides access to `/arena`, `/dkit`, `/duels setlobby`, `/duels reload`, Creative building in the lobby, and admin commands during a match. See [Arenas](page:arenas), [Kits](page:kits) and [Schematics](page:schematics) for command usage.

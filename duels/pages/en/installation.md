# Installation

## Requirements

| Requirement | Details |
|---|---|
| Server | Spigot 1.8.8 |
| Java | Use a Java version supported by your Spigot 1.8.8 server |
| Plugin jar | `target/Duels.jar` |

## Install

1. Copy `target/Duels.jar` into the server's `plugins/` folder.
2. Start the server.
3. Stand at the desired lobby location and run `/duels setlobby`.
4. Create at least one arena. Five example kits are created automatically: `nodebuff`, `builduhc`, `sumo`, `combo` and `archer`.

> This plugin is intended for a dedicated duels server or lobby. On join, a player's inventory is cleared and replaced with the lobby items.

## Build from source

Install Maven and run:

```bash
mvn package
```

The plugin jar is produced at `target/Duels.jar`. Alternatively, compile with `javac` against `spigot-api-1.8.8-R0.1-SNAPSHOT.jar`.

## Next steps

- [Create an arena](page:arenas)
- [Configure kits](page:kits)
- [Player commands](page:players)

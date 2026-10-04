# Installation


## Requirements

| | |
|---|---|
| **Server** | Paper 1.21.4 or newer |
| **Java** | 21 |
| **Dependencies** | None required |
| **Optional** | [SkinsRestorer](https://github.com/SkinsRestorer/SkinsRestorer): signed agent skins, also visible to the player themselves |
| **Resource pack** | Bundled in the jar, sent automatically |

## Fresh install

1. Put `Valocraft-2.2.jar` in the server's `plugins/` folder (plus SkinsRestorer if you want it).
2. Start the server. The resource pack is extracted to `plugins/Valocraft/resourcepack.zip`, and `abilities.yml` is created.
3. Stand where you want the lobby and run `/vc setlobby`.
4. [Build a map](page:map-setup) or [import one](page:importing-maps), then `/vc map enable <id>`.
5. Optional: place [leaderboards](page:progression) in the lobby with `/vc leaderboard set <type>`.

## Updating

- From any **2.x**: replace the old jar with `Valocraft-2.2.jar` in `plugins/`. Players get the updated pack automatically. New options are added to `config.yml` on startup.
- From **1.x**: 2.x is a complete rewrite that shares nothing with 1.x. Remove the old plugin and its data, and start fresh.

## Map worlds

Map worlds (`vc_<map>`) are **no longer loaded at server startup**. They stay on disk, are loaded when a match launches, then unloaded once nobody uses them. A map built in the main world (`world`) stays loaded all the time. See [Map Setup](page:map-setup).

## Resource pack

Nothing to configure by default. The pack (HrdaValorant plus Valocraft models) is served **on the Minecraft port itself** and sent to each player on join. The link reuses the address and port the player connected with: no extra port to open, and it also works on Pterodactyl.

See [Resource Pack](page:resource-pack) for alternatives and troubleshooting.

## SkinsRestorer (optional)

With SkinsRestorer, agent skins are signed through MineSkin on startup (in the background, one every 3 s), then cached in `plugins/Valocraft/data/agent-skins.yml`. The server needs Internet access on the first startup. Without SkinsRestorer, other players still see the agent skin; only the player themselves keeps their own skin in F5 view.

## Next steps

- [Lobby and Matchmaking](page:lobby)
- [Map Setup](page:map-setup)
- [Commands and Permissions](page:commands)

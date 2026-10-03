# Installation


## Requirements

| | |
|---|---|
| **Server** | Paper 1.21.4 or newer |
| **Java** | 21 |
| **Dependencies** | None (standalone) |
| **Resource pack** | Embedded in the jar, sent automatically |

## Fresh install

1. Put `Valocraft-2.2.jar` in the `plugins/` folder of your server.
2. Start the server. The resource pack is extracted to `plugins/Valocraft/resourcepack.zip` on first start.
3. Stand where you want the lobby and run `/vc setlobby`.
4. [Create a map](page:map-setup) or [import one](page:importing-maps), then `/vc map enable <id>`.

## Updating

- From **2.1**: replace `Valocraft-2.1.jar` with `Valocraft-2.2.jar` in `plugins/`. Players get the updated resource pack automatically, including the new weapon models and textures.
- From **2.0.0**: replace the old jar with `Valocraft-2.2.jar`. Players get the updated resource pack automatically.
- From **1.x**: 2.x is a full rewrite and shares nothing with 1.x. Remove the old plugin and its data, and start fresh.

## Resource pack

Nothing to configure by default. The pack (HrdaValorant, with a corrected Classic sound) is served on the **Minecraft port itself** and sent to every player on join. The link reuses the address and port the player used to connect, so no extra port is required, and it works on Pterodactyl.

See [Resource Pack](page:resource-pack) for alternatives and troubleshooting.

## Next steps

- [Lobby and Matchmaking](page:lobby)
- [Map Setup](page:map-setup)
- [Commands and Permissions](page:commands)

# Resource Pack


Valocraft uses the **HrdaValorant** resource pack (fixed Classic sound) plus Valocraft's own models and textures (weapons, skins, smokes, scope, white flashes). It's **bundled in the plugin jar**.

## Default behaviour

1. On startup, the pack is extracted to `plugins/Valocraft/resourcepack.zip` (and replaced automatically when the plugin is updated).
2. It's **served on the Minecraft port itself** and sent to each player on join.
3. The download link reuses **the address and port the player connected with**.

No extra port to open, and it works on **Pterodactyl**.

A player who declines the pack gets a message: without it, weapons, ability icons and scopes are invisible.

## Player commands

| Command | Effect |
|---|---|
| `/vc pack send` | (Re)receive the pack |
| `/vc pack remove` | Remove the pack |

## Admin commands

| Command | Effect |
|---|---|
| `/vc pack send <player\|all>` | Send the pack to a player or everyone |
| `/vc pack remove <player\|all>` | Remove the pack for a player or everyone |
| `/vc pack info` | Shows the mode and link |
| `/vc pack reload` | Reloads the pack after a change |

## Alternatives

Set in `config.yml`:

| Goal | Setting |
|---|---|
| Use a **dedicated HTTP port** | `resource-pack.self-host.http-port: 8164` |
| Use an **external URL** | `self-host.enabled: false`, then `resource-pack.url` and `sha1` |

## Reading the console

For each player, the console shows the **offered link** and the **client's answer**, for example: `ACCEPTED`, `DECLINED`, `FAILED_DOWNLOAD`, `SUCCESSFULLY_LOADED`.

See [Troubleshooting](page:troubleshooting) if the pack doesn't load, and [Development](page:development) to regenerate the resources.

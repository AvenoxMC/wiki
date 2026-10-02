# Resource Pack


Valocraft uses the **HrdaValorant** resource pack (with a corrected Classic sound) plus the Valocraft weapon models. It is **embedded in the plugin jar**.

## How it works by default

1. On first start the pack is extracted to `plugins/Valocraft/resourcepack.zip`.
2. It is **served on the Minecraft port itself** and sent to every player on join.
3. The download link reuses the **address and port the player connected with**.

So there is **no extra port to open**, and it works on **Pterodactyl**. The pack is updated automatically when the plugin updates.

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
| `/vc pack info` | Show the mode and link |
| `/vc pack reload` | Reload the pack after editing it |

## Alternatives

Set in `config.yml`:

| Goal | Setting |
|---|---|
| Use a **dedicated HTTP port** | `resource-pack.self-host.http-port: 8164` |
| Use an **external URL** | `self-host.enabled: false`, then `resource-pack.url` and `sha1` |

## Reading the console

For each player, the console logs the **link offered** and the **client's response**, for example: `ACCEPTED`, `DECLINED`, `FAILED_DOWNLOAD`, `SUCCESSFULLY_LOADED`.

See [Troubleshooting](page:troubleshooting) if the pack does not load.

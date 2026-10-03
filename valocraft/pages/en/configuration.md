# Configuration


Files live in `plugins/Valocraft/`. Reload `config.yml` and `weapons.yml` with `/vc reload`.

## Files and folders

| Path | Purpose |
|---|---|
| `config.yml` | General settings, controls, resource pack, map library |
| `weapons.yml` | All weapon stats (commented at the top of the file) |
| `stats.yml` | Player statistics |
| `resourcepack.zip` | Resource pack extracted from the jar at first start |
| `maps/<id>.yml` | One file per map |
| `playerdata/` | Inventories saved during a game, returned on reconnect after a crash |
| `data/` | Temporary blocks (walls, spike) restored after a crash |

## `config.yml` options

| Key | Purpose |
|---|---|
| `controls.fire-button` | `RIGHT` = fire on held right click, aim on left click. See [Controls](page:controls). |
| `controls.continuous-fire` | Enable the 2.2 held-click continuous-fire behavior. |
| `controls.semi-auto-hold` | Allow semi-automatic weapons to fire while held. |
| `controls.hide-swing` | Hide the arm-swing animation while firing. |
| `game.custom-tab` | Enable or disable the custom in-match Tab scoreboard. |
| `agents.tactical-map` | Enable the top-down targeting map for controller abilities; `false` restores the previous targeting behavior. |
| `agents.smokes-hide-players` | Hide enemies inside or behind smokes. |
| `agents.solid-smokes` | Use opaque 3D smoke and wall models. |
| `agents.wear-heads` | Show each player's agent head during a match. |
| `progression` | Configure Radianite rewards, shop prices and free agents. |
| `player.speed-bonus` | Walking speed bonus that stands in for Valorant's run speed (sprint is disabled) |
| `weapons.practice-mode` | Enable or disable the [Practice Range](page:practice-range) |
| `resource-pack.self-host.http-port` | Dedicated HTTP port for the pack (for example `8164`) |
| `resource-pack.self-host.enabled` | Set to `false` to use an external URL |
| `resource-pack.url` / `resource-pack.sha1` | External pack URL and its checksum |
| `map-library` | Catalog for `/vc import` ([Importing Maps](page:importing-maps)) |

Example, hold-to-fire:

```yaml
controls:
  fire-button: RIGHT
```

## `weapons.yml`

Holds every weapon stat: damage, fire rate, spread, recoil, penetration, zoom and more. See [Weapons](page:weapons).

## Ability tuning

Ability damage, durations and prices are defined in `AbilityType.java` and `Kits.java`. These are in the source, so changing them means rebuilding the plugin. See [Development](page:development).

Progression values are configurable in the `progression` section of `config.yml`. Admins can grant, remove or set player balances with `/vc radianite give|take|set <player> <amount>` and inspect a balance with `/vc radianite voir <player>`.

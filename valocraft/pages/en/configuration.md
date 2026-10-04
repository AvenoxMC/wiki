# Configuration


Files live in `plugins/Valocraft/`. `/vc reload` reloads `config.yml`, `weapons.yml` and `abilities.yml`. New options are added to `config.yml` automatically on updates.

## Files and folders

| Path | Purpose |
|---|---|
| `config.yml` | General settings, modes, controls, progression, battle pass, resource pack, map library |
| `weapons.yml` | Stats of every weapon (documented at the top of the file) |
| `abilities.yml` | Price, charges, cooldowns and damage of every ability, ult costs |
| `stats.yml` / `valocraft.db` | Player profiles (YAML by default, SQLite or MySQL) |
| `leaderboards.yml` | Lobby leaderboard positions |
| `resourcepack.zip` | Resource pack extracted from the jar |
| `maps/<id>.yml` | One file per map |
| `playerdata/` | Inventories saved during a match, given back after a crash |
| `data/` | Temporary blocks to restore after a crash, minimaps, signed agent skins (`agent-skins.yml`) |

## Main `config.yml` options

| Key | Purpose |
|---|---|
| `game.countdown`, `game.rounds-to-win`, `game.loading-time` | Countdown, rounds to win, minimum loading screen duration |
| `game.custom-tab`, `game.radar` | Custom scoreboard, off-hand radar |
| `modes.<mode>.*` | Settings of each [mode](page:modes) (rounds, kills, time, Escalation weapons...) |
| `maps.unload-check` | Seconds between two checks for map worlds to unload |
| `controls.fire-button`, `controls.aim-mode` | Fire button (`LEFT` / `RIGHT`) and aiming (`HOLD` / `TOGGLE`) |
| `controls.continuous-fire`, `controls.semi-auto-hold`, `controls.hide-swing` | Continuous fire ([Controls](page:controls)) |
| `controls.instant-abilities` | `false` (default): manual ability activation; `true`: trigger on keypress |
| `agents.select-time` | Agent select duration |
| `agents.full-skin`, `agents.wear-heads` | Full agent skin / agent heads |
| `agents.skins-restorer`, `agents.skins.<agent>` | Signed skins through SkinsRestorer / custom skin for an agent (image URL or username) |
| `agents.tactical-map`, `agents.smokes-hide-players`, `agents.solid-smokes` | Tactical map, smokes that hide, 3D smokes |
| `progression.*` | Radianite, prices, free agents (`default-agents: [ALL]`), `cosmetic-prices` |
| `battlepass.*` | Season, levels, XP, rewards ([Progression](page:progression)) |
| `leaderboards.refresh`, `leaderboards.size` | Lobby leaderboards |
| `reconnect.*`, `surrender.*`, `remake.*`, `afk.*` | Reconnect, votes, inactivity |
| `ranked.*`, `missions.*`, `party.*`, `chat.*`, `footsteps.*` | Ranked, missions, parties, chat, footsteps |
| `storage.type` | `yaml`, `sqlite` or `mysql` (automatic import from `stats.yml`) |
| `weapons.lag-compensation`, `weapons.practice-mode` | Lag compensation, [Practice Range](page:practice-range) |
| `player.speed-bonus` | Walking speed bonus (sprinting is disabled) |
| `resource-pack.*` | Pack hosting ([Resource Pack](page:resource-pack)) |
| `map-library` | `/vc import` catalog |

## `abilities.yml`

Created on first startup with the original values, completed automatically when new abilities appear.

```yaml
global:
  damage-multiplier: 1.0      # damage of every ability
  duration-multiplier: 1.0    # duration of smokes, fires, traps
agents:
  jett:
    ult-cost: 8
    cloudburst:
      price: 200
      max-charges: 2
      free-charges: 0
      cooldown: 0             # seconds to get a free charge back
      kill-recharge: 0        # comes back after N kills
      damage-multiplier: 1.0
```

Edit, then `/vc reload`: no recompiling needed.

## `weapons.yml`

Every weapon stat: damage, fire rate, inaccuracy, recoil, penetration, zoom and more. See [Weapons](page:weapons).

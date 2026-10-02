# Controls


| Key | Action |
|---|---|
| **Left click** | Shoot (automatic weapons: click fast to fire in bursts) |
| **Right click (hold)** | Aim / scope |
| **Q** | Reload |
| **Sneak + Q** | Drop the weapon (or the spike) |
| **F** | Shop during the buy phase, otherwise pick up the targeted weapon |
| **1 / 2 / 3 / 4** | Primary / sidearm / knife / spike |
| **5 / 6 / 7 / 8** | Agent abilities **C / Q / E / X** |
| **F** near a rope | Hook onto a [zipline](page:ziplines) |
| **Hold right click** with the spike on a site | Plant the spike (stay still) |
| **Hold right click** on the spike (defender) | Defuse (stay still) |

## Ability controls

- **Instant abilities** activate as soon as you press the key: Updraft, Tailwind, Devour, Dismiss, High Gear, Regrowth, and the ultimates Run it Back, Empress, Lockdown, Viper's Pit and Seekers.
- **All other abilities**: **left click** to cast, **right click** for the variant when one exists (Curveball on right click, Sova's arrows without bounce, Healing Orb on self, Blade Storm all knives at once).
- **Guided abilities** (Sova's drone, Skye's hawk and tiger, Gekko's Thrash) follow your gaze.
- **Jett** glides while holding the jump key.

## Automatic fire and the left-click limit

Minecraft only sends the server **one signal per left click** (nothing while the button stays held). With left-click shooting, automatic weapons therefore fire at your click rate, up to their maximum fire rate.

For true hold-to-fire, set this in `config.yml`:

```yaml
controls:
  fire-button: RIGHT
```

Fire is then on **held right click**, and aim is on **left click**.

## HUD

- **XP bar**: level = bullets in the magazine, bar = magazine / reload progress.
- **Hearts** = HP (100 HP = 10 hearts), **golden hearts** = shield.

# Controls


| Key | Action |
|---|---|
| **Left click** | Shoot; hold while aiming at a block within 64 blocks for continuous fire |
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

## Continuous fire (2.2)

Minecraft normally sends the server only **one signal per left click**. In a match, Valocraft uses the targeted block (up to **64 blocks** away) to receive a signal each tick while left click is held, letting the weapon fire at its configured rate. Blocks are never broken, no cracks are shown to other players, and the arm-swing animation is hidden. A single click still fires one bullet; semi-automatic weapons can also fire continuously at their maximum rate.

If you are aiming at the sky with no block within 64 blocks, click to fire. The knife still hits within 3 blocks. The `controls.continuous-fire`, `controls.semi-auto-hold` and `controls.hide-swing` options in `config.yml` control this behavior; see [Configuration](page:configuration).

## HUD

- **XP bar**: level = bullets in the magazine, bar = magazine / reload progress.
- **Hearts** = HP (100 HP = 10 hearts), **golden hearts** = shield.

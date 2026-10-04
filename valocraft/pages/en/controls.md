# Controls


| Key | Action |
|---|---|
| **Left click** | Shoot; hold while aiming at a block within 64 blocks for continuous fire |
| **Right click (hold)** | Aim / scope |
| **Q** | Reload |
| **Sneak + Q** | Drop the weapon (or the spike) |
| **F** | Shop during the buy phase, otherwise pick up the weapon you look at |
| **Sneak + F** | Spray on the wall you look at |
| **1 / 2 / 3 / 4** | Primary / sidearm / knife / spike |
| **5 / 6 / 7 / 8**, then **left click** | Take, then use ability **C / Q / E / X** |
| **F** near a rope | Grab a [zipline](page:ziplines) |
| **Hold right click** with the spike on a site | Plant (stand still) |
| **Hold right click** on the spike (defender) | Defuse (stand still) |
| **Tab** | Scoreboard |

## Abilities

- **Manual activation**: keys 5 to 8 take the ability in hand, **left click** uses it. Nothing fires just by switching slots. To trigger on keypress again (Tailwind, High Gear, Dismiss, instant ultimates...): `controls.instant-abilities: true`.
- **Thrown abilities**: **hold** left click to see the trajectory (visible only to you), **release** to throw. **Right click**: underhand lob, or the variant when there is one (Curveball to the right, Sova's bolts without bounce, Healing Orb on yourself, quick FLASH/drive, healing M-Pulse).
- **Sova's bolts**: the longer you hold, the further they go ("Power" gauge).
- **Piloting** (Sova's drone, Skye's tiger, Tejo's drone): you see through the creature's eyes, WASD to move, left click = action, right click = back to your body.
- **Tactical map**: WASD moves the cursor (sprint to go faster), left click places, right click or sneak cancels.
- **Anchor abilities**: first click = place, second click = use.
- **Neon**: sneak during High Gear = slide. **Viper**: clicking a placed emitter turns it on / off.
- **Tour de Force** (Chamber): right click = scope, left click = shoot.
- **Jett** glides while holding jump.

## Continuous fire

Minecraft normally sends **one signal per left click**. In a match, Valocraft uses the targeted block (up to **64 blocks**) to receive a signal every tick while the click is held: the weapon fires at its configured rate. No block is broken, no cracks are visible and the arm swing is hidden. A single click fires one bullet; semi-autos also fire continuously at their max rate.

When aiming at the sky with no block within 64 blocks, you need to click. The knife always hits within 3 blocks. Settings: `controls.continuous-fire`, `controls.semi-auto-hold`, `controls.hide-swing` ([Configuration](page:configuration)).

## HUD

- **XP bar**: level = bullets in the magazine, bar = magazine / reload progress.
- **Hearts** = HP (100 HP = 10 hearts), **golden hearts** = shield.
- **Action bar**: HP, ammo, credits, ultimate and agent gauges.
- **Off-hand**: radar.

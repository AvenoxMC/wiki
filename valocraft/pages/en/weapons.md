# Weapons


Every weapon has a 3D model.

## Arsenal

| Category | Weapons |
|---|---|
| Melee | Knife |
| Sidearms | Classic, Ghost, Sheriff, Shorty, Frenzy |
| SMGs | Stinger, Spectre |
| Shotguns | Bucky, Judge |
| Rifles | Bulldog, Guardian, Phantom, Vandal |
| Snipers | Marshal, Operator, Outlaw |
| Heavies | Ares, Odin |

Weapons and charges are bought in the shop during the buy phase (`F`, or `/vc shop`).

## Mechanics

| Mechanic | Behavior |
|---|---|
| **Shooting** | Hitscan |
| **Accuracy** | Spread depends on movement: it grows when moving or in the air, and differs when crouching. Stop (or crouch) before shooting for accurate shots. Running or jumping makes them inaccurate. |
| **Recoil** | Climb, then lateral sweep. Built entirely into the bullet trajectory. |
| **Damage** | Head / body / legs, with range falloff tiers |
| **Penetration** | Bullets can go through walls |
| **Reload** | Reload with **Q**. Progress shows on the XP bar. |
| **Aim / scope** | Hold right click. Scopes on Operator, Marshal and Outlaw. |
| **Shotguns** | Close-range weapons (Bucky, Judge) |
| **Knife** | **x3 damage** from behind |

## Recoil and the camera

Recoil **never moves the player's view**. The server can only force an absolute camera orientation, which made the screen snap back during bursts. In 2.1 all recoil is applied to the **bullet path** instead.

## Models

- **HrdaValorant pack**: Classic, Ghost, Sheriff, Spectre, Vandal, Ares, Operator, Knife (and its `model-data` skins 2 to 15), shields.
- **Valocraft models**, made for this project (`assets/valocraft` in the pack): Shorty, Frenzy, Stinger, Bucky, Judge, Bulldog, Guardian, Phantom, Marshal, Outlaw, Odin. They use the `item_model` component (`item-model: valocraft:<weapon>`, automatic).

Model sources and tools are covered in [Development](page:development).

## Tuning

All stats (damage, fire rate, spread, recoil, penetration, zoom...) live in `weapons.yml`, with comments at the top of the file. Reload with `/vc reload`. To test changes safely, use the [Practice Range](page:practice-range).

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
| Heavy | Ares, Odin |

Weapons and charges are bought in the shop during the buy phase (`F`, or `/vc shop`). A weapon you can't afford can be **requested from a teammate** ([Gameplay](page:gameplay)).

## Mechanics

| Mechanic | How it works |
|---|---|
| **Shooting** | Hitscan, with **lag compensation** (up to 200 ms) |
| **Accuracy** | Inaccuracy grows while moving or in the air and changes when crouching. Stopping (or crouching) before shooting makes shots accurate. |
| **Recoil** | Climb then side sway, entirely built into bullet trajectory (your view doesn't move). |
| **Damage** | Head / body / legs, with range falloff steps |
| **Penetration** | Bullets go through walls; they destroy **enemy utility** they hit (turret, camera, traps...) |
| **Reload** | Key **Q**. Progress shown on the XP bar. |
| **Aim / scope** | Hold right click. Scopes on Operator, Marshal and Outlaw. No scoping while flashed. |
| **Shotguns** | Short range (Bucky, Judge) |
| **Knife** | **x3 damage** from behind |

## Hold to fire

Holding left click while aiming at a block within 64 blocks fires the weapon at its real fire rate. No block is damaged and the arm swing is hidden. Semi-autos fire at their max rate while held. See [Controls](page:controls).

## Scopes

The Operator, Marshal, Outlaw and Chamber's ultimate (Tour de Force) use a full-screen 16:9 scope: sharp round lens, black around it, thin crosshair and red dot. It's carried by the helmet and doesn't flicker.

## Skins

The lobby shop offers six collections for the 18 weapons: Prime, Reaver, Glitchpop, Ion, Elderflame and Oni, plus 14 knives. Skins are bought and equipped per weapon; a picked-up weapon keeps its owner's skin. See [Progression and Cosmetics](page:progression).

## Models

- **HrdaValorant pack**: Classic, Ghost, Sheriff, Spectre, Vandal, Ares, Operator, knives, shields.
- **Valocraft models**, made for the project: Shorty, Frenzy, Stinger, Bucky, Judge, Bulldog, Guardian, Phantom, Marshal, Outlaw, Odin (`item_model` component).

## Tuning

All stats (damage, fire rate, inaccuracy, recoil, penetration, zoom...) are in `weapons.yml`, documented at the top of the file. Reload with `/vc reload`. To test, use the [Practice Range](page:practice-range).

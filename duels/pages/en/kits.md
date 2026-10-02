# Kits

Five example kits are created on first start: `nodebuff`, `builduhc`, `sumo`, `combo` and `archer`. Create and edit kits in-game with `/dkit`, or update `kits.yml` manually and run `/duels reload`.

## Create a kit from your inventory

Equip the inventory, armor and potion effects you want, then run:

```text
/dkit create <name>                 Create from your inventory; the held item becomes the icon
/dkit setinv <name>                 Replace the kit contents with your current setup
/dkit load <name>                   Load the kit to edit it (switch to Creative to rearrange)
/dkit setname <name> &bNoDebuff     Set the displayed name
/dkit seticon <name>                Set the icon from the held item
/dkit set <name> <setting> <value>  Change a kit setting
```

## Kit settings

| Setting | Effect |
|---|---|
| `build` | Allow building, for example in BuildUHC. |
| `break-map` | Allow breaking map blocks. If disabled, only player-placed blocks can be broken. |
| `hunger` / `regen` | Configure hunger and natural regeneration. |
| `no-damage` | Hits deal no damage but preserve knockback, for Sumo. |
| `water-kills` | Eliminate a player who touches water, for Sumo. |
| `hit-delay` | Ticks between hits (20 = vanilla, 2 = Combo). |
| `queue` | Show the kit in the “Play” menu. |
| `enabled` | Enable or disable the kit. |

A kit can also be restricted to particular arenas with `/arena kits <arena> add <kit>`.

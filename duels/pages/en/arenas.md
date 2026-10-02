# Arenas

Arenas are configured with `/arena`. A match is played in a disposable copy, never in the template world.

## Arena worlds

| World | Purpose |
|---|---|
| `duels_tpl_<arena>` | Arena template. Unloaded except while using `/arena edit`. |
| `duels_match_<arena>_<n>` | Temporary match copy, unloaded and deleted when the match ends. |

When players choose the same mode, the plugin selects an available arena that is enabled, has at least two spawns, supports the selected kit and is below its `max-instances` limit. It copies the template asynchronously, loads the copy and then teleports the players. `worlds.max-loaded-instances` limits the total loaded instances across the server. Leftover match copies from a crash are removed at startup. Spawn-chunk loading is disabled in these worlds to speed up copying.

## Create an arena

```text
/arena create <name> <type>             Create an empty world and teleport you there in Creative
/arena create <name> <type> <world>      Copy an existing world as the template
   type = duel or devine
   ... build the map ...
/arena addspawn <name>                   Add a spawn (repeat; at least two)
/arena setspec <name>                    Set the optional spectator point
/arena save <name>                       Save and unload the template
```

For a schematic-based arena, see [Schematics](page:schematics).

## Edit an arena later

`/arena edit <name>` loads its template for editing. Matches already in progress are unaffected because they use independent copies. Run `/arena save <name>` when done to save and unload the template.

## Optional settings

| Command | Effect |
|---|---|
| `/arena kits <name> add <kit>` | Restrict the arena to selected kits. With no restriction, every kit is accepted. |
| `/arena set <name> maxinstances <count>` | Set simultaneous matches allowed on the arena. |
| `/arena set <name> voidy <height>` | Eliminate players who fall below this Y coordinate. Useful for floating and Sumo maps. |
| `/arena set <name> buildlimit <height>` | Set the maximum building height. |
| `/arena set <name> displayname <name>` | Set the name displayed in menus. Color codes such as `&a` are supported. |
| `/arena set <name> icon` | Set the menu icon to the item in your hand. |

An arena must have at least two spawns to be available for a match.

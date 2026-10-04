# Map Setup


Maps are configured **in game** with `/vc map ...` and the selection wand. This page builds a map called `ascent` from scratch. To skip building, see [Importing Maps](page:importing-maps).

## What a playable map needs

- A **waiting room** (used at the end of a match and on reconnect)
- **Attack** and **defend** spawns (usually 5 each)
- At least one **spike site** (A, B, C...)
- **Pre-round walls**
- Player limits
- Being **enabled**

`/vc map info <id>` lists exactly what's missing.

## Full walkthrough

```
/vc map create ascent
/vc map setname ascent Ascent
/vc map setwaiting ascent            (waiting room = your position)
/vc map addspawn ascent attack       (repeat for each player, usually 5)
/vc map addspawn ascent defend
/vc wand                             (left click = pos1, right click = pos2)
/vc map addsite ascent A             (selection = plant zone of site A)
/vc map addsite ascent B
/vc map addwall ascent               (selection = pre-round wall, green glass by default)
/vc map addwall ascent light_blue_stained_glass
/vc map previewwalls ascent          (show / hide walls to check them)
/vc map setplayers ascent 2 10
/vc map setmode ascent unrated       (default mode, optional)
/vc map setmusic ascent hrdavalorant.maps.ascent
/vc map addorb ascent                (ult orbs, optional)
/vc map addzipline ascent            (ziplines, optional)
/vc map enable ascent
```

## Step by step

### 1. Create and name

`/vc map create <id>` then `/vc map setname <id> <display name>`.

### 2. Waiting room and spawns

Stand where you want it and run `/vc map setwaiting <id>`. Repeat `/vc map addspawn <id> attack` and `/vc map addspawn <id> defend` at each spawn position. `/vc map clearspawns <id> <attack|defend>` clears a list.

### 3. Spike sites

1. `/vc wand`
2. **Left click** = pos1, **right click** = pos2.
3. `/vc map addsite <id> A` (and `B`, `C`...). The selection becomes the plant zone. `/vc map removesite <id> <site>` removes one.

### 4. Pre-round walls

Select the area with the wand, then `/vc map addwall <id> [block]`. The default block is **green glass**.

- Walls only fill **empty** blocks and are removed exactly when the round starts: the map is **never damaged**.
- `/vc map previewwalls <id>` shows or hides a preview; `/vc map walls <id>` lists them, `/vc map removewall <id> <n>` removes one.

### 5. Players, mode and music

`/vc map setplayers <id> <min> <max>`, `/vc map setmode <id> <mode>` ([Game Modes](page:modes)), `/vc map setmusic <id> <sound|none>`.

### 6. Options

- [Ult orbs](page:ultimate): `/vc map addorb <id>` / `/vc map clearorbs <id>`
- [Ziplines](page:ziplines)
- Tactical map and radar area: computed from spawns, sites, walls and orbs. To set it manually, select the area with the wand and run `/vc map setminimap <id>`; `/vc map clearminimap <id>` goes back to automatic.

### 7. Enable

`/vc map enable <id>` (and `disable` to take it out of rotation).

## Map world: loaded on demand

- A map built in its **own world** (for example `vc_ascent`, created by [importing](page:importing-maps)) is **not loaded at server startup**. The world is loaded **when a match launches**, during the loading screen, then **saved and unloaded** once nobody uses it (checked every 30 s, `maps.unload-check`).
- `/vc map tp <id>` and `/vc map previewwalls <id>` load the world on demand to set the map up. It's unloaded once you leave.
- A map built in the **main world** (`world`) works too, but that world always stays loaded.

## Crash protection

Placed blocks (walls, spike, abilities) are **saved to disk** in `plugins/Valocraft/data/` and **restored the next time the world loads** if the server crashes.

## See also

- [Commands and Permissions](page:commands)
- [Importing Maps](page:importing-maps)

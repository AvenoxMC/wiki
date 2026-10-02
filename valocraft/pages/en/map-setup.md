# Map Setup


Maps are configured **in game** with `/vc map ...` and the selection wand. This page builds a map called `ascent` from scratch. To skip building, see [Importing Maps](page:importing-maps).

## What a playable map needs

- A **waiting room**
- **Attacker** and **defender** spawns (usually 5 each)
- At least one **spike site** (A, B, C...)
- **Pre-round walls**
- Player limits
- To be **enabled**

`/vc map info <id>` lists exactly what is still missing.

## Walkthrough

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
/vc map previewwalls ascent          (show / hide the walls to check them)
/vc map setplayers ascent 2 10
/vc map setmusic ascent hrdavalorant.maps.ascent
/vc map addorb ascent                (ultimate orbs, optional)
/vc map addzipline ascent            (ziplines, optional)
/vc map enable ascent
```

## Step by step

### 1. Create and name

`/vc map create <id>` then `/vc map setname <id> <display name>`.

### 2. Waiting room and spawns

Stand where you want it and run `/vc map setwaiting <id>`. Repeat `/vc map addspawn <id> attack` and `/vc map addspawn <id> defend` at each spawn position.

### 3. Spike sites

1. `/vc wand`
2. **Left click** = pos1, **right click** = pos2.
3. `/vc map addsite <id> A` (and `B`, `C`...). The selection becomes the plant zone.

### 4. Pre-round walls

Select the area with the wand, then `/vc map addwall <id> [block]`. The default block is **green glass**; pass another block name such as `light_blue_stained_glass` to change it.

- Walls only fill **empty** blocks of the zone and are removed identically at round start, so the map is **never damaged**.
- `/vc map previewwalls <id>` toggles a preview so you can check placement.

### 5. Players and music

`/vc map setplayers <id> <min> <max>` sets the player range, and `/vc map setmusic <id> <sound>` sets the music.

### 6. Optional features

- [Ultimate orbs](page:ultimate): `/vc map addorb <id>` / `/vc map clearorbs <id>`
- [Ziplines](page:ziplines)

### 7. Enable

`/vc map enable <id>`.

## Crash safety

Placed blocks (walls, spike) are **saved to disk** in `plugins/Valocraft/data/` and **restored if the server crashes**.

## Related

- [Commands and Permissions](page:commands)
- [Importing Maps](page:importing-maps)

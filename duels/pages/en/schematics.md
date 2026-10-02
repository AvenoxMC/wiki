# Schematics

You can create a new arena from a supported WorldEdit schematic with `/arena fromschem`.

## Supported formats

| Extension | Source | Block format |
|---|---|---|
| `.schem` | Sponge v1, v2 or v3, created by WorldEdit 7+ or FAWE in 1.13+ | Modern blocks are converted automatically to 1.8 equivalents. |
| `.schematic` | MCEdit, created by WorldEdit 6 for 1.8 | Blocks are already in 1.8 format. |

## Find and paste a schematic

1. Put the file in `plugins/Duels/schematics/`. The plugin also scans `plugins/WorldEdit/schematics/` and `plugins/FastAsyncWorldEdit/schematics/`; folders can be changed in `config.yml` under `schematics.folders`.
2. List available files and create an arena:

```text
/arena schematics                         List discovered schematics
/arena fromschem <name> <file> <type>     Create an empty world, paste the map and teleport you there
   (equivalent: /arena create <name> <type> <file.schem>)
/arena addspawn <name>                    Add at least two spawns
/arena setspec <name>                     Set the optional spectator point
/arena save <name>
```

The map is centered at `0 / 64 / 0`. Change the paste height with `schematics.paste-y`. The plugin places the lethal void zone five blocks below the map. `/arena paste <name> <file>` pastes a schematic at your position while editing an arena, similar to `//paste`; this is useful for assembling a map from multiple pieces.

## Conversion and performance

Modern blocks are converted using WorldEdit's conversion table while preserving orientation for stairs, slabs, logs, doors, signs and similar blocks. When a block has no 1.8 equivalent, it is approximated; examples include concrete to same-color wool, glazed terracotta to stained clay, crimson/warped/cherry wood to oak, deepslate to cobblestone, and lanterns to air. The plugin lists approximated block types after creation.

Blocks are written directly into chunks. Work is spread across ticks according to `schematics.ms-per-tick` to avoid freezing the server, and progress is shown as a percentage.

## Limitations

Air is not pasted. Block-entity contents are not copied: sign text, chest contents and banners are not preserved.

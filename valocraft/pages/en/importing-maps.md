# Importing Maps


Valocraft can download maps from [Ommo's VALORANT x Minecraft](https://ommo.me/valorant-x-minecraft) project directly in game.

## Commands

```
/vc import list          catalog + required Minecraft version
/vc import ascent        downloads, installs the vc_ascent world and creates the Valocraft map "ascent"
```

## What the import does

- Downloads the map and installs it as the `vc_<name>` world.
- Creates a Valocraft map with the same id.
- The world is then **loaded on demand**: when a match launches on that map, or with `/vc map tp <name>` to set it up. It's unloaded once nobody uses it ([Map Setup](page:map-setup)).

## What's left to do

The import does **not** place gameplay points. You still need:

- The waiting room
- Spawns (attack / defend)
- Spike sites
- Pre-round walls

Go to the map with `/vc map tp ascent`, follow [Map Setup](page:map-setup), then enable it:

```
/vc map enable ascent
```

## Version limits

A map saved in a **newer Minecraft version than the server** is refused. **Lotus, Sunset and Breeze** require **Minecraft 1.21.11**.

## Editing the catalog

The catalog is the `map-library` section of `config.yml`.

## ⚖️ License

Ommo's maps are licensed **CC BY-NC-ND 4.0**.

- Allowed on a **private server between friends**.
- A **public** server needs a **commercial license** (contact@ommo.me).
- **Do not republish** the maps.

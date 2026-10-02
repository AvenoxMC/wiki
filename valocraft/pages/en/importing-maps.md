# Importing Maps


Valocraft can download maps from Ommo's [VALORANT x Minecraft](https://ommo.me/valorant-x-minecraft) project directly from the game.

## Commands

```
/vc import list          catalog + required Minecraft version
/vc import ascent        downloads, installs the world vc_ascent and creates the Valocraft map "ascent"
```

## What the importer does

- Downloads the map and installs it as the world `vc_<name>`.
- Creates a Valocraft map with the same id.
- **Loads the world automatically** on every server start.

## What you still have to do

The importer does **not** place gameplay points. You still need to set:

- Spawns (attack / defend)
- Spike sites
- Pre-round walls

Follow [Map Setup](page:map-setup), then enable the map:

```
/vc map enable ascent
```

## Version limits

A map saved in a **newer Minecraft version than your server** is refused. **Lotus, Sunset and Breeze** require **Minecraft 1.21.11**.

## Editing the catalog

The map catalog is the `map-library` section of `config.yml`.

## ⚖️ License

Ommo's maps are under **CC BY-NC-ND 4.0**.

- Allowed on a **private server among friends**.
- A **public server** requires a **commercial license** (contact@ommo.me).
- **Do not republish** the maps.

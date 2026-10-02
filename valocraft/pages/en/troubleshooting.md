# Troubleshooting


## The resource pack doesn't load

1. Check the **server console**: it logs the link offered to each player and the client's response (`ACCEPTED`, `DECLINED`, `FAILED_DOWNLOAD`, `SUCCESSFULLY_LOADED`...).
2. Ask the player to run `/vc pack send` to receive it again.
3. Admins: `/vc pack info` shows the mode and link, `/vc pack reload` reloads it.
4. If the Minecraft-port hosting doesn't work for you, use a dedicated port (`resource-pack.self-host.http-port: 8164`) or an external URL. See [Resource Pack](page:resource-pack).

## My map won't start / isn't playable

Run `/vc map info <id>`: it lists what is missing (waiting room, spawns, sites, walls, player limits, enable). See [Map Setup](page:map-setup).

## An imported map is refused

The map was saved in a **newer Minecraft version** than your server. Lotus, Sunset and Breeze require **Minecraft 1.21.11**. See [Importing Maps](page:importing-maps).

## Automatic weapons fire slowly

Minecraft sends **one signal per left click**, so with left-click shooting automatic weapons fire at your click rate. For hold-to-fire, set `controls.fire-button: RIGHT` in `config.yml`. See [Controls](page:controls).

## My screen "goes back" during bursts

Fixed in **2.1**: recoil no longer moves the camera and is applied entirely to the bullet path. Update to 2.1. See [Weapons](page:weapons).

## I can't use abilities or shoot

You may be **immobilized** (Lockdown or Thrash). See the status effects table on [Agents](page:agents).

## Players lost their items after a crash

Inventories saved during a game are stored in `plugins/Valocraft/playerdata/` and **returned on reconnect**. Temporary blocks (walls, spike) in `plugins/Valocraft/data/` are restored automatically.

## I updated and things look wrong

- Remove the **old jar** (`Valocraft-2.0.0.jar`) so only `Valocraft-2.1.jar` remains. See [Installation](page:installation).
- Valocraft **1.x** is not compatible with 2.x.

## Still stuck?

Open an issue on this repository with your server version, the Valocraft version and the relevant console output.

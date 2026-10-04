# Troubleshooting


## The resource pack doesn't load

1. Check the **server console**: it shows the link offered to each player and the client's answer (`ACCEPTED`, `DECLINED`, `FAILED_DOWNLOAD`, `SUCCESSFULLY_LOADED`...).
2. Ask the player to run `/vc pack send` again.
3. Admins: `/vc pack info` shows the mode and link, `/vc pack reload` reloads it.
4. If hosting on the Minecraft port doesn't work for you, use a dedicated port (`resource-pack.self-host.http-port: 8164`) or an external URL. See [Resource Pack](page:resource-pack).

## An ability icon shows the wrong agent

Update the plugin: the fixed pack (Cove, Trademark / Rendezvous, FRAG/ment / FLASH/drive icons) is sent automatically. If the old pack is still cached, run `/vc pack send`.

## My map doesn't start / isn't playable

Run `/vc map info <id>`: it lists what's missing (waiting room, spawns, sites, walls, player limits, enabled). See [Map Setup](page:map-setup).

## "Map world not found"

The world folder (`vc_<map>`) no longer exists next to the server, or the world name saved in `maps/<id>.yml` (`world` key) is wrong. Worlds are no longer loaded at startup: it's normal not to see them in `/mv list` or similar until a match launches.

## I can't see my own agent skin in F5

Minecraft only accepts skins signed by Mojang for yourself. Other players do see your agent skin. Install **SkinsRestorer**: skins are then signed through MineSkin and visible to everyone ([Installation](page:installation)). The server needs Internet access on the first startup.

## A game started alone ends immediately

Use `/vc forcestart` (not `/vc start`): an empty team is then never considered eliminated.

## My ability doesn't fire when I press the key

That's expected: the key takes the ability in hand, **left click** uses it. For the old behaviour: `controls.instant-abilities: true` ([Controls](page:controls)).

## An imported map is refused

The map was saved in a **newer Minecraft version** than the server. Lotus, Sunset and Breeze need **Minecraft 1.21.11**. See [Importing Maps](page:importing-maps).

## Fire doesn't continue when I hold left click

Continuous fire needs you to aim at a block within **64 blocks**. When aiming at the sky, click instead. Check `controls.continuous-fire` and `controls.semi-auto-hold` ([Controls](page:controls)).

## I can't shoot or use abilities

You may be **detained**, **suppressed** or **jammed** (Lockdown, Thrash, ZERO/point, Steel Garden...), or piloting a drone. See the status table on [Agents](page:agents).

## A player was removed from the game

The AFK check removes a player who doesn't move for 90 s (`afk.kick-after`). A disconnected player has 3 minutes to come back (`reconnect.timeout`).

## Players lost their items after a crash

Inventories saved during a match are in `plugins/Valocraft/playerdata/` and **given back on reconnect**. Temporary blocks (walls, spike, abilities) are restored the next time the map world loads.

## I updated and something is off

- Keep only `Valocraft-2.2.jar` in `plugins/`. See [Installation](page:installation).
- Valocraft **1.x** isn't compatible with 2.x.

## Still stuck?

Open an issue on this repository with the server version, the Valocraft version and the relevant part of the console.

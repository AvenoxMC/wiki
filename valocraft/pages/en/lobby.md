# Lobby and Matchmaking


The lobby spawn is set with `/vc setlobby` (admin). Players go back to it with `/vc lobby`.

## Lobby items

| Item | Purpose |
|---|---|
| ⭐ **Join a match** (nether star) | Joins the fullest waiting game. **Sneak + right click**: list of all games. |
| 📖 **Statistics** (book) | Your stats (K/D, headshot %, wins, MVPs, favorite agent, rank) and the leaderboards. |
| 🔨 **Create a game** (anvil) | Pick a free map and a [mode](page:modes), and become the **host**. |
| 💎 **Shop** (emerald) | Weapon skins, knives, cards, titles, kill banners and sounds, sprays, battle pass, missions. Also `/vc boutique`. See [Progression and Cosmetics](page:progression). |

## Hosting a game

1. Use the **anvil** (Create a game), pick a free map, then the mode.
2. You become the host. Others join with the star or `/vc join <map>`.
3. The host gets a **green item** that starts the game from **2 players** (an admin can start alone with `/vc forcestart`).

## Joining by command

| Command | Effect |
|---|---|
| `/vc join` | Opens the game list |
| `/vc join <map>` | Joins a specific map |
| `/vc list` | Lists games |
| `/vc leave` | Leaves the game |

## Before the match

1. **Waiting room in the lobby**: players stay in the lobby with the game items (team, mode for the host, start, leave). The map world isn't loaded yet.
2. **Countdown**, then **agent select** (25 s) in a menu, still in the lobby. See [Agents](page:agents).
3. **Loading screen**: while the server loads the map world, a menu shows every player's **card (banner)**, **agent** and **title**, red team at the top and blue at the bottom. The boss bar shows progress.
4. Everyone is moved onto the map and the first round starts.

When the match ends, players go back to the lobby and the map world is unloaded.

## Parties

| Command | Effect |
|---|---|
| `/vc party invite <player>` | Invite (the player gets [Accept] / [Decline] buttons) |
| `/vc party leave` / `kick <player>` / `list` | Leave / kick / see the party |
| `/vc party chat <message>` | Talk to the party |

When the leader joins a game, the whole party follows if there's room, and plays on the same team. Teams are balanced on a hidden MMR.

## Lobby leaderboards

Leaderboard holograms (rank, kills, wins, ACS, headshots, aces, battle pass) can be placed in the lobby by an admin. See [Progression and Cosmetics](page:progression).

## Statistics

Tracked per player: kills / deaths, assists, headshots, wins, MVPs, first bloods, aces, damage, combat score, favorite agent, rank. Stored in `stats.yml`, SQLite or MySQL ([Configuration](page:configuration)). `/vc resume` reopens your last match summary and `/vc rang [player]` shows a rank.

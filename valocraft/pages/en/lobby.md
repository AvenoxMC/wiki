# Lobby and Matchmaking


Set the lobby spawn with `/vc setlobby` (admin). Players return to it with `/vc lobby`.

## Lobby items

| Item | What it does |
|---|---|
| ⭐ **Join a match** | Joins the fullest waiting game. **Sneak + right-click** lists all games. |
| 📖 **Statistics** | Your K/D, headshot %, wins, MVPs, favourite agent, and the leaderboards. |
| 🔨 **Create a game** | Pick a free map and become its **host**. |
| 💎 **Shop** | Spend Radianite on agent unlocks and weapon skins. Also available with `/vc boutique`. |

The lobby also offers a "Play" compass (games menu and quick match), a waiting room per map, team selection and a countdown.

## Hosting a game

1. Use the **anvil** (Create a game) and choose a free map.
2. You become the host. Other players join through the star or `/vc join <map>`.
3. The host gets a **green item** that starts the game with as few as **2 players**.

## Joining by command

| Command | Effect |
|---|---|
| `/vc join` | Opens the games menu |
| `/vc join <map>` | Joins a specific map |
| `/vc list` | Lists games |
| `/vc leave` | Leaves the game |

## After the countdown

An **agent select phase (25 s)** opens. See [Agents](page:agents).

## Statistics

Stats are tracked per player and stored in `plugins/Valocraft/stats.yml`:

- Kills / deaths (K/D)
- Headshot percentage
- Wins
- MVPs
- Favourite agent
- Leaderboards

## Radianite and unlocks

Earn Radianite when a match ends. Wins, losses, kills, assists, rounds won and MVP awards contribute; the amount is configurable. Five agents (Phoenix, Jett, Sova, Brimstone and Sage) are free by default; each of the other ten costs 1,000 ◆ by default. The shop also offers six weapon-skin collections for all 18 weapons. Buy and equip skins per weapon; weapons picked up from another player keep their owner's skin. Purchases require a confirmation click. Server owners can configure prices, rewards and free agents under `progression` in `config.yml`.

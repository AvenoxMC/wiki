# Progression and Cosmetics


Everything happens in the **lobby shop** (emerald, or `/vc boutique`). The currency is **Radianite (◆)**. Purchases take two clicks (the first one asks for confirmation).

## Radianite

Earned at the end of every match (`progression.rewards`):

| Source | Gain |
|---|---|
| Win | 150 ◆ |
| Loss | 60 ◆ |
| Kill | +5 ◆ |
| Assist | +2 ◆ |
| Round won | +5 ◆ |
| MVP | +50 ◆ |

Plus **daily missions** (3 per day, 150 ◆ each, `/vc missions`) and the **battle pass**. Admin: `/vc radianite give|take|set <player> <amount>`, `/vc radianite voir <player>`.

## Battle pass

- **30 levels of 1,000 XP** (`battlepass.levels`, `battlepass.xp-per-level`).
- XP every match: win 600, loss 300, draw 400, +20 per kill, +10 per assist, +30 per round won, +150 for MVP (`battlepass.xp`).
- **One reward per level**, given automatically: Radianite, cards, titles, kill banners and kill sounds, sprays.
- Menu: `/vc pass` or the **Battle pass** button in the shop.
- **New season**: changing `battlepass.season` resets everyone to level 0. Unlocked rewards are kept.
- A level's reward can be changed: `battlepass.rewards.<level>: "spray:gg"` (types `radianite`, `card`, `title`, `killbanner`, `killsound`, `spray`).
- Admin: `/vc pass addxp <player> <xp>`.

## What you can buy

| Category | Content |
|---|---|
| **Agents** | All free by default. To charge for them: `progression.default-agents` (e.g. `[JETT, PHOENIX, SOVA, BRIMSTONE, SAGE]`), `agent-price`. |
| **Weapon skins** | 6 collections × 18 weapons (1,000 to 2,000 ◆), equipped per weapon |
| **Knives** | 14 knives from the pack (600 to 2,500 ◆) |
| **Player cards** | One **banner** per agent (agent color, role symbol), 400 ◆ |
| **Titles** | 12 titles (200 to 3,000 ◆) |
| **Kill banners** | 8 styles: ❱ (free), ✦ ❤ ☠ ⚡ ✪ ⚔ ♛ |
| **Kill sounds** | 7 sounds (in-game names): Valorant (free), Carillon, Cloche, Xylophone, Pièces, Rétro 8-bit, Améthyste. Right click to preview. |
| **Sprays** | Text (GG free, EZ, NICE, ☠, ❤, ?, ACE, VALOCRAFT) and the emblems of all 29 agents |

Prices of banners, sounds and sprays: `progression.cosmetic-prices` (e.g. `killbanner: {couronne: 1000}`).

## Where they show

- **Card and title**: loading screen, match summary, chat (title before the name), statistics, and for your victim when you kill them.
- **Kill banner**: on each kill, your symbol is shown once per kill this round, in your card's color.
- **Kill sound**: the pitch rises with each kill of the round, special sound on the 5th.
- **Spray**: **sneak + F** in a match sticks your spray on the wall, floor or ceiling you look at (6 blocks). One per round, every 30 s in respawn modes; sprays disappear at the next round.

## Ranked

Competitive mode: ranks from Iron to Radiant, 5 placement games, RR based on result, performance and level gap. See [Game Modes](page:modes). The rank shows in chat, the waiting room, the loading screen, statistics and with `/vc rang`.

## Lobby leaderboards

Holograms refreshed every minute, placed by an admin:

```
/vc leaderboard set <type>     where you stand
/vc leaderboard remove         removes the nearest one (5 blocks)
/vc leaderboard list
```

Types: `rank`, `kills`, `wins`, `acs` (from 20 rounds), `headshots`, `aces`, `battlepass`. Settings: `leaderboards.refresh`, `leaderboards.size`. Positions are stored in `plugins/Valocraft/leaderboards.yml`.

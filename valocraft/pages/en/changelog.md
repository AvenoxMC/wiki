# Changelog

All notable changes to Valocraft, a Valorant recreation plugin for Paper (API 1.21.4, Java 21).

---

## [2.2]

> Replace the jar in `plugins/`; the resource pack updates automatically.

### Added

#### Interface and visuals
- **Full scoreboard (Tab)**, aligned in columns.

  | | Allies | Enemies |
  |---|---|---|
  | Agent and name | ✔ | ✔ |
  | Credits | current credits | credits at the start of the buy phase |
  | Weapon | weapon in hand | – |
  | Health | HP + shield | – |a
  | K / D / A | ✔ | ✔ |
  | Ultimate | ✔ | – |

- **Tactical minimap** for Sky Smoke, Dark Cover, Orbital Strike and From the Shadows: a rendered top-down map of the level with a cursor, the sites, teammates and smokes.
- **Smokes really hide players**:
  - smokes and walls are opaque, tinted 3D models, visible from afar;
  - an enemy inside or behind a smoke disappears from your screen at any distance.
- **Agent heads** worn by every player when full agent skins are turned off (`agents.full-skin: false`, see Agents).
- **Lobby shop and Radianite**:
  - agents to unlock;
  - 6 weapon skin collections (Prime, Reaver, Glitchpop, Ion, Elderflame, Oni) on 18 weapons, i.e. 108 models.

#### Game modes
- **Swiftplay**: first to 5 rounds, side swap after 4, economy and spike, no overtime (`modes.swiftplay`).
- **Replication**:
  - during agent select, everyone votes for an agent (duplicates allowed);
  - the whole team then plays the most-picked agent;
  - first to 5 rounds (`modes.replication`).
- **Escalation**:
  - two teams, respawns, no abilities;
  - each level forces a weapon: Odin, Ares, Phantom, Vandal, Spectre, Judge, Bulldog, Guardian, Sheriff, Marshal, Operator, then the **knife**;
  - 3 team kills per level (1 on the knife level). First team to finish wins, otherwise the furthest team after 10 minutes (`modes.escalation`).
- **Spike Rush**:
  - first to 4 rounds;
  - same random weapon for everyone;
  - full abilities;
  - every attacker carries a spike.
- **Deathmatch**:
  - free-for-all with 1.5 s respawns;
  - free weapons for 10 s after spawning;
  - a kill heals you;
  - 40 kills or 6 minutes.
- **Team Deathmatch**: two teams with agents and respawns, 100 kills or 9:30.
- **Competitive**:
  - ranks from Iron to Radiant, with 5 placement games;
  - RR based on result, performance (combat score) and team level gap;
  - leaving costs RR.
- Hosts pick the mode when creating a game. `/vc map setmode <map> <mode>` sets a map's default mode.

#### Agents (29 total)
- 13 new agents: Breach, Astra, Fade, Tejo, Clove, Deadlock, Veto, Iso, Chamber, KAY/O, Vyse, Yoru and Waylay.
- One new original agent: **Miks** (M-Pulse, Harmonize, Waveform, Bassquake).
- New status effects:
  - **suppressed**: no abilities;
  - **hindered**: lower fire rate, slowed;
  - **jammed**: no primary weapon;
  - **immune**: no negative effects.
- Two-step anchor abilities (Rendezvous, Gatecrash, Refract, Crosscut, Arc Rose): the first use places the anchor, the second uses it.
- **First-person piloting** for Sova's Owl Drone, Skye's Trailblazer and Tejo's Stealth Drone:
  - you become the creature, while your body stays behind and can be killed;
  - left click = creature action, right click = return to your body.
- **Full agent skins**: during a match, the player's whole skin becomes the agent's (not just a head). The original skin is restored back in the lobby (`agents.full-skin`).
- **SkinsRestorer support** (optional):
  - agent skins are signed through MineSkin, so the player also sees their own agent skin (F5 view, arms);
  - signed skins are created in the background on startup and cached in `data/agent-skins.yml`;
  - any agent's skin can be replaced with a skin image URL or a Minecraft username (`agents.skins.<agent>`).

#### Abilities
- **Manual activation**: keys 5–8 select the ability, and left click uses it. Nothing fires just by switching slots. `controls.instant-abilities: true` restores the old behaviour.
- **White flashes**: a full-screen white overlay that fades in 4 steps. You can't scope while flashed.
- **Hold-to-throw with trajectory preview**:
  - hold left click to see the arc (visible only to you), release to throw;
  - right click = underhand lob;
  - Sova's bolts go further the longer you hold.
- **Visible cooldown**: the signature ability icon stays in the hotbar with Minecraft's cooldown sweep while it recharges.
- **Destructible utility**: enemy bullets destroy deployed utility.

  | Utility | HP |
  |---|---|
  | Turret | 125 |
  | Spycam | 70 |
  | Leer, Interceptor | 60 |
  | Sonic Sensor, Chokehold, Trademark, Shear | 40 |
  | Alarmbot, Trapwire, Nanoswarm | 20 |

- **Enemy ultimates**: enemy ult points are shown in the scoreboard, with a chat alert and a sound when an enemy ult is ready.
- **More faithful kits**:
  - **Neon**: energy gauge, High Gear toggles the sprint, and crouching while sprinting slides;
  - **Viper**: fuel gauge, Poison Cloud and Toxic Screen are emitters you toggle on and off;
  - **Jett**: Tailwind is prepared first, then the dash is triggered;
  - **Iso**: Kill Contract opens a 1v1 glass arena above the map;
  - **Chamber**: Tour de Force now has a full-screen sniper scope on right click;
  - **Brimstone**: smokes are orange.
- **`abilities.yml`**: price, charges, cooldown, kill recharge and damage per ability, ult cost per agent, global damage and duration multipliers. Applied with `/vc reload`, no recompiling.

#### Maps and loading
- **On-demand map worlds**:
  - map worlds stay on disk and are no longer loaded at server startup;
  - when a match launches, the server loads the world, preloads the spawn chunks and moves everyone in;
  - an unused world is saved and unloaded (`maps.unload-check`).
- The **waiting room** and **agent select** now happen in the lobby.
- **Loading screen**: a menu showing every player's card (banner), agent and title, red team at the top and blue at the bottom, while the map loads (`game.loading-time`).
- **Player cards are now real banners**: agent color plus a role symbol. They appear in the shop, on the loading screen and in the match summary.

#### Progression and cosmetics
- **Battle pass**:
  - 30 levels of 1,000 XP, with XP earned every match (win, loss, kills, assists, rounds won, MVP);
  - one reward per level, given automatically: Radianite, cards, titles, kill banners, kill sounds, sprays;
  - `/vc pass` menu. Changing `battlepass.season` resets everyone's level (unlocked rewards are kept).
- **Kill banners**: on each kill, your symbol is repeated once per kill this round, in your card's color. The victim sees your card and title. 8 styles.
- **Kill sounds**: the pitch rises with each kill of the round, with a special 5th-kill sound. 7 sets, which you can preview in the shop.
- **Sprays**:
  - crouch + F in a match to spray on the targeted wall, floor or ceiling;
  - text sprays or the emblem of any of the 29 agents;
  - one per round (every 30 s in respawn modes).
- **Lobby leaderboards**: holograms placed with `/vc leaderboard set <type>`, refreshed every minute. Types: rank, kills, wins, ACS, headshots, aces, battle pass.
- **Shop additions**: 14 knives, player cards, 12 titles, kill banners, kill sounds, sprays.
- **Daily missions**: 3 random missions per day, 150 Radianite each (`/vc missions`).
- **Match summary**:
  - combat score, damage, first bloods, ACE announcements;
  - damage report on death;
  - end-of-match menu with every player's stats (`/vc resume`).

#### Team play and social
- **Weapon requests**: clicking a weapon you can't afford asks your team for it. A teammate who has the money clicks **[Buy for …]**: they pay and the weapon goes straight into your inventory.
- **Parties**:
  - `/vc party invite|leave|kick|list|chat`;
  - the party follows its leader into games and stays on the same team.
- **Team balancing** based on a hidden MMR.
- **Chat**: rank and title in front of names. Messages starting with `!` go to your team only.

#### Match flow
- **Reconnect**: a player who disconnects mid-match keeps their slot for 3 minutes and is put back in on return.
- **Surrender and remake votes**:
  - `/vc ff`: surrender, from round 5, 80% yes needed;
  - `/vc remake`: until round 3, if a teammate left.
- **AFK**: a player who doesn't move gets a warning at 45 s, then is kicked at 90 s.
- **Lag compensation**: shots are checked against where the shooter saw the target, up to 200 ms back.
- **Footsteps**:
  - running is audible to enemies, with a sound that depends on the block underneath;
  - crouch-walking is silent.
- **Permanent radar**: a map in the off-hand showing allies, spotted enemies, the spike, the sites and your team's smokes.

#### Admin
- `/vc forcestart [map]`: starts a match even with a single player. An empty team is never "eliminated", and the match doesn't count for ranked.
- `/vc ult add|set <player> [points]`: adds or sets ult points (`set` without a number fills the ult).
- `/vc pass addxp <player> <xp>`: gives battle pass XP.
- `/vc leaderboard set <type> | remove | list`: manages the lobby leaderboards.
- **All agents unlocked by default** (`progression.default-agents: [ALL]`).
- **SQLite / MySQL storage** (`storage.type`), with automatic import from `stats.yml`.

### Fixed
- **Ability icons**:
  - Harbor's Cove showed a Gekko icon (missing entry in the resource pack);
  - Chamber's Trademark and Rendezvous icons were swapped;
  - KAY/O's FRAG/ment and FLASH/drive icons were swapped.

  The pack's ability icon table is now rebuilt from the textures that actually exist.
- Right click to leave a piloted drone or tiger now works (a dedicated remote item is used).
- **Sniper scope**: a real full-screen 16:9 scope carried by the helmet. It no longer flickers.
- **Continuous fire**:
  - holding left click now fires at the weapon's real fire rate;
  - weapons can "mine" the targeted block up to 64 blocks away (nothing is ever broken), so the client sends a signal every tick;
  - the arm swing animation is hidden.

---

## [2.1] — Agent Update

### Added
- **15 playable agents** with an agent select phase and abilities on C / Q / E / X.
- **Ultimate system**: ult points from kills, deaths, spike and ult orbs.
- **Ziplines**.
- **Lobby** with a server selector and matchmaking.
- **3D models** for every weapon.

---

## [2.0]

### Added
- **Core game**:
  - Valorant-style rounds with economy and buy phase;
  - spike plant and defuse;
  - walls during the buy phase, overtime.
- **Weapons**:
  - the full Valorant arsenal, with damage falloff, spray patterns and wall penetration;
  - shields.
- **Maps**:
  - map setup commands (`/vc map ...`);
  - import of ready-made maps (`/vc import`).
- **Server and pack**:
  - automatic resource pack hosting on the Minecraft port;
  - Pterodactyl support.

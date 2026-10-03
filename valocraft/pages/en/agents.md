# Agents


Valocraft has **15 agents** in four roles. After the countdown, a **25 s agent select phase** opens:

- Each agent is **unique within a team**.
- A player who doesn't choose gets a **random free agent**.
- The menu groups agents by role and shows abilities, prices and ultimate cost.
- The agent's **voice line** (HrdaValorant pack) plays to the whole team on lock-in.

**How to read the tables:** prices are in ¤, and the number after the price is the **max charges**. *Free* means granted every round. Ultimate costs are in **points** (see [Ultimate System](page:ultimate)). Keys are **5 / 6 / 7 / 8** = **C / Q / E / X** ([Controls](page:controls)). Charges are bought in the shop's bottom row.

## Duelists

| Agent | C | Q | E (signature) | X (ultimate) |
|---|---|---|---|---|
| **Jett** | Cloudburst: thrown smoke (200 ¤, 2) | Updraft: high jump (150 ¤, 2) | Tailwind: dash in movement direction (free, returns after 2 kills) | Blade Storm: 5 precise knives, refilled on kill (8) |
| **Phoenix** | Blaze: fire wall that heals Phoenix (200 ¤) | Curveball: curving flash (250 ¤, 2) | Hot Hands: fire zone that heals Phoenix (free, returns after 2 kills) | Run it Back: 10 s, respawns at start point if killed (6) |
| **Raze** | Boom Bot: seeking explosive robot (300 ¤) | Blast Pack: charge that launches everyone, Raze included (200 ¤, 2) | Paint Shells: cluster grenade (free, returns after 2 kills) | Showstopper: devastating rocket (8) |
| **Reyna** | Leer: eye that blinds those who look at it (250 ¤, 2) | Devour: +100 HP after a kill (200 ¤, 2) | Dismiss: intangible and fast for 2 s after a kill (free) | Empress: 30 s of fire rate and speed, extended by kills (6) |
| **Neon** | Fast Lane: two electric walls (300 ¤) | Relay Bolt: concussive lightning bolt (200 ¤, 2) | High Gear: 8 s sprint, 30 s recharge | Overdrive: precise electric beam for 12 s, extended by kills (7) |

## Initiators

| Agent | C | Q | E (signature) | X (ultimate) |
|---|---|---|---|---|
| **Sova** | Owl Drone: gaze-guided drone that reveals (400 ¤) | Shock Bolt: explosive arrow (150 ¤, 2) | Recon Bolt: reveals enemies in view, 40 s recharge | Hunter's Fury: 3 shots that pierce walls (8) |
| **Skye** | Regrowth: heals nearby allies (200 ¤) | Trailblazer: guided tiger that concusses (250 ¤) | Guiding Light: guided hawk that flashes (1 free, 250 ¤, 40 s recharge) | Seekers: 3 seekers on the 3 nearest enemies (8) |
| **Gekko** | Mosh Pit: deadly puddle (250 ¤) | Wingman: creature that concusses the first enemy (300 ¤) | Dizzy: blinds enemies in view, 30 s recharge | Thrash: guided creature that immobilizes (8) |

## Controllers

| Agent | C | Q | E (signature) | X (ultimate) |
|---|---|---|---|---|
| **Brimstone** | Stim Beacon: fire rate and speed for allies (200 ¤) | Incendiary: incendiary grenade (250 ¤) | Sky Smoke: long-range smoke where you aim (1 free, 100 ¤, 3) | Orbital Strike: strike on the targeted area (8) |
| **Omen** | Shrouded Step: short teleport (100 ¤, 2) | Paranoia: shadow that passes through walls and blinds (300 ¤) | Dark Cover: long-range smoke (1 free, 150 ¤, 30 s recharge) | From the Shadows: teleport anywhere (7) |
| **Viper** | Snake Bite: acid + vulnerable (200 ¤, 2) | Poison Cloud: toxic cloud (200 ¤) | Toxic Screen: 30-block toxic wall through walls (free) | Viper's Pit: huge cloud, enemies inside can't see (9) |
| **Harbor** | Cascade: moving wave that slows (150 ¤) | Cove: water sphere (350 ¤) | High Tide: long water wall (free) | Reckoning: 3 geysers that concuss (7) |

## Sentinels

| Agent | C | Q | E (signature) | X (ultimate) |
|---|---|---|---|---|
| **Sage** | Barrier Orb: destructible ice wall (400 ¤) | Slow Orb: slowing zone (200 ¤, 2) | Healing Orb: heal an ally (left click) or yourself (right click), 45 s recharge | Resurrection: revives a targeted dead ally (8) |
| **Killjoy** | Nanoswarm: nanobot swarm (200 ¤, 2) | Alarmbot: trap that applies vulnerable (200 ¤) | Turret: 30 s turret (free) | Lockdown: immobilizes enemies within 20 blocks after 10 s (8) |
| **Cypher** | Trapwire: tripwire between two walls, reveals and concusses (200 ¤, 2) | Cyber Cage: small smoke (100 ¤, 2) | Spycam: camera that reveals for 45 s (free) | Neural Theft: on a dead enemy, reveals all enemies twice (6) |

## Status effects

| Status | Effect | Caused by |
|---|---|---|
| **Concussed** | Slowed, screen sways | Concussive abilities |
| **Blinded** | Black vision | Flashes, Leer, Paranoia, Dizzy, Seekers |
| **Vulnerable** | +50% damage taken | Alarmbot, Snake Bite |
| **Immobilized** | Cannot shoot or use abilities | Lockdown, Thrash |
| **Revealed** | Glowing outline visible through walls | Reveal abilities |
| **Intangible** | Takes no damage | Dismiss |

## Minecraft adaptations

- **Smokes** are made of particles and blind anyone standing inside them.
- **Flashes** turn vision **black**, not white.
- The outline of **revealed** enemies is visible to **everyone**, not only the revealing team.

## Agent appearance and smokes (2.2)

Players wear their agent's head for the full match, including enemies whose names are hidden. Gekko and Harbor use similar replacement heads. Set `agents.wear-heads: false` to disable agent heads.

Smokes and walls use opaque, tinted 3D models that remain visible at a distance and do not depend on the client's particle setting. An enemy inside or behind a smoke is hidden from your view at any distance. Players within 2.5 blocks can still see one another; allies and revealed enemies remain visible. Bullets still pass through smokes. Configure this with `agents.smokes-hide-players` and `agents.solid-smokes`.

## Balance

Abilities have **not yet been balanced in real matches**. Feedback is welcome through GitHub issues. Server owners can tune damage, durations and prices in `AbilityType.java` and `Kits.java` (see [Development](page:development)).

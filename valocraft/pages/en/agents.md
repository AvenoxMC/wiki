# Agents


Valocraft has **29 agents** in four roles. All of them are unlocked by default (`progression.default-agents: [ALL]`).

## Agent select

After the countdown, **agent select** (25 s) opens **in the lobby**, as a menu:

- Each agent is **unique within a team**, except in [Replication](page:modes) mode where the whole team plays the most-picked agent.
- A player who doesn't choose gets a **random free agent**.
- The agent's **voice line** plays to the whole team on lock-in.
- During the match, the player wears their agent's **full skin** (see below).

**How to read the tables:** prices are in ¤; *max* = maximum charges; *free* = granted every round; *cooldown* = time to get the free charge back. Ultimate costs are in **points** ([Ultimate System](page:ultimate)). Keys **5 / 6 / 7 / 8** = **C / Q / E / X**, then **left click** to use ([Controls](page:controls)). Charges are bought in the shop's bottom row. Everything can be tuned in `abilities.yml` ([Configuration](page:configuration)).

## Duelists

| Agent | C | Q | E (signature) | X (ultimate) |
|---|---|---|---|---|
| **Jett** | **Cloudburst**: thrown smoke that blocks vision (200 ¤, max 2) | **Updraft**: launches Jett into the air (150 ¤, max 2) | **Tailwind**: use to charge the wind (7.5 s), use again to dash; returns after 2 kills (free) | **Blade Storm**: 5 precise knives, refilled on kill — **8 pts** |
| **Phoenix** | **Blaze**: flame wall that blocks vision and heals Phoenix (200 ¤) | **Curveball**: curving flash: left click curves left, right click curves right (250 ¤, max 2) | **Hot Hands**: fireball: zone that burns enemies and heals Phoenix (free) | **Run it Back**: for 10 s, if Phoenix dies he respawns at the starting point — **6 pts** |
| **Raze** | **Boom Bot**: robot that rushes the nearest enemy and explodes (300 ¤) | **Blast Pack**: charge that knocks back everyone around (Raze included) (200 ¤, max 2) | **Paint Shells**: cluster grenade; returns after 2 kills (free) | **Showstopper**: rocket launcher: one devastating rocket — **8 pts** |
| **Reyna** | **Leer**: eye that blinds enemies who look at it (250 ¤, max 2) | **Devour**: after a kill (3 s): heal 100 HP (200 ¤, max 2) | **Dismiss**: after a kill (3 s): invulnerable and fast for 2 s (free, max 2) | **Empress**: 30 s frenzy: faster fire rate and movement — **6 pts** |
| **Neon** | **Fast Lane**: two electric walls that block vision (300 ¤) | **Relay Bolt**: bolt that bounces, then concusses nearby enemies (200 ¤, max 2) | **High Gear**: toggles the sprint (energy gauge); crouch while sprinting to slide (free) | **Overdrive**: 12 s: precise electric beam and max speed; refills energy — **7 pts** |
| **Iso** | **Contingency**: energy wall that moves forward and blocks vision (200 ¤) | **Undercut**: bolt that goes through walls and makes vulnerable (200 ¤, max 2) | **Double Tap**: shield that absorbs one bullet (12 s); returns after 2 kills (free) | **Kill Contract**: Iso and the enemy hit fight alone in a glass arena above the map (15 s) — **7 pts** |
| **Yoru** | **Fakeout**: decoy that walks forward and blinds enemies who approach (100 ¤) | **Blindside**: flash that bounces off walls (250 ¤, max 2) | **Gatecrash**: place a rift (left click), then teleport to it (left click) (free, 35 s cooldown) | **Dimensional Drift**: 10 s invisible and untouchable (can't shoot); left click to exit — **8 pts** |
| **Waylay** | **Saturate**: light orb that slows and hinders (lower fire rate) (200 ¤) | **Lightspeed**: two quick dashes (150 ¤) | **Refract**: place a beacon here (left click), then come back to it (left click, 8 s) (free, 30 s cooldown) | **Convergent Paths**: beam that slows and hinders every enemy in front of you — **8 pts** |

## Initiators

| Agent | C | Q | E (signature) | X (ultimate) |
|---|---|---|---|---|
| **Sova** | **Owl Drone**: drone you pilot in first person, its dart marks enemies (400 ¤) | **Shock Bolt**: explosive arrow (left click: 1 bounce, right click: none); hold to shoot further (150 ¤, max 2) | **Recon Bolt**: arrow that reveals enemies in its line of sight; hold to shoot further (free, 40 s cooldown) | **Hunter's Fury**: 3 energy blasts that go through walls — **8 pts** |
| **Skye** | **Regrowth**: heals nearby allies (60 HP) (200 ¤) | **Trailblazer**: tiger you pilot in first person, its leap concusses (250 ¤) | **Guiding Light**: guided hawk that explodes into a flash (free, +250 ¤, max 2, 40 s cooldown) | **Seekers**: 3 trackers that chase the 3 nearest enemies — **8 pts** |
| **Gekko** | **Mosh Pit**: creature that bursts into a very dangerous puddle (250 ¤) | **Wingman**: creature that walks forward and concusses the first enemy it meets (300 ¤) | **Dizzy**: flying creature that blinds enemies in view (free, 30 s cooldown) | **Thrash**: guided creature that detains enemies on impact — **8 pts** |
| **Breach** | **Aftershock**: charge through a wall: 3 blasts on the other side (200 ¤) | **Flashpoint**: flash that goes through the targeted wall (250 ¤, max 2) | **Fault Line**: straight seismic wave that concusses enemies (free, 35 s cooldown) | **Rolling Thunder**: cone earthquake: concusses and knocks up enemies — **9 pts** |
| **Fade** | **Prowler**: guided creature that blinds the first enemy it meets (250 ¤, max 2) | **Seize**: orb that detains enemies and makes them vulnerable (200 ¤) | **Haunt**: thrown eye that reveals enemies in view (free, 40 s cooldown) | **Nightfall**: nightmare wave: reveals and weakens the enemies it hits — **8 pts** |
| **Tejo** | **Stealth Drone**: drone you pilot in first person: reveals, then suppresses at the end (300 ¤) | **Special Delivery**: sticky concussive grenade (200 ¤) | **Guided Salvo**: tactical map: missile on the chosen point (free, max 2, 40 s cooldown) | **Armageddon**: tactical map: line of bombs (along your view) — **8 pts** |
| **KAY/O** | **FRAG/ment**: grenade that explodes several times (200 ¤) | **FLASH/drive**: flash: left click normal, right click quick (250 ¤, max 2) | **ZERO/point**: knife that suppresses nearby enemies' abilities (free, 40 s cooldown) | **NULL/cmd**: 12 s of suppression pulses, fire rate and speed — **8 pts** |

## Controllers

| Agent | C | Q | E (signature) | X (ultimate) |
|---|---|---|---|---|
| **Brimstone** | **Stim Beacon**: zone that boosts allies' fire rate and speed (200 ¤) | **Incendiary**: incendiary grenade: fire zone (250 ¤) | **Sky Smoke**: places a smoke where you aim on the tactical map (free, +100 ¤, max 3) | **Orbital Strike**: devastating orbital strike on the targeted zone — **8 pts** |
| **Omen** | **Shrouded Step**: short teleport where you aim (100 ¤, max 2) | **Paranoia**: shadow that goes through walls and blinds everything it touches (300 ¤) | **Dark Cover**: long-range smoke placed on the tactical map (free, +150 ¤, max 2, 30 s cooldown) | **From the Shadows**: teleport anywhere on the map — **7 pts** |
| **Viper** | **Snake Bite**: acid vial: damage and vulnerability (200 ¤, max 2) | **Poison Cloud**: toxic cloud emitter you toggle on and off (fuel) (200 ¤) | **Toxic Screen**: long toxic wall you toggle on and off (fuel) (free) | **Viper's Pit**: huge toxic cloud around Viper: enemies inside can't see — **9 pts** |
| **Harbor** | **Cascade**: wave that moves forward, blocks vision and slows (150 ¤) | **Cove**: water sphere that blocks vision (350 ¤) | **High Tide**: long water wall that slows (free) | **Reckoning**: 3 geysers that concuss enemies in the targeted zone — **7 pts** |
| **Astra** | **Gravity Well**: tactical map: pulls enemies in, then makes them vulnerable (150 ¤) | **Nova Pulse**: tactical map: concussive pulse (150 ¤) | **Nebula**: tactical map: smoke anywhere on the map (free, +150 ¤, max 2, 25 s cooldown) | **Cosmic Divide**: tactical map: giant cosmic wall that blocks vision (along your view) — **7 pts** |
| **Clove** | **Pick-me-up**: after a kill or assist (3 s): heal and speed (100 ¤) | **Meddle**: fragment that temporarily weakens enemies (decay) (250 ¤) | **Ruse**: tactical map: smokes anywhere (2 free, max 2, 40 s cooldown) | **Not Dead Yet**: triggers on death: you come back, get a kill or assist within 12 s — **8 pts** |
| **Miks** | **M-Pulse**: sound wave: left click concusses enemies, right click heals allies (250 ¤) | **Harmonize**: combat stim for the targeted ally and you (right click: you only) (200 ¤) | **Waveform**: tactical map: wall of sound waves that blocks vision (free, +150 ¤, max 2, 30 s cooldown) | **Bassquake**: shockwave in front of you: knocks back, slows and deafens — **8 pts** |

## Sentinels

| Agent | C | Q | E (signature) | X (ultimate) |
|---|---|---|---|---|
| **Sage** | **Barrier Orb**: raises a solid ice wall (400 ¤) | **Slow Orb**: zone that slows everyone crossing it (200 ¤, max 2) | **Healing Orb**: heals the targeted ally (left click) or yourself (right click) (free, 45 s cooldown) | **Resurrection**: revives a dead ally you look at — **8 pts** |
| **Killjoy** | **Nanoswarm**: grenade that releases a swarm of nanobots (200 ¤, max 2) | **Alarmbot**: trap: reveals and makes the approaching enemy vulnerable (200 ¤) | **Turret**: turret that shoots enemies for 30 s (free) | **Lockdown**: after 10 s, detains enemies in a large radius — **8 pts** |
| **Cypher** | **Trapwire**: wire between two walls: reveals and slows whoever crosses it (200 ¤, max 2) | **Cyber Cage**: small thrown smoke (100 ¤, max 2) | **Spycam**: wall camera that reveals enemies in view (45 s) (free) | **Neural Theft**: aim at a dead enemy: reveals all enemies twice — **6 pts** |
| **Deadlock** | **GravNet**: grenade that forces enemies to crouch (200 ¤) | **Sonic Sensor**: sensor that concusses enemies who make noise (200 ¤) | **Barrier Mesh**: cross-shaped barrier that blocks the way (free) | **Annihilation**: traps the first enemy hit: they die after 7 s — **7 pts** |
| **Veto** | **Crosscut**: place a beacon (left click), then teleport to it (left click) (200 ¤) | **Chokehold**: trap that detains and makes vulnerable (200 ¤, max 2) | **Interceptor**: device that destroys nearby enemy utility (15 s) (free) | **Evolution**: 25 s: immune to effects, regeneration, speed and fire rate — **7 pts** |
| **Chamber** | **Trademark**: trap that slows and reveals enemies (200 ¤) | **Headhunter**: heavy pistol: one charge = one bullet (159 to the head) (100 ¤, max 8) | **Rendezvous**: place an anchor (left click), then teleport to it (left click, 25 blocks) (free, 30 s cooldown) | **Tour de Force**: sniper with a full-screen scope (right click): 5 lethal bullets, slows around kills — **8 pts** |
| **Vyse** | **Razorvine**: thorns that hurt and slow (150 ¤) | **Shear**: trap: a wall rises when an enemy walks by (200 ¤) | **Arc Rose**: place a rose (left click), then make it flash (left click) (free, 30 s cooldown) | **Steel Garden**: jams nearby enemies' primary weapons for 8 s — **8 pts** |

> **Miks** is an original Valocraft agent.

## Ability mechanics

- **Manual activation**: the key takes the ability in hand, **left click** uses it. `controls.instant-abilities: true` restores trigger-on-keypress.
- **Hold to throw**: for thrown abilities (grenades, Jett's smokes, Sova's bolts, Nanoswarm...), holding left click shows the **trajectory** (visible only to you), releasing throws. **Right click**: underhand lob, except for abilities that have a right-click variant.
- **Visible cooldown**: the signature icon stays in the hotbar with the cooldown sweep.
- **First-person piloting**: Sova's drone, Skye's tiger and Tejo's drone. You become the creature, your body stays behind and can be killed. Left click = action, right click = back to your body.
- **Anchor abilities** (Rendezvous, Gatecrash, Refract, Crosscut, Arc Rose): the first click places the anchor, the second uses it.
- **Tactical map** (Sky Smoke, Dark Cover, Orbital Strike, From the Shadows, Nebula, Ruse, Waveform, Guided Salvo...): a top-down map opens; WASD to aim, left click to place, right click to cancel.
- **Gauges** in the action bar: **Neon**'s energy (High Gear drains it, kills refill it), **Viper**'s fuel (active emitters consume it), **Jett**'s charged wind.
- **Destructible utility**: enemy bullets destroy the Turret (125 HP), Spycam (70), Leer and Interceptor (60), Sonic Sensor, Chokehold, Trademark and Shear (40), Alarmbot, Trapwire and Nanoswarm (20).

## Status effects

| Status | Effect | Caused by |
|---|---|---|
| **Concussed** | Slowed, view wobbles | Concussive abilities |
| **Blinded** | **White** screen that fades (flashes) or reduced vision | Flashes, Leer, Paranoia, Dizzy, Seekers |
| **Vulnerable** | +50% damage taken | Alarmbot, Snake Bite, Seize, Undercut... |
| **Detained** | No shooting, no abilities | Lockdown, Thrash, Chokehold |
| **Suppressed** | No abilities | ZERO/point, NULL/cmd, Stealth Drone |
| **Hindered** | Lower fire rate, slowed | Saturate, Convergent Paths |
| **Jammed** | Primary weapon unusable | Steel Garden |
| **Immune** | No negative effects | Evolution (Veto) |
| **Revealed** | Glowing outline visible through walls | Reveal abilities |
| **Intangible** | No damage | Dismiss, Dimensional Drift |

## Agent appearance

- **Full skin**: during the match, the player's whole skin becomes their agent's. The original skin comes back in the lobby (`agents.full-skin`).
- With the **SkinsRestorer** plugin, skins are signed: the player also sees their own agent skin (F5 view, arms). Without it, only other players see it.
- An agent's skin can be replaced with another skin image or a Minecraft username: `agents.skins.<agent>`.
- `agents.full-skin: false` brings back **agent heads** (`agents.wear-heads`).

## Smokes

Smokes and walls are opaque, tinted 3D models (orange for Brimstone), visible from afar. An enemy inside or behind a smoke is hidden at any distance; within 2.5 blocks, players see each other. Bullets go through smokes. Settings: `agents.smokes-hide-players`, `agents.solid-smokes`.

## Balancing

Abilities haven't been balanced in real matches yet: feedback is welcome. Values are tuned in `abilities.yml`, no recompiling.

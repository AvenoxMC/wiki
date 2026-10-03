# Changelog

## 2.2

### Match HUD

- Added a Valorant-style **Tab scoreboard** with aligned columns. It shows the map, round, phase, timer, score and sides. Teammates' credits, weapon, health/shield, K/D/A and ultimate status are visible. Enemy credits are shown as they were at the start of the buy phase; their weapon, health and ultimate are hidden, and dead enemies' names are struck through. The vanilla player list is hidden during a match. Disable it with `game.custom-tab: false`.

### Tactical ability targeting

- Brimstone's Sky Smoke and Orbital Strike, and Omen's Dark Cover and From the Shadows, now use a top-down tactical map with block rendering and terrain shading.
- The map displays sites, teammates, friendly smokes and walls, ability range and the target marker. Move the cursor with **WASD** (or **ZQSD** on AZERTY); sprint to move faster. Left click confirms; right click or sneak cancels. The player is stationary while targeting.
- Brimstone can place Sky Smokes in sequence while charges remain. Smokes drop from above and deploy on landing.
- Map bounds are calculated from spawns, sites, walls and orbs. Set them with `/vc map setminimap <map>` and the selection wand; `/vc map clearminimap <map>` restores automatic bounds. Set `agents.tactical-map: false` to use the previous targeting behavior.

### Smokes, walls and agent appearance

- Smokes and walls now use opaque, tinted 3D models that swell on appearance, remain visible at a distance and ignore the client's particle setting.
- Enemies inside or behind a smoke are hidden at any distance. Players within 2.5 blocks can see one another; allies and revealed enemies remain visible. Bullets still pass through smokes.
- Players wear their agent's head throughout the match, including enemies with hidden names. Gekko and Harbor use similar replacement heads. Settings: `agents.smokes-hide-players`, `agents.solid-smokes` and `agents.wear-heads`.

### Radianite, agents and weapon skins

- Added a Radianite balance and a lobby shop, also available with `/vc boutique`.
- Default match rewards: **150 ◆** for a win, **60 ◆** for a loss, **5 ◆** per elimination, **2 ◆** per assist, **5 ◆** per round won and **50 ◆** for MVP. Rewards and prices are configurable under `progression` in `config.yml`.
- Phoenix, Jett, Sova, Brimstone and Sage are free by default; each of the other ten agents costs **1,000 ◆**. Random agent assignment only selects agents the player has unlocked.
- Added six skin collections for all 18 weapons: **Prime**, **Reaver**, **Glitchpop**, **Ion**, **Elderflame** and **Oni**. Skins cost 1,000–2,000 ◆ and are bought and equipped per weapon. A picked-up weapon retains its owner's skin. Purchases have a confirmation step.
- Admin commands: `/vc radianite give|take|set <player> <amount>` and `/vc radianite voir <player>`. Permissions `valocraft.agents.all` and `valocraft.skins.all` unlock all agents and skins.

### Weapons and controls

- Replaced the flickering pumpkin-helmet sniper scope with a fullscreen 16:9 scope: clear round lens, dark surround, fine reticle and red dot. Other players continue to see the agent head.
- Holding left click while targeting a block within **64 blocks** sends a firing signal each tick, allowing weapons to fire at their actual rate. Nothing is mined, no cracks are shown to other players, and the arm-swing animation is hidden. A single click still fires one bullet; semi-automatic weapons also fire at their maximum rate while held. Looking at the sky with no block within range still requires a click. Knife range remains 3 blocks.
- Settings: `controls.continuous-fire`, `controls.semi-auto-hold` and `controls.hide-swing`.

### Verification

Tested on Paper 1.21.4 with two test clients connected in a match. Continuous fire emptied a Classic magazine from 12 to 1 in 1.5 seconds; a single click fired one bullet. The tactical map placed a smoke at the selected point; players concealed by smoke disappeared from one another's screens; Tab showed both teams; agent heads and sniper scopes were checked. Radianite awarded 210 to the winner and 60 to the loser. No console errors were reported.

## 2.1 — Agent Update

### Agents and abilities

- Expanded the roster to **15 agents**: Jett, Phoenix, Raze, Reyna, Neon, Sova, Skye, Gekko, Brimstone, Omen, Viper, Harbor, Sage, Killjoy and Cypher.
- Added a **25-second agent selection** after the countdown. Agents are unique per team; players who do not choose receive a random available agent. The menu displays role, abilities, prices and ultimate cost. Agent voice lines play to the team on lock-in.
- Added status effects: concussed, blinded, vulnerable (+50% damage taken), immobilized, revealed and intangible.
- Ability slots use **5 / 6 / 7 / 8** for **C / Q / E / X**. Instant abilities activate on key press; other abilities are cast with left click, with right-click variants where available. Guided abilities follow the player's view; Jett glides while jump is held.

### Ultimate system

- Ultimate points come from eliminations, deaths, spike plants and defuses, and ultimate orbs. Points persist through halftime. Progress is displayed in the action bar; ready and activation notifications are shown to the player and team.
- Ultimate orbs respawn each round. Hold right click beside an orb for 1.5 seconds to gain one point. Add and clear map orbs with `/vc map addorb <map>` and `/vc map clearorbs <map>`.

### Match, weapons and server tools

- Added rideable ziplines: create them with `/vc map addzipline <map>` between the two wand-selection points. Press **F** to attach, use forward/back to move, and jump or sneak to detach.
- Added lobby matchmaking, host-created games, player statistics and leaderboards.
- Added 11 Valocraft 3D weapon models: Shorty, Frenzy, Stinger, Bucky, Judge, Bulldog, Guardian, Phantom, Marshal, Outlaw and Odin. Left click fires and held right click aims. Recoil now affects the bullet path, preventing the view from snapping back during bursts.
- The resource pack is served on the Minecraft port, works with Pterodactyl and updates with the plugin. Added `/vc pack send`, `/vc pack remove`, `/vc pack info` and `/vc pack reload` (including admin targets).
- Added map import from ommo.me with `/vc import` for private servers (CC BY-NC-ND 4.0).

### Minecraft adaptations

Smokes are particle-based and blind players inside them; flashes produce black rather than white vision; revealed-enemy outlines are visible to everyone. Ability balance and pricing may need adjustment in live matches.

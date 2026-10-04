# Gameplay


Valocraft follows Valorant's spike mode: attackers plant the spike, defenders stop them. Other rules exist depending on the [game mode](page:modes).

## Match flow (Unrated / Competitive)

1. **Waiting room in the lobby**, team choice, countdown.
2. **Agent select (25 s)**, then a **loading screen** while the map loads ([Lobby](page:lobby)).
3. **Buy phase**: open the shop with `F`. Pre-round walls keep teams in their spawn.
4. **Round** (100 s): attackers plant, defenders hold or defuse.
5. **Next round**. Sides swap after **12 rounds**. First to **13** wins.
6. **Overtime**: start with 5000 credits, win by **2 rounds**.

## Spike

| Action | Duration |
|---|---|
| Plant | 4 s (hold right click with the spike on a site, stand still) |
| Defuse | 7 s (hold right click on the spike, stand still). Half of the progress is kept. |
| Detonation | 45 s after the plant |

Drop the spike or a weapon: **Sneak + Q**.

## Economy

Valorant-style economy (¤ credits): weapons, shield and ability charges are bought in the shop during the buy phase. Charges are in the bottom row; your agent's **signature (E)** is free every round.

**Weapon requests**: in the shop, clicking a weapon you can't afford asks your team for it. A teammate who has the money clicks **[Buy for …]**: they pay and the weapon goes into your inventory (your old weapon is dropped on the ground).

## Health and HUD

- **Hearts** = HP (100 HP = 10 hearts). **Golden hearts** = shield.
- **XP bar**: level = bullets in the magazine, bar = magazine / reload progress.
- **Action bar**: HP, ammo, credits, ultimate progress (`X ●●●○○○`) and agent gauges (Neon's energy, Viper's fuel...).
- **Radar**: a map in the off-hand shows allies, spotted enemies, the spike, the sites and your team's smokes (`game.radar`).

## Scoreboard (Tab)

Press **Tab** to see the map, round, phase, time, score and sides, with players aligned in columns. Allies: credits, weapon in hand, HP/shield, K/D/A and ultimate. Enemies: credits at the start of the buy phase, K/D/A and **ult points** (red when the ult is ready). Dead enemies' names are struck through. `game.custom-tab: false` turns this scoreboard off.

## End of round and match

- **First blood** and **ACE** announcements.
- **Damage report** in chat on death and at the end of the round.
- **Kill banner and kill sound** on each kill ([Progression and Cosmetics](page:progression)).
- End of match: ranking, **Match summary** menu (`/vc resume`), Radianite, battle pass XP and RR in Competitive.

## Reconnect, votes and AFK

- **Reconnect**: a player who disconnects mid-match keeps their slot for 3 minutes and is put back in on return.
- **Surrender**: `/vc ff`, from round 5, 80% yes.
- **Remake**: `/vc remake`, until round 3, if a teammate left; everyone must vote yes.
- **AFK**: warning after 45 s of inactivity, kicked at 90 s.

## Movement and sound

- **Sprinting is disabled**, like in Valorant; walking speed is boosted (`player.speed-bonus`).
- Stopping or crouching before shooting makes shots accurate. Running or jumping makes them inaccurate.
- **Footsteps**: running is heard by enemies (sound depends on the block); crouch-walking is silent.
- [Ziplines](page:ziplines) can be used on maps that have them.

## Pre-round walls

Walls are placed during the buy phase and removed when the round starts. They only fill **empty** blocks and are restored exactly: the map is never damaged.

## See also

- [Game Modes](page:modes)
- [Controls](page:controls)
- [Agents](page:agents)
- [Weapons](page:weapons)

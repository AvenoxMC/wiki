# Gameplay


Valocraft follows Valorant's spike mode: attackers plant the spike, defenders stop them.

## Match flow

1. **Lobby / waiting room**: players join a map and pick a team.
2. **Countdown**, then the **agent select phase (25 s)**.
3. **Buy phase**: open the shop with `F`. Pre-round walls hold teams at their spawn.
4. **Round** (100 s): attackers plant, defenders defend or defuse.
5. **Next round**. Sides swap after **12 rounds**. First to **13** wins.
6. **Overtime**: starts with 5000 credits, win by **2 rounds**.

## Spike

| Action | Time |
|---|---|
| Plant | 4 s (hold right click with the spike on a site, stay still) |
| Defuse | 7 s (hold right click on the spike, stay still). Half progress is kept. |
| Detonation | 45 s after planting |

Drop the spike or a weapon with **Sneak + Q**.

## Economy

Valocraft uses a Valorant-style economy (¤ credits). Weapons and ability charges are bought in the shop during the buy phase. Ability charges are on the bottom row of the shop; your agent's **signature (E)** is granted every round.

## Health and HUD

- **Hearts** = HP (100 HP = 10 hearts). **Golden hearts** = shield.
- **XP bar**: level = bullets in the magazine, bar = magazine / reload progress.
- **Action bar**: ultimate progress (`X ●●●○○○`).

## Scoreboard (Tab)

Press **Tab** during a match to see the map, round, phase, remaining time, score and sides, plus a column-aligned roster. Teammates' entries show their credits, held weapon, health/shield, K/D/A and ultimate status. Enemy credits show their balance at the start of the buy phase; enemy weapon, health and ultimate are hidden. Dead enemies' names are struck through. The vanilla player list is hidden during a match. Set `game.custom-tab: false` to disable the custom scoreboard.

## Movement

- **Sprint is disabled**, as in Valorant. Walking speed is raised (`player.speed-bonus` in `config.yml`) to match Valorant's run speed.
- Standing still or crouching before shooting gives an accurate shot. Running or jumping makes it inaccurate.
- You can use [ziplines](page:ziplines) on maps that have them.

## Pre-round walls

Walls are placed during the buy phase and removed at round start. They only fill **empty** blocks and are restored exactly, so the map is never damaged.

## Related

- [Controls](page:controls)
- [Agents](page:agents)
- [Ultimate System](page:ultimate)
- [Weapons](page:weapons)

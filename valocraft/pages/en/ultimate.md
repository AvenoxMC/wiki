# Ultimate System


Every agent has an ultimate on key **8** (X). It costs a number of **ult points** (6 to 9 depending on the agent, listed on the [Agents](page:agents) page and editable in `abilities.yml`).

## Earning points

- **Kills**
- **Deaths**
- **Planting** and **defusing** the spike
- **Ult orbs** (see below)
- In Spike Rush: +1 point per round

Points are **kept at half-time**.

## Visual and audio feedback

| Moment | What happens |
|---|---|
| Progress | Always shown in the action bar (`X ●●●○○○`). Key **8** shows the ultimate with its points. |
| **Ult ready** | On-screen title, sound, and a message to your team. **Enemies** get a chat alert. |
| **Ult used** | Everyone hears the agent's voice line and chat announces it. |
| Scoreboard | Ult points of allies **and enemies** are visible (red when an enemy ult is ready). |

## Using the ultimate

Key **8** to take it in hand, **left click** to activate it ([manual activation](page:controls)).

Some ultimates turn key 8 into a weapon while active: Blade Storm, Hunter's Fury, Showstopper, Overdrive, Tour de Force (with a right-click scope). **Blade Storm**, **Overdrive** and **Empress** are extended or refilled by kills. **Not Dead Yet** (Clove) triggers by itself on death.

## Ult orbs

Orbs are a map element placed by admins.

- **Place**: `/vc map addorb <map>` where you stand.
- **Remove all**: `/vc map clearorbs <map>`.
- **Respawn**: orbs come back **every round** (and in Team Deathmatch).
- **Collect**: **hold right click for 1.5 s** next to an orb to gain **+1 ult point**.

## Admin commands

| Command | Effect |
|---|---|
| `/vc ult add <player> [points]` | Adds points (1 by default) |
| `/vc ult set <player> [points]` | Sets points; without a number, the ult is full (with the "ult ready" alerts) |

See [Map Setup](page:map-setup) to place orbs.

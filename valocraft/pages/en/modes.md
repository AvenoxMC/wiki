# Game Modes


The host picks the mode when creating the game ("Create a game" menu) or in the waiting room. An admin sets a map's default mode with `/vc map setmode <map> <mode>`. Each mode's settings live in the `modes` section of `config.yml`.

## The 8 modes

| Mode | Key | Rules |
|---|---|---|
| **Unrated** | `unrated` | First to 13 rounds, side swap after 12, economy, spike, overtime. |
| **Competitive** | `competitive` | Like Unrated, with rank and RR. Leaving costs RR. |
| **Swiftplay** | `swiftplay` | First to **5 rounds**, side swap after 4, economy and spike, no overtime. |
| **Replication** | `replication` | During agent select, everyone votes for an agent (duplicates allowed); **the whole team plays the most-picked agent**. First to 5 rounds. |
| **Spike Rush** | `spike_rush` | First to 4 rounds (swap after 3). Same random weapon for everyone, shield, full abilities, +1 ult point per round, every attacker carries a spike. |
| **Deathmatch** | `deathmatch` | Free-for-all, no agents. 1.5 s respawn, free weapons for 10 s after respawning, a kill heals you. 40 kills or 6 minutes. |
| **Team Deathmatch** | `team_deathmatch` | Two teams with agents, 2 s respawn, free weapons, ult orbs. 100 kills or 9:30. |
| **Escalation** | `escalation` | Two teams, respawns, no abilities: each level forces a weapon (see below). |

## Escalation

- Default weapon order: Odin, Ares, Phantom, Vandal, Spectre, Judge, Bulldog, Guardian, Sheriff, Marshal, Operator, then the **knife**.
- A team needs **3 kills** to reach the next level (`kills-per-level`); on the last level, **a single knife kill** is enough.
- The whole team switches weapon at once. No shop.
- The first team to finish the last level wins; otherwise, after 10 minutes, the furthest team wins.
- The boss bar and the sidebar show each team's level.

```yaml
modes:
  escalation:
    time-limit: 600
    kills-per-level: 3
    levels: [odin, ares, phantom, vandal, spectre, judge, bulldog, guardian, sheriff, marshal, operator, knife]
```

## Respawn modes

Deathmatch, Team Deathmatch and Escalation: 2 s of spawn protection (unless you shoot), spawn point picked as far as possible from enemies. A spray is available every 30 s.

## Competitive

- Ranks: Iron, Bronze, Silver, Gold, Platinum, Diamond, Ascendant and Immortal (3 divisions each), then Radiant.
- **5 placement games**, then RR based on the result (+20 / -16), performance (combat score) and the team level gap. Leaving costs -30 RR.
- A game started with `/vc forcestart` doesn't count for ranked.

See also [Progression and Cosmetics](page:progression).

# Players

## Queue and direct challenges

| Item or command | Action |
|---|---|
| “Play” sword / `/queue` | Open the mode menu; click a kit to join its queue. |
| `/duel <player> [kit] [arena]` | Challenge a player directly. Choose a kit and arena, then they can accept or refuse with clickable chat options. |
| Compass / `/spectate [player]` | Browse active matches and spectate, optionally targeting a player. |
| `/stats [player]` | View wins, losses, kills and deaths. |
| `/leave` | Leave a queue, forfeit a match or stop spectating. |

## Parties

Use the “Create Party” name tag or `/party` to open the party menu.

| Command | Action |
|---|---|
| `/party invite <player>` | Invite a player (clickable message). |
| `/party accept <leader>` | Accept a leader's invitation. |
| `/party open` | Make the party public. |
| `/party chat <message>` or `@message` | Send a party-chat message. |

The party leader starts a game from the menu:

- **FFA**: every player fights for themselves.
- **Teams**: the party is split into two random teams.
- **Challenge a party**: play party versus party; the other party leader accepts.

## Lobby

Use the bed or `/lobby` (`/hub`) to leave a match and return to the lobby. If `lobby-server` is set in `config.yml`, the player is sent to that server (for example, `lobby1`); otherwise they return to the Duels lobby.

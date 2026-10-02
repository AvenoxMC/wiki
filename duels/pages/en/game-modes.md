# Game Modes

## Duel

Arenas of type `duel` host combat matches with the selected kit. A queue match requires a compatible, enabled arena with at least two spawns. Arenas can be restricted to specific kits; see [Arenas](page:arenas).

## Guess! (mastermind)

**Guess!** is a non-combat 1v1 mode played with the automatically created `devine` kit on arenas of type `devine`.

1. Roles are assigned randomly. The **code maker** chooses a secret ordered combination of **four wool colors** within 30 seconds. If time runs out, the combination is completed randomly.
2. The **guesser** has **two minutes** to find the code. They compose attempts in the menu using the “Combination” item, or let it fill automatically, then submit.
3. Each color gets a clue: **green** means the correct color and position; **orange** means the color is present but in another position; **red** means the color is absent.
4. The guesser wins by finding the code in time; otherwise the code maker wins. Forfeit or disconnect awards the win to the other player.

Attempt history is shown on the map board (four wool blocks, a divider and four clue blocks per row), in the menu (the last three attempts), and in chat. The secret combination is revealed at the top of the board when the game ends.

## Create a Guess! arena

```text
/arena create guess devine                 Create a new mastermind arena
/arena addspawn guess                      Repeat for both players
/arena setboard guess                      Face the wall and target the board's bottom-left block
/arena save guess
```

The board is 9 blocks wide and 9 high: eight attempt rows plus the secret combination. It extends right and upward from the targeted block. Existing arenas are type `duel`; change one with `/arena set <name> type devine`. Set a kit's mode with `/dkit set <kit> mode devine`.

The `devine` section in `config.yml` controls selection and guessing time, maximum attempts, allowed colors, duplicate colors, board row count and board blocks.

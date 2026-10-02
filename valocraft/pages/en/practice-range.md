# Practice Range


Outside a match, a weapon obtained with `/vc give` can be fired at **mobs and armor stands**. It never shoots players.

Each hit displays:

- The **zone** hit
- The **damage** dealt
- The **distance**

This is the easiest way to tune `weapons.yml` before opening a match.

## Usage

```
/vc give <weapon> [player]
```

Shoot at mobs or armor stands, adjust `weapons.yml`, then `/vc reload`.

## Disabling

Set `weapons.practice-mode` to disable it in `config.yml`. See [Configuration](page:configuration).

Related: [Weapons](page:weapons).

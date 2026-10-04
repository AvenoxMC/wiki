# Development


## Building from source

Requirements: **Java 21** and **Maven**.

```bash
mvn package
```

The jar is in `target/Valocraft-2.2.jar` (the `resourcepack/valocraft-pack.zip` pack is bundled inside).

## Where to change what

| What | Where |
|---|---|
| Ability prices, charges, cooldowns, damage, ult costs | `abilities.yml` (no recompiling) |
| Ability behaviour | `agent/Kits.java`, `agent/NewKits.java`, engine in `agent/AbilityManager.java` |
| Agent and ability list | `agent/Agent.java`, `agent/AbilityType.java` |
| Weapon stats | `weapons.yml` (no recompiling) |
| General settings | `config.yml` (no recompiling) |
| Game modes | `game/Mode.java`, `game/Game.java` |
| Cosmetics (kill banners, sounds, sprays) | `cosmetic/` |
| Battle pass, progression | `stats/BattlePass.java`, `stats/Progression.java` |
| Map world loading | `map/MapWorlds.java` |
| Weapon models | `resourcepack/valocraft-models/`, `resourcepack/ModelGenerator.java` |
| Generated resources (scope, flashes, smokes, skins, icons) | `resourcepack/PackGenerator22.java` |

## Pack resources

`PackGenerator22.java` generates Valocraft's textures and models into `resourcepack/valocraft-models/` (scope, flash overlays, smokes, scoreboard font, 108 weapon skins) and rebuilds the ability icon table from the images present. Then:

```bash
cd resourcepack
java PackGenerator22.java valocraft-pack.zip valocraft-models
jar uf valocraft-pack.zip -C valocraft-models assets
```

Then rebuild the plugin. Valocraft weapon models open in **Blockbench** (Java Block/Item format).

## Optional integrations

- **SkinsRestorer**: called through reflection (`agent/SkinsRestorerHook.java`), no compile-time dependency. Declared as `softdepend`.

## Contributing

- Open an **issue** for bugs and balance feedback (agent, ability, situation).
- Pull requests are welcome.

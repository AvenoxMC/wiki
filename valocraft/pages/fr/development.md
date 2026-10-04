# Développement


## Compiler depuis les sources

Prérequis : **Java 21** et **Maven**.

```bash
mvn package
```

Le jar se trouve dans `target/Valocraft-2.2.jar` (le pack `resourcepack/valocraft-pack.zip` est embarqué dedans).

## Où modifier quoi

| Quoi | Où |
|---|---|
| Prix, charges, recharges, dégâts des capacités, coût des ultimes | `abilities.yml` (sans recompiler) |
| Comportement des capacités | `agent/Kits.java`, `agent/NewKits.java`, moteur dans `agent/AbilityManager.java` |
| Liste des agents et capacités | `agent/Agent.java`, `agent/AbilityType.java` |
| Statistiques des armes | `weapons.yml` (sans recompiler) |
| Réglages généraux | `config.yml` (sans recompiler) |
| Modes de jeu | `game/Mode.java`, `game/Game.java` |
| Cosmétiques (bannières, sons, sprays) | `cosmetic/` |
| Battle pass, progression | `stats/BattlePass.java`, `stats/Progression.java` |
| Chargement des mondes de maps | `map/MapWorlds.java` |
| Modèles d'armes | `resourcepack/valocraft-models/`, `resourcepack/ModelGenerator.java` |
| Ressources générées (lunette, flashs, fumées, skins, icônes) | `resourcepack/PackGenerator22.java` |

## Ressources du pack

`PackGenerator22.java` génère les textures et modèles Valocraft dans `resourcepack/valocraft-models/` (lunette, overlays de flash, fumées, police du tableau, 108 skins d'armes) et reconstruit la table des icônes de capacités à partir des images présentes. Ensuite :

```bash
cd resourcepack
java PackGenerator22.java valocraft-pack.zip valocraft-models
jar uf valocraft-pack.zip -C valocraft-models assets
```

Puis recompiler le plugin. Les modèles d'armes Valocraft s'ouvrent dans **Blockbench** (format Java Block/Item).

## Intégrations optionnelles

- **SkinsRestorer** : appelé par réflexion (`agent/SkinsRestorerHook.java`), aucune dépendance de compilation. Déclaré en `softdepend`.

## Contribuer

- Ouvrir une **issue** pour les bugs et les retours d'équilibrage (agent, capacité, situation).
- Les pull requests sont les bienvenues.

# Développement


## Compiler depuis les sources

Prérequis : **Java 21** et **Maven**.

```bash
mvn package
```

Le jar se trouve dans `target/Valocraft-2.1.jar`.

## Où modifier quoi

| Quoi | Où |
|---|---|
| Dégâts, durées et prix des capacités | `AbilityType.java` et `Kits.java` |
| Statistiques des armes | `weapons.yml` (sans recompiler) |
| Réglages généraux | `config.yml` (sans recompiler) |
| Modèles d'armes | `resourcepack/valocraft-models/` |
| Générateur de modèles | `resourcepack/ModelGenerator.java` |
| Aperçu des modèles | `resourcepack/apercu-armes.png` |

## Modèles d'armes

Les modèles Valocraft (Shorty, Frenzy, Stinger, Bucky, Judge, Bulldog, Guardian, Phantom, Marshal, Outlaw, Odin) sont générés par `resourcepack/ModelGenerator.java` dans `resourcepack/valocraft-models/`. Ils utilisent le composant `item_model` (`valocraft:<arme>`).

Pour retoucher un modèle, l'ouvrir dans **Blockbench** (format Java Block/Item).

## Pack de textures

Le pack HrdaValorant est embarqué dans le jar et extrait dans `plugins/Valocraft/resourcepack.zip` au premier démarrage. Voir [Pack de textures](page:resource-pack).

## Contribuer

- Ouvrir une **issue** pour les bugs et les retours d'équilibrage. Les capacités n'ont pas encore été équilibrées en partie réelle : un rapport avec du contexte (agent, capacité, situation) est très utile.
- Les pull requests sont les bienvenues.

# Installation

## Prérequis

| Prérequis | Détails |
|---|---|
| Serveur | Spigot 1.8.8 |
| Java | Version compatible avec votre serveur Spigot 1.8.8 |
| Jar du plugin | `target/Duels.jar` |

## Installer

1. Copier `target/Duels.jar` dans le dossier `plugins/` du serveur.
2. Démarrer le serveur.
3. Se placer à l'emplacement du lobby et lancer `/duels setlobby`.
4. Créer au moins une arène. Cinq kits d'exemple sont créés automatiquement : `nodebuff`, `builduhc`, `sumo`, `combo` et `archer`.

> Le plugin est prévu pour un serveur de duels ou un lobby dédié. À la connexion, l'inventaire du joueur est vidé et remplacé par les objets du lobby.

## Compiler depuis les sources

Installer Maven puis lancer :

```bash
mvn package
```

Le jar est produit dans `target/Duels.jar`. Autre possibilité : compiler avec `javac` contre `spigot-api-1.8.8-R0.1-SNAPSHOT.jar`.

## Pour commencer

- [Créer une arène](page:arenas)
- [Configurer les kits](page:kits)
- [Commandes joueur](page:players)

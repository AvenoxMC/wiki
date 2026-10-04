# Installation


## Prérequis

| | |
|---|---|
| **Serveur** | Paper 1.21.4 ou plus récent |
| **Java** | 21 |
| **Dépendances** | Aucune obligatoire |
| **Optionnel** | [SkinsRestorer](https://github.com/SkinsRestorer/SkinsRestorer) : skins d'agents signés, visibles aussi par le joueur lui-même |
| **Pack de textures** | Embarqué dans le jar, envoyé automatiquement |

## Nouvelle installation

1. Placer `Valocraft-2.2.jar` dans le dossier `plugins/` du serveur (et SkinsRestorer si tu le veux).
2. Démarrer le serveur. Le pack de textures est extrait dans `plugins/Valocraft/resourcepack.zip` au premier démarrage, et `abilities.yml` est créé.
3. Se placer à l'endroit voulu pour le lobby et faire `/vc setlobby`.
4. [Créer une map](page:map-setup) ou [en importer une](page:importing-maps), puis `/vc map enable <id>`.
5. Optionnel : poser des [classements](page:progression) dans le lobby avec `/vc leaderboard set <type>`.

## Mise à jour

- Depuis une **2.x** : remplacer l'ancien jar par `Valocraft-2.2.jar` dans `plugins/`. Les joueurs reçoivent automatiquement le pack mis à jour. Les nouvelles options sont ajoutées à `config.yml` au démarrage.
- Depuis la **1.x** : la 2.x est une réécriture complète qui ne partage rien avec la 1.x. Retirer l'ancien plugin et ses données, et repartir de zéro.

## Mondes des maps

Les mondes des maps (`vc_<map>`) **ne sont plus chargés au démarrage du serveur**. Ils restent sur le disque et sont chargés au lancement d'une partie, puis déchargés quand plus personne ne les utilise. Une map construite dans le monde principal (`world`) reste chargée en permanence. Voir [Création de map](page:map-setup).

## Pack de textures

Rien à configurer par défaut. Le pack (HrdaValorant, modèles Valocraft) est servi **sur le port Minecraft lui-même** et envoyé à chaque joueur à la connexion. Le lien reprend l'adresse et le port utilisés par le joueur pour se connecter : aucun port supplémentaire à ouvrir, et ça fonctionne aussi sur Pterodactyl.

Voir [Pack de textures](page:resource-pack) pour les alternatives et le dépannage.

## SkinsRestorer (optionnel)

Avec SkinsRestorer, les skins d'agents sont signés par MineSkin au démarrage (en arrière-plan, un toutes les 3 s), puis gardés dans `plugins/Valocraft/data/agent-skins.yml`. Le serveur doit avoir accès à Internet au premier démarrage. Sans SkinsRestorer, les autres joueurs voient quand même le skin de l'agent ; seul le joueur lui-même garde son skin en vue F5.

## Étapes suivantes

- [Lobby et matchmaking](page:lobby)
- [Création de map](page:map-setup)
- [Commandes et permissions](page:commands)

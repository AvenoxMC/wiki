# Installation


## Prérequis

| | |
|---|---|
| **Serveur** | Paper 1.21.4 ou plus récent |
| **Java** | 21 |
| **Dépendances** | Aucune (autonome) |
| **Pack de textures** | Embarqué dans le jar, envoyé automatiquement |

## Nouvelle installation

1. Placer `Valocraft-2.2.jar` dans le dossier `plugins/` du serveur.
2. Démarrer le serveur. Le pack de textures est extrait dans `plugins/Valocraft/resourcepack.zip` au premier démarrage.
3. Se placer à l'endroit voulu pour le lobby et faire `/vc setlobby`.
4. [Créer une map](page:map-setup) ou [en importer une](page:importing-maps), puis `/vc map enable <id>`.

## Mise à jour

- Depuis la **2.1** : remplacer `Valocraft-2.1.jar` par `Valocraft-2.2.jar` dans `plugins/`. Les joueurs reçoivent automatiquement le pack mis à jour, avec les nouveaux modèles et textures d'armes.
- Depuis la **2.0.0** : remplacer l'ancien jar par `Valocraft-2.2.jar`. Les joueurs reçoivent automatiquement le pack mis à jour.
- Depuis la **1.x** : la 2.x est une réécriture complète qui ne partage rien avec la 1.x. Retirer l'ancien plugin et ses données, et repartir de zéro.

## Pack de textures

Rien à configurer par défaut. Le pack (HrdaValorant, son du Classic corrigé) est servi **sur le port Minecraft lui-même** et envoyé à chaque joueur à la connexion. Le lien reprend l'adresse et le port utilisés par le joueur pour se connecter : aucun port supplémentaire à ouvrir, et ça fonctionne aussi sur Pterodactyl.

Voir [Pack de textures](page:resource-pack) pour les alternatives et le dépannage.

## Étapes suivantes

- [Lobby et matchmaking](page:lobby)
- [Création de map](page:map-setup)
- [Commandes et permissions](page:commands)

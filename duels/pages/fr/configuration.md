# Configuration

Les fichiers de configuration se trouvent dans `plugins/Duels/`.

## Fichiers

| Fichier | Contenu |
|---|---|
| `config.yml` | Lobby, objets du lobby, mondes, règles de match, parties et réglages des fonctionnalités. |
| `messages.yml` | Tous les messages du plugin, en français par défaut, avec les codes couleur `&`. |
| `kits.yml` | Définition des kits, également modifiable avec `/dkit`. |
| `arenas.yml` | Définition des arènes, écrite par les commandes d'arène. |
| `lobby.yml` | Position du lobby. |
| `stats.yml` | Statistiques des joueurs. |
| `schematics/` | Schématiques recherchées par le plugin. |

## Réglages principaux

| Réglage | Rôle |
|---|---|
| `lobby-server` | Serveur de destination avec `/lobby` ou `/hub` ; vide, le joueur revient au lobby Duels. |
| `worlds.max-loaded-instances` | Nombre maximal total d'instances de match chargées sur le serveur. |
| `max-instances` d'une arène | Nombre maximal de copies simultanées pour une arène. |
| `schematics.folders` | Dossiers parcourus pour trouver des schématiques. |
| `schematics.paste-y` | Coordonnée Y de centrage d'une map collée (64 par défaut). |
| `schematics.ms-per-tick` | Limite le travail d'écriture des blocs par tick pour réduire les ralentissements. |
| `devine` | Temps, nombre d'essais, couleurs, doublons et disposition du tableau du mode Devine ! |

Lancer `/duels reload` après modification de la configuration ou de `kits.yml` à la main.

## Permission admin

`duels.admin` est accordée aux opérateurs par défaut. Elle donne accès à `/arena`, `/dkit`, `/duels setlobby`, `/duels reload`, à la construction en créatif au lobby et aux commandes admin pendant un match. Voir [Arènes](page:arenas), [Kits](page:kits) et [Schématiques](page:schematics) pour les commandes.

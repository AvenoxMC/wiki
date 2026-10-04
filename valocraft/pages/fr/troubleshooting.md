# Dépannage


## Le pack de textures ne se charge pas

1. Regarder la **console du serveur** : elle indique le lien proposé à chaque joueur et la réponse du client (`ACCEPTED`, `DECLINED`, `FAILED_DOWNLOAD`, `SUCCESSFULLY_LOADED`...).
2. Demander au joueur de refaire `/vc pack send`.
3. Admins : `/vc pack info` affiche le mode et le lien, `/vc pack reload` le recharge.
4. Si l'hébergement sur le port Minecraft ne fonctionne pas chez vous, utiliser un port dédié (`resource-pack.self-host.http-port: 8164`) ou une URL externe. Voir [Pack de textures](page:resource-pack).

## Une icône de capacité affiche le mauvais agent

Mettre à jour le plugin : le pack corrigé (icônes de Cove, Trademark / Rendezvous, FRAG/ment / FLASH/drive) est envoyé automatiquement. Si l'ancien pack reste en cache, faire `/vc pack send`.

## Ma map ne démarre pas / n'est pas jouable

Faire `/vc map info <id>` : la commande liste ce qui manque (salle d'attente, spawns, sites, murs, limites de joueurs, activation). Voir [Création de map](page:map-setup).

## « Monde de la map introuvable »

Le dossier du monde (`vc_<map>`) n'existe plus à côté du serveur, ou le nom de monde enregistré dans `maps/<id>.yml` (clé `world`) est faux. Les mondes ne sont plus chargés au démarrage : c'est normal de ne pas les voir dans `/mv list` ou équivalent tant qu'aucune partie n'est lancée.

## Je ne vois pas mon propre skin d'agent en F5

Minecraft n'accepte pour soi-même que des skins signés par Mojang. Les autres joueurs voient bien ton skin d'agent. Installer **SkinsRestorer** : les skins sont alors signés via MineSkin et visibles par tout le monde ([Installation](page:installation)). Le serveur doit avoir accès à Internet au premier démarrage.

## Une partie lancée seule se termine tout de suite

Utiliser `/vc forcestart` (et non `/vc start`) : une équipe vide n'est alors jamais considérée comme éliminée.

## Ma capacité ne part pas quand j'appuie sur la touche

C'est normal : la touche prend la capacité en main, le **clic gauche** l'utilise. Pour l'ancien comportement : `controls.instant-abilities: true` ([Contrôles](page:controls)).

## Une map importée est refusée

La map a été sauvegardée dans une **version de Minecraft plus récente** que le serveur. Lotus, Sunset et Breeze demandent **Minecraft 1.21.11**. Voir [Import de maps](page:importing-maps).

## Le tir ne continue pas quand je maintiens le clic gauche

Le tir continu nécessite de viser un bloc à **64 blocs** ou moins. En visant le ciel, il faut cliquer. Vérifier `controls.continuous-fire` et `controls.semi-auto-hold` ([Contrôles](page:controls)).

## Je ne peux ni tirer ni utiliser de capacités

Tu es peut-être **immobilisé**, **supprimé** ou **bloqué** (Lockdown, Thrash, ZERO/point, Steel Garden...), ou en train de piloter un drone. Voir le tableau des états sur [Agents](page:agents).

## Un joueur a été exclu de la partie

L'anti-AFK exclut un joueur qui ne bouge pas pendant 90 s (`afk.kick-after`). Un joueur déconnecté a 3 min pour revenir (`reconnect.timeout`).

## Des joueurs ont perdu leurs objets après un crash

Les inventaires sauvegardés pendant une partie sont dans `plugins/Valocraft/playerdata/` et **rendus à la reconnexion**. Les blocs temporaires (murs, spike, capacités) sont restaurés au prochain chargement du monde de la map.

## J'ai mis à jour et quelque chose cloche

- Ne garder que `Valocraft-2.2.jar` dans `plugins/`. Voir [Installation](page:installation).
- Valocraft **1.x** n'est pas compatible avec la 2.x.

## Toujours bloqué ?

Ouvrir une issue sur ce dépôt avec la version du serveur, la version de Valocraft et la partie utile de la console.

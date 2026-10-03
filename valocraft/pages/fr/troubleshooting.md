# Dépannage


## Le pack de textures ne se charge pas

1. Regarder la **console du serveur** : elle indique le lien proposé à chaque joueur et la réponse du client (`ACCEPTED`, `DECLINED`, `FAILED_DOWNLOAD`, `SUCCESSFULLY_LOADED`...).
2. Demander au joueur de refaire `/vc pack send` pour le recevoir à nouveau.
3. Admins : `/vc pack info` affiche le mode et le lien, `/vc pack reload` le recharge.
4. Si l'hébergement sur le port Minecraft ne fonctionne pas chez vous, utiliser un port dédié (`resource-pack.self-host.http-port: 8164`) ou une URL externe. Voir [Pack de textures](page:resource-pack).

## Ma map ne démarre pas / n'est pas jouable

Faire `/vc map info <id>` : la commande liste ce qui manque (salle d'attente, spawns, sites, murs, limites de joueurs, activation). Voir [Création de map](page:map-setup).

## Une map importée est refusée

La map a été sauvegardée dans une **version de Minecraft plus récente** que le serveur. Lotus, Sunset et Breeze demandent **Minecraft 1.21.11**. Voir [Import de maps](page:importing-maps).

## Les armes automatiques tirent lentement

Minecraft envoie **un signal par clic gauche** : avec le tir au clic gauche, les armes automatiques tirent donc au rythme des clics. Pour un tir en maintenant le bouton, mettre `controls.fire-button: RIGHT` dans `config.yml`. Voir [Contrôles](page:controls).

## Mon écran « revient en arrière » pendant les rafales

Corrigé dans la **2.1** : le recul ne déplace plus la caméra et est appliqué entièrement à la trajectoire des balles. Mettre à jour en 2.1. Voir [Armes](page:weapons).

## Je ne peux ni tirer ni utiliser de capacités

Tu es peut-être **immobilisé** (Lockdown ou Thrash). Voir le tableau des états sur [Agents](page:agents).

## Des joueurs ont perdu leurs objets après un crash

Les inventaires sauvegardés pendant une partie sont dans `plugins/Valocraft/playerdata/` et **rendus à la reconnexion**. Les blocs temporaires (murs, spike) de `plugins/Valocraft/data/` sont restaurés automatiquement.

## J'ai mis à jour et quelque chose cloche

- Retirer l'ancien jar du plugin pour ne garder que `Valocraft-2.2.jar` dans `plugins/`. Voir [Installation](page:installation).
- Valocraft **1.x** n'est pas compatible avec la 2.x.

## Le tir ne continue pas quand je maintiens le clic gauche

Le tir continu nécessite de viser un bloc à **64 blocs** ou moins. Si tu vises le ciel ou qu'aucun bloc n'est à portée, clique pour tirer une seule balle. Vérifie `controls.continuous-fire` et `controls.semi-auto-hold` dans `config.yml` ; voir [Contrôles](page:controls).

## Toujours bloqué ?

Ouvrir une issue sur ce dépôt avec la version du serveur, la version de Valocraft et la partie utile de la console.

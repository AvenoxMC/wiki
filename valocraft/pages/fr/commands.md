# Commandes et permissions


La commande principale est `/vc` (alias `/valocraft`, `/valo`).

## Commandes joueur

| Commande | Description |
|---|---|
| `/vc join [map]` | Rejoindre une partie (menu sans argument) |
| `/vc leave` | Quitter la partie |
| `/vc list` | Lister les parties |
| `/vc shop` | Boutique de la phase d'achat (ou touche F) |
| `/vc lobby` | Retour au lobby |
| `/vc boutique` | Boutique de collection (au lobby) |
| `/vc radianite` | Ton solde de Radianite |
| `/vc pass` | Battle pass |
| `/vc missions` | Missions du jour |
| `/vc resume` | Résumé de ton dernier match |
| `/vc rang [joueur]` | Rang classé |
| `/vc party invite\|accept\|deny\|leave\|kick\|chat\|list` | Groupe d'amis |
| `/vc ff [non]` | Voter l'abandon (à partir du round 5) |
| `/vc remake [non]` | Annuler la partie si un coéquipier est parti tôt |
| `/vc pack send` / `remove` | (Re)recevoir / retirer le pack de textures |
| `!message` (en partie) | Chat d'équipe |

`/vc buyfor` est utilisée en interne par le bouton **[Acheter pour …]** des demandes d'arme.

## Commandes admin

| Commande | Description |
|---|---|
| `/vc setlobby` | Définir le lobby à ta position |
| `/vc wand` | Baguette de sélection (clic gauche = pos1 / point A, clic droit = pos2 / point B) |
| `/vc start <map>` | Forcer le début d'une partie (2 joueurs minimum) |
| `/vc forcestart [map]` | Lancer **même avec 1 seul joueur** (sans map : la partie où tu es). Ne compte pas en classé. |
| `/vc stop <map>` | Forcer l'arrêt d'une partie |
| `/vc ult add\|set <joueur> [points]` | Points d'ultime (`set` sans nombre = ultime pleine) |
| `/vc pass addxp <joueur> <xp>` | Donner de l'XP de battle pass |
| `/vc leaderboard set <type>` / `remove` / `list` | Classements du lobby ([Progression](page:progression)) |
| `/vc give <arme\|knife\|spike> [joueur]` | Donner une arme, le couteau ou la spike |
| `/vc reload` | Recharger `config.yml`, `weapons.yml` et `abilities.yml` |
| `/vc pack send\|remove <joueur\|all>` | Envoyer / retirer le pack de textures |
| `/vc pack info` / `reload` | Mode et lien du pack / le recharger |
| `/vc radianite give\|take\|set <joueur> <montant>` | Gérer la Radianite d'un joueur |
| `/vc radianite voir <joueur>` | Consulter le solde d'un joueur |
| `/vc import list` / `<nom>` | Catalogue / télécharger une map ([Import de maps](page:importing-maps)) |

## Commandes de map (admin)

Voir [Création de map](page:map-setup) pour le déroulé.

| Commande | Description |
|---|---|
| `/vc map create <id>` / `delete <id>` | Créer / supprimer une map |
| `/vc map list` / `info <id>` | Lister / voir ce qui manque |
| `/vc map setname <id> <nom>` | Nom affiché |
| `/vc map setwaiting <id>` | Salle d'attente = ta position |
| `/vc map addspawn <id> <attack\|defend>` | Ajouter un spawn à ta position |
| `/vc map clearspawns <id> <attack\|defend>` | Vider les spawns |
| `/vc map addsite <id> <A\|B\|C...>` / `removesite <id> <site>` | Site de spike (sélection) / le retirer |
| `/vc map addwall <id> [bloc]` / `removewall <id> <n>` / `walls <id>` | Murs de pré-round |
| `/vc map previewwalls <id>` | Afficher / masquer les murs |
| `/vc map setplayers <id> <min> <max>` | Limites de joueurs |
| `/vc map setmode <id> <mode>` | Mode par défaut (`unrated`, `competitive`, `swiftplay`, `replication`, `spike_rush`, `deathmatch`, `team_deathmatch`, `escalation`) |
| `/vc map setmusic <id> <son\|none>` | Musique de la map |
| `/vc map addorb <id>` / `clearorbs <id>` | Orbes d'ultime |
| `/vc map setminimap <id>` / `clearminimap <id>` | Zone de la carte tactique |
| `/vc map addzipline <id>` / `ziplines <id>` / `removezipline <id> <n>` | Tyroliennes |
| `/vc map enable\|disable <id>` | Activer / désactiver |
| `/vc map tp <id>` | Aller sur la map (charge son monde si besoin) |

## Permissions

| Permission | Par défaut | Description |
|---|---|---|
| `valocraft.play` | Tout le monde | Jouer à Valocraft |
| `valocraft.admin` | Opérateurs | Commandes d'administration |
| `valocraft.agents.all` | Personne | Débloquer tous les agents (déjà le cas par défaut avec `default-agents: [ALL]`) |
| `valocraft.skins.all` | Personne | Débloquer tous les skins d'armes |

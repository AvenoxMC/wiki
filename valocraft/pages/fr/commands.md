# Commandes et permissions


La commande principale est `/vc`.

## Commandes joueur

| Commande | Description |
|---|---|
| `/vc join [map]` | Rejoindre une partie (menu sans argument) |
| `/vc leave` | Quitter la partie |
| `/vc list` | Lister les parties |
| `/vc shop` | Ouvrir la boutique |
| `/vc boutique` | Ouvrir la boutique de Radianite |
| `/vc lobby` | Retour au lobby |
| `/vc pack send` | (Re)recevoir le pack de textures |
| `/vc pack remove` | Retirer le pack de textures |

## Commandes admin

| Commande | Description |
|---|---|
| `/vc setlobby` | Définir le lobby à ta position |
| `/vc wand` | Obtenir la baguette de sélection (clic gauche = pos1 / point A, clic droit = pos2 / point B) |
| `/vc start <map>` | Forcer le début d'une partie |
| `/vc stop <map>` | Forcer l'arrêt d'une partie |
| `/vc give <arme\|knife\|spike> [joueur]` | Donner une arme, le couteau ou la spike |
| `/vc reload` | Recharger `config.yml` et `weapons.yml` |
| `/vc pack send <joueur\|all>` | Envoyer le pack de textures |
| `/vc pack remove <joueur\|all>` | Retirer le pack de textures |
| `/vc pack info` | Mode et lien du pack |
| `/vc pack reload` | Recharger le pack après modification |
| `/vc radianite give <joueur> <montant>` | Donner de la Radianite à un joueur |
| `/vc radianite take <joueur> <montant>` | Retirer de la Radianite à un joueur |
| `/vc radianite set <joueur> <montant>` | Fixer le solde de Radianite d'un joueur |
| `/vc radianite voir <joueur>` | Consulter le solde de Radianite d'un joueur |
| `/vc import list` | Afficher le catalogue de maps |
| `/vc import <nom>` | Télécharger et installer une map ([Import de maps](page:importing-maps)) |

## Commandes de map (admin)

Voir [Création de map](page:map-setup) pour le déroulé.

| Commande | Description |
|---|---|
| `/vc map create <id>` | Créer une map |
| `/vc map setname <id> <nom>` | Définir le nom affiché |
| `/vc map setwaiting <id>` | Salle d'attente = ta position |
| `/vc map addspawn <id> <attack\|defend>` | Ajouter un spawn à ta position |
| `/vc map addsite <id> <A\|B\|C...>` | Site de spike à partir de la sélection |
| `/vc map addwall <id> [bloc]` | Mur de pré-round à partir de la sélection |
| `/vc map previewwalls <id>` | Afficher / masquer les murs |
| `/vc map setplayers <id> <min> <max>` | Limites de joueurs |
| `/vc map setmusic <id> <son>` | Musique de la map |
| `/vc map addorb <id>` | Ajouter un orbe d'ultime à ta position |
| `/vc map clearorbs <id>` | Retirer tous les orbes |
| `/vc map setminimap <id>` | Définir la zone de la carte tactique avec la sélection de la baguette |
| `/vc map clearminimap <id>` | Revenir au calcul automatique de la zone de la carte tactique |
| `/vc map addzipline <id>` | Tyrolienne entre les deux points de la baguette |
| `/vc map ziplines <id>` | Lister les tyroliennes |
| `/vc map removezipline <id> <n>` | Retirer une tyrolienne |
| `/vc map info <id>` | Voir ce qui manque pour que la map soit jouable |
| `/vc map enable <id>` | Activer la map |

## Permissions

| Permission | Par défaut | Description |
|---|---|---|
| `valocraft.play` | Tout le monde | Jouer à Valocraft |
| `valocraft.admin` | Opérateurs | Commandes d'administration |
| `valocraft.agents.all` | Opérateurs | Débloquer tous les agents |
| `valocraft.skins.all` | Opérateurs | Débloquer tous les skins d'armes |

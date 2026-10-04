# Lobby et matchmaking


Le point de spawn du lobby se définit avec `/vc setlobby` (admin). Les joueurs y reviennent avec `/vc lobby`.

## Objets du lobby

| Objet | Rôle |
|---|---|
| ⭐ **Rejoindre un match** (étoile) | Rejoint la partie en attente la plus remplie. **Accroupi + clic droit** : liste de toutes les parties. |
| 📖 **Statistiques** (livre) | Tes stats (K/D, % de tirs à la tête, victoires, MVP, agent favori, rang) et les classements. |
| 🔨 **Créer une partie** (enclume) | Choisis une map libre et un [mode](page:modes), et deviens l'**hôte**. |
| 💎 **Boutique** (émeraude) | Skins d'armes, couteaux, cartes, titres, bannières et sons d'élimination, sprays, battle pass, missions. Aussi `/vc boutique`. Voir [Progression et cosmétiques](page:progression). |

## Héberger une partie

1. Utiliser l'**enclume** (Créer une partie), choisir une map libre puis le mode.
2. Tu deviens l'hôte. Les autres joueurs rejoignent avec l'étoile ou `/vc join <map>`.
3. L'hôte reçoit un **objet vert** qui lance la partie dès **2 joueurs** (un admin peut lancer seul avec `/vc forcestart`).

## Rejoindre par commande

| Commande | Effet |
|---|---|
| `/vc join` | Ouvre le menu des parties |
| `/vc join <map>` | Rejoint une map précise |
| `/vc list` | Liste les parties |
| `/vc leave` | Quitte la partie |

## Déroulé avant le match

1. **Salle d'attente au lobby** : les joueurs restent au lobby avec les objets de la partie (équipe, mode pour l'hôte, lancer, quitter). Le monde de la map n'est pas encore chargé.
2. **Compte à rebours**, puis **sélection d'agent** (25 s) dans un menu, toujours au lobby. Voir [Agents](page:agents).
3. **Écran de chargement** : pendant que le serveur charge le monde de la map, un menu montre la **carte (bannière)**, l'**agent** et le **titre** de chaque joueur, équipe rouge en haut et bleue en bas. La barre de boss affiche la progression.
4. Tout le monde est placé sur la map et le premier round commence.

À la fin de la partie, les joueurs reviennent au lobby et le monde de la map est déchargé.

## Groupes d'amis

| Commande | Effet |
|---|---|
| `/vc party invite <joueur>` | Inviter (le joueur reçoit les boutons [Accepter] / [Refuser]) |
| `/vc party leave` / `kick <joueur>` / `list` | Quitter / exclure / voir le groupe |
| `/vc party chat <message>` | Parler au groupe |

Quand le chef rejoint une partie, tout le groupe le suit s'il reste de la place, et le groupe joue dans la même équipe. Les équipes sont équilibrées selon un niveau caché (MMR).

## Classements du lobby

Des hologrammes de classement (rang, éliminations, victoires, ACS, headshots, aces, battle pass) peuvent être posés dans le lobby par un admin. Voir [Progression et cosmétiques](page:progression).

## Statistiques

Suivies par joueur : éliminations / morts, assistances, tirs à la tête, victoires, MVP, premiers sangs, aces, dégâts, score de combat, agent favori, rang. Stockage dans `stats.yml`, SQLite ou MySQL ([Configuration](page:configuration)). `/vc resume` rouvre le résumé de ton dernier match et `/vc rang [joueur]` affiche un rang.

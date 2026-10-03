# Lobby et matchmaking


Le point de spawn du lobby se définit avec `/vc setlobby` (admin). Les joueurs y reviennent avec `/vc lobby`.

## Objets du lobby

| Objet | Rôle |
|---|---|
| ⭐ **Rejoindre un match** (étoile) | Rejoint la partie en attente la plus remplie. **Accroupi + clic droit** : liste de toutes les parties. |
| 📖 **Statistiques** (livre) | Tes stats (K/D, % de tirs à la tête, victoires, MVP, agent favori) et les classements. |
| 🔨 **Créer une partie** (enclume) | Choisis une map libre et deviens l'**hôte**. |
| 💎 **Boutique** | Dépenser de la Radianite pour débloquer des agents et acheter des skins. Aussi accessible avec `/vc boutique`. |

Le lobby propose aussi une boussole « Jouer » (menu des parties et partie rapide), une salle d'attente par map, le choix d'équipe et un compte à rebours.

## Héberger une partie

1. Utiliser l'**enclume** (Créer une partie) et choisir une map libre.
2. Tu deviens l'hôte. Les autres joueurs rejoignent avec l'étoile ou `/vc join <map>`.
3. L'hôte reçoit un **objet vert** qui lance la partie dès **2 joueurs**.

## Rejoindre par commande

| Commande | Effet |
|---|---|
| `/vc join` | Ouvre le menu des parties |
| `/vc join <map>` | Rejoint une map précise |
| `/vc list` | Liste les parties |
| `/vc leave` | Quitte la partie |

## Après le compte à rebours

Une **phase de sélection d'agent (25 s)** s'ouvre. Voir [Agents](page:agents).

## Statistiques

Les stats sont suivies par joueur et enregistrées dans `plugins/Valocraft/stats.yml` :

- Éliminations / morts (K/D)
- Pourcentage de tirs à la tête
- Victoires
- MVP
- Agent favori
- Classements

## Radianite et déblocages

La Radianite est attribuée en fin de partie. Victoires, défaites, éliminations, assists, rounds gagnés et récompenses MVP contribuent au gain ; les montants sont configurables. Cinq agents (Phoenix, Jett, Sova, Brimstone et Sage) sont offerts par défaut ; chacun des dix autres coûte 1 000 ◆ par défaut. La boutique propose aussi six collections de skins pour les 18 armes. Les skins s'achètent et s'équipent arme par arme ; une arme ramassée garde le skin de son propriétaire. Un clic de confirmation est requis pour acheter. Les prix, gains et agents offerts se règlent dans `progression` de `config.yml`.

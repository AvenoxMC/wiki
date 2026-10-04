# Déroulement du jeu


Valocraft reprend le mode spike de Valorant : les attaquants posent la spike, les défenseurs les en empêchent. D'autres règles existent selon le [mode de jeu](page:modes).

## Déroulement d'une partie (Non classé / Compétition)

1. **Salle d'attente au lobby**, choix d'équipe, compte à rebours.
2. **Sélection d'agent (25 s)**, puis **écran de chargement** pendant le chargement de la map ([Lobby](page:lobby)).
3. **Phase d'achat** : ouvrir la boutique avec `F`. Des murs de pré-round retiennent les équipes à leur spawn.
4. **Round** (100 s) : les attaquants posent, les défenseurs défendent ou désamorcent.
5. **Round suivant**. Changement de côté après **12 rounds**. Le premier à **13** gagne.
6. **Prolongations** : départ avec 5000 crédits, victoire avec **2 rounds d'écart**.

## Spike

| Action | Durée |
|---|---|
| Pose | 4 s (clic droit maintenu avec la spike sur un site, rester immobile) |
| Désamorçage | 7 s (clic droit maintenu sur la spike, rester immobile). La moitié de la progression est conservée. |
| Explosion | 45 s après la pose |

Lâcher la spike ou une arme : **Accroupi + Q**.

## Économie

Économie à la Valorant (crédits ¤) : armes, bouclier et charges de capacités s'achètent dans la boutique pendant la phase d'achat. Les charges sont sur la ligne du bas ; la **signature (E)** de ton agent est offerte à chaque round.

**Demander une arme** : dans la boutique, cliquer sur une arme trop chère envoie la demande à ton équipe. Un coéquipier qui a l'argent clique sur **[Acheter pour …]** : il paie et l'arme arrive dans ton inventaire (ton ancienne arme reste au sol).

## Santé et interface

- **Cœurs** = PV (100 PV = 10 cœurs). **Cœurs dorés** = bouclier.
- **Barre d'XP** : niveau = balles dans le chargeur, barre = chargeur / progression du rechargement.
- **Barre d'action** : PV, munitions, crédits, progression de l'ultime (`X ●●●○○○`) et jauges d'agent (énergie de Neon, carburant de Viper...).
- **Radar** : une carte en main gauche montre les alliés, les ennemis repérés, la spike, les sites et les fumées de ton équipe (`game.radar`).

## Tableau des scores (Tab)

Appuie sur **Tab** pour voir la map, le round, la phase, le temps, le score et les camps, avec les joueurs alignés en colonnes. Alliés : crédits, arme en main, PV/bouclier, K/D/A et ultime. Ennemis : crédits au début de la phase d'achat, K/D/A et **points d'ultime** (en rouge quand l'ultime est prête). Le pseudo des ennemis morts est barré. `game.custom-tab: false` désactive ce tableau.

## Fin de round et de match

- **Premier sang** et **ACE** annoncés.
- **Rapport de dégâts** dans le chat à la mort et en fin de round.
- **Bannière et son d'élimination** à chaque élimination ([Progression et cosmétiques](page:progression)).
- Fin de match : classement, menu **Résumé du match** (`/vc resume`), Radianite, XP de battle pass et RR en Compétition.

## Reconnexion, votes et AFK

- **Reconnexion** : un joueur déconnecté en pleine partie garde sa place 3 min et est replacé à son retour.
- **Abandon** : `/vc ff`, à partir du round 5, 80 % de oui.
- **Remake** : `/vc remake`, jusqu'au round 3, si un coéquipier est parti ; tout le monde doit voter oui.
- **AFK** : avertissement à 45 s d'inactivité, exclusion à 90 s.

## Déplacements et sons

- Le **sprint est désactivé**, comme dans Valorant ; la vitesse de marche est augmentée (`player.speed-bonus`).
- S'arrêter ou s'accroupir avant de tirer rend le tir précis. Courir ou sauter le rend imprécis.
- **Bruits de pas** : courir s'entend chez les ennemis (son selon le bloc) ; marcher accroupi est silencieux.
- Les [tyroliennes](page:ziplines) sont utilisables sur les maps qui en ont.

## Murs de pré-round

Les murs sont posés pendant la phase d'achat et retirés au début du round. Ils ne remplissent que les blocs **vides** et sont restaurés à l'identique : la map n'est jamais abîmée.

## Voir aussi

- [Modes de jeu](page:modes)
- [Contrôles](page:controls)
- [Agents](page:agents)
- [Armes](page:weapons)

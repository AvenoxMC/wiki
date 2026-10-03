# Déroulement du jeu


Valocraft reprend le mode spike de Valorant : les attaquants posent la spike, les défenseurs les en empêchent.

## Déroulement d'une partie

1. **Lobby / salle d'attente** : les joueurs rejoignent une map et choisissent une équipe.
2. **Compte à rebours**, puis **phase de sélection d'agent (25 s)**.
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

Valocraft utilise une économie à la Valorant (crédits ¤). Armes et charges de capacités s'achètent dans la boutique pendant la phase d'achat. Les charges sont sur la ligne du bas de la boutique ; la **signature (E)** de ton agent est offerte à chaque round.

## Santé et interface

- **Cœurs** = PV (100 PV = 10 cœurs). **Cœurs dorés** = bouclier.
- **Barre d'XP** : niveau = balles dans le chargeur, barre = chargeur / progression du rechargement.
- **Barre d'action** : progression de l'ultime (`X ●●●○○○`).

## Tableau des scores (Tab)

Appuie sur **Tab** pendant une partie pour voir la map, le round, la phase, le temps restant, le score et les camps, ainsi que les joueurs alignés en colonnes. Pour les alliés : crédits, arme en main, santé/bouclier, K/D/A et état de l'ultime. Pour les ennemis, les crédits correspondent au début de la phase d'achat ; arme, santé et ultime sont masqués. Le pseudo des ennemis morts est barré. La liste vanilla des joueurs est masquée pendant la partie. `game.custom-tab: false` désactive le tableau personnalisé.

## Déplacements

- Le **sprint est désactivé**, comme dans Valorant. La vitesse de marche est augmentée (`player.speed-bonus` dans `config.yml`) pour correspondre à la course de Valorant.
- S'arrêter ou s'accroupir avant de tirer rend le tir précis. Courir ou sauter le rend imprécis.
- Les [tyroliennes](page:ziplines) sont utilisables sur les maps qui en ont.

## Murs de pré-round

Les murs sont posés pendant la phase d'achat et retirés au début du round. Ils ne remplissent que les blocs **vides** et sont restaurés à l'identique : la map n'est jamais abîmée.

## Voir aussi

- [Contrôles](page:controls)
- [Agents](page:agents)
- [Système d'ultime](page:ultimate)
- [Armes](page:weapons)

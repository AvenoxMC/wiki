# Progression et cosmétiques


Tout se passe dans la **boutique du lobby** (émeraude, ou `/vc boutique`). La monnaie est la **Radianite (◆)**. Achat en deux clics (le premier demande de confirmer).

## Radianite

Gagnée à chaque fin de partie (`progression.rewards`) :

| Source | Gain |
|---|---|
| Victoire | 150 ◆ |
| Défaite | 60 ◆ |
| Élimination | +5 ◆ |
| Assistance | +2 ◆ |
| Round gagné | +5 ◆ |
| MVP | +50 ◆ |

Plus les **missions du jour** (3 par jour, 150 ◆ chacune, `/vc missions`) et le **battle pass**. Admin : `/vc radianite give|take|set <joueur> <montant>`, `/vc radianite voir <joueur>`.

## Battle pass

- **30 niveaux de 1 000 XP** (`battlepass.levels`, `battlepass.xp-per-level`).
- XP à chaque partie : victoire 600, défaite 300, égalité 400, +20 par élimination, +10 par assistance, +30 par round gagné, +150 pour le MVP (`battlepass.xp`).
- **Une récompense par niveau**, donnée automatiquement : Radianite, cartes, titres, bannières et sons d'élimination, sprays.
- Menu : `/vc pass` ou le bouton **Battle pass** de la boutique.
- **Nouvelle saison** : changer `battlepass.season` remet tout le monde au niveau 0. Les récompenses gagnées restent.
- Récompense d'un niveau modifiable : `battlepass.rewards.<niveau>: "spray:gg"` (types `radianite`, `card`, `title`, `killbanner`, `killsound`, `spray`).
- Admin : `/vc pass addxp <joueur> <xp>`.

## Ce qu'on peut acheter

| Catégorie | Contenu |
|---|---|
| **Agents** | Tous offerts par défaut. Pour en faire payer : `progression.default-agents` (ex. `[JETT, PHOENIX, SOVA, BRIMSTONE, SAGE]`), `agent-price`. |
| **Skins d'armes** | 6 collections × 18 armes (1 000 à 2 000 ◆), équipées arme par arme |
| **Couteaux** | 14 couteaux du pack (600 à 2 500 ◆) |
| **Cartes de joueur** | Une **bannière** par agent (couleur de l'agent, symbole de son rôle), 400 ◆ |
| **Titres** | 12 titres (200 à 3 000 ◆) |
| **Bannières d'élimination** | 8 styles : ❱ (offerte), ✦ ❤ ☠ ⚡ ✪ ⚔ ♛ |
| **Sons d'élimination** | 7 sons : Valorant (offert), Carillon, Cloche, Xylophone, Pièces, Rétro 8-bit, Améthyste. Clic droit pour écouter. |
| **Sprays** | Textes (GG offert, EZ, NICE, ☠, ❤, ?, ACE, VALOCRAFT) et emblèmes des 29 agents |

Prix des bannières, sons et sprays : `progression.cosmetic-prices` (ex. `killbanner: {couronne: 1000}`).

## Où on les voit

- **Carte et titre** : écran de chargement, résumé de match, chat (titre devant le pseudo), statistiques, et pour la victime quand tu l'élimines.
- **Bannière d'élimination** : à chaque élimination, ton symbole s'affiche autant de fois que tes éliminations du round, aux couleurs de ta carte.
- **Son d'élimination** : la note monte à chaque élimination du round, son spécial au 5e.
- **Spray** : **accroupi + F** en partie colle ton spray sur le mur, le sol ou le plafond visé (6 blocs). Un par round, toutes les 30 s dans les modes à réapparition ; ils disparaissent au round suivant.

## Classé

Mode Compétition : rangs de Fer à Radiant, 5 parties de placement, RR selon le résultat, la performance et l'écart de niveau. Voir [Modes de jeu](page:modes). Le rang s'affiche dans le chat, la salle d'attente, l'écran de chargement, les statistiques et avec `/vc rang`.

## Classements du lobby

Hologrammes mis à jour toutes les minutes, posés par un admin :

```
/vc leaderboard set <type>     à l'endroit où tu te trouves
/vc leaderboard remove         retire le plus proche (5 blocs)
/vc leaderboard list
```

Types : `rank`, `kills`, `wins`, `acs` (à partir de 20 rounds), `headshots`, `aces`, `battlepass`. Réglages : `leaderboards.refresh`, `leaderboards.size`. Positions dans `plugins/Valocraft/leaderboards.yml`.

# Modes de jeu

## Duel

Les arènes de type `duel` accueillent des combats avec le kit choisi. Un match en file nécessite une arène activée et compatible, avec au moins deux spawns. Une arène peut être réservée à certains kits ; voir [Arènes](page:arenas).

## Devine ! (mastermind)

**Devine !** est un mode 1v1 sans combat, joué avec le kit `devine` créé automatiquement sur une arène de type `devine`.

1. Les rôles sont tirés au sort. Le **maître du code** choisit une combinaison secrète ordonnée de **quatre couleurs de laine** en 30 secondes. Si le délai expire, la combinaison est complétée au hasard.
2. Le **devineur** a **deux minutes** pour trouver le code. Il compose ses essais dans le menu avec l'objet « Combinaison », ou laisse la combinaison se remplir automatiquement, puis valide.
3. Chaque couleur reçoit un indice : **vert** signifie bonne couleur et bonne position ; **orange**, couleur présente mais à une autre position ; **rouge**, couleur absente.
4. Si le devineur trouve le code à temps, il gagne ; sinon, le maître du code gagne. Abandon ou déconnexion : la victoire revient à l'autre joueur.

L'historique apparaît sur le tableau de la map (quatre laines, un séparateur et quatre blocs d'indice par ligne), dans le menu (les trois derniers essais) et dans le chat. La combinaison secrète est révélée en haut du tableau à la fin.

## Créer une arène Devine !

```text
/arena create devine1 devine                Crée une arène mastermind
/arena addspawn devine1                     Répéter pour les deux joueurs
/arena setboard devine1                     Face au mur, viser le bloc en bas à gauche du tableau
/arena save devine1
```

Le tableau fait 9 blocs de large et 9 de haut : huit lignes d'essais et la combinaison secrète. Il s'étend vers la droite et vers le haut depuis le bloc visé. Les arènes existantes sont de type `duel` ; changer avec `/arena set <nom> type devine`. Régler le mode d'un kit avec `/dkit set <kit> mode devine`.

La section `devine` de `config.yml` règle les temps de choix et de devinette, le nombre maximum d'essais, les couleurs autorisées et les doublons, le nombre de lignes et les blocs du tableau.

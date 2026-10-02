# Schématiques

Une arène peut être créée depuis une schématique WorldEdit compatible avec `/arena fromschem`.

## Formats acceptés

| Extension | Origine | Format des blocs |
|---|---|---|
| `.schem` | Sponge v1, v2 ou v3, créé par WorldEdit 7+ ou FAWE en 1.13+ | Les blocs modernes sont convertis automatiquement en équivalents 1.8. |
| `.schematic` | MCEdit, créé par WorldEdit 6 pour la 1.8 | Les blocs sont déjà au format 1.8. |

## Trouver et coller une schématique

1. Déposer le fichier dans `plugins/Duels/schematics/`. Le plugin consulte aussi `plugins/WorldEdit/schematics/` et `plugins/FastAsyncWorldEdit/schematics/` ; les dossiers se modifient dans `config.yml`, sous `schematics.folders`.
2. Lister les fichiers disponibles et créer une arène :

```text
/arena schematics                         Liste les schématiques trouvées
/arena fromschem <nom> <fichier> <type>   Crée un monde vide, colle la map et t'y téléporte
   (équivalent : /arena create <nom> <type> <fichier.schem>)
/arena addspawn <nom>                     Ajouter au moins deux spawns
/arena setspec <nom>                      Définir le point de spectateur facultatif
/arena save <nom>
```

La map est centrée en `0 / 64 / 0`. Régler la hauteur de collage avec `schematics.paste-y`. La zone de vide mortelle est posée cinq blocs sous la map. `/arena paste <nom> <fichier>` colle une schématique à ta position pendant l'édition d'une arène, comme `//paste` ; pratique pour assembler la map en plusieurs morceaux.

## Conversion et performances

Les blocs modernes sont convertis avec la table de conversion de WorldEdit, en conservant l'orientation des escaliers, dalles, bûches, portes, panneaux, etc. Si un bloc n'a pas d'équivalent en 1.8, il est approximé : par exemple béton vers laine de même couleur, terre cuite émaillée vers argile colorée, bois crimson/warped/cerisier vers chêne, deepslate vers cobblestone et lanterne vers air. Après la création, le plugin liste les types de blocs approximés.

Les blocs sont écrits directement dans les chunks. Le travail est réparti entre les ticks selon `schematics.ms-per-tick` pour éviter de figer le serveur ; l'avancement est affiché en pourcentage.

## Limites

L'air n'est pas collé. Le contenu des blocs spéciaux n'est pas copié : texte des panneaux, contenu des coffres et bannières.

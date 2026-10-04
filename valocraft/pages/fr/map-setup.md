# Création de map


Les maps se configurent **en jeu** avec `/vc map ...` et la baguette de sélection. Cette page construit une map nommée `ascent` de zéro. Pour éviter de la construire, voir [Import de maps](page:importing-maps).

## Ce qu'il faut pour qu'une map soit jouable

- Une **salle d'attente** (utilisée en fin de match et à la reconnexion)
- Des spawns **attaque** et **défense** (5 chacun en général)
- Au moins un **site de spike** (A, B, C...)
- Des **murs de pré-round**
- Les limites de joueurs
- Être **activée**

`/vc map info <id>` liste exactement ce qui manque.

## Déroulé complet

```
/vc map create ascent
/vc map setname ascent Ascent
/vc map setwaiting ascent            (salle d'attente = ta position)
/vc map addspawn ascent attack       (répéter pour chaque joueur, 5 en général)
/vc map addspawn ascent defend
/vc wand                             (clic gauche = pos1, clic droit = pos2)
/vc map addsite ascent A             (sélection = zone de pose du site A)
/vc map addsite ascent B
/vc map addwall ascent               (sélection = mur de pré-round, verre vert par défaut)
/vc map addwall ascent light_blue_stained_glass
/vc map previewwalls ascent          (afficher / masquer les murs pour vérifier)
/vc map setplayers ascent 2 10
/vc map setmode ascent unrated       (mode par défaut, optionnel)
/vc map setmusic ascent hrdavalorant.maps.ascent
/vc map addorb ascent                (orbes d'ultime, optionnel)
/vc map addzipline ascent            (tyroliennes, optionnel)
/vc map enable ascent
```

## Étape par étape

### 1. Créer et nommer

`/vc map create <id>` puis `/vc map setname <id> <nom affiché>`.

### 2. Salle d'attente et spawns

Se placer à l'endroit voulu et faire `/vc map setwaiting <id>`. Répéter `/vc map addspawn <id> attack` et `/vc map addspawn <id> defend` à chaque position de spawn. `/vc map clearspawns <id> <attack|defend>` vide une liste.

### 3. Sites de spike

1. `/vc wand`
2. **Clic gauche** = pos1, **clic droit** = pos2.
3. `/vc map addsite <id> A` (et `B`, `C`...). La sélection devient la zone de pose. `/vc map removesite <id> <site>` en retire un.

### 4. Murs de pré-round

Sélectionner la zone avec la baguette, puis `/vc map addwall <id> [bloc]`. Le bloc par défaut est le **verre vert**.

- Les murs ne remplissent que les blocs **vides** et sont retirés à l'identique au début du round : la map n'est **jamais abîmée**.
- `/vc map previewwalls <id>` affiche ou masque un aperçu ; `/vc map walls <id>` les liste, `/vc map removewall <id> <n>` en retire un.

### 5. Joueurs, mode et musique

`/vc map setplayers <id> <min> <max>`, `/vc map setmode <id> <mode>` ([Modes de jeu](page:modes)), `/vc map setmusic <id> <son|none>`.

### 6. Options

- [Orbes d'ultime](page:ultimate) : `/vc map addorb <id>` / `/vc map clearorbs <id>`
- [Tyroliennes](page:ziplines)
- Zone de la carte tactique et du radar : calculée à partir des spawns, sites, murs et orbes. Pour la régler, sélectionner la zone avec la baguette et faire `/vc map setminimap <id>` ; `/vc map clearminimap <id>` rétablit le calcul automatique.

### 7. Activer

`/vc map enable <id>` (et `disable` pour la retirer des parties).

## Monde de la map : chargé à la demande

- Une map construite dans son **propre monde** (par exemple `vc_ascent`, créé par [l'import](page:importing-maps)) n'est **pas chargée au démarrage du serveur**. Le monde est chargé au **lancement d'une partie**, pendant l'écran de chargement, puis **déchargé et sauvegardé** quand plus personne ne l'utilise (vérification toutes les 30 s, `maps.unload-check`).
- `/vc map tp <id>` et `/vc map previewwalls <id>` chargent le monde à la demande pour configurer la map. Il est déchargé quand tu en sors.
- Une map construite dans le **monde principal** (`world`) fonctionne aussi, mais ce monde reste toujours chargé.

## Protection en cas de crash

Les blocs posés (murs, spike, capacités) sont **enregistrés sur disque** dans `plugins/Valocraft/data/` et **restaurés au prochain chargement du monde** si le serveur plante.

## Voir aussi

- [Commandes et permissions](page:commands)
- [Import de maps](page:importing-maps)

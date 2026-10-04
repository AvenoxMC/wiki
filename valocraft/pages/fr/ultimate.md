# Système d'ultime


Chaque agent a un ultime sur la touche **8** (X). Il coûte un certain nombre de **points d'ultime** (de 6 à 9 selon l'agent, indiqués sur la page [Agents](page:agents), modifiables dans `abilities.yml`).

## Gagner des points

- Les **éliminations**
- Les **morts**
- La **pose** et le **désamorçage** de la spike
- Les **orbes d'ultime** (voir plus bas)
- En Spike Rush : +1 point par round

Les points sont **conservés à la mi-temps**.

## Retours visuels et sonores

| Moment | Ce qui se passe |
|---|---|
| Progression | Affichée en permanence dans la barre d'action (`X ●●●○○○`). La touche **8** montre l'ultime avec le nombre de points. |
| **Ultime prête** | Titre à l'écran, son, et message à toute l'équipe. Les **ennemis** reçoivent une alerte dans le chat. |
| **Ultime lancée** | Tout le monde entend la réplique de l'agent et le chat l'annonce. |
| Tableau des scores | Les points d'ultime des alliés **et des ennemis** sont visibles (en rouge quand une ultime ennemie est prête). |

## Utiliser l'ultime

Touche **8** pour la prendre en main, **clic gauche** pour l'activer ([activation manuelle](page:controls)).

Certaines ultimes transforment la touche 8 en arme tant qu'elles sont actives : Blade Storm, Hunter's Fury, Showstopper, Overdrive, Tour de Force (avec lunette au clic droit). **Blade Storm**, **Overdrive** et **Empress** sont prolongées ou rechargées par les éliminations. **Not Dead Yet** (Clove) s'active tout seul à la mort.

## Orbes d'ultime

Les orbes sont un élément de map placé par les admins.

- **Placer** : `/vc map addorb <map>` à l'endroit où l'on se trouve.
- **Tout retirer** : `/vc map clearorbs <map>`.
- **Réapparition** : les orbes reviennent à **chaque round** (et en Team Deathmatch).
- **Récupérer** : **maintenir clic droit 1,5 s** à côté d'un orbe pour gagner **+1 point d'ultime**.

## Commandes admin

| Commande | Effet |
|---|---|
| `/vc ult add <joueur> [points]` | Ajoute des points (1 par défaut) |
| `/vc ult set <joueur> [points]` | Fixe les points ; sans nombre, l'ultime est pleine (avec les alertes « ultime prête ») |

Voir [Création de map](page:map-setup) pour placer les orbes.

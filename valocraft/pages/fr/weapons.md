# Armes


Toutes les armes ont un modèle 3D.

## Arsenal

| Catégorie | Armes |
|---|---|
| Mêlée | Knife (couteau) |
| Pistolets | Classic, Ghost, Sheriff, Shorty, Frenzy |
| SMG | Stinger, Spectre |
| Fusils à pompe | Bucky, Judge |
| Fusils d'assaut | Bulldog, Guardian, Phantom, Vandal |
| Snipers | Marshal, Operator, Outlaw |
| Armes lourdes | Ares, Odin |

Les armes et charges s'achètent dans la boutique pendant la phase d'achat (`F`, ou `/vc shop`).

## Mécaniques

| Mécanique | Fonctionnement |
|---|---|
| **Tir** | Hitscan |
| **Précision** | L'imprécision dépend du mouvement : elle augmente en déplacement ou en l'air, et change en position accroupie. S'arrêter (ou s'accroupir) avant de tirer donne un tir précis ; courir ou sauter le rend imprécis. |
| **Recul** | Montée puis balayage latéral. Entièrement intégré à la trajectoire des balles. |
| **Dégâts** | Tête / corps / jambes, avec paliers selon la portée |
| **Pénétration** | Les balles traversent les murs |
| **Rechargement** | Touche **Q**. La progression s'affiche sur la barre d'XP. |
| **Visée / lunette** | Clic droit maintenu. Lunettes sur Operator, Marshal et Outlaw. |
| **Fusils à pompe** | Armes de courte portée (Bucky, Judge) |
| **Couteau** | **x3 dégâts** dans le dos |

## Recul et caméra

Le recul **ne déplace jamais la vue du joueur**. Le serveur ne peut imposer qu'une orientation absolue, ce qui faisait « revenir » l'écran en arrière pendant les rafales. Dans la 2.1, tout le recul est appliqué à la **trajectoire des balles**.

## Modèles

- **Pack HrdaValorant** : Classic, Ghost, Sheriff, Spectre, Vandal, Ares, Operator, couteau (et ses skins `model-data` 2 à 15), boucliers.
- **Modèles Valocraft**, créés pour le projet (`assets/valocraft` du pack) : Shorty, Frenzy, Stinger, Bucky, Judge, Bulldog, Guardian, Phantom, Marshal, Outlaw, Odin. Ils utilisent le composant `item_model` (`item-model: valocraft:<arme>`, automatique).

Les sources et outils des modèles sont décrits dans [Développement](page:development).

## Réglages

Toutes les statistiques (dégâts, cadence, imprécision, recul, pénétration, zoom...) sont dans `weapons.yml`, commentées en tête du fichier. Recharger avec `/vc reload`. Pour tester sans risque, utiliser le [Stand de tir](page:practice-range).

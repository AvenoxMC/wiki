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

Les armes et charges s'achètent dans la boutique pendant la phase d'achat (`F`, ou `/vc shop`). Une arme trop chère peut être **demandée à un coéquipier** ([Déroulement du jeu](page:gameplay)).

## Mécaniques

| Mécanique | Fonctionnement |
|---|---|
| **Tir** | Hitscan, avec **compensation de latence** (jusqu'à 200 ms) |
| **Précision** | L'imprécision augmente en déplacement ou en l'air et change accroupi. S'arrêter (ou s'accroupir) avant de tirer donne un tir précis. |
| **Recul** | Montée puis balayage latéral, entièrement intégré à la trajectoire des balles (la vue ne bouge pas). |
| **Dégâts** | Tête / corps / jambes, avec paliers selon la portée |
| **Pénétration** | Les balles traversent les murs ; elles détruisent l'**utilitaire ennemi** touché (tourelle, caméra, pièges...) |
| **Rechargement** | Touche **Q**. Progression sur la barre d'XP. |
| **Visée / lunette** | Clic droit maintenu. Lunettes sur Operator, Marshal et Outlaw. Pas de lunette quand on est flashé. |
| **Fusils à pompe** | Courte portée (Bucky, Judge) |
| **Couteau** | **x3 dégâts** dans le dos |

## Tir en maintenant le clic

Maintenir le clic gauche en visant un bloc à moins de 64 blocs fait tirer l'arme à sa cadence réelle. Aucun bloc n'est abîmé et l'animation du bras est masquée. Les semi-automatiques tirent à leur cadence maximale tant que le clic est maintenu. Voir [Contrôles](page:controls).

## Lunettes

L'Operator, le Marshal, l'Outlaw et l'ultime de Chamber (Tour de Force) utilisent une lunette plein écran 16:9 : lentille ronde nette, noir autour, réticule fin et point rouge. Elle est portée par le casque et ne clignote pas.

## Skins

La boutique du lobby propose six collections pour les 18 armes : Prime, Reaver, Glitchpop, Ion, Elderflame et Oni, ainsi que 14 couteaux. Les skins s'achètent et s'équipent arme par arme ; une arme ramassée garde le skin de son propriétaire. Voir [Progression et cosmétiques](page:progression).

## Modèles

- **Pack HrdaValorant** : Classic, Ghost, Sheriff, Spectre, Vandal, Ares, Operator, couteaux, boucliers.
- **Modèles Valocraft**, créés pour le projet : Shorty, Frenzy, Stinger, Bucky, Judge, Bulldog, Guardian, Phantom, Marshal, Outlaw, Odin (composant `item_model`).

## Réglages

Toutes les statistiques (dégâts, cadence, imprécision, recul, pénétration, zoom...) sont dans `weapons.yml`, commentées en tête du fichier. Recharger avec `/vc reload`. Pour tester, utiliser le [Stand de tir](page:practice-range).

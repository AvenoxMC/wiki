# Contrôles


| Touche | Action |
|---|---|
| **Clic gauche** | Tirer ; maintenir en visant un bloc à moins de 64 blocs pour le tir continu |
| **Clic droit (maintenu)** | Viser / lunette |
| **Q** | Recharger |
| **Accroupi + Q** | Lâcher l'arme (ou la spike) |
| **F** | Boutique pendant la phase d'achat, sinon ramasser l'arme visée |
| **Accroupi + F** | Spray sur le mur visé |
| **1 / 2 / 3 / 4** | Arme principale / pistolet / couteau / spike |
| **5 / 6 / 7 / 8**, puis **clic gauche** | Prendre puis utiliser la capacité **C / Q / E / X** |
| **F** près d'une corde | S'accrocher à une [tyrolienne](page:ziplines) |
| **Clic droit maintenu** avec la spike, sur un site | Poser la spike (rester immobile) |
| **Clic droit maintenu** sur la spike (défenseur) | Désamorcer (rester immobile) |
| **Tab** | Tableau des scores |

## Capacités

- **Activation manuelle** : la touche 5 à 8 prend la capacité en main, le **clic gauche** l'utilise. Rien ne part en changeant de slot. Pour revenir au déclenchement direct (Tailwind, High Gear, Dismiss, ultimes instantanées...) : `controls.instant-abilities: true`.
- **Objets lancés** : **maintenir** le clic gauche affiche la trajectoire (visible de toi seul), **relâcher** lance. **Clic droit** : lancer en cloche, ou la variante quand il y en a une (Curveball à droite, flèches de Sova sans rebond, Healing Orb sur soi, FLASH/drive rapide, M-Pulse qui soigne).
- **Flèches de Sova** : plus tu maintiens, plus elles vont loin (jauge « Puissance »).
- **Pilotage** (drone de Sova, tigre de Skye, drone de Tejo) : tu vois par les yeux de la créature, ZQSD pour te déplacer, clic gauche = action, clic droit = retour dans ton corps.
- **Carte tactique** : ZQSD déplace le curseur (sprint pour aller plus vite), clic gauche pose, clic droit ou accroupi annule.
- **Capacités de balise** : premier clic = poser, second clic = utiliser.
- **Neon** : accroupi pendant High Gear = glissade. **Viper** : clic sur un émetteur posé = l'activer / le couper.
- **Tour de Force** (Chamber) : clic droit = lunette, clic gauche = tirer.
- **Jett** plane en maintenant la touche de saut.

## Tir continu

Minecraft n'envoie normalement qu'**un signal par clic gauche**. En partie, Valocraft utilise le bloc visé (jusqu'à **64 blocs**) pour recevoir un signal à chaque tick tant que le clic est maintenu : l'arme tire à sa cadence configurée. Aucun bloc n'est cassé, aucune fissure n'est visible et l'animation du bras est masquée. Un clic simple tire une balle ; les semi-automatiques tirent aussi en continu à leur cadence maximale.

En visant le ciel sans bloc à moins de 64 blocs, il faut cliquer. Le couteau frappe toujours à moins de 3 blocs. Réglages : `controls.continuous-fire`, `controls.semi-auto-hold`, `controls.hide-swing` ([Configuration](page:configuration)).

## Interface

- **Barre d'XP** : niveau = balles dans le chargeur, barre = chargeur / progression du rechargement.
- **Cœurs** = PV (100 PV = 10 cœurs), **cœurs dorés** = bouclier.
- **Barre d'action** : PV, munitions, crédits, ultime et jauges d'agent.
- **Main gauche** : radar.

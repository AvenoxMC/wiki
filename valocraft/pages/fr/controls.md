# Contrôles


| Touche | Action |
|---|---|
| **Clic gauche** | Tirer ; maintenir en visant un bloc à moins de 64 blocs pour le tir continu |
| **Clic droit (maintenu)** | Viser / lunette |
| **Q** | Recharger |
| **Accroupi + Q** | Lâcher l'arme (ou la spike) |
| **F** | Boutique pendant la phase d'achat, sinon ramasser l'arme visée |
| **1 / 2 / 3 / 4** | Arme principale / pistolet / couteau / spike |
| **5 / 6 / 7 / 8** | Capacités de l'agent **C / Q / E / X** |
| **F** près d'une corde | S'accrocher à une [tyrolienne](page:ziplines) |
| **Clic droit maintenu** avec la spike, sur un site | Poser la spike (rester immobile) |
| **Clic droit maintenu** sur la spike (défenseur) | Désamorcer (rester immobile) |

## Contrôles des capacités

- **Capacités instantanées** : elles s'activent dès qu'on appuie sur la touche. Updraft, Tailwind, Devour, Dismiss, High Gear, Regrowth, et les ultimes Run it Back, Empress, Lockdown, Viper's Pit et Seekers.
- **Toutes les autres** : **clic gauche** pour lancer, **clic droit** pour la variante quand il y en a une (Curveball à droite, flèches de Sova sans rebond, Healing Orb sur soi, Blade Storm tous les couteaux).
- **Capacités guidées** (drone de Sova, faucon et tigre de Skye, Thrash de Gekko) : elles suivent ton regard.
- **Jett** plane en maintenant la touche de saut.

## Tir continu (2.2)

Minecraft n'envoie normalement qu'**un signal par clic gauche**. En partie, Valocraft utilise le bloc visé (jusqu'à **64 blocs**) pour recevoir un signal à chaque tick tant que le clic gauche est maintenu : l'arme tire ainsi à sa cadence configurée. Aucun bloc n'est cassé, aucune fissure n'est visible par les autres joueurs et l'animation du bras est masquée. Un clic simple tire toujours une balle ; les armes semi-automatiques peuvent aussi tirer en continu à leur cadence maximale.

Si tu vises le ciel sans bloc à moins de 64 blocs, clique pour tirer. Le couteau frappe toujours à moins de 3 blocs. Les options `controls.continuous-fire`, `controls.semi-auto-hold` et `controls.hide-swing` dans `config.yml` règlent ce comportement ; voir [Configuration](page:configuration).

## Interface

- **Barre d'XP** : niveau = balles dans le chargeur, barre = chargeur / progression du rechargement.
- **Cœurs** = PV (100 PV = 10 cœurs), **cœurs dorés** = bouclier.

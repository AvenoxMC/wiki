# Contrôles


| Touche | Action |
|---|---|
| **Clic gauche** | Tirer (armes automatiques : cliquer vite pour tirer en rafale) |
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

## Tir automatique et limite du clic gauche

Minecraft n'envoie au serveur qu'**un signal par clic gauche** (rien tant que le bouton reste enfoncé). Avec le tir au clic gauche, les armes automatiques tirent donc au rythme des clics, jusqu'à leur cadence maximale.

Pour un vrai tir automatique en maintenant le bouton, mettre dans `config.yml` :

```yaml
controls:
  fire-button: RIGHT
```

Le tir se fait alors au **clic droit maintenu**, et la visée au **clic gauche**.

## Interface

- **Barre d'XP** : niveau = balles dans le chargeur, barre = chargeur / progression du rechargement.
- **Cœurs** = PV (100 PV = 10 cœurs), **cœurs dorés** = bouclier.

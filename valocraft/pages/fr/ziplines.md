# Tyroliennes


Les tyroliennes sont un élément de map : une corde entre deux points sur laquelle les joueurs peuvent glisser. Elles peuvent être **horizontales, montantes ou descendantes**.

## Utiliser une tyrolienne (joueurs)

| Action | Touche |
|---|---|
| S'accrocher | **F**, près de la corde |
| Glisser | **Avancer / reculer**, dans un sens ou dans l'autre selon où tu regardes |
| Lâcher | **Saut** ou **accroupi** |

- Arrivé au bout de la corde, le joueur est déposé sur la plateforme.
- On **peut tirer** pendant le trajet.

## Créer une tyrolienne (admins)

1. Prendre la baguette : `/vc wand`.
2. **Clic gauche** sur un bloc pour le point **A**, **clic droit** sur un bloc pour le point **B**. Les points sont les **centres des blocs cliqués**.
3. Lancer :

```
/vc map addzipline <map>
```

### Gérer les tyroliennes

```
/vc map ziplines <map>               lister les tyroliennes
/vc map removezipline <map> <n>      retirer la tyrolienne numéro n
```

## Notes techniques

Chaque tyrolienne est **une seule entité d'affichage**, et le déplacement est **interpolé côté client**. C'est fluide et peu coûteux pour le serveur.

Voir aussi [Création de map](page:map-setup).

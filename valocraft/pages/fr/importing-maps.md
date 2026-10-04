# Import de maps


Valocraft peut télécharger les maps du projet [VALORANT x Minecraft d'Ommo](https://ommo.me/valorant-x-minecraft) directement depuis le jeu.

## Commandes

```
/vc import list          catalogue + version Minecraft requise
/vc import ascent        télécharge, installe le monde vc_ascent et crée la map Valocraft "ascent"
```

## Ce que fait l'import

- Télécharge la map et l'installe comme monde `vc_<nom>`.
- Crée une map Valocraft avec le même id.
- Le monde est ensuite **chargé à la demande** : au lancement d'une partie sur cette map, ou avec `/vc map tp <nom>` pour la configurer. Il est déchargé quand plus personne ne l'utilise ([Création de map](page:map-setup)).

## Ce qu'il reste à faire

L'import ne place **pas** les points de jeu. Il faut encore définir :

- La salle d'attente
- Les spawns (attaque / défense)
- Les sites de spike
- Les murs de pré-round

Aller sur la map avec `/vc map tp ascent`, suivre [Création de map](page:map-setup), puis activer :

```
/vc map enable ascent
```

## Limites de version

Une map sauvegardée dans une version de Minecraft **plus récente que le serveur** est refusée. **Lotus, Sunset et Breeze** demandent **Minecraft 1.21.11**.

## Modifier le catalogue

Le catalogue est la section `map-library` de `config.yml`.

## ⚖️ Licence

Les maps d'Ommo sont sous licence **CC BY-NC-ND 4.0**.

- Autorisées sur un serveur **privé entre amis**.
- Un serveur **public** nécessite une **licence commerciale** (contact@ommo.me).
- **Ne pas republier** les maps.

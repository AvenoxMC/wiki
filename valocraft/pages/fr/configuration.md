# Configuration


Les fichiers se trouvent dans `plugins/Valocraft/`. Recharger `config.yml` et `weapons.yml` avec `/vc reload`.

## Fichiers et dossiers

| Chemin | Rôle |
|---|---|
| `config.yml` | Réglages généraux, contrôles, pack de textures, bibliothèque de maps |
| `weapons.yml` | Statistiques de toutes les armes (commentées en tête du fichier) |
| `stats.yml` | Statistiques des joueurs |
| `resourcepack.zip` | Pack de textures extrait du jar au premier démarrage |
| `maps/<id>.yml` | Un fichier par map |
| `playerdata/` | Inventaires sauvegardés pendant une partie, rendus à la reconnexion après un crash |
| `data/` | Blocs temporaires (murs, spike) à restaurer après un crash |

## Options de `config.yml`

| Clé | Rôle |
|---|---|
| `controls.fire-button` | `RIGHT` = tir au clic droit maintenu, visée au clic gauche. Voir [Contrôles](page:controls). |
| `player.speed-bonus` | Bonus de vitesse de marche qui remplace la course de Valorant (le sprint est désactivé) |
| `weapons.practice-mode` | Active ou désactive le [Stand de tir](page:practice-range) |
| `resource-pack.self-host.http-port` | Port HTTP dédié au pack (par exemple `8164`) |
| `resource-pack.self-host.enabled` | Mettre `false` pour utiliser une URL externe |
| `resource-pack.url` / `resource-pack.sha1` | URL externe du pack et sa somme de contrôle |
| `map-library` | Catalogue de `/vc import` ([Import de maps](page:importing-maps)) |

Exemple, tir en maintenant le bouton :

```yaml
controls:
  fire-button: RIGHT
```

## `weapons.yml`

Contient toutes les statistiques d'armes : dégâts, cadence, imprécision, recul, pénétration, zoom et plus. Voir [Armes](page:weapons).

## Réglage des capacités

Les dégâts, durées et prix des capacités sont définis dans `AbilityType.java` et `Kits.java`. Ils sont dans le code source : les modifier demande de recompiler le plugin. Voir [Développement](page:development).

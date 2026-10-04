# Configuration


Les fichiers se trouvent dans `plugins/Valocraft/`. `/vc reload` recharge `config.yml`, `weapons.yml` et `abilities.yml`. Les nouvelles options sont ajoutées automatiquement à `config.yml` lors des mises à jour.

## Fichiers et dossiers

| Chemin | Rôle |
|---|---|
| `config.yml` | Réglages généraux, modes, contrôles, progression, battle pass, pack de textures, bibliothèque de maps |
| `weapons.yml` | Statistiques de toutes les armes (commentées en tête du fichier) |
| `abilities.yml` | Prix, charges, recharges et dégâts de chaque capacité, coût des ultimes |
| `stats.yml` / `valocraft.db` | Profils des joueurs (YAML par défaut, SQLite ou MySQL) |
| `leaderboards.yml` | Positions des classements du lobby |
| `resourcepack.zip` | Pack de textures extrait du jar |
| `maps/<id>.yml` | Un fichier par map |
| `playerdata/` | Inventaires sauvegardés pendant une partie, rendus après un crash |
| `data/` | Blocs temporaires à restaurer après un crash, mini-maps, skins d'agents signés (`agent-skins.yml`) |

## Principales options de `config.yml`

| Clé | Rôle |
|---|---|
| `game.countdown`, `game.rounds-to-win`, `game.loading-time` | Compte à rebours, rounds gagnants, durée minimale de l'écran de chargement |
| `game.custom-tab`, `game.radar` | Tableau des scores personnalisé, radar en main gauche |
| `modes.<mode>.*` | Réglages de chaque [mode](page:modes) (rounds, éliminations, temps, armes d'Escalation...) |
| `maps.unload-check` | Secondes entre deux vérifications des mondes de maps à décharger |
| `controls.fire-button`, `controls.aim-mode` | Bouton de tir (`LEFT` / `RIGHT`) et visée (`HOLD` / `TOGGLE`) |
| `controls.continuous-fire`, `controls.semi-auto-hold`, `controls.hide-swing` | Tir continu ([Contrôles](page:controls)) |
| `controls.instant-abilities` | `false` (défaut) : activation manuelle des capacités ; `true` : déclenchement à l'appui sur la touche |
| `agents.select-time` | Durée de la sélection d'agent |
| `agents.full-skin`, `agents.wear-heads` | Skin complet de l'agent / têtes d'agents |
| `agents.skins-restorer`, `agents.skins.<agent>` | Skins signés via SkinsRestorer / skin personnalisé d'un agent (URL d'image ou pseudo) |
| `agents.tactical-map`, `agents.smokes-hide-players`, `agents.solid-smokes` | Carte tactique, fumées qui cachent, fumées 3D |
| `progression.*` | Radianite, prix, agents offerts (`default-agents: [ALL]`), `cosmetic-prices` |
| `battlepass.*` | Saison, niveaux, XP, récompenses ([Progression](page:progression)) |
| `leaderboards.refresh`, `leaderboards.size` | Classements du lobby |
| `reconnect.*`, `surrender.*`, `remake.*`, `afk.*` | Reconnexion, votes, inactivité |
| `ranked.*`, `missions.*`, `party.*`, `chat.*`, `footsteps.*` | Classé, missions, groupes, chat, bruits de pas |
| `storage.type` | `yaml`, `sqlite` ou `mysql` (import automatique depuis `stats.yml`) |
| `weapons.lag-compensation`, `weapons.practice-mode` | Compensation de latence, [Stand de tir](page:practice-range) |
| `player.speed-bonus` | Bonus de vitesse de marche (le sprint est désactivé) |
| `resource-pack.*` | Hébergement du pack ([Pack de textures](page:resource-pack)) |
| `map-library` | Catalogue de `/vc import` |

## `abilities.yml`

Créé au premier démarrage avec les valeurs d'origine, complété automatiquement quand de nouvelles capacités apparaissent.

```yaml
global:
  damage-multiplier: 1.0      # dégâts de toutes les capacités
  duration-multiplier: 1.0    # durée des fumées, feux, pièges
agents:
  jett:
    ult-cost: 8
    cloudburst:
      price: 200
      max-charges: 2
      free-charges: 0
      cooldown: 0             # secondes pour regagner une charge offerte
      kill-recharge: 0        # revient après N éliminations
      damage-multiplier: 1.0
```

Modifier, puis `/vc reload` : pas besoin de recompiler.

## `weapons.yml`

Toutes les statistiques d'armes : dégâts, cadence, imprécision, recul, pénétration, zoom et plus. Voir [Armes](page:weapons).

# Kits

Cinq kits d'exemple sont créés au premier démarrage : `nodebuff`, `builduhc`, `sumo`, `combo` et `archer`. Créer et modifier les kits en jeu avec `/dkit`, ou éditer `kits.yml` manuellement puis lancer `/duels reload`.

## Créer un kit depuis son inventaire

Équiper l'inventaire, l'armure et les effets de potion souhaités, puis lancer :

```text
/dkit create <nom>                  Crée le kit depuis l'inventaire ; l'objet tenu devient l'icône
/dkit setinv <nom>                  Remplace le contenu du kit par l'équipement actuel
/dkit load <nom>                    Charge le kit pour le modifier (passer en créatif pour réorganiser)
/dkit setname <nom> &bNoDebuff      Définit le nom affiché
/dkit seticon <nom>                 Définit l'icône avec l'objet tenu
/dkit set <nom> <réglage> <valeur>  Modifie un réglage du kit
```

## Réglages des kits

| Réglage | Effet |
|---|---|
| `build` | Autorise la construction, par exemple en BuildUHC. |
| `break-map` | Autorise à casser la map. Sinon, seuls les blocs posés par les joueurs peuvent être cassés. |
| `hunger` / `regen` | Règle la faim et la régénération naturelle. |
| `no-damage` | Les coups n'infligent pas de dégâts mais conservent le knockback (Sumo). |
| `water-kills` | Élimine un joueur qui touche l'eau (Sumo). |
| `hit-delay` | Ticks entre deux coups (20 = vanilla, 2 = Combo). |
| `queue` | Affiche le kit dans le menu « Jouer ». |
| `enabled` | Active ou désactive le kit. |

Une arène peut aussi être réservée à certains kits avec `/arena kits <arène> add <kit>`.

# Arènes

Les arènes se configurent avec `/arena`. Un match se joue dans une copie jetable, jamais dans le monde modèle.

## Mondes d'arène

| Monde | Rôle |
|---|---|
| `duels_tpl_<arène>` | Modèle de l'arène. Déchargé sauf pendant `/arena edit`. |
| `duels_match_<arène>_<n>` | Copie temporaire de match, déchargée puis supprimée à la fin. |

Quand des joueurs choisissent le même mode, le plugin sélectionne une arène disponible : activée, avec au moins deux spawns, compatible avec le kit choisi et sous sa limite `max-instances`. Le monde modèle est copié en asynchrone, la copie est chargée, puis les joueurs y sont téléportés. `worlds.max-loaded-instances` plafonne le nombre total d'instances chargées sur le serveur. Les copies de match restantes après un crash sont supprimées au démarrage. Le chargement des chunks de spawn est désactivé dans ces mondes pour accélérer les copies.

## Créer une arène

```text
/arena create <nom> <type>               Crée un monde vide et t'y téléporte en créatif
/arena create <nom> <type> <monde>       Copie un monde existant comme modèle
   type = duel ou devine
   ... construire la map ...
/arena addspawn <nom>                     Ajoute un spawn (répéter, au moins deux)
/arena setspec <nom>                      Définit le point de spectateur facultatif
/arena save <nom>                         Sauvegarde et décharge le modèle
```

Pour créer une arène depuis une schématique, voir [Schématiques](page:schematics).

## Modifier une arène

`/arena edit <nom>` charge le modèle pour le modifier. Les matchs en cours ne sont pas affectés : ils jouent sur des copies indépendantes. Lancer `/arena save <nom>` après les modifications pour sauvegarder et décharger le modèle.

## Réglages facultatifs

| Commande | Effet |
|---|---|
| `/arena kits <nom> add <kit>` | Limite l'arène aux kits choisis. Sans restriction, tous les kits sont acceptés. |
| `/arena set <nom> maxinstances <nombre>` | Définit le nombre de matchs simultanés autorisés sur l'arène. |
| `/arena set <nom> voidy <hauteur>` | Élimine les joueurs qui tombent sous cette coordonnée Y. Utile pour les maps flottantes et Sumo. |
| `/arena set <nom> buildlimit <hauteur>` | Définit la hauteur maximale de construction. |
| `/arena set <nom> displayname <nom>` | Définit le nom affiché dans les menus. Les codes couleur comme `&a` sont acceptés. |
| `/arena set <nom> icon` | Utilise l'objet tenu en main comme icône de menu. |

Une arène doit avoir au moins deux spawns pour être disponible en match.

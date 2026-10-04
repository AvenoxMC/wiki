# Pack de textures


Valocraft utilise le pack de textures **HrdaValorant** (son du Classic corrigé) ainsi que les modèles et textures Valocraft (armes, skins, fumées, lunette, flashs blancs). Il est **embarqué dans le jar du plugin**.

## Fonctionnement par défaut

1. Au démarrage, le pack est extrait dans `plugins/Valocraft/resourcepack.zip` (et remplacé automatiquement quand le plugin est mis à jour).
2. Il est **servi sur le port Minecraft lui-même** et envoyé à chaque joueur à la connexion.
3. Le lien de téléchargement reprend **l'adresse et le port utilisés par le joueur** pour se connecter.

Aucun port supplémentaire à ouvrir, et ça fonctionne sur **Pterodactyl**.

Un joueur qui refuse le pack voit un message : sans lui, les armes, icônes de capacités et lunettes sont invisibles.

## Commandes joueur

| Commande | Effet |
|---|---|
| `/vc pack send` | (Re)recevoir le pack |
| `/vc pack remove` | Retirer le pack |

## Commandes admin

| Commande | Effet |
|---|---|
| `/vc pack send <joueur\|all>` | Envoyer le pack à un joueur ou à tout le monde |
| `/vc pack remove <joueur\|all>` | Retirer le pack pour un joueur ou tout le monde |
| `/vc pack info` | Affiche le mode et le lien |
| `/vc pack reload` | Recharge le pack après modification |

## Alternatives

À régler dans `config.yml` :

| Objectif | Réglage |
|---|---|
| Utiliser un **port HTTP dédié** | `resource-pack.self-host.http-port: 8164` |
| Utiliser une **URL externe** | `self-host.enabled: false`, puis `resource-pack.url` et `sha1` |

## Lire la console

Pour chaque joueur, la console indique le **lien proposé** et la **réponse du client**, par exemple : `ACCEPTED`, `DECLINED`, `FAILED_DOWNLOAD`, `SUCCESSFULLY_LOADED`.

Voir [Dépannage](page:troubleshooting) si le pack ne se charge pas, et [Développement](page:development) pour régénérer les ressources.

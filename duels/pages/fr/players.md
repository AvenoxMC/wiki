# Joueurs

## File et défis directs

| Objet ou commande | Action |
|---|---|
| Épée « Jouer » / `/queue` | Ouvre le menu des modes ; cliquer sur un kit pour rejoindre sa file. |
| `/duel <joueur> [kit] [arène]` | Défie directement un joueur. Choisir un kit et une arène ; il peut accepter ou refuser via les options cliquables du chat. |
| Boussole / `/spectate [joueur]` | Parcourt les matchs en cours et permet de les regarder, éventuellement en ciblant un joueur. |
| `/stats [joueur]` | Affiche victoires, défaites, éliminations et morts. |
| `/leave` | Quitte une file, abandonne un match ou arrête le mode spectateur. |

## Parties

Utiliser l'étiquette « Créer une party » ou `/party` pour ouvrir le menu.

| Commande | Action |
|---|---|
| `/party invite <joueur>` | Invite un joueur (message cliquable). |
| `/party accept <chef>` | Accepte l'invitation d'un chef. |
| `/party open` | Rend la party publique. |
| `/party chat <message>` ou `@message` | Envoie un message dans le chat de party. |

Le chef lance une partie depuis le menu :

- **FFA** : chacun pour soi.
- **Équipes** : la party est divisée en deux équipes aléatoires.
- **Défier une party** : party contre party ; l'autre chef accepte le défi.

## Lobby

Utiliser le lit ou `/lobby` (`/hub`) pour quitter le match et revenir au lobby. Si `lobby-server` est renseigné dans `config.yml`, le joueur est envoyé sur ce serveur (par exemple `lobby1`) ; sinon, il revient au lobby Duels.

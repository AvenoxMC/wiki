# Modes de jeu


L'hôte choisit le mode en créant la partie (menu « Créer une partie ») ou en salle d'attente. Un admin fixe le mode par défaut d'une map avec `/vc map setmode <map> <mode>`. Les réglages de chaque mode sont dans la section `modes` de `config.yml`.

## Les 8 modes

| Mode | Clé | Règles |
|---|---|---|
| **Non classé** | `unrated` | 13 rounds gagnants, changement de côté après 12, économie, spike, prolongations. |
| **Compétition** | `competitive` | Comme le non classé, avec rang et RR. Quitter la partie coûte des RR. |
| **Swiftplay** | `swiftplay` | Premier à **5 rounds**, changement de côté après 4, économie et spike, sans prolongations. |
| **Replication** | `replication` | Pendant la sélection, chacun vote pour un agent (doublons autorisés) ; **toute l'équipe joue l'agent le plus choisi**. Premier à 5 rounds. |
| **Spike Rush** | `spike_rush` | Premier à 4 rounds (changement après 3). La même arme tirée au sort pour tout le monde, bouclier, capacités pleines, +1 point d'ultime par round, une spike par attaquant. |
| **Deathmatch** | `deathmatch` | Chacun pour soi, sans agents. Réapparition en 1,5 s, armes gratuites 10 s après la réapparition, une élimination soigne. 40 éliminations ou 6 min. |
| **Team Deathmatch** | `team_deathmatch` | Deux équipes avec agents, réapparition en 2 s, armes gratuites, orbes d'ultime. 100 éliminations ou 9 min 30. |
| **Escalation** | `escalation` | Deux équipes, réapparition, sans capacités : chaque niveau impose une arme (voir plus bas). |

## Escalation

- Ordre des armes par défaut : Odin, Ares, Phantom, Vandal, Spectre, Judge, Bulldog, Guardian, Sheriff, Marshal, Operator, puis **couteau**.
- Il faut **3 éliminations d'équipe** pour passer au niveau suivant (`kills-per-level`) ; au dernier niveau, **une seule élimination au couteau** suffit.
- Toute l'équipe change d'arme en même temps. Pas de boutique.
- La première équipe qui termine le dernier niveau gagne ; sinon, au bout de 10 min, l'équipe la plus avancée.
- La barre de boss et le tableau de droite affichent le niveau de chaque équipe.

```yaml
modes:
  escalation:
    time-limit: 600
    kills-per-level: 3
    levels: [odin, ares, phantom, vandal, spectre, judge, bulldog, guardian, sheriff, marshal, operator, knife]
```

## Modes à réapparition

Deathmatch, Team Deathmatch et Escalation : 2 s de protection à l'apparition (sauf si on tire), point d'apparition le plus loin possible des ennemis. Un spray est disponible toutes les 30 s.

## Compétition

- Rangs : Fer, Bronze, Argent, Or, Platine, Diamant, Ascendant et Immortel (3 divisions chacun), puis Radiant.
- **5 parties de placement**, puis RR selon le résultat (+20 / -16), la performance (score de combat) et l'écart de niveau entre les équipes. Un abandon coûte -30 RR.
- Une partie lancée par `/vc forcestart` ne compte pas pour le classé.

Voir aussi [Progression et cosmétiques](page:progression).

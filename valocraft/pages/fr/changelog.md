# Journal des modifications

Toutes les évolutions de Valocraft, une reproduction de Valorant sous forme de plugin Paper (API 1.21.4, Java 21).
Version anglaise : [CHANGELOG.md](CHANGELOG.md).

---

## [2.2]

> Installation : remplacer l'ancien jar par `Valocraft-2.2.jar` dans `plugins/`. Le pack de textures est mis à jour automatiquement.

### Ajouts

#### Interface et visuels
- **Tableau des scores complet (Tab)**, aligné en colonnes. En haut : map, round, phase, temps, score et camp (`game.custom-tab`).

  | | Alliés | Ennemis |
  |---|---|---|
  | Agent et pseudo | ✔ | ✔ (barré si mort) |
  | Crédits | crédits actuels | crédits **au début de la phase d'achat** |
  | Arme | arme en main | – |
  | Vie | PV + bouclier | – |
  | K / D / A | ✔ | ✔ |
  | Ultime | points ou PRÊTE | points ou PRÊTE |

- **Mini-map tactique** pour Sky Smoke, Dark Cover, Orbital Strike et From the Shadows :
  - carte de la map vue du dessus, avec les sites, les coéquipiers, les fumées et la portée maximale ;
  - ZQSD pour déplacer le curseur, clic gauche pour poser, clic droit pour annuler (`agents.tactical-map`).
- **Les fumées cachent vraiment** :
  - fumées et murs en modèles 3D opaques et teintés, visibles de loin ;
  - un ennemi dans une fumée ou derrière disparaît de l'écran, quelle que soit la distance (`agents.smokes-hide-players`, `agents.solid-smokes`).
- **Têtes d'agents** portées par chaque joueur, quand le skin complet est désactivé (`agents.full-skin: false`, voir Agents).
- **Boutique du lobby et Radianite (◆)** :
  - gagnée à chaque fin de partie : victoire 150, défaite 60, +5 par élimination, +2 par assistance, +5 par round gagné, +50 pour le MVP ;
  - agents à débloquer ;
  - 6 collections de skins d'armes (Prime, Reaver, Glitchpop, Ion, Elderflame, Oni) pour 18 armes, soit 108 modèles ;
  - achat en deux clics (confirmation).

#### Modes de jeu

| Mode | Règles |
|---|---|
| **Non classé** | 13 rounds gagnants, économie, spike, prolongations. |
| **Compétition** | Comme le non classé, avec rang et RR. |
| **Swiftplay** | Premier à 5 rounds, changement de côté après 4, économie et spike, sans prolongations (`modes.swiftplay`). |
| **Replication** | Pendant la sélection, chacun vote pour un agent (doublons autorisés). Toute l'équipe joue ensuite l'agent le plus choisi. Premier à 5 rounds (`modes.replication`). |
| **Escalation** | Deux équipes, réapparition, sans capacités. Chaque niveau impose une arme : Odin, Ares, Phantom, Vandal, Spectre, Judge, Bulldog, Guardian, Sheriff, Marshal, Operator, puis **couteau**. 3 éliminations d'équipe par niveau (1 au couteau) : la première équipe qui finit gagne, sinon la plus avancée après 10 min (`modes.escalation`). |
| **Spike Rush** | Premier à 4 rounds, la même arme tirée au sort pour tout le monde, capacités pleines, une spike par attaquant. |
| **Deathmatch** | Chacun pour soi, réapparition en 1,5 s, armes gratuites 10 s après la réapparition, une élimination soigne. 40 éliminations ou 6 min. |
| **Team Deathmatch** | Deux équipes avec agents, réapparition, armes gratuites. 100 éliminations ou 9 min 30. |

- L'hôte choisit le mode en créant la partie. `/vc map setmode <map> <mode>` fixe le mode par défaut d'une map.
- Dans les modes à réapparition, on a 2 s de protection à l'apparition. Le point d'apparition est choisi le plus loin possible des ennemis.
- **Classé (mode Compétition)** :
  - rangs Fer, Bronze, Argent, Or, Platine, Diamant, Ascendant et Immortel (3 divisions chacun), puis Radiant ;
  - 5 parties de placement ;
  - RR selon le résultat (+20 / -16), la performance (score de combat) et l'écart de niveau entre les équipes ;
  - quitter coûte -30 RR.

#### Agents (29 au total)

13 nouveaux agents :

| Agent | C | Q | E | X |
|---|---|---|---|---|
| **Breach** | Aftershock | Flashpoint | Fault Line | Rolling Thunder |
| **Astra** | Gravity Well | Nova Pulse | Nebula | Cosmic Divide |
| **Fade** | Prowler | Seize | Haunt | Nightfall |
| **Tejo** | Stealth Drone | Special Delivery | Guided Salvo | Armageddon |
| **Clove** | Pick-me-up | Meddle | Ruse | Not Dead Yet |
| **Deadlock** | GravNet | Sonic Sensor | Barrier Mesh | Annihilation |
| **Veto** | Crosscut | Chokehold | Interceptor | Evolution |
| **Iso** | Contingency | Undercut | Double Tap | Kill Contract |
| **Chamber** | Trademark | Headhunter | Rendezvous | Tour de Force |
| **KAY/O** | FRAG/ment | FLASH/drive | ZERO/point | NULL/cmd |
| **Vyse** | Razorvine | Shear | Arc Rose | Steel Garden |
| **Yoru** | Fakeout | Blindside | Gatecrash | Dimensional Drift |
| **Waylay** | Saturate | Lightspeed | Refract | Convergent Paths |

Un agent original : **Miks** (contrôleur).

| C | Q | E | X |
|---|---|---|---|
| M-Pulse (clic gauche sonne, clic droit soigne) | Harmonize (stim pour l'allié visé et soi) | Waveform (fumées par carte tactique) | Bassquake (onde qui repousse, ralentit et assourdit) |

- Nouveaux états :
  - **supprimé** : plus de capacités ;
  - **gêné** : cadence réduite et ralenti ;
  - **bloqué** : arme principale inutilisable ;
  - **immunisé** : aucun effet négatif.
- Capacités de balise en deux temps (Rendezvous, Gatecrash, Refract, Crosscut, Arc Rose) : la première utilisation pose la balise, la seconde l'utilise.
- **Pilotage à la première personne** du drone de Sova, du tigre de Skye et du drone de Tejo :
  - tu deviens la créature, ton corps reste sur place et peut être tué ;
  - clic gauche = action de la créature, clic droit = retour dans ton corps.
- **Skin complet de l'agent** : pendant la partie, tout le skin du joueur devient celui de son agent, pas seulement la tête. Le skin d'origine revient au lobby (`agents.full-skin`).
- **Compatibilité SkinsRestorer** (optionnelle) :
  - MineSkin signe les skins d'agents : le joueur voit aussi son propre skin d'agent (vue F5, bras) ;
  - les skins signés sont créés en arrière-plan au démarrage et gardés dans `data/agent-skins.yml` ;
  - le skin de n'importe quel agent peut être remplacé par l'URL d'une image de skin ou un pseudo Minecraft (`agents.skins.<agent>`).

#### Capacités
- **Activation manuelle** : la touche 5 à 8 prend la capacité en main, le clic gauche l'utilise. Plus rien ne part en changeant de slot (`controls.instant-abilities: true` pour l'ancien comportement).
- **Flashs blancs** : écran entièrement blanc qui s'estompe en 4 étapes, plus de vision noire. Pas de lunette pendant un flash.
- **Lancers maintenus avec trajectoire** :
  - maintenir le clic gauche affiche l'arc (visible de toi seul), relâcher lance ;
  - clic droit = lancer en cloche ;
  - les flèches de Sova vont plus loin quand on maintient plus longtemps.
- **Recharge visible** : l'icône de la signature reste dans la barre avec le balayage de recharge de Minecraft.
- **Utilitaire destructible** : les balles ennemies détruisent les objets posés.

  | Objet | PV |
  |---|---|
  | Tourelle | 125 |
  | Caméra | 70 |
  | Leer, Interceptor | 60 |
  | Sonic Sensor, Chokehold, Trademark, Shear | 40 |
  | Alarmbot, Trapwire, Nanoswarm | 20 |

- **Ultimes ennemies** : leurs points sont affichés dans le tab. Une alerte (chat et son) prévient quand une ultime ennemie est prête.
- **Kits plus fidèles** :
  - **Neon** : jauge d'énergie, High Gear active / coupe le sprint, et s'accroupir en sprint fait une glissade ;
  - **Viper** : jauge de carburant, Poison Cloud et Toxic Screen deviennent des émetteurs qu'on active et coupe ;
  - **Jett** : Tailwind se prépare, puis on déclenche le dash ;
  - **Iso** : Kill Contract ouvre une arène de verre en 1v1 au-dessus de la map ;
  - **Chamber** : Tour de Force a une lunette plein écran au clic droit ;
  - **Brimstone** : fumées orange.
- **`abilities.yml`** : prix, charges, recharge, recharge par élimination et dégâts de chaque capacité, coût des ultimes, multiplicateurs globaux de dégâts et de durée. Pris en compte avec `/vc reload`, sans recompiler.

#### Maps et chargement
- **Mondes des maps chargés à la demande** :
  - ils restent sur le disque et ne sont plus chargés au démarrage du serveur ;
  - au lancement d'une partie, le serveur charge le monde, précharge les chunks des spawns et y place tout le monde ;
  - un monde inutilisé est sauvegardé puis déchargé (`maps.unload-check`).
- La **salle d'attente** et la **sélection d'agent** se font au lobby.
- **Écran de chargement** : pendant le chargement de la map, un menu montre la carte (bannière), l'agent et le titre de chaque joueur, équipe rouge en haut et bleue en bas (`game.loading-time`).
- **Les cartes de joueur sont de vraies bannières** : couleur de l'agent et symbole de son rôle. Elles apparaissent dans la boutique, à l'écran de chargement et dans le résumé de match.

#### Progression et cosmétiques
- **Battle pass** :
  - 30 niveaux de 1 000 XP ;
  - XP gagnée à chaque partie : victoire 600, défaite 300, +20 par élimination, +10 par assistance, +30 par round gagné, +150 pour le MVP ;
  - une récompense par niveau, donnée automatiquement : Radianite, cartes, titres, bannières et sons d'élimination, sprays ;
  - menu `/vc pass`. Changer `battlepass.season` remet tout le monde au niveau 0 ; les récompenses gagnées restent.
- **Bannières d'élimination** : à chaque élimination, ton symbole s'affiche autant de fois que tes éliminations du round, aux couleurs de ta carte. La victime voit ta carte et ton titre. 8 styles : ❱ ✦ ❤ ☠ ⚡ ✪ ⚔ ♛.
- **Sons d'élimination** :
  - la note monte à chaque élimination du round, avec un son spécial au 5e ;
  - 7 sons : Valorant, Carillon, Cloche, Xylophone, Pièces, Rétro 8-bit, Améthyste ;
  - un clic droit dans la boutique permet d'écouter.
- **Sprays** :
  - accroupi + F en partie : ton spray se colle sur le mur, le sol ou le plafond visé ;
  - textes (GG, EZ, NICE, ☠, ❤, ?, ACE, VALOCRAFT) ou emblème de l'un des 29 agents ;
  - un par round, toutes les 30 s dans les modes à réapparition.
- **Classements dans le lobby** : hologrammes posés avec `/vc leaderboard set <type>`, mis à jour toutes les minutes. Types : rang, éliminations, victoires, ACS, headshots, aces, battle pass.
- **Boutique** : 14 couteaux, cartes de joueur, 12 titres, bannières et sons d'élimination, sprays.
- **Missions du jour** : 3 missions tirées au sort chaque jour, 150 ◆ chacune (`/vc missions`).
- **Fin de match** :
  - score de combat, dégâts, premiers sangs, annonce des ACE ;
  - rapport de dégâts à la mort ;
  - menu « Résumé du match » avec les stats de chaque joueur (`/vc resume`).

#### Jeu en équipe et social
- **Demande d'arme** : cliquer sur une arme trop chère la demande à ton équipe. Un coéquipier qui a l'argent clique sur **[Acheter pour …]** : il paie et l'arme arrive directement dans ton inventaire.
- **Groupes d'amis** :
  - `/vc party invite|leave|kick|list|chat` ;
  - le groupe suit son chef dans les parties et reste dans la même équipe.
- **Équipes équilibrées** selon un niveau caché (MMR).
- **Chat** : rang et titre devant les pseudos. Un message qui commence par `!` va à l'équipe seulement.

#### Déroulement des parties
- **Reconnexion** : un joueur déconnecté en pleine partie garde sa place 3 min et y est replacé à son retour.
- **Votes** :
  - `/vc ff` : abandon, à partir du round 5, 80 % de oui ;
  - `/vc remake` : jusqu'au round 3, si un coéquipier est parti.
- **AFK** : un joueur immobile reçoit un avertissement à 45 s et est exclu à 90 s.
- **Compensation de latence** : les tirs sont vérifiés là où le tireur voyait sa cible, jusqu'à 200 ms en arrière.
- **Bruits de pas** :
  - courir s'entend chez les ennemis, avec un son qui dépend du bloc ;
  - marcher accroupi est silencieux.
- **Radar permanent** : une carte en main gauche montre les alliés, les ennemis repérés, la spike, les sites et les fumées de l'équipe.

#### Administration
- `/vc forcestart [map]` : lance la partie même avec un seul joueur. Une équipe vide n'est jamais « éliminée » et la partie ne compte pas en classé.
- `/vc ult add|set <joueur> [points]` : ajoute ou fixe les points d'ultime (`set` sans nombre = ultime pleine).
- `/vc pass addxp <joueur> <xp>` : donne de l'XP de battle pass.
- `/vc leaderboard set <type> | remove | list` : classements du lobby.
- **Tous les agents débloqués par défaut** (`progression.default-agents: [ALL]`).
- **Stockage SQLite / MySQL** (`storage.type`), avec import automatique depuis `stats.yml`.
- Admin Radianite : `/vc radianite give|take|set <joueur> <montant>`, `/vc radianite voir <joueur>`.

### Corrections
- **Icônes de capacités** :
  - Cove de Harbor affichait une icône de Gekko (entrée manquante dans le pack) ;
  - les icônes de Trademark et Rendezvous (Chamber) étaient inversées ;
  - les icônes de FRAG/ment et FLASH/drive (KAY/O) étaient inversées.

  La table des icônes du pack est maintenant reconstruite à partir des images qui existent vraiment.
- Le clic droit pour quitter un drone ou un tigre piloté fonctionne (une télécommande dédiée est utilisée).
- **Lunette des snipers** : vrai viseur plein écran en 16:9, porté par le casque, qui ne clignote plus.
- **Tir continu** :
  - maintenir le clic gauche tire à la vraie cadence de l'arme ;
  - les armes peuvent « miner » le bloc visé jusqu'à 64 blocs (rien n'est cassé), donc le client envoie un signal à chaque tick ;
  - l'animation de coup de bras est masquée.

---

## [2.1] — Mise à jour des agents

### Ajouts

#### 15 agents
Une phase de **sélection d'agent** (25 s) s'ouvre après le compte à rebours. Chaque agent est unique dans une équipe. Un joueur qui ne choisit pas reçoit un agent libre au hasard.

| Rôle | Agents |
|---|---|
| Duellistes | Jett, Phoenix, Raze, Reyna, Neon |
| Initiateurs | Sova, Skye, Gekko |
| Contrôleurs | Brimstone, Omen, Viper, Harbor |
| Sentinelles | Sage, Killjoy, Cypher |

- **Contrôles** :
  - touches **5 / 6 / 7 / 8** = **C / Q / E / X** ;
  - clic gauche pour lancer, clic droit pour la variante quand il y en a une ;
  - les objets guidés (drone de Sova, faucon et tigre de Skye, Thrash de Gekko) suivent le regard ;
  - Jett plane en maintenant la touche de saut.
- **États** :

  | État | Effet |
  |---|---|
  | Sonné | ralenti, la vue tangue |
  | Aveuglé | vision noire (flashs, Leer, Paranoia, Dizzy, Seekers) |
  | Vulnérable | +50 % de dégâts reçus |
  | Immobilisé | ni tir, ni capacité |
  | Révélé | contour lumineux visible à travers les murs |
  | Intangible | aucun dégât |

#### Système d'ultime
- Points gagnés avec les éliminations, les morts, la pose et le désamorçage de la spike, et les **orbes d'ultime**. Ils sont conservés à la mi-temps.
- Progression affichée en permanence dans la barre d'action. Quand l'ultime est prête : titre, son et message à l'équipe.
- Ultime lancée : tout le monde entend la réplique de l'agent.
- Orbes d'ultime : `/vc map addorb <map>`. Maintenir clic droit 1,5 s à côté d'un orbe donne +1 point.

#### Autres ajouts
- **Tyroliennes** : `/vc map addzipline <map>`. En jeu, F pour s'accrocher, saut ou accroupi pour lâcher.
- **Lobby et matchmaking** : objets « Rejoindre un match », « Statistiques » et « Créer une partie ».
- **Modèles 3D** pour toutes les armes, dont 11 nouveaux modèles : Shorty, Frenzy, Stinger, Bucky, Judge, Bulldog, Guardian, Phantom, Marshal, Outlaw, Odin.
- **Contrôles Valorant** : clic gauche pour tirer, clic droit maintenu pour viser.
- **Pack de textures** servi par le port Minecraft lui-même (compatible Pterodactyl) et mis à jour automatiquement.
- **`/vc pack send | remove`**, et en admin `/vc pack send <joueur|all>`, `/vc pack info`, `/vc pack reload`.
- **Import de maps** depuis ommo.me (`/vc import`), réservé aux serveurs privés (licence CC BY-NC-ND 4.0).

### Corrections
- L'écran ne « revient plus en arrière » pendant les rafales : le recul est entièrement dans la trajectoire des balles.

---

## [2.0]

### Ajouts
- **Jeu de base** :
  - rounds à la Valorant avec économie et phase d'achat ;
  - pose et désamorçage de la spike ;
  - murs pendant la phase d'achat, prolongations.
- **Armes** :
  - tout l'arsenal de Valorant, avec baisse des dégâts selon la distance, schémas de recul et pénétration des murs ;
  - boucliers.
- **Maps** : commandes de configuration (`/vc map ...`).
- **Serveur et pack** :
  - hébergement automatique du pack de textures ;
  - compatibilité Pterodactyl.

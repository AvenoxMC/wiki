# Agents


Valocraft compte **29 agents** répartis en quatre rôles. Tous sont débloqués par défaut (`progression.default-agents: [ALL]`).

## Sélection d'agent

Après le compte à rebours, la **sélection d'agent** (25 s) s'ouvre **au lobby**, dans un menu :

- Chaque agent est **unique dans une équipe**, sauf en mode [Replication](page:modes) où toute l'équipe joue l'agent le plus choisi.
- Un joueur qui ne choisit pas reçoit un **agent libre au hasard**.
- La **réplique** de l'agent est jouée à toute l'équipe au verrouillage.
- Pendant la partie, le joueur prend le **skin complet** de son agent (voir plus bas).

**Lire les tableaux :** les prix sont en ¤ ; *max* = nombre de charges maximum ; *offert* = donné à chaque round ; *recharge* = temps pour regagner la charge offerte. Le coût des ultimes est en **points** ([Système d'ultime](page:ultimate)). Touches **5 / 6 / 7 / 8** = **C / Q / E / X**, puis **clic gauche** pour utiliser ([Contrôles](page:controls)). Les charges s'achètent sur la ligne du bas de la boutique. Tout est modifiable dans `abilities.yml` ([Configuration](page:configuration)).

## Duellistes

| Agent | C | Q | E (signature) | X (ultime) |
|---|---|---|---|---|
| **Jett** | **Cloudburst** : lance une fumée qui bloque la vue (200 ¤, max 2) | **Updraft** : propulse Jett dans les airs (150 ¤, max 2) | **Tailwind** : utilise pour préparer le vent (7,5 s), réutilise pour dasher. Revient après 2 éliminations (offert) | **Blade Storm** : 5 couteaux précis. Une élimination les recharge — **8 pts** |
| **Phoenix** | **Blaze** : mur de flammes qui bloque la vue et soigne Phoenix (200 ¤) | **Curveball** : flash courbée : clic gauche vers la gauche, clic droit vers la droite (250 ¤, max 2) | **Hot Hands** : boule de feu : zone qui brûle les ennemis et soigne Phoenix (offert) | **Run it Back** : pendant 10 s, si Phoenix meurt il renaît au point de départ — **6 pts** |
| **Raze** | **Boom Bot** : robot qui fonce vers l'ennemi le plus proche et explose (300 ¤) | **Blast Pack** : charge qui projette tout le monde autour (Raze compris) (200 ¤, max 2) | **Paint Shells** : grenade à fragmentation. Revient après 2 éliminations (offert) | **Showstopper** : lance-roquettes : une roquette dévastatrice — **8 pts** |
| **Reyna** | **Leer** : œil qui aveugle les ennemis qui le regardent (250 ¤, max 2) | **Devour** : après une élimination (3 s) : récupère 100 PV (200 ¤, max 2) | **Dismiss** : après une élimination (3 s) : invulnérable et rapide 2 s (offert, max 2) | **Empress** : 30 s de frénésie : cadence et vitesse augmentées — **6 pts** |
| **Neon** | **Fast Lane** : deux murs d'électricité qui bloquent la vue (300 ¤) | **Relay Bolt** : éclair qui rebondit puis sonne les ennemis proches (200 ¤, max 2) | **High Gear** : active / coupe le sprint (jauge d'énergie). Accroupi en sprint : glissade (offert) | **Overdrive** : 12 s : rayon électrique précis et vitesse maximale — **7 pts** |
| **Iso** | **Contingency** : mur d'énergie qui avance et bloque la vue (200 ¤) | **Undercut** : éclair qui traverse les murs et rend vulnérable (200 ¤, max 2) | **Double Tap** : bouclier qui absorbe une balle (12 s). Revient après 2 éliminations (offert) | **Kill Contract** : contrat : Iso et l'ennemi touché s'affrontent seuls dans une arène (15 s) — **7 pts** |
| **Yoru** | **Fakeout** : leurre qui avance et aveugle les ennemis qui l'approchent (100 ¤) | **Blindside** : flash qui rebondit (250 ¤, max 2) | **Gatecrash** : pose une faille (clic gauche), puis téléporte-toi dessus (clic gauche) (offert, recharge 35 s) | **Dimensional Drift** : 10 s invisible et intouchable (sans tirer). Clic gauche pour sortir — **8 pts** |
| **Waylay** | **Saturate** : orbe de lumière qui ralentit et gêne (cadence réduite) (200 ¤) | **Lightspeed** : deux dashes rapides (150 ¤) | **Refract** : pose une balise ici (clic gauche), puis reviens-y (clic gauche, 8 s) (offert, recharge 30 s) | **Convergent Paths** : rayon qui ralentit et gêne tous les ennemis devant toi — **8 pts** |

## Initiateurs

| Agent | C | Q | E (signature) | X (ultime) |
|---|---|---|---|---|
| **Sova** | **Owl Drone** : drone guidé par le regard qui révèle les ennemis proches (400 ¤) | **Shock Bolt** : flèche explosive (clic gauche : 1 rebond, clic droit : aucun) (150 ¤, max 2) | **Recon Bolt** : flèche qui révèle les ennemis à portée de vue (offert, recharge 40 s) | **Hunter's Fury** : 3 tirs d'énergie qui traversent les murs — **8 pts** |
| **Skye** | **Regrowth** : soigne les alliés proches (60 PV) (200 ¤) | **Trailblazer** : tigre guidé par le regard qui sonne l'ennemi touché (250 ¤) | **Guiding Light** : faucon guidé qui explose en flash (offert, +250 ¤, max 2, recharge 40 s) | **Seekers** : 3 traqueurs qui poursuivent les 3 ennemis les plus proches — **8 pts** |
| **Gekko** | **Mosh Pit** : créature qui explose en flaque très dangereuse (250 ¤) | **Wingman** : créature qui avance et sonne le premier ennemi rencontré (300 ¤) | **Dizzy** : créature volante qui aveugle les ennemis en vue (offert, recharge 30 s) | **Thrash** : créature guidée qui immobilise les ennemis à l'impact — **8 pts** |
| **Breach** | **Aftershock** : charge à travers un mur : 3 explosions de l'autre côté (200 ¤) | **Flashpoint** : flash qui traverse le mur visé (250 ¤, max 2) | **Fault Line** : onde sismique en ligne droite qui sonne les ennemis (offert, recharge 35 s) | **Rolling Thunder** : séisme en cône : sonne et projette les ennemis — **9 pts** |
| **Fade** | **Prowler** : créature guidée qui aveugle le premier ennemi rencontré (250 ¤, max 2) | **Seize** : orbe qui immobilise et rend vulnérables les ennemis (200 ¤) | **Haunt** : œil lancé qui révèle les ennemis en vue (offert, recharge 40 s) | **Nightfall** : vague de cauchemar : révèle et affaiblit les ennemis touchés — **8 pts** |
| **Tejo** | **Stealth Drone** : drone guidé qui révèle, puis supprime en fin de course (300 ¤) | **Special Delivery** : grenade collante qui sonne (200 ¤) | **Guided Salvo** : carte tactique : missile sur le point choisi (offert, max 2, recharge 40 s) | **Armageddon** : carte tactique : tapis de bombes en ligne (dans l'axe de ton regard) — **8 pts** |
| **KAY/O** | **FRAG/ment** : grenade qui explose plusieurs fois (200 ¤) | **FLASH/drive** : flash : clic gauche normal, clic droit rapide (250 ¤, max 2) | **ZERO/point** : couteau qui supprime les capacités des ennemis proches (offert, recharge 40 s) | **NULL/cmd** : 12 s d'impulsions de suppression, cadence et vitesse — **8 pts** |

## Contrôleurs

| Agent | C | Q | E (signature) | X (ultime) |
|---|---|---|---|---|
| **Brimstone** | **Stim Beacon** : zone qui accélère la cadence de tir et la vitesse des alliés (200 ¤) | **Incendiary** : grenade incendiaire : zone de feu (250 ¤) | **Sky Smoke** : place une fumée là où tu vises (longue portée) (offert, +100 ¤, max 3) | **Orbital Strike** : frappe orbitale dévastatrice sur la zone visée — **8 pts** |
| **Omen** | **Shrouded Step** : téléportation courte là où tu vises (100 ¤, max 2) | **Paranoia** : ombre qui traverse les murs et aveugle tout sur son passage (300 ¤) | **Dark Cover** : fumée longue portée là où tu vises (offert, +150 ¤, max 2, recharge 30 s) | **From the Shadows** : téléportation n'importe où sur la map — **7 pts** |
| **Viper** | **Snake Bite** : fiole d'acide : dégâts et vulnérabilité (200 ¤, max 2) | **Poison Cloud** : émetteur de nuage toxique, à activer / couper (carburant) (200 ¤) | **Toxic Screen** : long mur toxique à activer / couper (carburant) (offert) | **Viper's Pit** : immense nuage toxique autour de Viper : les ennemis n'y voient rien — **9 pts** |
| **Harbor** | **Cascade** : vague qui avance, bloque la vue et ralentit (150 ¤) | **Cove** : sphère d'eau qui bloque la vue (350 ¤) | **High Tide** : long mur d'eau qui ralentit (offert) | **Reckoning** : 3 geysers qui sonnent les ennemis dans la zone visée — **7 pts** |
| **Astra** | **Gravity Well** : carte tactique : attire les ennemis puis les rend vulnérables (150 ¤) | **Nova Pulse** : carte tactique : impulsion qui sonne (150 ¤) | **Nebula** : carte tactique : fumée n'importe où sur la map (offert, +150 ¤, max 2, recharge 25 s) | **Cosmic Divide** : carte tactique : mur cosmique géant qui bloque la vue (dans l'axe de ton regard) — **7 pts** |
| **Clove** | **Pick-me-up** : après une élimination ou une assistance (3 s) : soin et vitesse (100 ¤) | **Meddle** : fragment qui affaiblit temporairement les ennemis (dégradation) (250 ¤) | **Ruse** : carte tactique : fumées n'importe où (2 offertes, max 2, recharge 40 s) | **Not Dead Yet** : s'active automatiquement à ta mort : tu reviens, élimine ou assiste en 12 s — **8 pts** |
| **Miks** | **M-Pulse** : onde sonore : clic gauche sonne les ennemis, clic droit soigne les alliés (250 ¤) | **Harmonize** : stim de combat pour l'allié visé et toi (clic droit : toi seul) (200 ¤) | **Waveform** : carte tactique : mur d'ondes sonores qui bloque la vue (offert, +150 ¤, max 2, recharge 30 s) | **Bassquake** : onde de choc devant toi : repousse, ralentit et assourdit — **8 pts** |

## Sentinelles

| Agent | C | Q | E (signature) | X (ultime) |
|---|---|---|---|---|
| **Sage** | **Barrier Orb** : érige un mur de glace solide (400 ¤) | **Slow Orb** : zone qui ralentit tous ceux qui la traversent (200 ¤, max 2) | **Healing Orb** : soigne un allié visé (clic gauche) ou soi-même (clic droit) (offert, recharge 45 s) | **Resurrection** : ressuscite un allié mort visé — **8 pts** |
| **Killjoy** | **Nanoswarm** : grenade qui libère un essaim de nanobots (200 ¤, max 2) | **Alarmbot** : piège : rend vulnérable et révèle l'ennemi qui approche (200 ¤) | **Turret** : tourelle qui tire sur les ennemis pendant 30 s (offert) | **Lockdown** : après 10 s, immobilise les ennemis dans un grand rayon — **8 pts** |
| **Cypher** | **Trapwire** : fil tendu entre deux murs : révèle et ralentit qui le franchit (200 ¤, max 2) | **Cyber Cage** : petite fumée lancée (100 ¤, max 2) | **Spycam** : caméra murale qui révèle les ennemis en vue (45 s) (offert) | **Neural Theft** : vise un ennemi mort : révèle tous les ennemis deux fois — **6 pts** |
| **Deadlock** | **GravNet** : grenade qui force les ennemis à s'accroupir (200 ¤) | **Sonic Sensor** : capteur qui sonne les ennemis qui font du bruit (200 ¤) | **Barrier Mesh** : barrière en croix qui bloque le passage (offert) | **Annihilation** : emprisonne le premier ennemi touché : il meurt au bout de 7 s — **7 pts** |
| **Veto** | **Crosscut** : pose une balise (clic gauche), puis téléporte-toi dessus (clic gauche) (200 ¤) | **Chokehold** : piège qui immobilise et rend vulnérable (200 ¤, max 2) | **Interceptor** : dispositif qui détruit l'utilitaire ennemi proche (15 s) (offert) | **Evolution** : 25 s : immunisé aux effets, régénération, vitesse et cadence — **7 pts** |
| **Chamber** | **Trademark** : piège qui ralentit et révèle les ennemis (200 ¤) | **Headhunter** : pistolet lourd : une charge = une balle (159 à la tête) (100 ¤, max 8) | **Rendezvous** : pose une ancre (clic gauche), puis téléporte-toi dessus (clic gauche, 25 blocs) (offert, recharge 30 s) | **Tour de Force** : sniper : 5 balles mortelles, ralentit autour des éliminés — **8 pts** |
| **Vyse** | **Razorvine** : ronces qui blessent et ralentissent (150 ¤) | **Shear** : piège : un mur se dresse quand un ennemi passe (200 ¤) | **Arc Rose** : pose une rose (clic gauche), puis fais-la flasher (clic gauche) (offert, recharge 30 s) | **Steel Garden** : bloque les armes principales des ennemis proches pendant 8 s — **8 pts** |

> **Miks** est un agent original de Valocraft.

## Mécaniques des capacités

- **Activation manuelle** : la touche prend la capacité en main, le **clic gauche** l'utilise. `controls.instant-abilities: true` rétablit le déclenchement à l'appui sur la touche.
- **Lancers maintenus** : pour les objets lancés (grenades, fumées de Jett, flèches de Sova, Nanoswarm...), maintenir le clic gauche affiche la **trajectoire** (visible de toi seul), relâcher lance. **Clic droit** : lancer en cloche, sauf pour les capacités qui ont une variante au clic droit.
- **Recharge visible** : l'icône de la signature reste dans la barre, grisée par le balayage de recharge.
- **Pilotage à la première personne** : drone de Sova, tigre de Skye et drone de Tejo. Tu deviens la créature, ton corps reste sur place et peut être tué. Clic gauche = action, clic droit = retour dans ton corps.
- **Capacités de balise** (Rendezvous, Gatecrash, Refract, Crosscut, Arc Rose) : le premier clic pose la balise, le second l'utilise.
- **Carte tactique** (Sky Smoke, Dark Cover, Orbital Strike, From the Shadows, Nebula, Ruse, Waveform, Guided Salvo...) : une carte vue du dessus s'ouvre ; ZQSD pour viser, clic gauche pour poser, clic droit pour annuler.
- **Jauges** affichées dans la barre d'action : énergie de **Neon** (High Gear vide la jauge, les éliminations la remplissent), carburant de **Viper** (émetteurs actifs = consommation), vent préparé de **Jett**.
- **Utilitaire destructible** : les balles ennemies détruisent la tourelle (125 PV), la caméra (70), Leer et Interceptor (60), Sonic Sensor, Chokehold, Trademark et Shear (40), Alarmbot, Trapwire et Nanoswarm (20).

## États

| État | Effet | Causé par |
|---|---|---|
| **Sonné** | Ralenti, la vue tangue | Capacités qui sonnent |
| **Aveuglé** | Écran **blanc** qui s'estompe (flashs) ou vision réduite | Flashs, Leer, Paranoia, Dizzy, Seekers |
| **Vulnérable** | +50 % de dégâts reçus | Alarmbot, Snake Bite, Seize, Undercut... |
| **Immobilisé** | Ni tir ni capacité | Lockdown, Thrash, Chokehold |
| **Supprimé** | Plus de capacités | ZERO/point, NULL/cmd, Stealth Drone |
| **Gêné** | Cadence réduite, ralenti | Saturate, Convergent Paths |
| **Bloqué** | Arme principale inutilisable | Steel Garden |
| **Immunisé** | Aucun effet négatif | Evolution (Veto) |
| **Révélé** | Contour lumineux visible à travers les murs | Capacités de révélation |
| **Intangible** | Aucun dégât | Dismiss, Dimensional Drift |

## Apparence des agents

- **Skin complet** : pendant la partie, tout le skin du joueur devient celui de son agent. Le skin d'origine revient au lobby (`agents.full-skin`).
- Avec le plugin **SkinsRestorer**, les skins sont signés : le joueur voit aussi son propre skin d'agent (vue F5, bras). Sans lui, seuls les autres joueurs le voient.
- On peut remplacer le skin d'un agent par une autre image de skin ou un pseudo Minecraft : `agents.skins.<agent>`.
- `agents.full-skin: false` rétablit les **têtes d'agents** (`agents.wear-heads`).

## Fumées

Les fumées et les murs sont des modèles 3D opaques et teintés (orange pour Brimstone), visibles de loin. Un ennemi dans une fumée ou derrière est masqué, quelle que soit la distance ; à moins de 2,5 blocs, on se voit. Les balles traversent les fumées. Réglages : `agents.smokes-hide-players`, `agents.solid-smokes`.

## Équilibrage

Les capacités n'ont pas encore été équilibrées en partie réelle : vos retours sont les bienvenus. Les valeurs se règlent dans `abilities.yml`, sans recompiler.

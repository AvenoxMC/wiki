# Changelog

## 2.2

### Interface de partie

- Ajout d'un **tableau des scores avec Tab**, en colonnes comme dans Valorant. Il affiche la map, le round, la phase, le temps, le score et les camps. Les crédits, l'arme, la santé/le bouclier, le K/D/A et l'état de l'ultime des alliés sont visibles. Les crédits des ennemis correspondent au début de la phase d'achat ; leur arme, leur santé et leur ultime sont masqués, et le pseudo des morts est barré. La liste vanilla des joueurs est masquée pendant une partie. `game.custom-tab: false` désactive le tableau personnalisé.

### Ciblage tactique des capacités

- Sky Smoke et Orbital Strike de Brimstone, ainsi que Dark Cover et From the Shadows d'Omen, ouvrent une carte tactique vue du dessus, avec rendu des blocs et ombrage du relief.
- La carte montre les sites, les coéquipiers, les fumées et murs alliés, la portée de la capacité et le point visé. Déplacer le curseur avec **ZQSD** (ou **WASD** sur QWERTY) ; sprinter pour accélérer. Clic gauche pour confirmer ; clic droit ou accroupi pour annuler. Le joueur reste immobile pendant le ciblage.
- Brimstone peut placer ses Sky Smokes à la suite tant qu'il lui reste des charges. Les fumées tombent du ciel et se déploient à l'atterrissage.
- La zone est calculée à partir des spawns, sites, murs et orbes. La définir avec `/vc map setminimap <map>` et la sélection de la baguette ; `/vc map clearminimap <map>` rétablit le calcul automatique. `agents.tactical-map: false` rétablit l'ancien ciblage.

### Fumées, murs et apparence des agents

- Les fumées et les murs ont désormais des modèles 3D opaques et teintés, qui gonflent à leur apparition, restent visibles de loin et ne dépendent pas du réglage de particules du client.
- Les ennemis dans une fumée ou derrière elle sont masqués quelle que soit la distance. À moins de 2,5 blocs, les joueurs se voient ; les alliés et les ennemis révélés restent visibles. Les balles traversent toujours les fumées.
- Les joueurs portent la tête de leur agent pendant toute la partie, y compris les ennemis dont le pseudo est masqué. Gekko et Harbor utilisent des têtes de remplacement ressemblantes. Réglages : `agents.smokes-hide-players`, `agents.solid-smokes` et `agents.wear-heads`.

### Radianite, agents et skins d'armes

- Ajout d'un solde de Radianite et d'une boutique au lobby, également accessible avec `/vc boutique`.
- Gains par défaut en fin de partie : **150 ◆** pour une victoire, **60 ◆** pour une défaite, **5 ◆** par élimination, **2 ◆** par assistance, **5 ◆** par round gagné et **50 ◆** pour le MVP. Gains et prix sont réglables dans `progression` de `config.yml`.
- Phoenix, Jett, Sova, Brimstone et Sage sont offerts par défaut ; chacun des dix autres agents coûte **1 000 ◆**. L'attribution aléatoire ne propose que les agents débloqués par le joueur.
- Ajout de six collections de skins pour les 18 armes : **Prime**, **Reaver**, **Glitchpop**, **Ion**, **Elderflame** et **Oni**. Les skins coûtent de 1 000 à 2 000 ◆, s'achètent et s'équipent arme par arme. Une arme ramassée conserve le skin de son propriétaire. L'achat demande une confirmation.
- Commandes admin : `/vc radianite give|take|set <joueur> <montant>` et `/vc radianite voir <joueur>`. Les permissions `valocraft.agents.all` et `valocraft.skins.all` débloquent tous les agents et skins.

### Armes et contrôles

- Remplacement de l'ancienne lunette de sniper (casque citrouille clignotant) par une lunette plein écran 16:9 : lentille ronde et nette, noir autour, réticule fin et point rouge. Les autres joueurs voient toujours la tête de l'agent.
- Maintenir le clic gauche en visant un bloc à **64 blocs** ou moins envoie un signal de tir à chaque tick : les armes tirent à leur cadence réelle. Rien n'est miné, aucune fissure n'est montrée aux autres joueurs et l'animation du bras est masquée. Un clic simple tire toujours une balle ; les armes semi-automatiques tirent aussi à leur cadence maximale tant que le bouton est maintenu. En visant le ciel sans bloc à portée, il faut cliquer. La portée du couteau reste de 3 blocs.
- Réglages : `controls.continuous-fire`, `controls.semi-auto-hold` et `controls.hide-swing`.

### Vérifications

Testé sur Paper 1.21.4 avec deux clients connectés à une partie. Le chargeur du Classic est passé de 12 à 1 balle en 1,5 seconde de tir maintenu ; un clic simple a tiré une balle. La mini-map a placé une fumée au point visé ; les joueurs masqués par une fumée ont disparu de l'écran l'un de l'autre ; Tab a affiché les deux équipes ; les têtes d'agents et les lunettes ont été vérifiées. Le gagnant a reçu 210 Radianites et le perdant 60. Aucune erreur dans la console.

## 2.1 — Agent Update

### Agents et capacités

- Le roster passe à **15 agents** : Jett, Phoenix, Raze, Reyna, Neon, Sova, Skye, Gekko, Brimstone, Omen, Viper, Harbor, Sage, Killjoy et Cypher.
- Ajout d'une **sélection d'agent de 25 secondes** après le compte à rebours. Les agents sont uniques dans une équipe ; un joueur qui ne choisit pas reçoit un agent disponible au hasard. Le menu indique rôle, capacités, prix et coût de l'ultime. La réplique de l'agent est jouée à l'équipe au verrouillage.
- Ajout des états sonné, aveuglé, vulnérable (+50 % de dégâts reçus), immobilisé, révélé et intangible.
- Les touches **5 / 6 / 7 / 8** sélectionnent **C / Q / E / X**. Les capacités instantanées s'activent à l'appui ; les autres se lancent au clic gauche, avec des variantes au clic droit lorsqu'elles existent. Les capacités guidées suivent le regard ; Jett plane en maintenant saut.

### Système d'ultime

- Les points d'ultime s'obtiennent avec les éliminations, les morts, les poses et désamorçages de spike, ainsi que les orbes d'ultime. Ils sont conservés à la mi-temps. La progression apparaît dans la barre d'action ; des notifications annoncent la disponibilité et le lancement à l'agent et à l'équipe.
- Les orbes réapparaissent à chaque round. Maintenir le clic droit 1,5 seconde à côté d'un orbe donne un point. Ajouter ou supprimer les orbes d'une map avec `/vc map addorb <map>` et `/vc map clearorbs <map>`.

### Partie, armes et outils serveur

- Ajout des tyroliennes : les créer avec `/vc map addzipline <map>` entre les deux points sélectionnés à la baguette. Appuyer sur **F** pour s'accrocher, avancer/reculer pour glisser, sauter ou s'accroupir pour lâcher.
- Ajout du matchmaking depuis le lobby, des parties créées par un hôte, des statistiques joueurs et des classements.
- Ajout de 11 modèles 3D Valocraft : Shorty, Frenzy, Stinger, Bucky, Judge, Bulldog, Guardian, Phantom, Marshal, Outlaw et Odin. Le clic gauche tire et le clic droit maintenu permet de viser. Le recul agit désormais sur la trajectoire des balles, sans faire revenir la vue en arrière pendant les rafales.
- Le pack de textures est servi sur le port Minecraft, fonctionne avec Pterodactyl et se met à jour avec le plugin. Ajout de `/vc pack send`, `/vc pack remove`, `/vc pack info` et `/vc pack reload` (avec cibles admin).
- Ajout de l'import de maps depuis ommo.me avec `/vc import`, pour les serveurs privés (CC BY-NC-ND 4.0).

### Adaptations Minecraft

Les fumées sont composées de particules et aveuglent les joueurs à l'intérieur ; les flashs rendent la vision noire plutôt que blanche ; le contour des ennemis révélés est visible par tout le monde. L'équilibrage et les prix des capacités peuvent nécessiter des ajustements en partie réelle.

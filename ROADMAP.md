[CURRENT] v. 0.0.1

[DONE] task-0

Documentation

    * documentation: ROADMAP.md

v. 0.0.0

    Poetry stuff

===============================================================================
A game (chess, tic-tac-toe: [=Game]) has rules;
  A game (=a match, a party) has players [=PlayersDescription]
  A game (=a match, a party) begins with an initial position [=GameState]. A move [=Move] is played,
  creating another position [=GameState]. Every information a player has to know is stored in the
  [Board] object: it may be a conventional board (e.g. 2D board) but also informations (e.g. at chess,
  has a king already moved?)

===============================================================================
[phase A]
phase non publique
    ✓ [A.I] plan
    ✓ [A.II] essai: est-ce que je peux faire communiquer deux ordinateurs entre eux
             en utilisant Urwid comme interface ?
    ✗ [A.III] essai: est-ce que je peux construire un programme permettant:
              * de jouer à des jeux aussi différents que 五目並べ NxN-Pp / Capuccino / échecs / jeux de carte
              * de charger/sauvegarder des parties
              * de jouer contre l'ordinateur
              * d'alimenter une base de données
              * d'utiliser un moteur de jeu (comme Stockfish)
              * de calculer le meilleur coup
              * d'envoyer un signal pour reprendre l'étude des meilleurs coups
              * de faire de l'analyse inverse (inventer des fins de partie et revenir en arrière)
              * dessiner l'arbre des possibilités
    ✗ [A.IV] mettre en place le 五目並べ 3x3-2p (=tic-tac-toe) à titre d'exemple.

[phase B]
phase publique: dépôt Github publique (tout basculer en anglais, écrire la doc., surveiller

[CURRENT] v. 0.0.1

* baseclasses_gomokunarabe_NxN_2players > dans nikw/games
* evaluate_position(last_move=None) > pour accélérer, évaluer depuis le dernier coup
* je n'aime pas le fait que improved_str() renvoie tantôt une string tantônt olusieurs lignes. > ça marche pourtant avec un simple .append() (pas besoin d'extend()). A documenter dans exc_***.
* "keep intermediate xxx" n'est pas implémenté
* nondefaultvalues > playervalues
  1 constantes supplémentaire: NOPLAYER_ID, PLAYER1_ID, PLAYER2_ID, IMPOSSIBLE_ID

[DONE] task-10

    * gomokunarabe_19x19_2p_5_boardimp1/game.py has now new constants
      XYMIN, XYMAX, NBR_PLAYERS

[DONE] task-9

    * a gomokunarabe game can be created; the first move can be played

[DONE] task-8

    - Board: two implementations
    - gomokunarabe_19x19/5/;2p

[DONE] task-7

    * nikw/game/baseclasses_2Drectint.py
    * improved doc.

[DONE] task-6

    * 'value' > 'int_value'
    * improved doc

[DONE] task-5

    * new files

[DONE] task-4

    * xy syntax instead of (x, y)

[DONE] task-3

    * nikw/game now contains gamerules/
    * classes: BoardCellNoneOrNvalues, Board2DCellsRectangleIntValue

[DONE] task-2

Documentation + hasfuncs

    * documentation: ROADMAP.md
          
[DONE] task-1

Documentation.

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
              * de jouer à des jeux aussi différents que gomokunarabe NxN-Pp / Capuccino / échecs / jeux de carte
              * de charger/sauvegarder des parties
              * de jouer contre l'ordinateur
              * d'alimenter une base de données
              * d'utiliser un moteur de jeu (comme Stockfish)
              * de calculer le meilleur coup
              * d'envoyer un signal pour reprendre l'étude des meilleurs coups
              * de faire de l'analyse inverse (inventer des fins de partie et revenir en arrière)
              * dessiner l'arbre des possibilités
       ✗ [A.III.1] construire un gomokunarabe NxN-Pp de manière très généraliste
       ✗ [A.III.2] construire un gomokunarabe 3x3-2p de manière optimisée
    ✗ [A.IV] mettre en place le gomokunarabe 3x3-2p (=tic-tac-toe) à titre d'exemple.

[phase B]
phase publique: dépôt Github publique (tout basculer en anglais, écrire la doc., surveiller

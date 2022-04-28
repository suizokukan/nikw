#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
#    nikw Copyright (C) 2022 suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of nikw.
#    nikw is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    nikw is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with nikw.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""
    nikw project : nikw/game/gamerules/gomokunarabe_19x19_5_2p_boardimp1/game.py
"""
from game.baseclasses import BoardCellIntegerValue
from game.baseclasses import PlayersDescription as RootPlayersDescription
from game.baseclasses_2Dboardint import Board2DCellsIntValueIMP1, PlayerDescriptionIntValue
from game.constants import CELL_INTVALUE_PLAYERS, CELL_INTVALUE_NOPLAYER, IMPROVEDSTR_SYMBOLS_FOR_INTVALUES
from game.baseclasses_gomokunarabeNxN_S_Pplayers import Game as RootGame
from game.baseclasses_gomokunarabeNxN_S_Pplayers import GameState as RootGameState


# ! game rule name MUST BE EXACTLY THE ONE DEFINED AS game.py::RULESNAME
# TODO: pimydoc à définir.
RULESNAME = "gomokunarabe/19x19;5;2p;boardimp1"

XYMIN = (-10, -10)
XYMAX = (8, 8)

ALIGNEMENT_LENGTH = 5

NBR_PLAYERS = 2


class PlayerDescription(PlayerDescriptionIntValue):
    pass


class PlayersDescription(RootPlayersDescription):
    def __init__(self):
        RootPlayersDescription.__init__(self,
                                        nbr_players=NBR_PLAYERS)


class Board(Board2DCellsIntValueIMP1):
    def __init__(self):
        Board2DCellsIntValueIMP1.__init__(
            self,
            cell_acceptable_intvalues= \
            [CELL_INTVALUE_NOPLAYER,] + \
            [CELL_INTVALUE_PLAYERS[player_index] for player_index in range(NBR_PLAYERS)],
            cell_default_value=CELL_INTVALUE_NOPLAYER,
            xymin=XYMIN,
            xymax=XYMAX,
            boardcell_type=BoardCellIntegerValue,
            improvedstr_symbols_for_intvalues=IMPROVEDSTR_SYMBOLS_FOR_INTVALUES)


class GameState(RootGameState):
    def __init__(self,
                 next_player_turn_index,
                 next_moveid,
                 players_description,
                 first_player_turn_index,
                 board,
                 gameresults):
        RootGameState.__init__(
            self,
            next_player_turn_index=next_player_turn_index,
            next_moveid=next_moveid,
            players_description=players_description,
            first_player_turn_index=first_player_turn_index,
            board=board,
            gameresults=gameresults,
            alignement_length=ALIGNEMENT_LENGTH)


class Game(RootGame):
    def __init__(self,
                 players_description):
        RootGame.__init__(self,
                          rules_name=RULESNAME,
                          board_type=Board,
                          gamestate_type=GameState,
                          players_description=players_description,
                          alignement_length=ALIGNEMENT_LENGTH)


def create_game(players_data):
    player1_data, player2_data = players_data

    p1 = PlayerDescription(player_turn_index=0,
                           player_name=player1_data[0],
                           player_type=player1_data[1])
    p2 = PlayerDescription(player_turn_index=1,
                           player_name=player2_data[0],
                           player_type=player2_data[1])
    players = PlayersDescription()
    players.append(p1)
    players.append(p2)

    return Game(players_description=players)

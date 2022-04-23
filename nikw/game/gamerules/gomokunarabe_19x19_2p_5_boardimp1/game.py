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
    nikw project : nikw/game/gamerules/gomokunarabe_19x19_2p_5_boardimp1/game.py
"""
from game.baseclasses_2Dboardint import Game2DCellsRectangleIntValue, Move2DCellsRectangleIntValue, Board2DCellsIntValueIMP1
from game.baseclasses_2Dboardint import PlayerDescriptionIntValue
from game.baseclasses import PlayersDescription as RootPlayersDescription
from game.baseclasses import Moves, GameState, BoardCellIntegerValue
from game.baseclasses import GameResult as RootGameResult
from game.constants import CELL_INTVALUE_PLAYERS, CELL_INTVALUE_NOPLAYER, IMPROVEDSTR_SYMBOLS_FOR_INTVALUES

# ! game rule name MUST BE EXACTLY THE ONE DEFINED AS game.py::RULENAME
# TODO: pimydoc à définir.
RULENAME = "gomokunarabe/19x19;2p;5;boardimp1"

XYMIN = (0, 0)
XYMAX = (18, 18)

NBR_PLAYERS = 2


class PlayersDescription(RootPlayersDescription):
    pass


class PlayerDescription(PlayerDescriptionIntValue):
    pass


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


class GameResult(RootGameResult):
    def __init__(self):
        RootGameResult.__init__(
            self,
            nbr_players=NBR_PLAYERS)


class Game(Game2DCellsRectangleIntValue):
    def __init__(self,
                 players_description,
                 ):
        Game2DCellsRectangleIntValue.__init__(
            self,
            rules_name=RULENAME,
            players_description=players_description,
            board_type=Board,
            move_type=Move2DCellsRectangleIntValue,
            moves_type=Moves,
            gamestate_type=GameState,
            gameresult_type=GameResult)

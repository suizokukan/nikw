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
    nikw project : nikw/game/baseclasses_gomokunarabeNxN_S_Pplayers.py
"""
from game.baseclasses import GameResult as RootGameResult
from game.baseclasses_2Dboardint import PlayerDescriptionIntValue
from game.baseclasses import PlayersDescription as RootPlayersDescription
from game.baseclasses_2Dboardint import Game2DCellsRectangleIntValue, Move2DCellsRectangleIntValue
from game.baseclasses import Moves, GameState


class PlayersDescription(RootPlayersDescription):
    pass


class PlayerDescription(PlayerDescriptionIntValue):
    pass


class GameResult(RootGameResult):
    pass


class Game(Game2DCellsRectangleIntValue):
    def __init__(self,
                 rules_name,
                 board_type,
                 players_description,
                 ):
        Game2DCellsRectangleIntValue.__init__(
            self,
            rules_name=rules_name,
            board_type=board_type,
            players_description=players_description,
            move_type=Move2DCellsRectangleIntValue,
            moves_type=Moves,
            gamestate_type=GameState,
            gameresult_type=GameResult)

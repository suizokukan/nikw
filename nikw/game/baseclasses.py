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
    nikw project : nikw/game/baseclasses.py
"""
from exc_motherclass.motherclass import MotherClassSerErr

from game.constants import DATANATURE_INMEMORY, PLAYERTYPE__NOPLAYER


class RootClass(MotherClassSerErr):
    """
    Root class of all classes in this file.
    """
    def copy(self):
        self.export_as(expected_data_type=DATANATURE_INMEMORY)

    def export_as(self,
                  expected_data_type=DATANATURE_INMEMORY):
        raise NotImplementedError

    def init_from(self,
                  source,
                  source_type=DATANATURE_INMEMORY):
        raise NotImplementedError


class Game(RootClass):
    """
    Game as "chess" or "tic-tac-toe", not as "party" or "match".
    """
    def __init__(self,
                 rules_name,
                 players_description=None,
                 gamestates=None):
        self.rules_name = rules_name
        self.players_description = players_description
        self.gamestates = gamestates

    def apply_a_move_to_a_gamestate(self,
                                    gamestate,
                                    move):
        raise NotImplementedError

    def is_this_a_legal_move_for_a_gamestate(self,
                                             gamestate,
                                             move):
        raise NotImplementedError


class GameStates(RootClass, dict):
    """
    * initial_gamestate
    [gamestate_id: 0, 1, 2...] : (Move, GameState)
    """
    pass


class GameState(RootClass):
    def __init__(self,
                 is_over=False,
                 board=None):
        self.is_over = is_over
        self.board = board


class Moves(RootClass, list):
    """
    [move index] = Move
    """
    pass


class Move(RootClass):
    def __init__(self,
                 player_id):
        self.player_id = player_id


class PlayersDescription(RootClass, dict):
    """
    [player_id] = Player
    """
    pass


class PlayerDescription(RootClass):
    def __init__(self,
                 player_id=None,
                 player_name=None,
                 player_type=PLAYERTYPE__NOPLAYER):
        self.player_id = player_id
        self.player_name = player_name
        self.player_type = player_type


class Board(RootClass):
    pass


class BoardCell(RootClass):
    def __init__(self,
                 int_value=None):
        RootClass.__init__(self)
        self.int_value = int_value

    def hashvalue(self):
        raise NotImplementedError


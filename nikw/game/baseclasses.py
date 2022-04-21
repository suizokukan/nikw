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
from hashfuncs import hashfunction
from exc_motherclass.motherclass import MotherClassSerErr
from exc_errors.errors import ErrorSer as Error

from game.constants import DATANATURE_INMEMORY, PLAYERTYPE__NOPLAYER


class RootClass(MotherClassSerErr):
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
    pass


class Board(RootClass):
    pass


class Board2DCellsRectangleIntValue(Board):
    def __init__(self,
                 cell_values,
                 xymin,
                 xymax,
                 boardcell_object):
        Board.__init__(self)
        self.cell_values = cell_values
        self.xymin = xymin
        self.xymax = xymax
        self.cells = {}
        self.boardcell_object = boardcell_object

        self.set_default_cells()

    def get_hashvalue(self):
        """
            Board2DCellsRectangleIntValue.get_hashvalue()

            Return a hash value of <self>.
            ___________________________________________________________________

            no PARAMETER

            RETURNED VALUE: (bytes)hash value
        """
        res = hashfunction()
        for xy in self.get_all_xy():
            res.update(self.cells[xy].get_hashvalue())
        return res.digest()

    def get_all_xy(self):
        for x in range(self.xymin[0], self.xymax[0]+1):
            for y in range(self.xymin[1], self.xymax[1]+1):
                yield (x, y)

    def get_cell(self,
                 xy):
        return self.cells[xy]

    def set_cell(self,
                 xy, value):
        self.cells[xy] = self.boardcell_object(value)

    def set_default_cells(self):
        for xy in self.get_all_xy():
            self.set_cell(xy, value=0)

            if not self.get_cell(xy).errors.zero_error_or_warning():
                self.errors.extend(self.cells[xy].errors)


class BoardCell(RootClass):
    def __init__(self,
                 value=None):
        RootClass.__init__(self)
        self.value = value

    def hashvalue(self):
        raise NotImplementedError


class BoardCellNoneOrNvalues(BoardCell):
    # values[0] is the null value, i.e. __init__(value=BoardCellNoneOrNvalues.values[0])
    values = (0, 1, 2)

    def __init__(self,
                 value=0):
        if value not in BoardCellNoneOrNvalues.values:
            BoardCell.__init__(self, None)
            self.errors.append(
                Error(f"Error: can't initialize {self.__class__.__name__} object."
                      f"Incorrect value '{value}' given to initialize the object."
                      f"Acceptable values are {BoardCellNoneOrNvalues.values}."))
        else:
            BoardCell.__init__(self, value)

    def get_hashvalue(self):
        """
            BoardCellNoneOrNvalues.get_hashvalue()

            Return a hash value of <self>.
            ___________________________________________________________________

            no PARAMETER

            RETURNED VALUE: (bytes)hash value
        """
        res = hashfunction()
        res.update(str(self.value).encode())
        return res.digest()


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

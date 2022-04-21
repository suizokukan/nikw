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
    nikw project : nikw/game/baseclasses_2Drectint.py

        2D-Rectangular board + cells having an int value.
"""
from hashfuncs import hashfunction
from exc_errors.errors import ErrorSer as Error

from game.baseclasses import Board, BoardCell, Move


class Board2DCellsRectangleIntValue(Board):
    """
    Board + 2D rectangular board + Cell(int_value)

    BEWARE: very slow way to achieve this !
    """
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
                 xy,
                 int_value):
        self.cells[xy] = self.boardcell_object(int_value)

    def set_default_cells(self):
        for xy in self.get_all_xy():
            self.set_cell(xy, int_value=0)

            if not self.get_cell(xy).errors.zero_error_or_warning():
                self.errors.extend(self.cells[xy].errors)


class BoardCellIntValues(BoardCell):
    """
    Very slow and dumb way to achieve this !
    """
    # int_values[0] is the null value, i.e.
    #  __init__(int_value=BoardCellNoneOrNint_values.int_values[0])
    int_values = range(0, 255)

    def __init__(self,
                 int_value=0):
        if int_value not in BoardCellIntValues.int_values:
            BoardCell.__init__(self, None)
            self.errors.append(
                Error(f"Error: can't initialize {self.__class__.__name__} object."
                      f"Incorrect value '{int_value}' given to initialize the object."
                      f"Acceptable values are {BoardCellIntValues.int_values}."))
        else:
            BoardCell.__init__(self, int_value)

    def get_hashvalue(self):
        """
            BoardCellIntValues.get_hashvalue()

            Return a hash value of <self>.
            ___________________________________________________________________

            no PARAMETER

            RETURNED VALUE: (bytes)hash value
        """
        res = hashfunction()
        res.update(str(self.int_value).encode())
        return res.digest()


class Move2DCellsRectangleIntValue(Move):
    def __init__(self,
                 player_id,
                 xy):
        Move.__init__(self, player_id)
        self.xy = xy

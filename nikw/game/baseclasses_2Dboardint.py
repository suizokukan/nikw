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
    nikw project : nikw/game/baseclasses_2Dboardint.py

        2D board + cells having an int value.

            Board
              |
       Board2DCellsIntValue
              |
    -------------------------------------
    |                                   |
Board2DCellsIntValueIMP1             Board2DCellsIntValueIMP2
   - xymin/xymax must be defined        - xymin/xymax may be not defined
   - .cells() defined for all xy        - .cells() defined only for non default
                                        (interesting for infinite board)
"""
from hashfuncs import hashfunction
from exc_errors.errors import ErrorSer as Error

from game.baseclasses import Board, Move


class Board2DCellsIntValue(Board):
    """
    Board + 2D rectangular board + Cell(int_value)
    """
    def __init__(self,
                 cell_values,
                 cell_default_value,
                 xymin,  # may be None; in this case xymax is None
                 xymax,  # may be None; in this case xymin is None
                 boardcell_object):
        Board.__init__(self)
        self.cell_values = cell_values
        self.cell_default_value = cell_default_value
        self.xymin = xymin  # may be None
        self.xymax = xymax  # may be None
        self.cells = {}
        self.boardcell_object = boardcell_object

        self.set_cells_to_default_value()

    def get_cell(self,
                 xy):
        raise NotImplementedError

    def set_cell(self,
                 xy,
                 int_value):
        if not self.is_xy_inside_fixed_limits(xy):
            self.errors.append(
                Error(f"Error: can't initialize a cell in a {self.__class__.__name__} object."
                      f"Incorrect value '{int_value}' given to initialize the object."
                      f"Acceptable values are {self.cell_values}."))

        elif int_value not in self.cell_values:
            self.errors.append(
                Error(f"Error: can't initialize a cell in a {self.__class__.__name__} object."
                      f"Incorrect xy '{xy}' given to initialize the object."
                      f"Acceptable values are {self.xymin} / {self.xymax}."))
        else:
            self.cells[xy] = self.boardcell_object(int_value)

    def set_cells_to_default_value(self):
        raise NotImplementedError

    def is_xy_inside_fixed_limits(self,
                                  xy):
        # special case: no limits defined
        # if self.xymin is None, self.xymax is None.
        if self.xymin is None:
            return True

        # real test with the defined limits:
        return (self.xymin[0] <= xy[0] <= self.xymax[0]) and \
            (self.xymin[1] <= xy[1] <= self.xymax[1])


class Board2DCellsIntValueIMP1(Board2DCellsIntValue):
    """
        Board2DCellsIntValueIMP1: fixed cells dict, i.e.
        self.xymin and self.xymax can't be None.

        self.cells[] is defined for all values, default values or real values.
    """
    def get_all_xy(self):
        for x in range(self.xymin[0], self.xymax[0]+1):
            for y in range(self.xymin[1], self.xymax[1]+1):
                yield (x, y)

    def get_cell(self,
                 xy):
        return self.cells[xy]

    def get_hashvalue(self):
        """
            Board2DCellsIntValue.get_hashvalue()

            Return a hash value of <self>.
            ___________________________________________________________________

            no PARAMETER

            RETURNED VALUE: (bytes)hash value
        """
        res = hashfunction()
        for xy in self.get_all_xy():
            res.update(self.cells[xy].get_hashvalue())
        return res.digest()

    def set_cells_to_default_value(self):
        for xy in self.get_all_xy():
            self.set_cell(xy, int_value=self.cell_default_value)

            if not self.get_cell(xy).errors.zero_error_or_warning():
                self.errors.extend(self.cells[xy].errors)


class Board2DCellsIntValueIMP2(Board2DCellsIntValue):
    """
        Board2DCellsIntValueIMP2: non fixed cells dict, i.e.
        self.xymin and self.xymax can be None.

        We store in cells only the non default values.
    """
    def get_cell(self,
                 xy):
        """
            Board2DCellsIntValueIMP2.get_cell()
        """
        if xy in self.cells:
            return self.cell_default_value
        return self.cells[xy]

    def get_hashvalue(self):
        """
            Board2DCellsIntValueIMP2.get_hashvalue()

            Return a hash value of <self>.
            ___________________________________________________________________

            no PARAMETER

            RETURNED VALUE: (bytes)hash value
        """
        res = hashfunction()
        for xy, value in self.cells.items():
            res.update(str(xy).encode())
            res.update(value.get_hashvalue())
        return res.digest()

    def set_cells_to_default_value(self):
        """
            Board2DCellsIntValueIMP2.set_cells_to_default_value()
        """
        self.cells = {}


class Move2DCellsRectangleIntValue(Move):
    def __init__(self,
                 player_id,
                 xy):
        Move.__init__(self, player_id)
        self.xy = xy

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

from game.constants import PLAYERTYPE__NOPLAYER
from game.utils import explicit_playertype_constant
from game.baseclasses import Board, Move, Game, PlayerDescription


class PlayerDescriptionIntValue(PlayerDescription):
    def __init__(self,
                 player_turn_index,
                 player_name,
                 cell_intvalue,
                 player_type=PLAYERTYPE__NOPLAYER):
        PlayerDescription.__init__(self,
                                   player_turn_index=player_turn_index,
                                   player_name=player_name,
                                   player_type=player_type)
        self.cell_intvalue = cell_intvalue

    def improved_str(self):
        return f"'{self.player_name}': {self.cell_intvalue=}; " \
            f"(id #{self.player_turn_index}/{explicit_playertype_constant(self.player_type)})"


class Board2DCellsIntValue(Board):
    """
    Board + 2D rectangular board + Cell(int_value)
    """
    def __init__(self,
                 cell_acceptable_intvalues,
                 cell_default_value,
                 xymin,  # may be None; in this case xymax is None
                 xymax,  # may be None; in this case xymin is None
                 boardcell_type,
                 improvedstr_symbols_for_intvalues):
        Board.__init__(self)
        self.cell_acceptable_intvalues = cell_acceptable_intvalues
        self.cell_default_value = cell_default_value
        self.xymin = xymin  # may be None
        self.xymax = xymax  # may be None
        self.cells = {}
        self.boardcell_type = boardcell_type
        self.xymin_xymax_nondefaultvalues = None  # None or ((xmin, ymin), (xmax, ymax))
        self.improvedstr_symbols_for_intvalues = improvedstr_symbols_for_intvalues
        self.set_cells_to_default_value()

    def is_a_cell_set_to_default_value(self,
                                       xy):
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

    def get_cell(self,
                 xy):
        raise NotImplementedError

    def improved_str(self):
        ((xmin, ymin), (xmax, ymax)) = self.xymin_xymax_nondefaultvalues

        res = []

        for y in range(ymin, ymax+1):
            line = []
            for x in range(xmin, xmax+1):
                line.append(self.improvedstr_symbols_for_intvalues[self.cells[(x, y)].int_value])
            res.append("".join(line))

        return "\n".join(res)

    def set_cell(self,
                 xy,
                 int_value):
        if not self.is_xy_inside_fixed_limits(xy):
            self.errors.append(
                Error(f"Error: can't initialize a cell in a {self.__class__.__name__} object."
                      f"Incorrect value '{int_value}' given to initialize the object."
                      f"Acceptable values are {self.cell_acceptable_intvalues}."))

        elif int_value not in self.cell_acceptable_intvalues:
            self.errors.append(
                Error(f"Error: can't initialize a cell in a {self.__class__.__name__} object."
                      f"Incorrect xy '{xy}' given to initialize the object."
                      f"Acceptable values are {self.xymin} / {self.xymax}."))
        else:
            self.update__xymin_xymax_nondefaultvalues(xy)
            self.cells[xy] = self.boardcell_type(int_value)

    def set_cells_to_default_value(self):
        raise NotImplementedError

    def update__xymin_xymax_nondefaultvalues(self,
                                             xy):
        if self.xymin_xymax_nondefaultvalues is None:
            self.xymin_xymax_nondefaultvalues = xy
        else:
            self.xymin_xymax_nondefaultvalues = [[0, 0], [0, 0]]
            x, y = xy
            self.xymin_xymax_nondefaultvalues[0][0] = \
                min(x,
                    self.xymin_xymax_nondefaultvalues[0][0])

            self.xymin_xymax_nondefaultvalues[0][1] = \
                min(y,
                    self.xymin_xymax_nondefaultvalues[0][1])

            self.xymin_xymax_nondefaultvalues[1][0] = \
                max(x,
                    self.xymin_xymax_nondefaultvalues[1][0])

            self.xymin_xymax_nondefaultvalues[1][1] = \
                max(y,
                    self.xymin_xymax_nondefaultvalues[1][1])


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

    def is_a_cell_set_to_default_value(self,
                                       xy):
        return self.cells[xy].int_value == self.cell_default_value

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

    def is_a_cell_set_to_default_value(self,
                                       xy):
        return xy not in self.cells

    def set_cells_to_default_value(self):
        """
            Board2DCellsIntValueIMP2.set_cells_to_default_value()
        """
        self.cells = {}


class Move2DCellsRectangleIntValue(Move):
    def __init__(self,
                 player_turn_index,
                 xy):
        Move.__init__(self, player_turn_index)
        self.xy = xy

    def improved_str(self):
        return f"player id #{self.player_turn_index} at {self.xy}"


class Game2DCellsRectangleIntValue(Game):

    def apply_a_move_to_current_gamestate(self,
                                          move):
        """
        <move> must be valid.
        """
        int_value = self.players_description[move.player_turn_index].cell_intvalue
        self.current_gamestate.board.cells[move.xy] = \
            self.current_gamestate.board.boardcell_type(int_value)

    def is_a_validmove(self,
                       move):
        """
        Is it possible to apply <move> to the last gameresult ?
        """
        if not move.player_turn_index == self.current_gamestate.next_player_turn_index:
            return False
        if not self.current_gamestate.board.is_a_cell_set_to_default_value(move.xy):
            return False
        return True

    def play_a_move(self,
                    xy):
        move = self.move_type(self.current_gamestate.next_player_turn_index, xy)

        if self.is_a_validmove(move):
            self.apply_a_move_to_current_gamestate(move)
            self.moves[self.current_gamestate.next_moveid] = (move,)
            self.current_gamestate.next_moveid += 1

            if self.current_gamestate.next_player_turn_index < self.players_description.nbr_players:
                self.current_gamestate.next_player_turn_index += 1
            else:
                self.current_gamestate.next_player_turn_index = self.first_player_turn_index
        else:
            self.errors.append(Error(f"Error: invalid move {move}."))

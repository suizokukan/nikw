#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#    nikw Copyright (C) 2021 suizokukan
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
################################################################################
"""
    nikw project : nikw/nikw.py
"""
import sys

from hashfuncs import hashfunction, binhash_to_strb85
from exc_motherclass.motherclass import MotherClassSerErr


# KNOWN_GAMESRULES[(str) game rulen name] = ("game rule module",
#                                            None < will be the imported module
#                                           )
KNOWN_GAMESRULES = {"gomokunarabe/3x3;2p": ("gamerules.gomokunarabe_3x3_2p",
                                            None,
                                            ),
                    }



DATANATURE_INMEMORY = 0x01
DATANATURE_DB = 0x02
DATANATURE_SERIALIZED = 0x03
DATANATURE_CLIRAWOUTPUT = 0x04
DATANATURE_CLIRICHOUTPUT = 0x05
DATANATURE_CLIURWIDOUTPUT = 0x06

PLAYERTYPE__NOPLAYER = 0x01
PLAYERTYPE__RANDOM = 0x02
PLAYERTYPE__HUMAN = 0x03
PLAYERTYPE__AI = 0x04


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


class Board2DCellsRectangle(Board):
    def __init__(self,
                 xmin,
                 xmax,
                 ymin,
                 ymax,
                 boardcell_object):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.cells = {}
        for (x, y) in self.get_xy():
            self.cells[(x, y)] = boardcell_object(value=None)

    def get_hashvalue(self):
        """
            Board2DCellsRectangle.get_hashvalue()

            Return a hash value of <self>.
            ___________________________________________________________________

            no PARAMETER

            RETURNED VALUE: (bytes)hash value
        """
        res = hashfunction()
        for x, y in self.get_xy():
            res.update(self.cells[x, y].get_hashvalue())
        return res.digest()
            
    def get_xy(self):
        for x in range(self.xmin, self.xmax+1):
            for y in range(self.ymin, self.ymax+1):
                yield (x, y)


class BoardCell(RootClass):
    def __init__(self,
                 value=None):
        RootClass.__init__(self)
        self.value = value

    def hashvalue(self):
        raise NotImplementedError


class BoardCellWhiteOrBlackOrNone(BoardCell):
    def __init__(self,
                 value=None):
        BoardCell.__init__(self, value)

    def get_hashvalue(self):
        """
            BoardCellWhiteOrBlackOrNone.get_hashvalue()

            Return a hash value of <self>.
            ___________________________________________________________________

            no PARAMETER

            RETURNED VALUE: (bytes)hash value
        """
        res = hashfunction()
        res.update(str(self.value).encode())
        return res.digest()


board = Board2DCellsRectangle(0, 0, 18, 18, BoardCellWhiteOrBlackOrNone)
print(binhash_to_strb85(board.get_hashvalue()))


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


def main():
    import importlib
    try:
        for gamerule, gamerule_data in KNOWN_GAMESRULES.items():
            importlib.import_module(gamerule_data[0])
    except ModuleNotFoundError:
        print("Boom !", gamerule)

if __name__ == '__main__':
    sys.exit(main())
        

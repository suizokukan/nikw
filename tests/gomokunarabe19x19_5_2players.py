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
    nikw project : nikw/tests/gomokunarabe19x19_5_2players.py

    * inverse_dict(src)
"""
import unittest
"""
* gomokunarabe19x19_5_2players.1.iaswn
      -10  -5   +0   +5
       |----|----|----|---
 -10 - ................... - -10
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 -5  - ................... - -5
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 +0  - ................... - +0
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 +5  - ................... - +5
     | ................... |
     | ................... |
     | ................... |
       |----|----|----|---
       -10  -5   +0   +5

* gomokunarabe19x19_5_2players.2.iaswn
       -10  -5   +0   +5
       |----|----|----|---
 -10 - ................... - -10
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 -5  - ................... - -5
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 +0  - ................... - +0
     | ...........X....... |
     | ................... |
     | ................... |
     | ................... |
 +5  - ................... - +5
     | ................... |
     | ................... |
     | ................... |
       |----|----|----|---
       -10  -5   +0   +5

* gomokunarabe19x19_5_2players.3.iaswn
       -10  -5   +0   +5
       |----|----|----|---
 -10 - ................... - -10
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 -5  - ................... - -5
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 +0  - ..........OX....... - +0
     | ..........OX....... |
     | ..........OX....... |
     | ..........OX....... |
     | ...........X....... |
 +5  - ................... - +5
     | ................... |
     | ................... |
     | ................... |
       |----|----|----|---
       -10  -5   +0   +5

* gomokunarabe19x19_5_2players.4.iaswn
       -10  -5   +0   +5
       |----|----|----|---
 -10 - ................... - -10
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 -5  - ................... - -5
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 +0  - ..........OX....... - +0
     | ..........OX....... |
     | ..........OX....... |
     | ..........OX....... |
     | ..........OX....... |
 +5  - ................... - +5
     | ................... |
     | ................... |
     | ................... |
       |----|----|----|---
       -10  -5   +0   +5

* gomokunarabe19x19_5_2players.5.iaswn
       -10  -5   +0   +5
       |----|----|----|---
 -10 - ................... - -10
     | ................... |
     | ................... |
     | ................... |
     | ................... |
 -5  - ................... - -5
     | ................... |
     | ................... |
     | ........O.......... |
     | ................... |
 +0  - ..........OX....... - +0
     | ..........OX....... |
     | ..........OX....... |
     | ..........OX....... |
     | ...........X....... |
 +5  - ...........X....... - +5
     | ................... |
     | ................... |
     | ................... |
       |----|----|----|---
       -10  -5   +0   +5

* gomokunarabe19x19_5_2players.6.iaswn
       -10  -5   +0   +5
       |----|----|----|---
 -10 - ................... - -10
     | ................... |
     | ................... |
     | ...........X....... |
     | ...........X....... |
 -5  - .....O.....X....... - -5
     | ......O....X....... |
     | .......O...X....... |
     | ........O.......... |
     | ................... |
 +0  - ..........OX....... - +0
     | ..........OX....... |
     | ..........OX....... |
     | ..........OX....... |
     | ...........X....... |
 +5  - ................... - +5
     | ....O.............. |
     | ................... |
     | ................... |
       |----|----|----|---
       -10  -5   +0   +5
"""
import sys

from iaswn.iaswn import from_jsonstr
from nikw.game.gamerules.gamerules import import_gamerules
from nikw.game.constants import CELL_INTVALUE_PLAYERS

sys.path.append("nikw/")

class Tests__gomokunarabe_19x19_5_2players(unittest.TestCase):

    def setUp(self):
        """
            Tests__gomokunarabe_19x19_5_2players.setUp()
        """
        gamerules = ('gomokunarabe/19x19;5;2p;boardimp1',)
        if not import_gamerules(gamerules):
            self.fail(f"Can't setup the test '{self.__class__.__name__}': "
                      f"can't import '{gamerules}'.")

    def test_file_1(self):
        """
            Tests__gomokunarabe_19x19_5_2players.test_file_1()

            Test based upon the following file:
                tests/gomokunarabe19x19_5_2players.1.iaswn

                (see content of this game at the beginning of the current file)
        """
        with open("tests/gomokunarabe19x19_5_2players.1.iaswn", "r") as inputfile:
            jsonstr = inputfile.read()
            game = from_jsonstr(jsonstr)
            player_turn_index = 0
            self.assertFalse(
                game.current_gamestate.gameresults.is_there_only_one_winner(
                    CELL_INTVALUE_PLAYERS[player_turn_index]))

    # def test_file_6(self):
    #     """
    #         Tests__gomokunarabe_19x19_5_2players.test_file_6()

    #         Test based upon the following file:
    #             tests/gomokunarabe19x19_5_2players.6.iaswn

    #             (see content of this game at the beginning of the current file)
    #     """
    #     with open("tests/gomokunarabe19x19_5_2players.6.iaswn", "r") as inputfile:
    #         jsonstr = inputfile.read()
    #         game = from_jsonstr(jsonstr)
    #         player_turn_index = 0
    #         self.assertTrue(
    #             game.current_gamestate.gameresults.is_there_only_one_winner(
    #                 CELL_INTVALUE_PLAYERS[player_turn_index]))

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
    nikw project : nikw/game/constants.py
"""
DEFAULT_GAME_CONFIGURATION = {"keep intermediate gamestates": False}
DEFAULT_FIRSTPLAYER_TURN_INDEX = 0  # if #0, the first player to play will be players_description[0]
DEFAULT_FIRSTMOVEID = 0

DATANATURE_INMEMORY = 0x01
DATANATURE_DB = 0x02
DATANATURE_SERIALIZED = 0x03
DATANATURE_CLIRAWOUTPUT = 0x04
DATANATURE_CLIRICHOUTPUT = 0x05
DATANATURE_CLIURWIDOUTPUT = 0x06

# conferexplicit_playertype_constant() defined in nikw/game/utils.py
PLAYERTYPE__NOPLAYER = 0x01
PLAYERTYPE__RANDOM = 0x02
PLAYERTYPE__HUMAN = 0x03
PLAYERTYPE__AI = 0x04

# TODO
#   explicit_***
GAMEMAINRESULT_UNDEFINED = 0x00
GAMEMAINRESULT_GAMEISNOTOVER = 0x01
GAMEMAINRESULT_GAMEISOVER = 0x02

# TODO
#   explicit_***
PLAYERRESULT_UNDEFINED = 0x00
PLAYERRESULT_NOTVICTORIOUS = 0x01
PLAYERRESULT_VICTORIOUS = 0x02
PLAYERRESULT_DRAW = 0x03

CELL_INTVALUE_NOPLAYER = 0
CELL_INTVALUE_FORBIDDEN = 1
CELL_INTVALUE_PLAYERS = (2, 3, 4, 5, 6, 7, 8, 9)  # CELL_INTVALUE_PLAYERS[player_turn_index] = value for int_value

IMPROVEDSTR_SYMBOLS_FOR_INTVALUES = {
    CELL_INTVALUE_NOPLAYER: ".",
    CELL_INTVALUE_FORBIDDEN: "@",
    CELL_INTVALUE_PLAYERS[0]: "X",
    CELL_INTVALUE_PLAYERS[1]: "O",
    CELL_INTVALUE_PLAYERS[2]: "A",
    CELL_INTVALUE_PLAYERS[3]: "B",
    CELL_INTVALUE_PLAYERS[4]: "C",
    CELL_INTVALUE_PLAYERS[5]: "D",
    CELL_INTVALUE_PLAYERS[6]: "E",
    CELL_INTVALUE_PLAYERS[7]: "F",
    }

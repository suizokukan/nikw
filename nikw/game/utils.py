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
    nikw project : nikw/game/utils.py
"""
from game.constants import PLAYERTYPE__NOPLAYER, PLAYERTYPE__RANDOM, PLAYERTYPE__HUMAN, PLAYERTYPE__AI
from hashfuncs import hashfunction


def explicit_playertype_constant(player_type):
    """
    confer constants defined in nikw/game/constants.py
    """
    if player_type == PLAYERTYPE__NOPLAYER:
        return "no player"
    if player_type == PLAYERTYPE__RANDOM:
        return "random player"
    if player_type == PLAYERTYPE__HUMAN:
        return "human player"
    if player_type == PLAYERTYPE__AI:
        return "AI player"
    raise NotImplementedError


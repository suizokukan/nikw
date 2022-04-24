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
    nikw project : nikw/game/gamerules/gamerules.py
"""
# KNOWN_GAMESRULES[(str) game rule name] = ("game rule module",
#                                           None < will be the imported module
#                                          )
#
# ! game rule name MUST BE EXACTLY THE ONE DEFINED AS game.py::RULENAME
# TODO: pimydoc à définir.
KNOWN_GAMESRULES = \
    {"gomokunarabe/19x19;5;2p;boardimp1":
     ["game.gamerules.gomokunarabe_19x19_5_2p_boardimp1.game", None,],
     }

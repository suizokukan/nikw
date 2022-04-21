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

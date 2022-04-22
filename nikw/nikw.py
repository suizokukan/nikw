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
    nikw project : nikw/nikw.py
"""
import sys

from game.gamerules.gamerules import KNOWN_GAMESRULES


def main():
    import importlib
    try:
        for gamerule, gamerule_data in KNOWN_GAMESRULES.items():
            importlib.import_module(gamerule_data[0])
            print("... imported a new rule:", gamerule)
    except ModuleNotFoundError:
        print("TODO/Boom !", gamerule)


if __name__ == '__main__':
    from hashfuncs import binhash_to_strb85
    from game.baseclasses import BoardCellIntegerValue
    from game.baseclasses_2Dboardint import Board2DCellsIntValueIMP1
    board = Board2DCellsIntValueIMP1(cell_values=(0, 1, 2),
                                     cell_default_value=0,
                                     xymin=(0, 0),
                                     xymax=(18, 18),
                                     boardcell_object=BoardCellIntegerValue)
    print(binhash_to_strb85(board.get_hashvalue()))
    print(board.errors)
    sys.exit(main())

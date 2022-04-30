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

from game.gamerules.gamerules import import_gamerules


def main():
    if not import_gamerules():
        sys.exit(1)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!! tous les types sont empruntés au module via getattr: !!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    from game.constants import PLAYERTYPE__RANDOM, DATANATURE_SERIALIZED
    import game.gamerules.gamerules
    create_game = getattr(game.gamerules.gamerules.KNOWN_GAMESRULES["gomokunarabe/19x19;5;2p;boardimp1"][1],
                          "create_game")
    GAME = create_game(players_data=(("Xavier", PLAYERTYPE__RANDOM),
                                     ("Lionel", PLAYERTYPE__RANDOM)))

    GAME.play_a_move((1, 1))
    GAME.play_a_move((0, 0))
    GAME.play_a_move((1, 0))
    GAME.play_a_move((0, 1))
    GAME.play_a_move((1, 2))
    GAME.play_a_move((0, 2))
    GAME.play_a_move((1, 3))
    GAME.play_a_move((0, 3))
    # GAME.play_a_move((1, 4))
    # GAME.play_a_move((-2, -2))
    # GAME.play_a_move((1, -7))
    # GAME.play_a_move((-3, -3))
    # GAME.play_a_move((1, -6))
    # GAME.play_a_move((-4, -4))
    # GAME.play_a_move((1, -5))
    # GAME.play_a_move((-5, -5))
    # GAME.play_a_move((1, -4))
    # GAME.play_a_move((-6, 6))
    # GAME.play_a_move((1, -3))

    # serialized_game = GAME.export_as(DATANATURE_SERIALIZED)
    # with open("z.dump", "w") as exportfile:
    #     exportfile.write(serialized_game)
    # from iaswn.iaswn import from_jsonstr, diagnostic
    # GAME = from_jsonstr(serialized_game)
    print(GAME)

    # print(diagnostic(GAME))

    # from iaswn.iaswn import from_jsonstr
    # with open("tests/gomokunarabe19x19_5_2players.6.iaswn", "r") as inputfile:
    #     jsonstr = inputfile.read()
    #     GAME = from_jsonstr(jsonstr)
    #     print(GAME)

if __name__ == '__main__':
    sys.exit(main())

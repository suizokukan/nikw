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

import game.gamerules.gamerules


def main():
    import importlib
    try:
        for gamerule, gamerule_data in game.gamerules.gamerules.KNOWN_GAMESRULES.items():
            new_module = importlib.import_module(gamerule_data[0])
            gamerule_data[1] = new_module
            print("... imported a new rule:", gamerule)
    except ModuleNotFoundError as err:
        print("TODO/Boom !", err, gamerule)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!! tous les types sont empruntés au module via getattr: !!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    GAME_TYPE = getattr(game.gamerules.gamerules.KNOWN_GAMESRULES["gomokunarabe/19x19;5;2p;boardimp1"][1],
                        "Game")
    PLAYERDESCRIPTION_TYPE = getattr(game.gamerules.gamerules.KNOWN_GAMESRULES["gomokunarabe/19x19;5;2p;boardimp1"][1],
                                     "PlayerDescription")
    PLAYERSDESCRIPTION_TYPE = getattr(game.gamerules.gamerules.KNOWN_GAMESRULES["gomokunarabe/19x19;5;2p;boardimp1"][1],
                                      "PlayersDescription")

    from game.constants import PLAYERTYPE__RANDOM
    P1 = PLAYERDESCRIPTION_TYPE(player_turn_index=0,
                                player_name="Xavier",
                                player_type=PLAYERTYPE__RANDOM)
    P2 = PLAYERDESCRIPTION_TYPE(player_turn_index=1,
                                player_name="Lionel",
                                player_type=PLAYERTYPE__RANDOM)
    PLAYERS = PLAYERSDESCRIPTION_TYPE()
    PLAYERS.append(P1)
    PLAYERS.append(P2)

    GAME = GAME_TYPE(players_description=PLAYERS)
    GAME.play_a_move((1, 1))

    print(GAME)


if __name__ == '__main__':
    sys.exit(main())

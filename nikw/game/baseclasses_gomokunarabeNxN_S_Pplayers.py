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
    nikw project : nikw/game/baseclasses_gomokunarabeNxN_S_Pplayers.py
"""
from game.constants import GAMEMAINRESULT_GAMEISOVER
from game.constants import PLAYERRESULT_NOTVICTORIOUS, PLAYERRESULT_VICTORIOUS
from game.baseclasses import GameResults as RootGameResults
from game.baseclasses_2Dboardint import PlayerDescriptionIntValue
from game.baseclasses import PlayersDescription as RootPlayersDescription
from game.baseclasses_2Dboardint import Game2DCellsRectangleIntValue, Move2DCellsRectangleIntValue, GameStatePlayersInSetOrderIntValue
from game.baseclasses import Moves


# TODO pas sûr que ces coquilles vides soient vraiment utiles
class PlayersDescription(RootPlayersDescription):
    pass


class PlayerDescription(PlayerDescriptionIntValue):
    pass


class GameResults(RootGameResults):
    pass


class GameState(GameStatePlayersInSetOrderIntValue):
    def __init__(self,
                 next_player_turn_index,
                 next_moveid,
                 players_description,
                 first_player_turn_index,
                 board,
                 gameresults,
                 alignement_length):
        self.alignement_length = alignement_length
        GameStatePlayersInSetOrderIntValue.__init__(
            self,
            next_player_turn_index=next_player_turn_index,
            next_moveid=next_moveid,
            players_description=players_description,
            first_player_turn_index=first_player_turn_index,
            board=board,
            gameresults=gameresults)

    def find_winning_positions_for_deltaxy(self,
                                           delta_xy):
        """
            Find all winning positions for delta_xy.

            Return a dict: res[(xy, delta_xy)] = (stone_index, stone_value)

            Not optimized: Please note that all winning positions are found,
                           not the the first one to be found.
        """
        res = {}

        # xyranges: a tuple of generator.

        # why -(self.alignement_length+1) / +(self.alignement_length-1) ?
        #
        #  Since we're looking to <self.alignement_length> stones-in-a-row,
        #  it's not necessary to be too near the limits:
        #
        #   By example, if <self.alignement_length> is 5:
        #            x   |
        #             x  |
        #              x |
        #               x|
        #                x
        #            ----/
        #  .. the last 'x' is outside limits: only 4 'x' are aligned.
        if delta_xy == (0, 1):  # vertical
            xyranges = (
                ((x, self.board.xymin[1]) for x in range(
                    self.board.xymin[0],
                    self.board.xymax[0]+1-(self.alignement_length+1))),
            )
        elif delta_xy == (1, 0):  # horizontal
            xyranges = (
                ((self.board.xymin[0], y) for y in range(
                    self.board.xymin[1],
                    self.board.xymax[1]+1-(self.alignement_length+1))),
            )
        elif delta_xy == (1, 1):  # diagonal downwards+to the right
            xyranges = (
                ((x, self.board.xymin[1]) for x in range(
                    self.board.xymin[0],
                    self.board.xymax[0]+1-(self.alignement_length+1))),
                # the first +1 (in range(self.board.xymin[1]+1)) is due to the fact
                # that precedent generator would overlap with this one.
                # Indeed,...
                #  rather than that:   /------
                #                      |x
                #                      | x
                #                      |  x
                #   ... which is already covered by the first generator...
                #
                #  it's better to start with:
                #                      /------
                #                      |
                #                      |x
                #                      | x
                #                      |  x
                ((self.board.xymin[0], y) for y in range(
                    self.board.xymin[1]+1,
                    self.board.xymax[1]+1-(self.alignement_length+1))),
            )
        elif delta_xy == (-1, 1):  # diagonal downwards+to the left
            xyranges = (
                ((x, self.board.xymin[1]) for x in range(
                    self.board.xymin[0]+(self.alignement_length-1),
                    self.board.xymax[0]+1)),
                ((self.board.xymax[0], y) for y in range(
                    self.board.xymin[1]+1,
                    self.board.xymax[1]+1-(self.alignement_length+1))),
                )

        else:
            # TODO: error / raise NotImplementedError (?)
            raise NotImplementedError

        for xyrange in xyranges:
            for xy in xyrange:
                first_xy = None  # beginning of the found stones-line
                stone_value = None
                stone_index = 0
                while True:
                    cell_intvalue = self.board.get_cell(xy=xy, delta_xy=delta_xy).int_value
                    if cell_intvalue not in self.cellintvalue2player:
                        # cell_intvalue is a cell which do not belong to a player:
                        # maybe a default value cell (=a cell without no stone).
                        stone_value = None
                        stone_index = 0
                    # cell_intvalue is a cell which does belong to a player.
                    # let's update <stone_value>, if necessary:
                    elif stone_value is None:
                        stone_index = 1
                        stone_value = cell_intvalue
                        first_xy = xy
                    elif cell_intvalue != stone_value:
                        stone_value = 1
                        stone_index = cell_intvalue
                        first_xy = xy
                    else:
                        # at least two stones of the searched color have been found:
                        stone_index += 1
                        if stone_index >= self.alignement_length:
                            res[(first_xy, delta_xy)] = (stone_index, stone_value)

                    xy = (xy[0] + delta_xy[0],
                          xy[1] + delta_xy[1])

                    if self.board.is_xy_outside_limits(xy):
                        break

        return res

    def search_winning_position(self,
                                last_move=None):
        res = {}

        # TODO
        #   dans un premier temps je ne tiens pas compte de <last_move>
        for delta_xy in ((0, 1),
                         (1, 0),
                         (1, 1),
                         (-1, 1),
                         ):
            _res = self.find_winning_positions_for_deltaxy(delta_xy)
            if _res:
                res.update(_res)

        return res

    def update_results_from_current_board(self,
                                          last_move=None):
        res = self.search_winning_position(last_move)

        if not res:
            return

        # TODO
        #   On considère que le premier résultat est le seul à être pris en compte.
        (xy, delta_xy), (stone_index, stone_value) = tuple(res.items())[0]

        self.end_game()

        winner__player_id = self.cellintvalue2player[stone_value]
        self.gameresults.set_all_players_result(value=PLAYERRESULT_NOTVICTORIOUS)
        self.gameresults.players_results[winner__player_id] = PLAYERRESULT_VICTORIOUS


class Game(Game2DCellsRectangleIntValue):
    def __init__(self,
                 rules_name,
                 board_type,
                 gamestate_type,
                 players_description,
                 alignement_length,
                 ):
        self.alignement_length = alignement_length
        Game2DCellsRectangleIntValue.__init__(
            self,
            rules_name=rules_name,
            board_type=board_type,
            players_description=players_description,
            move_type=Move2DCellsRectangleIntValue,
            moves_type=Moves,
            gamestate_type=gamestate_type,
            gameresults_type=GameResults)

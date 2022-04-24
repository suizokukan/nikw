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
from game.baseclasses import GameResults as RootGameResults
from game.baseclasses_2Dboardint import PlayerDescriptionIntValue
from game.baseclasses import PlayersDescription as RootPlayersDescription
from game.baseclasses_2Dboardint import Game2DCellsRectangleIntValue, Move2DCellsRectangleIntValue
from game.baseclasses import Moves
from game.baseclasses import GameStatePlayersInSetOrder


class PlayersDescription(RootPlayersDescription):
    pass


class PlayerDescription(PlayerDescriptionIntValue):
    pass


class GameResults(RootGameResults):
    pass


class GameState(GameStatePlayersInSetOrder):
    def __init__(self,
                 next_player_turn_index,
                 next_moveid,
                 nbr_players,
                 first_player_turn_index,
                 board,
                 gameresults,
                 alignement_length):
        self.alignement_length = alignement_length
        GameStatePlayersInSetOrder.__init__(
            self,
            next_player_turn_index=next_player_turn_index,
            next_moveid=next_moveid,
            nbr_players=nbr_players,
            first_player_turn_index=first_player_turn_index,
            board=board,
            gameresults=gameresults)

    def is_board_a_winning_position(self,
                                    last_move=None):
        # TODO
        #   dans un premier temps je ne tiens pas compte de <last_move>
        winning_position, who_won = 777, 888
        return winning_position, who_won

    def update_results_from_current_board(self,
                                          last_move=None):
        winning_position, who_won = self.is_board_a_winning_position(last_move)
        self.gameresults.mainresult = 777


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

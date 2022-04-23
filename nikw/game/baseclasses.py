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
    nikw project : nikw/game/baseclasses.py
"""
from datetime import datetime

from exc_motherclass.motherclass import MotherClassSerErr
from hashfuncs import hashfunction, binhash_to_strb85

from game.constants import DEFAULT_GAME_CONFIGURATION
from game.constants import DEFAULT_FIRSTPLAYER_TURN_INDEX, DEFAULT_FIRSTMOVEID
from game.constants import DATANATURE_INMEMORY, PLAYERTYPE__NOPLAYER
from game.constants import GAMERESULT_UNDEFINED, PLAYERRESULT_UNDEFINED
from game.utils import explicit_playertype_constant


class RootClass(MotherClassSerErr):
    """
    Root class of all classes in this file.
    """
    def copy(self):
        self.export_as(expected_data_type=DATANATURE_INMEMORY)

    def export_as(self,
                  expected_data_type=DATANATURE_INMEMORY):
        raise NotImplementedError

    def init_from(self,
                  source,
                  source_type=DATANATURE_INMEMORY):
        raise NotImplementedError


class Game(RootClass):
    """
    Game as "chess" or "tic-tac-toe", not as "party" or "match".
    """
    def __init__(self,
                 rules_name,
                 players_description,
                 board_type,
                 move_type,
                 moves_type,
                 gamestate_type,
                 gameresult_type,
                 configuration=DEFAULT_GAME_CONFIGURATION):
        self.configuration = configuration

        self.rules_name = rules_name
        self.timestamp_start = datetime.now()

        self.gameid = self.get_gameid()

        self.players_description = players_description

        self.board_type = board_type

        self.move_type = move_type
        self.moves_type = moves_type
        self.moves = moves_type()

        self.gameresult_type = gameresult_type

        self.gamestate_type = gamestate_type
        self.current_gamestate = gamestate_type(
            next_player_turn_index=self.players_description.first_player_turn_index,
            next_moveid=self.moves.first_moveid,
            board=self.board_type(),
            gameresult=self.gameresult_type())

    def get_gameid(self):
        res = hashfunction()
        res.update(str(self.rules_name).encode())
        res.update(str(self.timestamp_start).encode())
        return res.digest()

    def improved_str(self):
        res = []
        res.append(f"Game '{binhash_to_strb85(self.gameid)}'")
        res.append(f"o  rules: '{self.rules_name}'.")
        res.append(f"o  started at {self.timestamp_start}.")

        res.append(self.players_description.improved_str())

        res.append(f"{len(self.moves)} move(s) already played:")
        res.append(self.moves.improved_str())

        res.append(f"o  current game state:")
        res.append(self.current_gamestate.improved_str())

        return "\n".join(res)

    def play_a_move(self):
        raise NotImplementedError


class GameState(RootClass):
    def __init__(self,
                 next_player_turn_index,
                 next_moveid,
                 board,
                 gameresult):
        self.next_player_turn_index = next_player_turn_index
        self.next_moveid = next_moveid
        self.board = board
        self.gameresult = gameresult

    def improved_str(self):
        res = []
        res.append("Game state:")
        res.append(f"o  next player turn index: {self.next_player_turn_index}")
        res.append(f"o  next move id: {self.next_moveid}")
        if self.next_player_turn_index == 0:
            res.append(f"o  game result: the game has not begun.")
        else:
            res.append(f"o  game result: {self.gameresult.improved_str()}")
        res.append(self.board.improved_str())
        return "\n".join(res)


class GameResult(RootClass):
    def __init__(self,
                 nbr_players):
        self.result = GAMERESULT_UNDEFINED
        self.players_results = {}
        for player_turn_index in range(nbr_players):
            self.players_results[player_turn_index] = PLAYERRESULT_UNDEFINED

    def improved_str(self):
        # TODO: explicit self.result + self.players_results
        return f"{self.result=}; {self.players_results=}"


class Moves(RootClass, dict):
    """
    [move index]: (Move,
                   GameState if config["keep intermediate gamestates"] is True)

    """
    def __init__(self,
                 first_moveid=DEFAULT_FIRSTMOVEID):
        self.first_moveid = first_moveid

    def improved_str(self):
        res = []
        for move_id, data in self.items():
            res.append(f"   o  move #{move_id}: {data[0].improved_str()}")
            if len(data) == 2:
                res.append(data[1].improved_str())
        return "\n".join(res)


class Move(RootClass):
    def __init__(self,
                 player_turn_index):
        self.player_turn_index = player_turn_index

    def improved_str(self):
        raise NotImplementedError


class PlayersDescription(RootClass, list):
    """
    [player_turn_index] = Player
    """
    def __init__(self,
                 nbr_players,
                 first_player_turn_index=DEFAULT_FIRSTPLAYER_TURN_INDEX):
        self.first_player_turn_index = first_player_turn_index
        self.nbr_players = nbr_players

    def improved_str(self):
        res = []
        res.append("Players:")
        for player_description in self:
            res.append(f"o  {player_description}")
        return "\n".join(res)


class PlayerDescription(RootClass):
    def __init__(self,
                 player_turn_index=None,
                 player_name=None,
                 player_type=PLAYERTYPE__NOPLAYER):
        self.player_turn_index = player_turn_index
        self.player_name = player_name
        self.player_type = player_type

    def improved_str(self):
        return f"'{self.player_name}' " \
            f"(id #{self.player_turn_index}/{explicit_playertype_constant(self.player_type)})"


class Board(RootClass):
    pass


class BoardCellIntegerValue(RootClass):

    def __init__(self,
                 int_value=None):
        RootClass.__init__(self)
        self.int_value = int_value

    def get_hashvalue(self):
        """
            BoardCellIntegerValue.get_hashvalue()

            Return a hash value of <self>.
            ___________________________________________________________________

            no PARAMETER

            RETURNED VALUE: (bytes)hash value
        """
        res = hashfunction()
        res.update(str(self.int_value).encode())
        return res.digest()

    def improved_str(self):
        return f"{self.int_value}"

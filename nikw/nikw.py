"""
Board > Board2D
"""
from exc_motherclass import MotherClassSerErr


DATANATURE_INMEMORY = 0x01
DATANATURE_DB = 0x02
DATANATURE_SERIALIZED = 0x03

PLAYERTYPE__NOPLAYER = 0x01
PLAYERTYPE__RANDOM = 0x02
PLAYERTYPE__HUMAN = 0x03
PLAYERTYPE__AI = 0x04


class RootClass(MotherClassSerErr):
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
    def __init__(self,
                 rules_name,
                 players_description=None,
                 gamestates=None):
        self.rules_name = rules_name
        self.players_description = players_description
        self.gamestates = gamestates

    def apply_a_move_to_a_gamestate(self,
                                    gamestate,
                                    move):
        raise NotImplementedError

    def is_this_a_legal_move_for_a_gamestate(self,
                                             gamestate,
                                             move):
        raise NotImplementedError


class GameStates(RootClass, dict):
    """
    * initial_gamestate
    [gamestate_id: 0, 1, 2...] : (Move, GameState)
    """
    pass


class GameState(RootClass):
    def __init__(self,
                 is_over=False,
                 board=None):
        self.is_over = is_over
        self.board = board


class Moves(RootClass, list):
    """
    [move index] = Move
    """
    pass


class Move(RootClass):
    pass


class Board(RootClass):
    pass


class PlayersDescription(RootClass, dict):
    """
    [player_id] = Player
    """
    pass


class PlayerDescription(RootClass):
    def __init__(self,
                 player_id=None,
                 player_name=None,
                 player_type=PLAYERTYPE__NOPLAYER):
        self.player_id = player_id
        self.player_name = player_name
        self.player_type = player_type

from qmove import QMove
from subprocess import Popen, PIPE
import os


class QPlayer:
    """ Player instance to interact with QEngine

    Attributes:
        is_ai (bool): Defines if current Players is an AI or not
        id_ (uuid instance): Unique identifier of Player
        name (str): Name of player
        executable (Pathlib.resolve() instance) : Path of executable
        color (str) : Color of current_player
        time_per_game (int) : Time per entire game for current player
    """

    def __init__(self, player_raw: dict, time_per_player_game: int):
        """ Receives player_raw object/dictionary and creates instance of QPlayer

        Args:
            player_raw (dict) : `{is_ai : True/False, id_ : uuid, name : name, executable: path}`
        """
        self.is_ai = player_raw["is_ai"]
        self.id_ = player_raw["id_"]
        self.name = player_raw["name"]
        self.executable = player_raw["executable"]
        self.color = player_raw["color"]
        self.time_per_game = time_per_player_game

        if self.is_ai and os.path.isfile(self.executable):
            self.proc = Popen([self.executable], stdin=PIPE, stdout=PIPE)
        else:
            self.proc = None

    def get_move(self, last_move: QMove):
        """ If AI, executes process. Else, stdin for move.

        Args:
            last_move (QMove): Move by last player.
        """

        if self.is_ai:
            self.proc.stdin.write(str.encode(last_move.to_string() + '\n'))
            self.proc.stdin.flush()
            new_move = QMove(os.read(self.proc.stdout.fileno(), 100))
        else:
            new_move = QMove(input("Move, it's your turn:\n\t>> "))

        return new_move

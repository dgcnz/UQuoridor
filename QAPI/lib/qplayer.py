from qmove import QMove
from subprocess import Popen, PIPE
from c_types import Coordinates
import os
from typing import Optional


class QPlayer:
    """ Player instance to interact with QEngine

    Attributes:
        is_ai (bool): Defines if current Players is an AI or not
        id_ (uuid instance): Unique identifier of Player
        name (str): Name of player
        executable (Pathlib.resolve() instance) : Path of executable
        color (str) : Color of current_player
        time_per_game (int) : Time per entire game for current player
        coordinates (Coordinates) : Current coordinates of player
    """

    def __init__(self, player_raw: dict, time_per_player_game: int,
                 start_side: int, board_size: int, n_players: int):
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
        self.start_side = start_side
        self.n_players = n_players
        self.coordinates = self.get_starting_coordinates(
            board_size, start_side)

        if self.is_ai and os.path.isfile(self.executable):
            self.proc: Optional[Popen] = self.start_ai(
                self.executable,
                self.n_players,
                self.time_per_game,
                self.start_side,
            )

    def get_starting_coordinates(self, board_size: int,
                                 start_side: int) -> Coordinates:

        if start_side == 0:
            coords = Coordinates(0, (board_size - 1) / 2)

        elif start_side == 1:
            coords = Coordinates((board_size - 1) / 2, board_size - 1)

        elif start_side == 2:
            coords = Coordinates(board_size - 1, (board_size - 1) / 2)

        elif start_side == 3:
            coords = Coordinates((board_size - 1) / 2, 0)

        return coords

    def start_ai(self, executable: str, n_players: int, time_per_game: int,
                 start_side: int) -> Popen:
        """ Initialize AI with corresponding starting position
        """
        proc = Popen([executable], stdin=PIPE, stdout=PIPE)

        INIT_MSG = f"$START {n_players} {start_side} {time_per_game}"

        proc.stdin.write(str.encode(INIT_MSG + '\n'))
        proc.stdin.flush()

        return proc

    def get_move(self, last_move: QMove):
        """ If AI, executes process. Else, stdin for move.

        Args:
            last_move (QMove): Move by last player.
        """

        # TODO: reduce time_per_game second by second
        if self.is_ai and self.proc is not None:
            self.proc.stdin.write(str.encode(last_move.to_string() + '\n'))
            self.proc.stdin.flush()
            new_move = QMove(os.read(self.proc.stdout.fileno(), 100))
        else:
            new_move = QMove(input("Move, it's your turn:\n\t>> "))

        if new_move.type == "player":
            self.coordinates = new_move.get_to()

        return new_move

    def update_coordinates(self, coordinates: Coordinates):
        self.coordinates = coordinates

    def fix_move(self, invalid_move: QMove):
        """ If AI, executes process. Else, stdin for move.

        Args:
            invalid_move (QMove): Move to be fixed
        """

        # TODO: reduce time_per_game second by second
        ERROR_MSG = f"INVALID_MOVE {invalid_move.to_string()}"

        if self.is_ai and self.proc is not None:
            self.proc.stdin.write(str.encode(ERROR_MSG + '\n'))
            self.proc.stdin.flush()
            new_move = QMove(os.read(self.proc.stdout.fileno(), 100))
        else:
            new_move = QMove(
                input("Move was invalid, enter a valid move:\n\t>> "))

        return new_move

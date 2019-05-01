from typing import List, Tuple, Type, Optional
import pprint
import uuid
from pathlib import Path
from lib.qmove import QMove, QMovePlayer, QMoveWall
from lib.qboard import QBoard
from lib.qplayer import QPlayer
from lib.c_types import Coordinates
from lib.utilities import parse_players, sort_players
import numpy as np

pp = pprint.PrettyPrinter(indent=4)


class QGame:
    """ Engine for Quoridor Board.

    Attributes:
        players (List[QPlayer]): list of QPlayer instances
        current_player (QPlayer): Player to be executed
        plies (int): number of turns each player had so far
        last_move (QMove): move played by current_player.prev
        board (np.ndarray[List[int]]): matrix
    """

    def __init__(self, player_list: List[dict], first_player: int,
                 time_per_player_game: int, board_size: int):

        self.players = [
            QPlayer(player, time_per_player_game, i, board_size)
            for i, player in enumerate(
                sort_players(player_list, first_player))
        ]

        self.plies = 0
        self.current_player = self.players[0]
        self.last_move = QMove("")
        self.history = []
        self.board_size = board_size
        self.board = QBoard(board_size)

    def save_move(self, move: QMove, player: QPlayer):
        """ Saves move to history

        Note: This will allow games to be reproduced.
        TODO: dump_history()
        """
        self.history.append({
            "ply": self.plies,
            "player_name": player.get_name(),
            "player_uuid": player.get_uuid(),
            "move": move.to_string()
        })

    def next(self):
        """ Get next move of next player
        Args:
            None
        Returns:
            (str) move : move in chess-like notation
        """

        exceeded = 5

        new_move = self.current_player.get_move(self.last_move)
        while not self.is_valid_move(new_move) and not exceeded:
            new_move = self.current_player.fix_move(new_move)
            exceeded -= 1

        if exceeded == 0:
            raise Exception("Player is retarded.")

        # Updating

        self.current_player.update_coordinates(new_move.get_to())

        self.save_move(new_move, self.current_player)

        self.current_player = self.players[(self.current_player + 1) % len(
            self.players)]

        self.update_board(new_move)

        self.last_move = new_move

        return new_move.to_string()

    def is_valid_move(self, move: Type[QMove]) -> bool:
        """ Checks if move is valid given Wall and Player constraints
        """
        if isinstance(move, QMoveWall):
            return self.check_wall_place(move)
        elif isinstance(move, QMovePlayer):
            return self.check_player_move(move)
        raise Exception("Wrong Type.")

    def update_board(self, move: Type[QMove]) -> None:
        # TODO: update_board
        if move.type == "player":
            return "owo"

    def game_finished(self) -> Optional[QPlayer]:
        """ Checks if game has finished.

        If yes, returns winner player, else returns None.
        """
        winner: Optional[QPlayer]

        for i, player in enumerate(self.players):
            abs_i = i * 4 / len(self.players)
            if abs_i == 0:
                if player.coordinates.x == self.board_size:
                    winner = player
            elif abs_i == 1:
                if player.coordinates.y == self.board_size:
                    winner = player
            elif abs_i == 2:
                if player.coordinates.x == 0:
                    winner = player
            elif abs_i == 3:
                if player.coordinates.y == 0:
                    winner = player

        return winner

    def check_wall_place(self, move: QMoveWall) -> bool:
        """ Check if Wall placement is legal
        Algorithm:
            * Check if wall overlaps with other wall
            * Check if wall is in it's entirety in the board
            * Check if wall blocks the last path from any player to its goal
        """
        return True

    def check_player_move(self, move: QMovePlayer) -> bool:
        player = self.players[self.plies % len(self.players)]
        x, y = move.get_to()

        return self.board.connected(player.coordinates, Coordinates(x, y))


def main():
    players: list
    first: int
    board_size = 9

    players = parse_players(input("Enter players:\n\t>> "))

    # TODO: random_generator or input to choose first player
    first = 0

    # TODO: hard code better time or input to choose time (seconds per entire playerxgame)
    time_per_player_game = 300

    quoridor = QGame(players, first, time_per_player_game, board_size)


if __name__ == '__main__':
    main()

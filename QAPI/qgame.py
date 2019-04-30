from typing import List, Tuple
import pprint
import uuid
from pathlib import Path
from lib.qmove import QMove
from lib.qplayer import QPlayer
from lib.utilities import parse_players, define_order

pp = pprint.PrettyPrinter(indent=4)


class QGame:
    """ Engine for Quoridor Board.

    Attributes:
        players (List[QPlayer]): list of QPlayer instances
        current_player (QPlayer): Player to be executed
        plies (int): number of turns each player had so far
        last_move (QMove): move played by current_player.prev

    """

    def __init__(self, player_list: List[dict], first_player: int,
                 time_per_player_game: int, board_size: int):

        self.players = define_order(
            [QPlayer(player, time_per_player_game) for player in player_list],
            first_player)

        self.plies = 0
        self.current_player = self.players[0]
        self.last_move = QMove("")
        self.history = []
        self.board_size = board_size

    def save_move(self, move: QMove, player: QPlayer):
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

        self.save_move(new_move, self.current_player)

        self.current_player = self.players[(self.current_player + 1) % len(
            self.players)]

        self.update_board(new_move)

        self.last_move = new_move

        return new_move.to_string()

    def is_valid_move(self, move: QMove) -> bool:
        if move.type == "wall":
            return self.check_wall_place(move)
        else:
            return self.check_player_move(move)

    def update_board(self, move: QMove):
        #TODO : update board

        if self.last_move == None:
            return

        #Update move on wall move

        if self.last_move.isWallPlace():
            #TODO Update move when wall is placed
            a = 1

        #Update board on player move
        else:
            x, y = last_p_move.getCoords()
            p_x, p_y, = self.getPlayerByColor(
                last_p_move.getPlayerColor()).getCoords()

            #Check sparse matrix for all positions pointing to the last place and updates
            #TODO Check for walls
            if (p_x > 0):
                self.board[transform_to_sparse(tuple(
                    x, y), self.i)][transform_to_sparse(
                        tuple(p_x - 1, p_y), self.i)] = 1
            if (p_x < self.i - 1):
                self.board[transform_to_sparse(tuple(
                    x, y), self.i)][transform_to_sparse(
                        tuple(p_x + 1, p_y), self.i)] = 1
            if (p_y > 0):
                self.board[transform_to_sparse(tuple(
                    x, y), self.i)][transform_to_sparse(
                        tuple(p_x, p_y - 1), self.i)] = 1
            if (p_y < self.j - 1):
                self.board[transform_to_sparse(tuple(
                    x, y), self.i)][transform_to_sparse(
                        tuple(p_x, p_y + 1), self.i)] = 1
                """
            for w in self.walls: #TODO Write conditions for checking a wall when a ove is made
                if(p_x > 0):
                    if( (w.north_west[0] == p_x - 1 and w.north_west[1] == p_y) or w.north_west[
                """

    def game_finished(self) -> QPlayer:
        winner: QPlayer = None

        for i, player in enumerate(player):
            abs_i = i * 4 / len(self.players)
            if abs_i == 0:
                if player.get_coords().x == self.board_size:
                    winner = player
            elif abs_i == 1:
                if player.get_coords().y == self.board_size:
                    winner = player
            elif abs_i == 2:
                if player.get_coords().x == 0:
                    winner = player
            elif abs_i == 3:
                if player.get_coords().y == 0:
                    winner = player

        return winner

    def check_wall_place(self, move: QMove):
        wall_t = move.get_wall()
        nw, se = wall_t.get_points()
        ori = wall_t.get_orientation()

        #Check for making sure it's not place on top of other wall
        for w in self.walls:
            if w.orient == ori and nw == w.get_points()[0] and se.get_coords()[1] == se:
                return False
            if w.orient == "h":
                if nw == w.get_coordsi[0] and se == tuple(se[0], se[1] - 1):
                    return False
            if w.orient == "v":
                if nw == w.get_coords()[0] and tuple(se[0] + 1, se[1]):
                    return False

        #Check to make sure there's still a path to the goal

        #TODO Implement A* or something else

        return True

    def check_player_move(self, move: QMove):
        q_player = getQPlayerByColor(q_pmove.getPlayerColor())
        x, y = move.getTo()

        # Make sure player is going to a valid position

        return isConnected(q_player.getCoords(), tuple(x, y))


def main():
    players: list
    first: int

    players = parse_players(input("Enter players:\n\t>> "))

    # TODO: random_generator or input to choose first player
    first = 0

    # TODO: hard code better time or input to choose time (seconds per entire playerxgame)
    time_per_player_game = 300

    quoridor = QGame(players, first, time_per_player_game)


if __name__ == '__main__':
    main()

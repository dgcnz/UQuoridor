from typing import List
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
                 time_per_player_game: int):

        self.players = define_order(
            [QPlayer(player, time_per_player_game) for player in player_list],
            first_player)

        self.plies = 0
        self.current_player = self.players[0]
        self.last_move = QMove("")
        self.history = []

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

        not_exceeded = 5

        new_move = self.current_player.get_move(self.last_move)
        while not self.is_valid_move(new_move) and not_exceeded:
            new_move = self.current_player.fix_move(new_move)
            not_exceeded -= 1

        self.save_move(new_move, self.current_player)
        self.current_player = self.players[(self.current_player + 1) % len(
            self.players)]
        self.last_move = new_move

        return new_move.to_string()

    def is_valid_move(self, move: QMove) -> bool:
        if move.is_wall():
            return self.check_wall_place(move)
        else:
            return self.check_player_move(move)

    def check_wall_place(self, move: QMove):
        wall_t = move.getWall()
        nw, se = wall_t.getCoords()
        ori = wall_t.getOrient()

        #Check to make sure it's within bounds
        if (nw[0] < 0 or se[0] < 0 or nw[1] > i - 1 or se[1] > j - 1):
            return False

        #Check for making sure it's not place on top of other wall
        for w in self.walls:
            if w.orient == ori and nw == w.getCoords()[0] and se.getCoords(
            )[1] == se:
                return False
            if w.orient == "h":
                if nw == w.getCoords[0] and se == tuple(se[0], se[1] - 1):
                    return False
            if w.orient == "v":
                if nw == w.getCoords()[0] and tuple(se[0] + 1, se[1]):
                    return False
        #Check to make sure there's still a path to the goal

        #TODO Implement A* or something else

        return True

    def check_player_move(self, move: QMove):

        if q_pmove.getPlayerColor() != self.color_turn:
            return False
        q_player = getQPlayerByColor(q_pmove.getPlayerColor())
        x, y = move.getTo()

        # Make sure the move request is in the bound of the board and it's not the same position
        if x > 0 and x >= self.i:
            return False
        if y < 0 or y >= self.j:
            return False
        if x == q_player.getCoords()[0] and y == q_player.getCoords()[1]:
            return False

        if not isConnected(q_player.getCoords(), tuple(x, y)):
            return False

        return True


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

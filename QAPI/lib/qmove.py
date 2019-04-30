from utilities import parse_move
from c_types import Coordinates
from qwall import QWall


class QMove:
    """
    {
        type (str): wall | player,
        coordinates : nw | next_pos,
        orientation: (h|w) | None,
    }
    """

    def __init__(self, raw_move: str):
        parse = parse_move(raw_move)

        self.raw = raw_move
        self.type = parse["type"]
        self.coordinates = parse["coordinates"]
        self.orientation = parse["orientation"]

    def get_type(self) -> str:
        return self.type

    def to_string(self) -> str:
        return self.raw


class QMoveWall(QMove):
    def __init__(self, raw_move: str):
        super().__init__(raw_move)

        self.wall = QWall(self.coordinates, self.orientation)

    def get_wall(self):
        return self.wall


class QMovePlayer(QMove):
    def __init__(self, raw_move: str):
        super().__init__(raw_move)

        self.coords_to = self.coordinates

    def get_to(self) -> Coordinates:
        return self.coords_to

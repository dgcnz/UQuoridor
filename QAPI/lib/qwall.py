from c_types import Coordinates


class QWall:
    def __init__(self, nw: Coordinates, orientation: str):

        self.se = Coordinates(
            nw.x, nw.y) if orientation.lower() == "v" else Coordinates(
                nw.x + 1, nw.y)

        self.nw = nw
        self.orientation = orientation

    def get_points(self) -> tuple:
        return tuple(self.nw, self.se)

    def get_orientation(self) -> str:
        return self.orientation

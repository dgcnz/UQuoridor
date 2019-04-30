class QMove:
    """
    {
        type: wall | player,
        coordinates: nw | next_pos,
        orientation: (h|w) | None,
    }
    """

    def __init__(self, raw_move: str):
        self.raw = raw_move

    def isWallPlace(self) -> bool:
        return

    def isPlayerMove(self) -> bool:
        return False

    def to_string(self):
        return self.raw


class QMoveWall(QMove):
    def __init__(self, raw_move: str):
        QMove.__init__(raw_move)

        self.wall = QWall(tuple(0, 0),
                          "h")  #TODO Parse into wall movement and orientation

    def isWallPlace(self) -> bool:
        return True

    def isPlayerMove(self) -> bool:
        return False

    def getWall(self):
        return self.wall


class QMovePlayer(QMove):
    def __init__(self, raw_move: str):
        QMove.__init__(raw_move)
        self.coords_to: SparsePoint = tuple(
            0, 0)  #TODO Parse raw_move into coords
        self.color: Color = 0  #TODO Parse raw_move into color
        self.walls_remaining: int = 10

    def getCountWalls(self) -> int:
        return self.walls_remaining

    def isWallPlace(self) -> bool:
        return False

    def isPLayerMove(self) -> bool:
        return True

    def getQPlayerColor(self) -> Color:
        return self.color

    def getTo(self) -> SparsePoint:
        return self.coords_to

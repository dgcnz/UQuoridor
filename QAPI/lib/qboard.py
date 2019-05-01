import numpy as np
from math import inf as INFINITY
from typing import Union, Optional, Tuple, List
from c_types import Coordinates
from operator import itemgetter


class QBoard:
    """ Board API for Quoridor

    Attributes:
        size (int): length of board
        matrix (2d numpy array with integer lists inside): 2d adjacency list
    """

    def __init__(self, size: int):
        self.size = size
        self.matrix = np.empty([size, size], dtype=object)
        self.fill_at_start()

    def fill_at_start(self):
        """ Fills board as size x size grid graph

        *Note*: for the board to be playable it needs to allocate players
        and modify the edges around them.
        """
        for j, row in enumerate(self.matrix):
            for i, col in enumerate(row):
                edges = []

                if j > 0:
                    edges.append(Coordinates(i, j - 1))
                if j < self.size - 1:
                    edges.append(Coordinates(i, j + 1))
                if i > 0:
                    edges.append(Coordinates(i - 1, j))
                if i < self.size - 1:
                    edges.append(Coordinates(i + 1, j))

                self.matrix[i][j] = edges

    def connected(self,
                  p1: Coordinates,
                  p2: Coordinates,
                  dist: Optional[int] = None) -> bool:
        """ Returns true if there is a path between p1 and p2 with distance dist

        Note: distance is calculated as number of edges away from one point
        """

        if dist == 1:
            # Checks for single edge existence
            for p_i in self.matrix[p1]:
                if p_i == p2:
                    return True
            return False

        elif dist is None:
            # Checks path in the entirety of the board
            return True

        else:
            # Checks path in bounded dist
            return True

    def __getitem__(self, key: Union[Coordinates, Tuple[int, int]]
                    ) -> List[Coordinates]:
        return self.matrix[key]


def main():

    c = Coordinates(1, 2)
    t = (1, 2)

    b = QBoard(size=9)

    print(f"coordinates {c} -> {b[c]}")
    print(f"tuple {t} -> {b[t]}")


if __name__ == '__main__':
    main()

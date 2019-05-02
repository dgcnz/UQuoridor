import numpy as np
from typing import Union, Optional, Tuple, List, Set
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

    def show(self):
        print("\\", end=" ")
        for i in range(self.size):
            print(i, end="   ")
        print("")
        for y, row in enumerate(self.matrix):
            print(y, end=" ")
            for x, col in enumerate(row):
                print("x", end="")
                if x < self.size - 1 and (x + 1, y) in col:
                    print("---", end="")
                else:
                    print("   ", end="")
            print("\n  ", end="")
            if y < self.size - 1:
                for x, col in enumerate(row):
                    if (x, y + 1) in col:
                        print("|", end="   ")
                    else:
                        print(" ", end="   ")
            print("")

    def fill_at_start(self):
        """ Fills board as size x size grid graph

        *Note*: for the board to be playable it needs to allocate players
        and modify the edges around them.
        """
        for y, row in enumerate(self.matrix):
            for x, col in enumerate(row):
                edges = []

                if y > 0:
                    edges.append(Coordinates(x, y - 1))
                if y < self.size - 1:
                    edges.append(Coordinates(x, y + 1))
                if x > 0:
                    edges.append(Coordinates(x - 1, y))
                if x < self.size - 1:
                    edges.append(Coordinates(x + 1, y))

                self.matrix[(y, x)] = edges

    def connected(self,
                  p1: Coordinates,
                  p2: Union[List[Coordinates], Coordinates],
                  dist: Optional[int] = None) -> bool:
        """ Returns true if there is a path between p1 and p2 with distance dist

        Note: distance is calculated as number of edges away from one point
        """

        if dist == 1 and isistance(p2, Coordinates):
            # Checks for single edge existence
            for p_i in self.matrix[p1]:
                if p_i == p2:
                    return True
            return False

        elif dist is None and isinstance(p2, Coordinates):
            # Checks path in the entirety of the board
            return path_exists(self, p1, [p2])

        elif dist is None and isinstance(p2, list):
            # Checks if there is at least one path between p1 and its goal
            return path_exists(self, p1, p2)
        else:
            # Checks path in bounded dist
            return True

    def __getitem__(self, key: Union[Coordinates, Tuple[int, int]]
                    ) -> List[Coordinates]:
        return self.matrix[(key[1], key[0])]


def path_exists(board: QBoard, start: Coordinates,
                goals: List[Coordinates]) -> bool:
    """ BFS implementation for path checking
    """

    visited: Set[Coordinates] = set()
    queue = [start]

    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.add(v)
            print(f"Visiting {v}")
            queue.extend(set(board[v]) - visited)
        if v in goals:
            return True

    # print(visited)
    return False


def main():
    b = QBoard(size=9)
    b.show()
    b[(0, 0)].remove((0, 1))
    b[(0, 0)].remove((1, 0))

    b.show()
    print(path_exists(b, (0, 0), [(1, 1)]))
    """
    for y, row in enumerate(b.matrix):
        for x, col in enumerate(row):
            print(f"{(x, y)} : {col}")
    """


if __name__ == '__main__':
    main()

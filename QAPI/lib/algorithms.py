from typing import List, Set
from c_types import Coordinates


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

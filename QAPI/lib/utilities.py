from typing import List
import uuid, re
from pathlib import Path
from qplayer import QPlayer


def is_valid_pattern_move(raw_move: str, rows: int, cols: int):
    """
    Returns True if raw_move is valid
    """

    rows_ = chr(ord('a') + rows)
    cols_ = cols

    pattern = re.compile(
        f"^(?:w|b)(([a-{rows_}][1-{cols_}])|([a-{rows_}][1-{cols_}](v|h)))$")
    if pattern.match(raw_move).group():
        return True
    return False


def random_name() -> str:
    """
    Gives a random name to our dear AI Agent. Please be considerate.

    Returns:
        (str) name
    """
    return "Antonio"


def parse_players(raw_line: str) -> List[dict]:
    """Parses raw input of players.


    Args:
        raw_line (str): raw_input string of format:
            ```
            Human:{name}:{color} ... AI:{executable_path}:{color} Human:{name}:{color} ...
            ```

    Returns:
        (List[dict]):
            - list of objects with attributes:
            `{is_ai : True/False, id_ : uuid, name : name, executable: path, color: str}`
    """
    res = []

    players_raw = raw_line.split(" ")
    for player in players_raw:
        kind, name_exec, color = player.split(":")

        res.append({
            "is_ai": (kind == "AI"),
            "id_":
            uuid.uuid4(),
            "name":
            name_exec if kind != "AI" else random_name(),
            "executable":
            Path(name_exec).resolve() if kind == "AI" else None,
            "color":
            color
        })

    return res


def sort_players(player_list: list, first_player: int) -> list:
    """ Sorts list clockwise relative to first_player

    Args:
        player_list (list) : List of players to be sorted
        first_player : player to be used as pivot

    Returns:
        (list) : list of sorted players
    """
    # TODO: Sorting. For now it returns the list assuming the first is the first in the list

    return player_list

from typing import List
import uuid, re
from pathlib import Path
from qplayer import QPlayer
from c_types import Coordinates


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


def define_order(player_list: List[QPlayer],
                 first_player: int) -> List[QPlayer]:
    """ Sorts list clockwise relative to first_player

    Args:
        player_list (List[QPlayer]) : List of QPlayers to be sorted
        first_player : Player to be used as pivot

    Returns:
        (List[QPlayer]) : list of sorted players
    """
    # TODO: Sorting. For now it returns the list assuming the first is the first in the list

    return player_list


def parse_move(sequence: str):
	"""
	Parses move string sequence to an object 

	Args:
		sequence : Sequence encoded in the form xy[d]
			x: Substring that encodes the horizontal position as a sequence of alphabetic characters.
			y: Substring that encodes the vertical position as a sequence of numeric characters.
			d: Optional character that encodes vertical (v) or horizontal (h) wall direction.
	
	Return value:
		{
			"type": "player" | "wall",
			"coordinates": Coordinates(x, y),
			"direction": None | "v" | "h"
		}
	
	"""
	
	# Define type of object

	is_player = sequence[-1].isnumeric()

	if is_player:
		obj_type = "player"
		coordinate_string = sequence
	else:
		obj_type = "wall"
		coordinate_string = sequence[:-1]
	

	# Define coordinates

	coordinate_regex= re.match(r"([a-z]+)([0-9]+)", coordinate_string, re.I)

	digits = [ord(char) - ord('a') for char in coordinate_regex.group(1)[::-1]]

	y = 0

	for digit in digits:
		y *= 26
		y += digit
	
	x = int(coordinate_regex.group(2)) - 1
	
	coordinates = Coordinates(x, y)


	# Define Orientation

	if is_player:
		orientation = None
	else:
		orientation = sequence[-1]

	
	# Return object

	return {
		"type": obj_type,
		"coordinates": coordinates,
		"orientation": orientation
	}

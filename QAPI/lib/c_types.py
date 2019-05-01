from operator import itemgetter


class Coordinates(tuple):
    """ Coordinates (x, y)

    Attributes:
        x (int) : coordinate x
        y (int) : coordinate y
    """
    x = property(itemgetter(0))
    y = property(itemgetter(1))

    def __new__(cls, x: int, y: int):
        return tuple.__new__(Coordinates, (x, y))

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

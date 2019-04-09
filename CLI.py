import numpy
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
# from Quoridor import QuoridorGame

WIDTH = 50
HEIGHT = 25
TIMEOUT = 100


class QuoridorCurses(object):
    def __init__(self, window):
        self.window = window

    """
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.walls = []
    """

    def render(self):
        self.render_static(4, 4)

    def render_static(self, x0, y0):
        i = 1
        j = 0
        for x in range(x0, curses.COLS - 1):
            xp = x - x0
            for y in range(y0, curses.LINES - 1):
                yp = y - y0
                if (yp == 1) and (xp <= 40) and (xp >=
                                                 7) and self.valid_row(xp):
                    self.window.addch(y, x, chr(j + ord('a')))
                    j += 1
                if (xp == 3) and (yp <= 20) and (yp >= 3) and ((
                    (yp + 1) % 2) == 0):
                    self.window.addch(y, x, chr(i + ord('0')))
                    i += 1
                if self.in_board(
                        xp, yp, 7,
                        3) and self.valid_row(xp) and self.valid_col(yp):
                    self.window.addch(y, x, '\u2610')

    def valid_row(self, xp):
        return ((xp + 1) % 4) == 0

    def valid_col(self, yp):
        return ((yp + 1) % 2) == 0

    def in_board(self, xp, yp, saxis_x, saxis_y):
        return (xp <= saxis_x + 32) and (xp >= saxis_x) and (
            yp <= saxis_y + 16) and (yp >= saxis_y)


def main():
    curses.initscr()
    curses.beep()
    curses.beep()
    window = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    # quoridor = QuoridorCurses(QuoridorGame(), window)
    quoridor = QuoridorCurses(window)

    while True:
        window.clear()
        window.border(0)
        # quoridor.render()

        event = window.getch()
        if event >= ord('a') and event <= ord('z'):
            window.addstr(10, 10, "ssd")

        if event == 27:
            break

        if event == 32:
            key = -1
            while key != 32:
                key = window.getch()

        if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            #asd
            print("keyup")


if __name__ == '__main__':
    main()

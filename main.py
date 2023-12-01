from graphics import Window
from maze import Maze


def main() -> None:
    win = Window(550, 550)

    m = Maze(25, 25, 10, 10, 50, 50, win)
    m._break_entrance_and_exit()
    win.wait_for_close()


main()

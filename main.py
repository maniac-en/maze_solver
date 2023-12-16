from graphics import Window
from maze import Maze


def main() -> None:
    startx, starty = 25, 25
    row, col = 15, 15
    cellx, celly = 50, 50
    height = 2 * startx + row * cellx
    width = 2 * starty + col * celly
    win = Window(height, width)
    m = Maze(startx, starty, row, col, cellx, celly, win)
    m._break_entrance_and_exit()
    m._break_walls_r(0, 0)
    m._draw_start_line()
    m._solve()
    m._draw_end_line()
    win.wait_for_close()


main()

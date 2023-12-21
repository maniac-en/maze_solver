from graphics import Window
from maze import Maze
import click


@click.command()
@click.option(
    '--maze-size',
    type=(int, int),
    default=(15, 15),
    show_default=True,
    help='row, column for the maze')
def main(maze_size) -> None:
    """Welcome to Maniac's Maze solver"""

    startx, starty = 25, 25
    row, col = maze_size
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

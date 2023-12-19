from cell import Cell
from graphics import Line, Point
from time import sleep
import random


class Maze():
    """Maze class

    This class is used to build the actual maze by making the use of Cell class
    which in turn makes use of graphics.Line and graphics.Point class.

    Maze consists a grid of Cells, and each Cell has walls which can be broken,
    which in turn helps to build an actual maze and then the solution for the
    same.

    Attributes
    ----------
    x1 : int
        x coordinate of maze of start on the Window canvas.
    y1 : int
        y coordinate of maze of start on the Window canvas.
    num_rows : int
        number of rows in maze.
    num_cols : int
        number of column in maze.
    cell_size_x : int
        size of cell wall in maze along x axis, i.e., length.
    cell_size_y : int
        size of cell wall in maze along y axis, i.e., width.
    _win : graphics.Window
        Window class instance on which the maze would be built and solved.
    _cells : list[list[Cell]]
        list of lists of Cell class instances which build up the Maze.
    """

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None) -> None:
        """Instantiates the Maze class

        This method create the instance of Maze by first setting the attributes
        passed from driver code, and then invokes the Maze._create_cells to
        create Cell instance for the Maze using the attributes passed to
        __init__.
        """

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        return

    def _create_cells(self) -> None:
        """Create Maze cells

        This method creates an attribute called _cells for a given Maze instance
        which is a list of lists of Cell class instances.

        Once the _cells is populated, it invokes Maze._draw_cell on each of
        above create Cell instances.
        """

        self._cells = []
        for c in range(self.num_cols):
            self._cells.append([])
            for r in range(self.num_rows):
                self._cells[c].append(Cell(self._win))

        for i, cell_col in enumerate(self._cells):
            for j, cell in enumerate(cell_col):
                self._draw_cell(cell, i, j)
        return

    def _draw_cell(self, cell, i, j, fill_color="black") -> None:
        """Draw a Cell class instance on Maze's canvas

        This method graphically draws the cell on the canvas with wall color as
        "black" unless specifically passed in arguments with the help of
        Cell.draw method, post which it invokes Maze._animate which redraws the
        canvas to visually show the above drawn Cells.

        The top-left and bottom-right corners of every Cell instance is
        calculated using starting position of maze as well as size of cell walls
        specified during the Maze creation.
        """

        x = self.x1 + i * self.cell_size_x
        y = self.y1 + j * self.cell_size_y

        cell.draw(x, y, x + self.cell_size_x, y + self.cell_size_y, fill_color)
        self._animate()
        return

    def _break_entrance_and_exit(self) -> None:
        """This method removes the top wall from start Cell and bottom wall from
        end Cell of the Maze

        It first marks the required wall as False, and invokes the
        Maze._draw_cell to redraw that Cell on the canvas where the Maze is
        previously already drawn.
        """

        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0], 0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._cells[-1][-1], len(self._cells) - 1,
                        len(self._cells[0]) - 1)
        return

    def _get_neighbours(self, i, j) -> list:
        """This method returns list of neighbours of a given Cell

        It takes the row and column index of a Cell and append the Tuple of
        (row, column) in the neighbours list if the neighbour exists.

        In case any of the Cell passed as input lies on border of maze, it will
        at-most not have one of the neighbours.

                            top_neighbour
        left_neighbour          Cell            right_neighbour
                            bottom_neighbour
        """

        neighbours = []
        if i != 0:
            neighbours.append((i - 1, j))
        if j != 0:
            neighbours.append((i, j - 1))
        if i < len(self._cells) - 1:
            neighbours.append((i + 1, j))
        if j < len(self._cells[0]) - 1:
            neighbours.append((i, j + 1))
        return neighbours

    def _break_walls_r(self, i, j) -> None:
        """Break Maze Cell walls recursively to build the Maze

        This first invocation of this method is done from driver code starting
        from first Cell, i.e, both i and j equal to 0

        - Mark the current Cell as visited
        - While the last Cell of maze is not visited:
            - Get neighbours of current Cell which are not yet visited
            - If there's at-least one neighbour:
                - Randomly choose one of those neighbours
                - Break the wall between current Cell and randomly chosen
                  neighbour by marking the common Cell wall between the two as
                  False and then redrawing both the Cells
                - Invoke the Maze._break_walls_r taking the randomly selected
                  neighbour as input
            - If there's no neighbour available which it not visited:
                - Randomly select any of the neighbour
                - Invoke the Maze._break_walls_r taking the randomly selected
                  neighbour as input
        """

        self._cells[i][j].visited = True
        while not self._cells[-1][-1].visited:
            possible_directions = [d for d in filter(
                lambda c: not self._cells[c[0]][c[1]].visited,
                self._get_neighbours(i, j))]
            if len(possible_directions) == 0:
                self._draw_cell(self._cells[i][j], i, j)
                i, j = random.choice(self._get_neighbours(i, j))
            else:
                to_i, to_j = random.choice(possible_directions)
                if j == to_j:  # same row movement
                    if to_i > i:
                        self._cells[i][j].has_right_wall = False
                        self._cells[to_i][to_j].has_left_wall = False
                    else:
                        self._cells[i][j].has_left_wall = False
                        self._cells[to_i][to_j].has_right_wall = False
                elif i == to_i:  # same column movement
                    if to_j > j:
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[to_i][to_j].has_top_wall = False
                    else:
                        self._cells[i][j].has_top_wall = False
                        self._cells[to_i][to_j].has_bottom_wall = False

                self._draw_cell(self._cells[i][j], i, j)
                self._draw_cell(self._cells[to_i][to_j], to_i, to_j)
                return self._break_walls_r(to_i, to_j)

    def _reset_cells_visited(self) -> None:
        """Mark all Maze Cells as not visited"""

        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _is_not_blocked(self, x, y, to_x, to_y) -> bool:
        """Check if Cell at (x, y) is blocked or not to go Cell at (to_x, to_y)

        This method checks weather the common wall between the two Cells are
        both broken or not. If yes, then return True else False.

        In case any of the passed Cell coordinates do not exist, handle the
        IndexError exception printing where it was caught and then return False.
        """

        try:
            if x == to_x:
                if to_y > y:  # going down
                    return not (self._cells[x][y].has_bottom_wall and
                                self._cells[to_x][to_y].has_top_wall)
                else:  # going up
                    return not (self._cells[x][y].has_top_wall and
                                self._cells[to_x][to_y].has_bottom_wall)
            elif y == to_y:
                if to_x > x:  # going right
                    return not (self._cells[x][y].has_right_wall and
                                self._cells[to_x][to_y].has_left_wall)
                else:  # going left
                    return not (self._cells[x][y].has_left_wall and
                                self._cells[to_x][to_y].has_right_wall)
        except IndexError as e:
            print("\n\nCaught exception at Maze._is_not_blocked function")
            print(f"{e} for {x}, {y}...{to_x}, {to_y}\n")
            return False
        return False

    def _draw_start_line(self) -> bool:
        """Draw a line from top-mid of start Cell to center of start Cell"""

        start_x, start_y = self._cells[0][0].get_center()
        if start_x is not None and start_y is not None:
            if self._win:
                self._win.draw_line(Line(Point(start_x, start_y - self.y1),
                                         Point(start_x, start_y)), "red")
            return True
        return False

    def _draw_end_line(self) -> bool:
        """Draw a line from center of end Cell to bottom-mid of end Cell"""

        end_x, end_y = self._cells[-1][-1].get_center()
        if end_x is not None and end_y is not None:
            if self._win:
                self._win.draw_line(Line(Point(end_x, end_y + self.y1),
                                         Point(end_x, end_y)), "red")
            return True
        return False

    def _solve(self) -> bool:
        """Solve the Maze by invoking Maze._solve_r at 0, 0 as input

        Returns the same boolean value as received from Maze._solve_r
        """

        self._reset_cells_visited()
        return self._solve_r(0, 0)

    def _solve_r(self, i, j) -> bool:
        """Solve the Maze recursively using Depth-First search algorithm

        - If the current Cell is an end Cell of the Maze, or, if it's one of the
          neighbours of the end Cell, recursion can be stopped as the solution
          is found
        - Else,
            - Mark the current Cell as visited
            - For every neighbour of current Cell:
                - If the path to that neighbour is not blocked:
                    - Draw the move from current Cell to that neighbour
                    - Invoke Maze._solve_r with current neighbour as input
                    - If the return value of above invocation is False, that
                      means there's no path which is a solution from current
                      neighbour to the end Cell
                      - We draw a move from this neighbour back to old cell, but
                        in undo color to show the backtracking
                - Proceed to check the neighbour as the their was no valid path
                  for the previous neighbour (depth of that neighbour)
        """

        end_cell_ix = len(self._cells) - 1
        end_cell_iy = len(self._cells[0]) - 1
        self._animate(0.05)
        if (i == end_cell_ix and j == end_cell_iy):
            return True
        elif (end_cell_ix, end_cell_iy) in self._get_neighbours(i, j) and\
                self._is_not_blocked(i, j, end_cell_ix, end_cell_iy):
            current = self._cells[i][j]
            target = self._cells[end_cell_ix][end_cell_iy]
            current.visited = True
            current.draw_move(target)
            self._animate(0.05)
            return True
        else:
            current = self._cells[i][j]
            current.visited = True
            for (to_x, to_y) in self._get_neighbours(i, j):
                target = self._cells[to_x][to_y]
                if self._is_not_blocked(
                        i, j, to_x, to_y) and not target.visited:
                    current.draw_move(target)
                    self._animate(0.05)
                    if not self._solve_r(to_x, to_y):
                        target.draw_move(current, True)
                    else:
                        return True

    def _animate(self, time=0.02) -> None:
        """Redraw the graphics.Window with a delay to visualise drawing"""

        if self._win:
            self._win.redraw()
            sleep(time)
        return

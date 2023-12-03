from cell import Cell
from time import sleep
import random


class Maze():

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None) -> None:
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
        x = self.x1 + i * self.cell_size_x
        y = self.y1 + j * self.cell_size_y

        cell.draw(x, y, x + self.cell_size_x, y + self.cell_size_y, fill_color)
        self._animate()
        return

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0], 0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._cells[-1][-1], len(self._cells) - 1,
                        len(self._cells[0]) - 1)
        return

    # @@@ test case pending
    def _get_neighbours(self, i, j) -> list:
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

    # @@@ test case pending
    def _break_walls_r(self, i, j) -> None:
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

    # @@@ test case pending
    def _reset_cells_visited(self) -> None:
        for row in self._cells:
            for cell in row:
                cell.visited = False

    # @@@ test case pending
    def _is_not_blocked(self, x, y, to_x, to_y) -> bool:
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

    # @@@ test case pending
    def _solve(self) -> bool:
        self._reset_cells_visited()
        return self._solve_r(0, 0)

    # @@@ test case pending
    def _solve_r(self, i, j) -> bool:
        self._animate(0.05)
        if (i == len(self._cells) - 1 and j ==
                len(self._cells[0]) - 1) or (-1, -1) in self._get_neighbours(i, j):
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
                        return False
                    else:
                        return True

    def _animate(self, time=0.02) -> None:
        if self._win:
            self._win.redraw()
            sleep(time)
        return

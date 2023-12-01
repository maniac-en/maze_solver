from cell import Cell
from time import sleep


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

    def _draw_cell(self, cell, i, j) -> None:
        x = self.x1 + i * self.cell_size_x
        y = self.y1 + j * self.cell_size_y

        cell.draw(x, y, x + self.cell_size_x, y + self.cell_size_y)
        self._animate()
        return

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0], 0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._cells[-1][-1], len(self._cells) - 1,
                        len(self._cells[0]) - 1)
        return

    def _animate(self) -> None:
        if self._win:
            self._win.redraw()
            # sleep(0.05)
        return

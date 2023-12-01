from graphics import Line, Point


class Cell:
    def __init__(self, win=None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        return

    def draw(self, x1, y1, x2, y2, fill_color="black") -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self.left_line = Line(Point(x1, y1), Point(x1, y2))
        self.top_line = Line(Point(x1, y1), Point(x2, y1))
        self.right_line = Line(Point(x2, y1), Point(x2, y2))
        self.bottom_line = Line(Point(x1, y2), Point(x2, y2))

        if self._win:
            bg_color = self._win.background
            self.left_fill_color = fill_color if self.has_left_wall else bg_color
            self.top_fill_color = fill_color if self.has_top_wall else bg_color
            self.right_fill_color = fill_color if self.has_right_wall else bg_color
            self.bottom_fill_color = fill_color if self.has_bottom_wall else bg_color
            self._win.draw_line(self.left_line, self.left_fill_color)
            self._win.draw_line(self.top_line, self.top_fill_color)
            self._win.draw_line(self.right_line, self.right_fill_color)
            self._win.draw_line(self.bottom_line, self.bottom_fill_color)
        else:
            bg_color = "white"
            self.left_fill_color = fill_color if self.has_left_wall else bg_color
            self.top_fill_color = fill_color if self.has_top_wall else bg_color
            self.right_fill_color = fill_color if self.has_right_wall else bg_color
            self.bottom_fill_color = fill_color if self.has_bottom_wall else bg_color
        return

    def get_center(self) -> tuple[int, int] | tuple[None, None]:
        if self._x1 is not None\
                and self._y1 is not None\
                and self._x2 is not None\
                and self._y2 is not None:
            return (self._x2 + self._x1) / 2, (self._y2 + self._y1) / 2
        else:
            return None, None

    def draw_move(self, to_cell, undo=False) -> bool:
        self.move_color = "red" if not undo else "gray"
        x1, y1 = self.get_center()
        x2, y2 = to_cell.get_center()
        if x1 is None or\
                y1 is None or\
                x2 is None or\
                y2 is None:
            return False
        self.draw(x1, y1, x2, y2, self.move_color)
        return True

    def __repr__(self) -> str:
        out_string = f"""{self._x1}, {self._y1} {self._x2}, {self._y2} {self.has_left_wall} {self.has_top_wall} {self.has_right_wall} {self.has_bottom_wall}"""
        return out_string

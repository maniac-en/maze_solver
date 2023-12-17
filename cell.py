from graphics import Line, Point


class Cell:
    """Cell class to create a maze cell on the Canvas of graphics.Window object

    This class creates a cell which has four lines: left, top, right, bottom
    which are all instances of graphics.Line class. Each Cell instance is
    uniquely determined by it's top-left coordinate and bottom-right coordinate.

    Attributes
    ----------
    has_left_wall : bool
        determines weather the Cell instance has left wall or not.
    has_top_wall : bool
        determines weather the Cell instance has top wall or not.
    has_right_wall : bool
        determines weather the Cell instance has right wall or not.
    has_bottom_wall : bool
        determines weather the Cell instance has bottom wall or not.
    visited : bool
        determines weather the Cell instance has been visited or not whilst
        trying to determine the Maze solution.
    _x1 : tuple[None, int]
        x coordinate of top-left corner.
    _y1 : tuple[None, int]
        y coordinate of top-left corner.
    _x2 : tuple[None, int]
        x coordinate of bottom-right corner.
    _y2 : tuple[None, int]
        y coordinate of bottom-right corner.
    _win : graphics.Window
        Instance of graphics.Window class on which Cell Lines are drawn
    """

    def __init__(self, win=None) -> None:
        """Instantiates the Cell class

        Default:
        - All four walls of Cell instance exists
        - Cell instance is not visited
        - Corner coordinates of Cell instance are None

        Optional:
        - Use the passed Window instance else None
        (None Window instance is used in testing)
        """

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        return

    def draw(self, x1, y1, x2, y2, fill_color="black") -> bool:
        """Draw the Cell instance onto graphics.Window canvas

        - If any of the corner coordinates are None, return False stating that
        the cell wasn't drawn.
        - Else,
            - Create all four Cell wall Lines.
            - Set the bg_color to use the passed background color or "white".
            ("white" is default background color)
            - Set the Cell wall Line colors to either:
                - Same as bg_color (When the wall shouldn't exist).
                - Passed fill_color else default fill_color, i.e, "black".
            - Draw the walls using graphics.Window.draw_line if Window instance
              exists.
            - return True stating the Cell walls were created, and perhaps drawn
              if possible.
        """

        if x1 is None or y1 is None or\
                x2 is None or y2 is None:
            return False

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self.left_line = Line(Point(x1, y1), Point(x1, y2))
        self.top_line = Line(Point(x1, y1), Point(x2, y1))
        self.right_line = Line(Point(x2, y1), Point(x2, y2))
        self.bottom_line = Line(Point(x1, y2), Point(x2, y2))

        # hard-coded background color as white for tests
        bg_color = self._win.background if self._win else "white"

        self.left_fill_color = fill_color if self.has_left_wall else bg_color
        self.right_fill_color = fill_color if self.has_right_wall else bg_color
        self.top_fill_color = fill_color if self.has_top_wall else bg_color
        self.bottom_fill_color = fill_color if self.has_bottom_wall else bg_color

        if self._win:
            self._win.draw_line(self.left_line, self.left_fill_color)
            self._win.draw_line(self.top_line, self.top_fill_color)
            self._win.draw_line(self.right_line, self.right_fill_color)
            self._win.draw_line(self.bottom_line, self.bottom_fill_color)

        return True

    def get_center(self) -> tuple[int, int] | tuple[None, None]:
        """Get the center coordinate of a Cell instance

        - If all corner coordinates exist, return tuple of center coordinates
        - Else, return (None, None)
        """

        if self._x1 is not None\
                and self._y1 is not None\
                and self._x2 is not None\
                and self._y2 is not None:
            return (self._x2 + self._x1) / 2, (self._y2 + self._y1) / 2
        else:
            return None, None

    def draw_move(self, to_cell, undo=False) -> bool:
        """Draw move from current Cell instance

        Default move is "not an undo move". Undo move is used to show
        backtracked paths whilst solving the Maze using Maze._solve_r whereas
        "not an undo move" is used to show the default solution path of Maze

        Drawing move is essentially drawing a line from center of current Cell
        instance to center of target Cell instance with a move_color as "red" if
        move type is not an undo move, else it's "gray" with help of
        graphics.Window.draw_line

        Return True if center exists for both current and target Cell instance
        else return False
        """

        self.move_color = "red" if not undo else "gray"
        x1, y1 = self.get_center()
        x2, y2 = to_cell.get_center()
        if x1 is None or\
                y1 is None or\
                x2 is None or\
                y2 is None:
            return False
        if self._win:
            self._win.draw_line(
                Line(Point(x1, y1), Point(x2, y2)), self.move_color)
        return True

    def __repr__(self) -> str:
        """String representation of Cell instance

        x1, y1 x2, y2, has_left_wall, has_top_wall, has_right_wall,
        has_bottom_wall
        (all in same line)

        For e.g,
        1, 1 5, 5 True True False True
        """

        out_string = f"""{self._x1}, {self._y1} {self._x2}, {self._y2} {self.has_left_wall} {self.has_top_wall} {self.has_right_wall} {self.has_bottom_wall}"""
        return out_string

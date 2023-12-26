from cell import Cell
from graphics import Point, Line
from maze import Maze


class TestCellClass():

    def test_cell_constructor(self):
        c = Cell()
        assert c.has_left_wall
        assert c.has_right_wall
        assert c.has_top_wall
        assert c.has_bottom_wall
        assert not c.visited
        assert c._x1 is None
        assert c._y1 is None
        assert c._x2 is None
        assert c._y2 is None

    def test_cell_draw(self):
        c = Cell()
        x1, y1, x2, y2 = 0, 0, 10, 10
        assert c.draw(x1, y1, x2, y2)
        assert c.left_line.p1 == Point(x1, y1)
        assert c.left_line.p2 == Point(x1, y2)
        assert c.top_line.p1 == Point(x1, y1)
        assert c.top_line.p2 == Point(x2, y1)
        assert c.right_line.p1 == Point(x2, y1)
        assert c.right_line.p2 == Point(x2, y2)
        assert c.bottom_line.p1 == Point(x1, y2)
        assert c.bottom_line.p2 == Point(x2, y2)

    def test_cell_no_draw(self):
        c = Cell()
        assert not c.draw(0, None, 10, 10)

    def test_cell_draw_no_left_wall(self):
        c = Cell()
        c.has_left_wall = False
        c.draw(0, 0, 10, 10)
        # compare no wall color with a colored wall
        assert c.left_fill_color == "white"

    def test_cell_draw_no_top_wall(self):
        c = Cell()
        c.has_top_wall = False
        c.draw(0, 0, 10, 10)
        # compare no wall color with a colored wall
        assert c.top_fill_color == "white"

    def test_cell_draw_no_right_wall(self):
        c = Cell()
        c.has_right_wall = False
        c.draw(0, 0, 10, 10)
        # compare no wall color with a colored wall
        assert c.right_fill_color == "white"

    def test_cell_draw_no_bottom_wall(self):
        c = Cell()
        c.has_bottom_wall = False
        c.draw(0, 0, 10, 10)
        # compare no wall color with a colored wall
        assert c.bottom_fill_color == "white"

    def test_cell_get_center(self):
        c = Cell()
        c.draw(0, 0, 10, 10)
        assert c.get_center() == (5, 5)
        c.draw(10, 10, 0, 0)
        assert c.get_center() == (5, 5)
        c.draw(10, 30, 25, 45)
        assert c.get_center() == (17.5, 37.5)

    def test_cell_get_center_for_undrawn_cell(self):
        c = Cell()
        assert c.get_center() == (None, None)

    def test_cell_draw_move_for_undrawn_cell(self):
        c = Cell()
        assert not c.draw_move(Cell())

    def test_cell_draw_move_undo_true(self):
        c1 = Cell()
        c1.draw(0, 0, 10, 10)

        c2 = Cell()
        c2.draw(10, 0, 20, 10)

        assert c1.draw_move(c2, True)
        assert c1.move_color == "gray"

    def test_cell_draw_move_undo_false(self):
        c1 = Cell()
        c1.draw(0, 0, 10, 10)

        c2 = Cell()
        c2.draw(10, 0, 20, 10)

        assert c1.draw_move(c2, False)
        assert c1.move_color == "red"

    def test_cell_draw_move_no_undo(self):
        c1 = Cell()
        c1.draw(0, 0, 10, 10)

        c2 = Cell()
        c2.draw(10, 0, 20, 10)

        assert c1.draw_move(c2)
        assert c1.move_color == "red"

    def test_cell_repr(self):
        c = Cell()
        x1, y1, x2, y2 = 0, 0, 10, 10
        c.draw(x1, y1, x2, y2)
        expected_repr = f"""{x1}, {y1} {x2}, {y2} True True True True"""
        assert repr(c) == expected_repr


class TestPointClass():

    def test_point_constructor(self):
        p = Point(0, 0)
        assert p.x == 0
        assert p.y == 0

    def test_point_equals(self):
        assert Point(0, 0) == Point(0, 0)
        assert Point(0, 1) != Point(0, 0)


class TestLineClass():
    def test_line_constructor(self):
        p = Line(Point(0, 0), Point(0, 1))
        assert p.p1 == Point(0, 0)
        assert p.p2 == Point(0, 1)


class TestMazeClass():
    def test_maze_create_cells(self):
        num_rows, num_cols = 10, 12
        m = Maze(0, 0, num_rows, num_cols, 11, 13)
        assert len(m._cells) == num_cols
        assert len(m._cells[0]) == num_rows

    def test_maze_draw_cell(self):
        m = Maze(9, 8, 10, 12, 11, 13)
        for i, cell_col in enumerate(m._cells):
            for j, cell in enumerate(cell_col):
                x_adjust, y_adjust = 9 + i * 10, 8 + j * 12

                # point 1 for top line and left line
                p1 = Point(i + x_adjust, j + y_adjust)

                # point 2 for left line
                p2 = Point(i + x_adjust, j + y_adjust + 13)
                assert cell.left_line == Line(p1, p2)
                # point 2 for top line
                p2 = Point(i + x_adjust + 11, j + y_adjust)
                assert cell.top_line == Line(p1, p2)

                # point 2 for right line and bottom line
                p2 = Point(i + x_adjust + 11, j + y_adjust + 13)

                # point 1 for right line
                p1 = Point(i + x_adjust + 11, j + y_adjust)
                assert cell.right_line == Line(p1, p2)
                # point 1 for bottom line
                p1 = Point(i + x_adjust, j + y_adjust + 13)
                assert cell.bottom_line == Line(p1, p2)

    def test_maze_break_enterance_and_exit(self):
        m = Maze(0, 0, 10, 12, 11, 13)
        m._break_entrance_and_exit()
        assert not m._cells[0][0].has_top_wall
        assert not m._cells[-1][-1].has_bottom_wall

    def test_maze_get_neighbours(self):
        m = Maze(9, 8, 10, 12, 11, 13)
        for i, cell_col in enumerate(m._cells):
            for j, _ in enumerate(cell_col):
                expected_neighbours = []
                if i != 0:
                    expected_neighbours.append((i - 1, j))
                if j != 0:
                    expected_neighbours.append((i, j - 1))
                if i < 11:
                    expected_neighbours.append((i + 1, j))
                if j < 9:
                    expected_neighbours.append((i, j + 1))
                for ix, n in enumerate(m._get_neighbours(i, j)):
                    assert expected_neighbours[ix] == n

    def test_maze_break_walls_r(self):
        m = Maze(9, 8, 10, 12, 11, 13)
        m._break_entrance_and_exit()
        assert m._break_walls_r(0, 0)
        assert m._cells[-1][-1].visited
#

    def test_maze_reset_cells_visited(self):
        m = Maze(9, 8, 10, 12, 11, 13)
        m._break_entrance_and_exit()
        m._break_walls_r(0, 0)
        m._reset_cells_visited()
        for _, cell_col in enumerate(m._cells):
            for _, cell in enumerate(cell_col):
                assert not cell.visited

    def test_maze_is_not_blocked(self):
        m = Maze(9, 8, 10, 12, 11, 13)
        m._break_entrance_and_exit()

        m._cells[0][0].has_bottom_wall = False
        m._cells[0][1].has_top_wall = False
        assert m._is_not_blocked(0, 0, 0, 1)

        m._cells[-1][-1].has_top_wall = False
        m._cells[-2][-1].has_bottom_wall = False
        assert m._is_not_blocked(11, 8, 11, 9)

        m._cells[0][0].has_right_wall = False
        m._cells[1][0].has_left_wall = False
        assert m._is_not_blocked(0, 0, 1, 0)

        m._cells[-1][-1].has_left_wall = False
        m._cells[-1][-2].has_right_wall = False
        assert m._is_not_blocked(10, 9, 11, 9)

        # impossible move
        assert not m._is_not_blocked(4, 4, 5, 5)

        # expected exception
        assert not m._is_not_blocked(100, 100, 100, 100)

    def test_maze_start_end_lines(self):
        m = Maze(9, 8, 10, 12, 11, 13)
        assert m._draw_start_line()
        assert m._draw_end_line()

    def test_maze_solve(self):
        m = Maze(9, 8, 10, 12, 11, 13)
        m._break_entrance_and_exit()
        m._break_walls_r(0, 0)
        assert m._solve()

    def test_maze_solve_r(self):
        m = Maze(9, 8, 10, 12, 11, 13)
        m._break_entrance_and_exit()
        m._break_walls_r(0, 0)
        m._reset_cells_visited()
        assert m._solve_r(0, 0)

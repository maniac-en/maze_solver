import unittest
from cell import Cell
from maze import Maze
from graphics import Point


class Tests(unittest.TestCase):
    def test_cell_draw(self):
        c = Cell()
        x1, y1, x2, y2 = 0, 0, 10, 10
        c.draw(x1, y1, x2, y2)
        self.assertEqual(c.left_line.p1, Point(x1, y1))
        self.assertEqual(c.left_line.p2, Point(x1, y2))
        self.assertEqual(c.top_line.p1, Point(x1, y1))
        self.assertEqual(c.top_line.p2, Point(x2, y1))
        self.assertEqual(c.right_line.p1, Point(x2, y1))
        self.assertEqual(c.right_line.p2, Point(x2, y2))
        self.assertEqual(c.bottom_line.p1, Point(x1, y2))
        self.assertEqual(c.bottom_line.p2, Point(x2, y2))

    def test_cell_draw_no_left_wall(self):
        c = Cell()
        c.has_left_wall = False
        x1, y1, x2, y2 = 0, 0, 10, 10
        c.draw(x1, y1, x2, y2)
        # compare no wall color with a colored wall
        self.assertEqual(c.left_fill_color != c.top_fill_color, True)

    def test_cell_draw_no_top_wall(self):
        c = Cell()
        c.has_top_wall = False
        x1, y1, x2, y2 = 0, 0, 10, 10
        c.draw(x1, y1, x2, y2)
        # compare no wall color with a colored wall
        self.assertEqual(c.left_fill_color != c.top_fill_color, True)

    def test_cell_draw_no_right_wall(self):
        c = Cell()
        c.has_right_wall = False
        x1, y1, x2, y2 = 0, 0, 10, 10
        c.draw(x1, y1, x2, y2)
        # compare no wall color with a colored wall
        self.assertEqual(c.right_fill_color != c.bottom_fill_color, True)

    def test_cell_draw_no_bottom_wall(self):
        c = Cell()
        c.has_bottom_wall = False
        x1, y1, x2, y2 = 0, 0, 10, 10
        c.draw(x1, y1, x2, y2)
        # compare no wall color with a colored wall
        self.assertEqual(c.right_fill_color != c.bottom_fill_color, True)

    def test_cell_get_center(self):
        c = Cell()
        x1, y1, x2, y2 = 0, 0, 10, 10
        c.draw(x1, y1, x2, y2)
        self.assertEqual(c.get_center(), (5, 5))

    def test_cell_get_center_for_undrawn_cell(self):
        c = Cell()
        self.assertEqual(c.get_center(), (None, None))

    def test_cell_draw_move_for_undrawn_cell(self):
        c = Cell()
        self.assertEqual(c.draw_move(Cell()), False)

    def test_cell_draw_move_undo_true(self):
        c1 = Cell()
        x1, y1, x2, y2 = 0, 0, 10, 10
        c1.draw(x1, y1, x2, y2)

        c2 = Cell()
        x1, y1, x2, y2 = 10, 0, 20, 10
        c2.draw(x1, y1, x2, y2)

        self.assertEqual(c1.draw_move(c2, True), True)
        self.assertEqual(c1.move_color, "gray")

    def test_cell_draw_move_undo_false(self):
        c1 = Cell()
        x1, y1, x2, y2 = 0, 0, 10, 10
        c1.draw(x1, y1, x2, y2)

        c2 = Cell()
        x1, y1, x2, y2 = 10, 0, 20, 10
        c2.draw(x1, y1, x2, y2)

        self.assertEqual(c1.draw_move(c2, False), True)
        self.assertEqual(c1.move_color, "red")

    def test_cell_draw_move_no_undo(self):
        c1 = Cell()
        x1, y1, x2, y2 = 0, 0, 10, 10
        c1.draw(x1, y1, x2, y2)

        c2 = Cell()
        x1, y1, x2, y2 = 10, 0, 20, 10
        c2.draw(x1, y1, x2, y2)

        self.assertEqual(c1.draw_move(c2), True)
        self.assertEqual(c1.move_color, "red")

    def test_cell_repr(self):
        c = Cell()
        x1, y1, x2, y2 = 0, 0, 10, 10
        c.draw(x1, y1, x2, y2)
        expected_repr = f"""{x1}, {y1} {x2}, {y2} True True True True"""
        self.assertEqual(repr(c), expected_repr)

    def test_maze_create_cells(self):
        num_rows, num_cols = 10, 12
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m._cells), num_cols)
        self.assertEqual(len(m._cells[0]), num_rows)

    def test_maze_break_enterance_and_exit(self):
        num_rows, num_cols = 10, 12
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        m._break_entrance_and_exit()
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[-1][-1].has_bottom_wall, False)

    def test_point(self):
        p = Point(0, 0)
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)

    def test_point_equals(self):
        self.assertEqual(Point(0, 0) == Point(0, 0), True)
        self.assertEqual(Point(0, 1) == Point(0, 0), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)

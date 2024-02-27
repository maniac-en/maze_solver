from tkinter import Tk, BOTH, Canvas


class Window():
    """Graphics Window class to create window for app

    This class creates a Tk window as a dialog type window with window title as
    "Maniac's Maze Solver"

    Attributes
    ----------
    __root : tkinter.Tk
        A tkinter Tk object used to create window
    background : str
        Window object's background color, defaults to "white"
    __canvas : tkinter.Canvas
        Canvas object packed onto the Window object
    __is_running : bool
        Determines weather the Window object is open or exited
    """

    def __init__(self, height, width, background="white") -> None:
        """Instantiates the Window class object with a canvas as per passed
        height, width and the background color is provided else defaults to
        "white" color."""

        self.__root = Tk()
        self.__root.attributes('-type', 'dialog')
        self.__root.title = "Maniac's Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.background = background
        self.__canvas = Canvas(
            self.__root,
            bg=self.background,
            height=height,
            width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        return

    def redraw(self) -> None:
        """Redraws the Window object"""

        self.__root.update_idletasks()
        # self.__root.update()
        return

    def wait_for_close(self) -> None:
        """This sets the default behaviour of Window object to be running and
        is called by the driver code where the Window object is instantiated"""

        self.__is_running = True
        while self.__is_running:
            self.redraw()
        return

    def draw_line(self, line, fill_color="black") -> None:
        """This draw the line which is an instance of graphics.Line class using
        the canvas with the default color as "black" unless specified"""

        if line:
            line.draw(self.__canvas, fill_color)
        return

    def close(self) -> None:
        """This is invoked in a protocol bound to Window object when it's
        closed marking the running behaviour to False, hence "wait_for_close"
        will return the control back to driver code"""

        self.__is_running = False
        return


class Point():
    """Graphics Point class

    This class creates a point analogous to coordinate system point having x and
    a y coordinate.

    Attributes
    ----------
    x : float
        x coordinate of the Point
    y: float
        y coordinate of the Point
    """

    def __init__(self, x, y) -> None:
        """Instantiates the Point class object setting it's x and y coordinate.
        """

        self.x = x
        self.y = y
        return

    def __eq__(self, t) -> bool:
        """Returns an equality check of a Point object in comparison with a
        target Point object such that both their x and y coordinate are equal.
        """

        return self.x == t.x and self.y == t.y


class Line:
    """Graphics Line class

    This class creates a line analogous to a line on a coordinate system
    consisting of two points, start and end, which in this case would actual
    be an instance of graphics.Point class

    Attributes
    ----------
    p1 : graphics.Point
        start point of the line
    p2 : graphics.Point
        end point of the line
    """

    def __init__(self, p1, p2) -> None:
        """Instantiates the Line class setting the start and end point."""

        self.p1 = p1
        self.p2 = p2

    def __eq__(self, t) -> bool:
        """Returns an equality check of a Line object in comparison with a
        target Line object such that both their start and end points are equal.
        """

        return self.p1 == t.p1 and self.p2 == t.p2

    def draw(self, canvas, fill_color="black") -> None:
        """This draws a line using tkinter.canvas.create_line from start point
        to end point with 2 pixels width and line color as "black" unless
        specified in "fill_color"
        """

        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2)
        canvas.pack(fill=BOTH, expand=1)

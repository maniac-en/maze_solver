from tkinter import Tk, BOTH, Canvas


class Window():

    def __init__(self, height, width, background="white") -> None:
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
        self.__root.update_idletasks()
        self.__root.update()
        return

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        return

    def draw_line(self, line, fill_color="black") -> None:
        if line:
            line.draw(self.__canvas, fill_color)
        return

    def close(self) -> None:
        self.__is_running = False
        return


class Point():

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        return

    def __eq__(self, t) -> bool:
        return self.x == t.x and self.y == t.y


class Line:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black") -> None:
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2)
        canvas.pack(fill=BOTH, expand=1)

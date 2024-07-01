from abc import ABC, abstractmethod

class Tool(ABC):

    @abstractmethod
    def mouse_down(self):
        pass

    @abstractmethod
    def mouse_up(self):
        pass


class Brush(Tool):

    def mouse_down(self):
        print("brushing")

    def mouse_up(self):
        print("dash line")

class Canvas:

    def __init__(self) -> None:
        self.current_tool = None

    def set_current_tool(self, tool:Tool):
        self.current_tool = tool

    def mouse_down(self):
        self.current_tool.mouse_down()

    def mouse_up(self):
        self.current_tool.mouse_up() 

canvas = Canvas()
canvas.set_current_tool(Brush())
canvas.mouse_down()
canvas.mouse_up()
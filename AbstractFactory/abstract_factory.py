from abc import ABC, abstractmethod
from typing import Text

class Widget(ABC):

    @abstractmethod
    def render(self):
        pass

class Button(Widget):
    pass
    # edge, hover etc

class TextBox(Widget):
    pass
    # font, size etc

class MaterialButton(Button):
    def render(self):
        print("Meterial Button")

class MaterialTextBox(TextBox):
    def render(self):
        print("Material TextBox")

class AntButton(Button):
    def render(self):
        print("Ant Button")

class AntTextBox(TextBox):
    def render(self):
        print("Ant TextBox")

class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self)->Button:
        pass
    
    @abstractmethod
    def create_text(self)->TextBox:
        pass

class MaterialWidgetFactory(WidgetFactory):
    def create_button(self)->Button:
        return MaterialButton()
    
    def create_text(self)->TextBox:
        return MaterialTextBox()

class AntWidgetFactory(WidgetFactory):

    def create_button(self)->Button:
        return AntButton()
    
    def create_text(self)->TextBox:
        return AntTextBox()


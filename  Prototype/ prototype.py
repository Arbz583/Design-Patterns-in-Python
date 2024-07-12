from abc import ABC, abstractmethod

class Component(ABC):

    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def clone(self) -> "Component":
        pass

class Circle(Component):

    def __init__(self, radius) -> None:
        self._radius = radius
        self.render()
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius = r


    def render(self):
        print("Rendering a circle")
    
    def clone(self):
        print("Cloning a circle")
        new_circl = Circle(self.radius)
        return new_circl

class ContextMenu:

    def duplicate(self, component:Component):
        new_component = component.clone()

    # adding to document

    
circle = Circle(4)
context_menu = ContextMenu()
context_menu.duplicate(circle)
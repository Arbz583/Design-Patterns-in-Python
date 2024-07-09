# in python this pattern is meaningless!

from abc import ABC, abstractmethod

class Component(ABC):

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Shape(Component):

    def render(self):
        print("render shape")

    def move(self):
        print("move shape")

class Group(Component):

    def __init__(self) -> None:
        self.components = []
    
    def add(self, component:Component):
        self.components.append(component)
    
    def render(self):
        for component in self.components:
            component.render()

    def move(self):
        for component in self.components:
            component.move()

group1 = Group()
group1.add(Shape())
group1.add(Shape())

group2 = Group()
group2.add(Shape())
group2.add(Shape())

group = Group()
group.add(group1)
group.add(group1)
group.render()
group.move()
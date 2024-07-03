from abc import ABC, abstractmethod

class Observor(ABC):

    @abstractmethod
    def update(self, value):
        pass

class Chart(Observor):

    def update(self, value):
        print(f"chart got notified: {value}")

class SpreadSheet(Observor):

    def update(self, value):
        print(f"spreadsheet got notified: {value}")
    
class Structure:

    def __init__(self) -> None:
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observor):
        self.observers.remove(observor)

    def notify_observers(self, value):
        for observor in self.observers:
            observor.update(value)
        
class DataSource(Structure):

    def __init__(self) -> None:
        super().__init__()
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, amount):
        self._value = amount
        self.notify_observers(self._value)

data_source = DataSource()
chart = Chart()
spread_sheet = SpreadSheet()
data_source.add_observer(chart)
data_source.add_observer(spread_sheet)
data_source.value = 22

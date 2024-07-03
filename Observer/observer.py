from abc import ABC, abstractmethod

class Observor(ABC):

    @abstractmethod
    def update(self):
        pass

class Chart(Observor):

    def update(self):
        print("chart get notified")

class SpreadSheet(Observor):

    def update(self):
        print("spreadsheet get notified")
    
class Structure:

    def __init__(self) -> None:
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observor):
        self.observers.remove(observor)

    def notify_observers(self):
        for observor in self.observers:
            observor.update()
        
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
        self.notify_observers()

data_source = DataSource()
chart = Chart()
spread_sheet = SpreadSheet()
data_source.add_observer(chart)
data_source.add_observer(spread_sheet)
data_source.value = 22
data_source.value = 22

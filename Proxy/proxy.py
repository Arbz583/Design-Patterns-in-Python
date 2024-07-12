from abc import ABC, abstractmethod

class Ebook(ABC):

    @abstractmethod
    def __init__(self, filename) -> None:
        pass

    @property
    @abstractmethod
    def file_name(self):
        pass

    @abstractmethod
    def show(self):
        pass
    
class RealEbook(Ebook):

    def __init__(self, file_name) -> None:
        self._file_name = file_name
        self.load()

    @property
    def file_name(self):
        return self._file_name
    
    def load(self):
        print(f"Loading the ebook: {self._file_name}")

    def show(self):
        print(f"Showing the ebook: {self._file_name}")

# lazy initialization or lazy loading     
class EbookProxy(Ebook):

    def __init__(self, file_name) -> None:
        self._file_name = file_name
        self.ebook = None
    
    @property
    def file_name(self):
        return self._file_name

    def show(self):
        if not self.ebook:
            self.ebook = RealEbook(self.file_name)
        self.ebook.show()
    

class Library:

    def __init__(self) -> None:
        # file name -> its pythonic object
        self.ebook_collection = dict()
    
    def add(self, ebook:Ebook):
        self.ebook_collection[ebook.file_name] = ebook

    def open_ebook(self, file_name):
        self.ebook_collection[file_name].show()

library = Library()
# reading list from db. we have file and its name in the db.
file_names = [
    "Dog Man: the Scarlet Shedder",
    "A Court of Thorns and Roses",
    "House of Flame and Shadow",
]
for file_name in file_names:
    library.add(EbookProxy(file_name))


library.open_ebook("A Court of Thorns and Roses")


class LoggingEbookProxy(Ebook):

    def __init__(self, file_name) -> None:
        self._file_name = file_name
        self.ebook = None
    
    @property
    def file_name(self):
        return self._file_name

    def show(self):
        if not self.ebook:
            self.ebook = RealEbook(self.file_name)
        print("Logging")
        self.ebook.show()
    
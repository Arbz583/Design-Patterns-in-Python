from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute():
        pass

class UndoableCommand(Command):

    @abstractmethod
    def unexecute(self):
        pass

class BoldCommand(UndoableCommand):

    def __init__(self, document, history) -> None:
        self.prev_content = None
        self.document = document
        self.history = history

    def execute(self):
        self.prev_content = self.document.content
        self.document.make_bold()
        self.history.push(self)

    def unexecute(self):
        self.document.content = self.prev_content

class HtmlDocument:

    def __init__(self) -> None:
        self._content = None
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, title):
        self._content = title

    def make_bold(self):
        self.content = f"<b>{self.content}</b>"

class History:
    
    def __init__(self) -> None:
        self.commands = []
    
    def push(self, command):
        self.commands.append(command)
    
    def pop(self):
        return self.commands.pop()

class UndoCommand(Command):

    def __init__(self, history:History) -> None:
        self.history = history
    
    def execute(self):
        if self.history.commands:
            self.history.pop().unexecute()
        

document = HtmlDocument()
document.content = "ali"
history = History()
command = BoldCommand(document, history)
undo_command = UndoCommand(history)
command.execute()
print(document.content)
undo_command.execute()
print(document.content)


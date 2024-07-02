from abc import ABC, abstractmethod

class Button:
    def __init__(self, command) -> None:
        self.command = command

    def click(self):
        self.command.execute()

class Command(ABC):

    @abstractmethod
    def execute():
        pass

class AddCustomer(Command):
    
    def __init__(self, service) -> None:
        self.service = service

    def execute(self):
        self.service.add_customer()

class CustomerService:

    def add_customer(self):
        print("adding customer")

service = CustomerService()
command = AddCustomer(service)
button = Button(command)
button.click()

class CompositeCommand(Command):

    def __init__(self) -> None:
        self.commands = []

    def add(self, command:Command):
            self.commands.append(command)
    
    def execute(self):
        for command in self.commands:
            command.execute()

composite_command = CompositeCommand()
composite_command.add(command)
composite_command.add(command)
composite_command.execute()


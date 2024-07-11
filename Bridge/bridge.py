from abc import ABC, abstractmethod
from os import device_encoding

from click import Abort

class Device(ABC):

    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    @abstractmethod
    def set_channel(self, number):
        pass

class SonyTV(Device):

    def turn_on(self):
        print("Sony: turn on")

    def turn_off(self):
        print("Sony: turn off")

    def set_channel(self, number):
        print(f"Sony: set channel to {number}")

class SumsungTV(Device):

    def turn_on(self):
        print("Sumsung: turn on")

    def turn_off(self):
        print("Sumsung: turn off")

    def set_channel(self, number):
        print(f"Sumsung: set channel to {number}")

class RemoteControl:

    def __init__(self, device:Device) -> None:
        self.device = device
    
    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

class AdvancedRemoteControl(RemoteControl):

    def __init__(self, device: Device) -> None:
        super().__init__(device)
    
    def set_channel(self, number):
        self.device.set_channel(number)

remote_control = RemoteControl(SonyTV())
remote_control.turn_on()
advanced_remote_control = AdvancedRemoteControl(SumsungTV())
advanced_remote_control.set_channel(12)

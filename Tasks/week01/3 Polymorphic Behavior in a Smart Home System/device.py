from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class SmartDevice(ABC):
    deviceName: str
    status: bool = False # defaut to off

    @abstractmethod
    def operate(self):
        """Perform the device-specific action."""
        pass

@dataclass
class SmartLight(SmartDevice):
    def operate(self):
        self.status = not self.status # toggges between the values
        return print(f"{self.deviceName} is now {'on' if self.status == True else 'off'}")

@dataclass
class SmartThermostat(SmartDevice):
    temperature: int = 20

    def operate(self):
        self.temperature = input("Set temperature: ")
        return print(f"{self.deviceName} is set to {self.temperature}°C")

@dataclass
class SmartLock(SmartDevice):
    def operate(self):
        self.status = not self.status
        return print(f"{self.deviceName} is now {'locked' if self.status == True else 'unlocked'}")
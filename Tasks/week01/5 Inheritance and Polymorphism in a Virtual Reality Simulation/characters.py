from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Entity(ABC):
    name: str
    position = (0, 0 ,0)

    @abstractmethod
    def interact(self) -> None:
        pass

class Player(Entity):
    def interact(self):
        print(f"Player: {self.name} explores the area")

class NPC(Entity):
    def interact(self):
        print(f"NPC: {self.name} ignores the player")
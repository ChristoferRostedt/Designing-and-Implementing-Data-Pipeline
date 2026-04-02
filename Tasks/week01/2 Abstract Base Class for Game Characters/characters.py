from abc import abstractmethod, ABC

class GameCharacter(ABC):
    __attack: str
    __defend: str

    @abstractmethod
    def __init__(self, attack: str, defend: str) -> None:
        self.__attack = attack
        self.__defend = defend
    def attack(self) -> None:
        print(self.attack)
        return None
    def defend(self) -> None:
        print(self.defend)
        return None

class Warrior(GameCharacter):
    def __init__(self):
        super().__init__("SWINGS", "DINNG")
        return None

class Mage(GameCharacter):
    def __init__(self):
        super().__init__("FIRE BALL", "FAAH")
        return None

class Archer(GameCharacter):
    def __init__(self):
        super().__init__("PEWW", "AHHHH")
        return None

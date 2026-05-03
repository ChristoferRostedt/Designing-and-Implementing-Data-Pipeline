from abc import abstractmethod, ABC

class GameCharacter(ABC):
    
    @abstractmethod
    def __init__(self, attack_sound: str, defend_sound: str, hp: int = 30, damage: int = 5) -> None:
        self._attack = attack_sound
        self._defend = defend_sound
        self.hp = hp # current hp
        self.max_hp = hp # for reference / reset
        self.damage = damage

    # Basic actions
    def attack(self) -> None:
        print(self._attack)
        return None
        
    def defend(self) -> None:
        print(self._defend)
        return None
        
    
    #combat helpers
    def is_alive(self) -> bool:
        return self.hp > 0
    
    def receive_damage(self, amount: int) -> None:
        self.hp = max(self.hp - amount, 0) # max(x, 0) Makes sure that variable x can't drop below 0
        self.defend()

    def reset(self) -> None:
        self.hp = self.max_hp
    
    
# Character types
class Warrior(GameCharacter):
    def __init__(self):
        super().__init__("Warrior: SWINGS", "Warrior: DINNG", hp=35, damage=7)
        return None

class Mage(GameCharacter):
    def __init__(self):
        super().__init__("Mage: FIRE BALL", "Mage: FAAH", hp=25, damage=10)
        return None

class Archer(GameCharacter):
    def __init__(self):
        super().__init__("Archer: PEWW", "Archer: AHHHH", hp=30, damage=6)
        return None

from abc import abstractmethod, ABC

class Animal(ABC):
    __sound: str
    @abstractmethod
    def __init__(self, sound: str) -> None:
        self.__sound = sound
        return None
    def makeSound(self) -> None:
        print(self.__sound)
        return None
    
class Cat(Animal):
    def __init__(self) -> None:
        super().__init__("Meow!")
        return None
    
cat1 = Cat()
cat1.makeSound()
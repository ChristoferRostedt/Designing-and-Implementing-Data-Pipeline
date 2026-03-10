class Cat():
    sound: str
    def __init__(self) -> None:
        self.sound = "Meow!"
        return None
    def makeSound(self) -> None:
        print(self.sound)
        return None
    
class Dog():
    sound: str
    def __init__(self) -> None:
        self.sound = "Woff!"
        return None
    def makeSound(self) -> None:
        print(self.sound)
        return None
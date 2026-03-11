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
    
class Pomeranian(Dog):
    def __init(self):
        super().__init__()
    
    def showTrick(self):
        print(f"{self.sound}, I'm dancing")

class Labrador(Dog):
    def __init__(self):
        super().__init__()

    def fetchBall(self):
        print(f"{self.sound}, I'm fetching a ball!")

pomeranian = Pomeranian()
labrador = Labrador()

pomeranian.makeSound()
pomeranian.showTrick()

labrador.makeSound()
labrador.showTrick()
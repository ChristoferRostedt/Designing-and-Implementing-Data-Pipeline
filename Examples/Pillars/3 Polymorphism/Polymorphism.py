class Animal:
    sound: str
    def __init__(self, sound: str) -> None:
        self.sound = sound
    # Inheriting (1)
    def makeSound(self) -> None:
        print(self.sound)

# Inheriting (2)
class Cat(Animal):
    def __init__(self) -> None:
        super().__init__("Meow!")

# Inheriting (2)
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__("Bark")
    #Override the ("Bark")
    def makeSound(self) -> None:
        print("Who let the dogs out!?")
         
Cat().makeSound() # Meow!
Dog().makeSound() # Who let the dogs out!?
class SodaBottle:
    brand: str
    capOpen: bool

    def __init__(self, brand) -> None:
        self.brand = brand
        self.capOpen = False
    
    def openBottle(self) -> None:
        if not self.capOpen:
            print("sihhh")
            self.capOpen = True

    def drink(self) -> None:
        if not self.capOpen:
            print("Can't drink from a closed bottle...")
        else:
            print(f"Glunk glunk! mmmm... taste like {self.brand}.")
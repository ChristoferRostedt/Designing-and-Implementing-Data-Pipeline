from sodabottle import SodaBottle

class Main:
    def __init__(self) -> None:
        print("Program starting.")
        bottle_cola = SodaBottle("Coca-cola")
        print(f"Bottle brand is: {bottle_cola.brand}")
        bottle_cola.drink()
        bottle_cola.openBottle()
        bottle_cola.drink()
        print("Program ending.")
        return None

if __name__ == "__main__":
    app = Main()
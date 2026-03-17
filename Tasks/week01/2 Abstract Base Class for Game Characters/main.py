import characters as chac

def showMenu() -> None:
    print("1 - Create Charater")
    print("2 - Simulate Battle")
    print("0 - Exit")
    return None

def charactersChoices():
    print("1 - Warrior")
    print("2 - Mage")
    print("3 - Archer")

def main() -> None:
    print("Program starting.")

    while True:
        showMenu()
        choice = input("Your choice: ")

        if(choice == 1):
            print("choose your character!")
            charactersChoices()
            charChoice = input("Choice: ")
            char = -1
            while True:
                try:
                    if(charChoice == 1):
                        char = 1
                        break
                    elif(charChoice == 2):
                        char = 2
                        break
                    elif(charChoice == 3):
                        char = 3
                        break
                    else:
                        print("Unknown option. Try again.")
                except ValueError:
                    print("Unknown option, try again!")

        elif(choice == 2):
            
        elif(choice == 0):
            
        else:
            print("Unknown option!")
    print("Program ending")
    return None

if __name__ == "__main__":
    main()
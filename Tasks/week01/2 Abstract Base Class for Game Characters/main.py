import characters
from battle import simulateBattle

def showMenu() -> None:
    print("\n### Options ###")
    print("1 - Create Charater")
    print("2 - Simulate Battle")
    print("0 - Exit")
    return None

def option() -> None:
    while True:
        choice = input("Option: ")
        try:
            choice = int(choice)
            print()
            return choice
        except ValueError:
            print("Value must be an integer please try again.")
        except Exception:
            print("Something went wrong")
    

def characterCreationMenu() -> None:
    print("Choose character type")
    print("1 - Warrior")
    print("2 - Mage")
    print("3 - Archer")
    
    while True:
        try:
            choice = int(input("Select your class: "))
            print()
        except ValueError:
            print("Invalid choice, try again.")
            print()
            continue

        if(choice == 1):
            char = characters.Warrior()
            return char
        elif(choice == 2):
            char = characters.Mage()
            return char
        elif(choice == 3):
            char = characters.Archer()
            return char
        else:
            print("Invalid character type, try again.")

def main() -> None:
    print("Program starting.")

    while True:
        showMenu()
        choice = option()
        
        if(choice == 1):
            print("### Create character 1. ###")
            char1 = characterCreationMenu()
            print("### Create character 2. ###")
            char2 = characterCreationMenu()

            print("### Character Types ###")
            print(f"Character 1 is: {type(char1).__name__}")
            print(f"Character 2 is: {type(char2).__name__}")
            print("### Character Types ###")

        elif(choice == 2):
            try:
                simulateBattle(char1, char2)
            except Exception:
                print("Error, no character found!")
            
        elif(choice == 0):
            print("Exiting...")
            break

        elif choice == 3:
            p1 = characters.Mage()
            p2 = characters.Warrior()
            simulateBattle(p1, p2)

        else:
            print("Unknown option!\n")
            
    print("Program ending")
    return None

if __name__ == "__main__":
    main()
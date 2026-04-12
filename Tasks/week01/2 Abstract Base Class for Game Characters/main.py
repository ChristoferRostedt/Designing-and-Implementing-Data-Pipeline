import characters

def showMenu() -> None:
    print("1 - Create Charater")
    print("2 - Simulate Battle")
    print("0 - Exit")
    return None

def characterCreationMenu() -> None:
    print("Choose character type")
    print("1 - Warrior")
    print("2 - Mage")
    print("3 - Archer")
    
    while True:
        try:
            choice = int(input("Select your class: "))
        except ValueError:
            print("Invalid choice, try again.")
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
    
def simulateBattle(Pchar1, Pchar2) -> None:
    
    return None

def main() -> None:
    print("Program starting.")

    while True:
        showMenu()
        choice = input("Your choice: ")

        if(choice == 1):
            print("Create character 1.")
            char1 = characterCreationMenu()
            print("Create character 2.")
            char2 = characterCreationMenu()

        elif(choice == 2):
            try:
                simulateBattle(char1, char2)
            except Exception:
                print("Error, no character found!")
            
        elif(choice == 0):
            print("Exiting...")
            break

        else:
            print("Unknown option!\n")
            
    print("Program ending")
    return None

if __name__ == "__main__":
    main()
import characters as chac

def showMenu() -> None:
    print("1 - Create Charater")
    print("2 - Simulate Battle")
    print("0 - Exit")
    return None

def main() -> None:
    print("Program starting.")

    while True:
        showMenu()
        choice = input("Your choice: ")

        if(choice == 1):
            
        elif(choice == 2):
            
        elif(choice == 0):
            
        else:
            print("Unknown option!")
    print("Program ending")
    return None

if __name__ == "__main__":
    main()
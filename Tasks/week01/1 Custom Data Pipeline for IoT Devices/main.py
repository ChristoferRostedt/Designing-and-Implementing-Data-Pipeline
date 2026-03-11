import file_handler as fh

def showMenu() -> None:
    print("1 - Add IoT Devices")
    print("2 - Serialize Data")
    print("3 - Deserialize Data")
    print("4 - Encrypt Data")
    print("5 - Decrypt Data")
    print("0 - Exit")
    return None

def main() -> None:
    print("Program starting")
    devices = fh.FileHandler()
    while True:
        showMenu()
        choice = input("Your choice: ")
        
        if(choice == 1):
            
        elif(choice == 2):

        elif(choice == 3):

        elif(choice == 4):

        elif(choice == 5):

        elif(choice == 0):
            print("Exiting...")
            break    
        else:
            print("Unknown option!")

    return None

if __name__ == "__main__":
    main()
from coin_acceptor import CoinAcceptor

def displayOptions() -> None:
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")

    while True:
        displayOptions()
        try:
            option = input("Your choice: ")
        except ValueError:
            print("Value must be an integer, try again...\n")
            continue
        
        if(option == 1):
            return
        elif(option == 2):
            return
        elif(option == 3):
            return
        elif(option == 0):
            return
    return None

if __name__ == "__main__":
    main()
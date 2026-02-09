from coin_acceptor import CoinAcceptor

def displayOptions() -> None:
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
    ca = CoinAcceptor()

    while True:
        displayOptions()
        try:
            val = int(input("Insert coin(0 return, -1 exit: )"))
            print("Inserting")
        except ValueError:
            print("Value must be an integer, try again...\n")
            continue
        
        if(val > 0 or val < 0):
            
            return

        elif(val == 0):
            break

        else:
            print("Unknown option.")
        
        print() # newline for each loop
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
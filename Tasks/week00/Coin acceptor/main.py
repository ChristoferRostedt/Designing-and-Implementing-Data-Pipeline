########################################################
# main.py
# Developer: Christofer Rostedt
# Date:
########################################################
from coin_acceptor import CoinAcceptor

def displayOptions() -> None:
    print("1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit")

def main() -> None:
    print("Program starting.")
    ca = CoinAcceptor()

    while True:
        displayOptions()
        try:
            option = int(input("Your choice: "))
        except ValueError:
            print("Value must be an integer, try again...\n")
            continue
        
        if(option == 1):
            ca.insertCoin()

        elif(option == 2):
            val = ca.getAmount()
            print(f"Currently '{val}' coins in coin acceptor.")

        elif(option == 3):
            val = ca.returnCoins()
            print(f"Coin acceptor returned '{val}' coins.")

        elif(option == 0):
            break

        else:
            print("Unknown option.")
        
        print() # newline for each loop
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
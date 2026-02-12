########################################################
# main.py
# Developer: Christofer Rostedt
# Date:
########################################################
from coin_acceptor_cli import CoinAcceptor

def main() -> None:
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)\n")
    ca = CoinAcceptor()

    while True:
        try:
            feed = float(input("Insert coin(0 return, -1 exit): "))
        except ValueError:
            print("Value must be a float, try again...\n")
            continue
        
        if(feed > 0):
            print("Inserting...")
            ca.insertCoin(feed) # inserts the feed to the function
            valList = ca.returnCoins(feed)
            coins = valList[0]
            val = valList[1]
            print(f"Inserted coins = {coins}, value = {val}€")

        elif(feed == 0):
            valList = ca.returnCoins(feed)
            coins = valList[0]
            val = valList[1]
            print(f"Inserted coins = {coins}, value = {val}€")

        elif(feed == -1):
            print("Exiting program.\n")
            break

        else:
            print("Unknown option.")
        
        print() # newline for each loop
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
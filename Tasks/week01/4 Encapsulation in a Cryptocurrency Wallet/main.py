from wallet import CryptoWallet

def menu() -> None:
    print("\n### Menu ###")
    print("1 - Create Wallet")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Check Balance")
    print("5 - Transacition History")
    print("0 - Exit")
    print("### Menu ###")
    return None

def choice(text: str) -> int:
    while True:
        choice = input(text).strip() # .strip() -> removes any random empty space(s)
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print("Value must be an interger! Try again.")

def selectWallet(wallets: dict) -> str:
    '''Ask user to pick wallet. Returns choosen ID or raises'''
    if not wallets:
        raise RuntimeError("No wallets have been created yet.")
    print("\nAvailable wallets:")
    for i, wid in enumerate(wallets, start=1): # i starts at 1
        print(f"{i}) Wallet ID:{wid}") # This is kinda dumb because the ID is an integer
    opt = choice("\nSelect your wallet: ")
    if not 1 <= opt <= len(wallets):
        raise ValueError("Invalid wallet selection.")
    return list(wallets.keys())[opt - 1]

def main() -> None:
    print("Program starting.")
    wallets: dict[str, CryptoWallet] = {}

    while True:
        menu()
        opt = choice("\nOption: ")
        
        try:
            if opt == 1: # create wallet
                w = CryptoWallet()
                wallets[w.walletId] = w
                print(f"Wallet created - ID: {w.walletId}")
                
            elif opt == 2: # Deposit
                wid = selectWallet(wallets)
                amount = float(input("Deposit amount: "))
                wallets[wid].deposit(amount)
                print(f"Deposited {amount:.2f} Catge to wallet {wid}")

            elif opt == 3: # Withdraw
                wid = selectWallet(wallets)
                amount = float(input("Withdraw amount: "))
                wallets[wid].withdraw(amount)
                print(f"Withdrew {amount:.2f} Catge from wallet {wid}")

            elif opt == 4: # Check Balance
                wid = selectWallet(wallets)
                bal = wallets[wid].get_balance()
                print(f"Balance of wallet {wid}: {bal:.2f} Catge")


            elif opt == 5:
                wid = selectWallet(wallets)
                hist = wallets[wid].get_history()
                if not hist:
                    print("No transactions yet.")
                else:
                    print("\nTransaction History:")
                    for ts, ttype, amt in hist:
                        print(f"{ts:%Y-%m-%d %H:%M:%S} | {ttype:8} | {amt:.4f}")

            elif opt == 0:
                print("Exiting...")
                break

            else:
                print("Unknown option.")
        except (ValueError, RuntimeError) as err:
            print(f"\nError: {err}")
        except KeyboardInterrupt:
            print(("\nInterrupted - Exiting..."))
            
    return None

if __name__ == "__main__":
    main()
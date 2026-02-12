########################################################
# main.py
# Developer: Christofer Rostedt
# Date:
########################################################
from counter import Counter

def displayOptions() -> None:
    print("Options:")
    print("1) Add count")
    print("2) Get count")
    print("3) Zero count")
    print("0) Exit program")
    return None

def main() -> None:
    print("Program starting.")
    print("Initializing counter...")
    Count = Counter()
    print("Counter initalized.")
    print()

    while True:
        displayOptions()
        choice = input("Choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print(f"Error value {choice} must be an integer!\n")
            continue

        if(choice == 1):
            Count.addCount()
            print()

        elif(choice == 2):
            count = Count.getCount()
            print(f"Current count '{count}'\n")

        elif(choice == 3):
            Count.zeroCount()
            print()

        elif(choice == 0):
            print("Exiting program.\n")
            break

        else:
            print("Unknown option!\n")

    return None

if __name__ == "__main__":
    main()
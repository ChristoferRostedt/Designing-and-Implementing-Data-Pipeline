# This code could use some improvements

from characters import Player, NPC

def showMenu() -> None:
    print("\n### Menu ###")
    print("1 - Add Entity")
    print("2 - Interact with Entities")
    print("3 - Exit")
    print("### Menu ###")
    return None

def choice(text: str) -> int:
    while True:
        choice = input(text).strip()
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print("Value must be an interger! Try again.")

def interact_all_entities(entities: list) -> None:
    if not entities:
        print("No entities to interact with.")
        return
    
    print("\n########")
    for entity in entities:
        entity.interact()
        print("########")

def characterCreation(entities: list) -> None:
    print("\nEntity type:")
    print("1 - Player")
    print("2 - NPC")
    entity_type = choice("\nSelect your entity: ")
    name = input("Enter entity name: ")
    
    try:
        if entity_type == 1:
            entities.append(Player(name))

        elif entity_type == 2:
            entities.append(NPC(name))

        else:
            print("Invalid entity type.")

    except ValueError:
        print("Invalid input. Numeric values required where applicable.")

def main() -> None:
    print("Program starting.")
    entities = []
    while True:
        showMenu()
        opt = choice("\nOption: ")
        try:
            if opt == 1: # Add entity
                characterCreation(entities)

            elif opt == 2: # Interact with Entities
                interact_all_entities(entities)              

            elif opt == 3: # Exit
                print("Exiting...")
                break

            else:
                print("Invalid option. Try again.")

        except Exception as err:
            print(f"Error: {err}")

    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
from file_handler import FileHandler
from item import Item

filename = "inventory.csv"
inventory_file = FileHandler(filename) # Create an object
rows = inventory_file.read() #Use read method for the previously created object
items: list[Item] = []
print("#### inventory ####")
for i in range(len(rows)):
    _item = Item.deserialize(rows[i])
    print(f"{i + 1}. ", end='')
    _item.display_price()
    items.append(_item)
# allow user to set new item value...
print ("\n Update the item values: ")
for item in items: 
    new_value = input (f"New value for {item.name} (current{item.value}): ")
    if new_value.strip != "":
        try: 
            item.set_value(float(new_value))
        except ValueError: 
            print ("Invalid input")

print("Serializing items into rows.")
print("#### rows ####")
for item in items:
    row = item.serialize()
    print(row)
print("#### rows ####")

rows: list[str] = []
for item in items:
    row = item.serialize()
    rows.append(row)
inventory_file.write(rows)
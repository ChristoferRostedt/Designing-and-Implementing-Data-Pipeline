from dataclasses import dataclass #comes from the standard library module dataclasses. Have to be imported.

@dataclass
class Item: 
    SEPARATOR = ","
    name : str
    value : float
    category : str
    weight : float
    
    # 2 separate decorators, you don't have to use staticmethod AND dataclass; it's either-or
    @staticmethod
    def deserialize(row: str) -> 'Item':
        columns = row.split(Item.SEPARATOR) #Comma seperated values 
        item = Item(
            columns[0], #name
            float(columns[1]), #value
            columns[2],
            float(columns[2]), #weight
        )
        return item
    
    def serialize(self) -> str:
        columns: list[str] = [] # Constructing row from columns
        # columns => [ "name", value, "category", weight ]
        columns.append(self.name)
        columns.append(str(self.value)) # textfile accepts only characters
        columns.append(str(self.weight))
        columns.append(self.category)
        row = self.SEPARATOR.join(columns) # "name,value,category,weight"
        return row
    
    def set_value(self, new_value: float) -> None:
        if new_value < 0:
            print("Value can't be negative.")
        else:
            self.value = new_value
        return None

    def display_price(self) -> None:
        print (f"{self.name} costs {self.value} €.")
        return None
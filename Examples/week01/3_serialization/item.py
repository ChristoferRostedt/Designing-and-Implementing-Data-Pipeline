from dataclasses import dataclass # comes from the standard library module dataclasses. Have to be imported

@dataclass
class Item:
    SEPARATOR = ","
    name: str
    value: float
    category: str
    weight: float

    @staticmethod
    def serialize(self) -> str:
        columns: list[str] = [] # Constructing row from columns
        columns.append(self.name)
        columns.append(str(self.value)) # textfile accepts only characters
        columns.append(self.category)
        columns.append(str(self.weight))
        row = self.SEPARATOR.join(columns) # "name,value,category,weight"
        return row
    def set_value(self, new_value: float) -> None:
        if new_value < 0:
            print("Value can't be negative.")
        else:   
            self.value = new_value
        return None
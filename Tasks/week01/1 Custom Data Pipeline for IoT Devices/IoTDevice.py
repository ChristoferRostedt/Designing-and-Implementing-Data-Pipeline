from dataclasses import dataclass

@dataclass
class Device: 
    SEPARATOR = ","
    deviceId: int
    location: str
    data: float
    
    # 2 separate decorators, you don't have to use staticmethod AND dataclass; it's either-or
    @staticmethod
    def deserialize(row: str) -> 'Device':
        columns = row.split(Device.SEPARATOR) #Comma seperated values 
        device = Device(
            int(columns[0]), #deviceId
            str(columns[1]), #location
            float(columns[2]), # 
        )
        return device
    
    def serialize(self) -> str:
        columns: list[str] = [] # Constructing row from columns
        # columns => [ "deviceId", value, "category", weight ]
        columns.append(str(self.deviceId)) # textfile accepts only characters
        columns.append(self.location) 
        columns.append(str(self.data))
        row = self.SEPARATOR.join(columns) # "deviceId,value,category,weight"
        return row
    
    def set_value(self, new_value: float) -> None:
        if new_value < 0:
            print("Value can't be negative.")
        else:
            self.value = new_value
        return None

    
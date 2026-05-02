from file_handler import FileHandler
from IoTDevice import Item
# class IoTDevice:
#     def __init__(self, deviceId: int, location: str, data: int):
#         self.deviceId = deviceId
#         self.location = location
#         self.data = data

# class TemperatureSensor(IoTDevice):

def showMenu() -> None:
    print("1 - Add IoT Devices")
    print("2 - Serialize Data")
    print("3 - Deserialize Data")
    print("4 - Encrypt Data (under work)")
    print("5 - Decrypt Data (under work)")
    print("0 - Exit")
    return None

def main() -> None:
    print("Program starting")
    filename = "devices.csv"
    deviceFile = FileHandler(filename)
    tempDevices = ''

    while True:
        showMenu()
        choice = input("Your choice: ")
        
        if(choice == 1):
            # Add devices
            # tempDevices += input("Insert the device you wish to add: ") + ', '


        elif(choice == 2):
            # Serialize Data
            file_handler.
            

        elif(choice == 3):
            # Deserialize Data

        elif(choice == 4):

        elif(choice == 5):

        elif(choice == 0):
            print("Exiting...")
            break    
        else:
            print("Unknown option!")

    return None

if __name__ == "__main__":
    main()
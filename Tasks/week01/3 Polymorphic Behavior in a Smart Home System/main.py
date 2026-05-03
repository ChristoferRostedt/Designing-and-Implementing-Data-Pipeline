from device import SmartLight, SmartThermostat, SmartLock

def showMenu() -> None:
    print("\n### Menu ###")
    print("1 - Add Smart Device")
    print("2 - Operate Devices")
    print("0 - Exit")
    return None

def choice() -> int:
    while True:
        choice = input("\nOption: ")
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print("Value must be an interger! Try again.")
            
def main() -> None:
    print("Program starting.")
    devices_classes = [SmartLight, SmartThermostat, SmartLock]
    RegDevice = []
    while True:
        showMenu()
        option = choice()

        if option == 1:
            print("\n### Select Device ###")
            count = 1
            for device in devices_classes:
                print(f"{count}: {(device).__name__}")
                count += 1
            
            option = choice()
            if (option < count) and (option > 0):
                selDevice = devices_classes[option - 1]

                print(f"You choose {(selDevice).__name__}")
                
                deviceName = (input(str("\nInput device name: ")))
                instance = selDevice(deviceName=deviceName)
                RegDevice.append(instance)
                print(f"added {selDevice.__name__} named \"{deviceName}\"")
  
            else:
                print("invalid option! Try again.")


        elif option == 2:
            # Shows list of RegDevices
            if not RegDevice:
                    print("\nNo devices have been registered yet.")
                    continue
            
            print("### Select your registered device(s) ###")
            for i, device in enumerate(RegDevice, start=1): # Shows list of avaliable devices
                print(f"{i}) Device: {type(device).__name__}. Name: {device.deviceName}. ")
            
            sel = choice()
            if 0 < sel <= len(RegDevice):
               selDevice = RegDevice[sel - 1]
               selDevice.operate()
            
            else:
                print("Invalid option!")

        elif option == 0:
            print("Exiting...")
            break

        else:
            print("Unknown option. Try again.")
            
    return None

if __name__ == "__main__":
    main()
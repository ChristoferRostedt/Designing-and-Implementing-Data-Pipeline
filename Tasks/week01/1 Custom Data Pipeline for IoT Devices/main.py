from IoTDevice import TemperatureSensor, HumiditySensor, MotionSensor, IoTDevice
from file_handler import FileHandler, DataSecurity

def show_menu():
    print("\n--- IoT Data Pipeline ---")
    print("1 - Add IoT Device")
    print("2 - Serialize Data (Save to File)")
    print("3 - Deserialize Data (Load from File)")
    print("4 - Encrypt Data File")
    print("5 - Decrypt Data File")
    print("0 - Exit")

def choice(text: str) -> int:
    while True:
        choice = input(text).strip() # .strip() -> removes any random empty space(s)
        try:
            choice = int(choice)
            return choice
        except ValueError:
            print("Value must be an interger! Try again.")

def main():
    handler = FileHandler("devices.csv")
    active_devices = []

    while True:
        show_menu()
        opt = choice("Your choice: ")

        if opt == 1:
            try:
                d_id = int(input("Enter Device ID: "))
                loc = input("Enter Location: ")
                val = float(input("Enter Data Value: "))
                print("Type: 1-Temp, 2-Humidity, 3-Motion")
                opt = choice("Select Type: ")
                
                if opt == 1: active_devices.append(TemperatureSensor(d_id, loc, val))
                elif opt == 2: active_devices.append(HumiditySensor(d_id, loc, val))
                elif opt == 3: active_devices.append(MotionSensor(d_id, loc, val))
                else: print("Invalid sensor type.")
            except ValueError:
                print("Invalid input! Please enter numeric values for ID and Data.")

        elif opt == 2:
            serialized = [d.serialize() for d in active_devices]
            handler.write(serialized)
            print(f"Serialized {len(serialized)} devices to CSV.")

        elif opt == 3:
            rows = handler.read()
            active_devices = [IoTDevice.deserialize(r) for r in rows if r]
            print(f"Deserialized {len(active_devices)} devices from CSV.")

        elif opt == 4:
            data = handler.read()
            encrypted = [DataSecurity.encrypt(line) for line in data]
            handler.write(encrypted)
            print("Data file encrypted.")

        elif opt == 5:
            data = handler.read()
            decrypted = [DataSecurity.decrypt(line) for line in data]
            handler.write(decrypted)
            print("Data file decrypted.")

        elif opt == 0:
            print("Exiting...")
            break

        else:
            print("Unknown option! Please try again[cite: 1].")

if __name__ == "__main__":
    main()
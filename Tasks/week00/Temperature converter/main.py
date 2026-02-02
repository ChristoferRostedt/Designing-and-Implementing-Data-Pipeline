from temperature_converter import TemperatureConverter

def displayOptions() -> None:
    print("Options:")
    print("1) Set temperature")
    print("2) Convert to Celsius")
    print("3) Convert to Fahrenheit")
    print("4) Convert to Kelvin")
    print("0) Exit program")
    return None

def main() -> None:
    print("Program starting.")
    print("Initalizing temperature converter...")
    ts = TemperatureConverter()
    print("Temperature converter initialized.\n")
    
    while True:
        displayOptions()
        choice = input("Choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print(f"Value '{choice}' must be an integer. Try again...\n")
            continue

        if(choice == 1): # Set Temp
            while True:
                try:
                    temp = float(input("Enter temperature in Celsius: "))
                    break
                except ValueError:
                    print("Error, invalid value, try again...")

            ts.setTemperature(temp)
        
        elif(choice == 2): # Convert C
            ts.toCelsius()

        elif(choice == 3): # Convert F
            ts.toFahrenheit()

        elif(choice == 4): # Covert K
            ts.toKelvin()

        elif(choice == 0):
            break

        else:
            print("Unknown option.")
        
        print() # Linebreak for when function loops

    print("Program ending.")

if __name__ == "__main__":
    main()
56# Converting the factors for different length units
conversion_factors = {
    'meters': 1,
    'kilometers': 0.001,
    'miles': 0.000621371,
    'feet': 3.28084,
    'inches': 39.3701
}

def convert_length(value, from_unit, to_unit):
    # Convert value into meters first, then to target unit
    value_in_meters = value / conversion_factors[from_unit]
    converted_value = value_in_meters * conversion_factors[to_unit]
    return converted_value

def display_units():
    print("\nAvailable units: meters, kilometers, miles, feet, inches")

def main():
    print("Welcome to the Length Unit Converter!")

    while True:
        display_units()
        
        # Take  input from user
        value = float(input("\nEnter the value to convert: "))
        from_unit = input("Convert from (choose a unit): ").lower()
        to_unit = input("Convert to (choose a unit): ").lower()

        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            print("Invalid unit! Please choose from the available units.")
            continue
        
        # Perform the conversion in different forms
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

        # Check if the user wants to perform another conversion
        another = input("\nDo you want to convert another value? (yes/no): ").lower()
        if another != 'yes':
            print("Goodbye!")
            break

# Run the converter
main()

"""
File: Temperature_Converter.py
--------------------
This program takes in a choice from the user,
fahrenheit to celsius or vice versa.
Read in the appropriate temperature and
output the converted temperature.

Concepts showcased:
Computation and Control flow
"""


def temperature_converter():
    """
    Function to prompt user for a temperature input,
    convert it from Fahrenheit to Celsius or vice-versa to print the results
    """
    while True:
        # Get the choice from the user
        print("Enter choice (1/2):")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        user_choice = int(input())

        # Based on the option chosen, get temperature input, process and print output
        if user_choice == 1:
            fahrenheit = float(input("Enter Temperature in Fahrenheit : "))
            celsius = (fahrenheit - 32) * 5 / 9
            print("Temperature: " + str(fahrenheit) + " F = " + str(celsius) + " C")
        elif user_choice == 2:
            celsius = float(input("Enter Temperature in Celsius : "))
            fahrenheit = (celsius * 9 / 5) + 32
            print("Temperature: " + str(celsius) + " C = " + str(fahrenheit) + " F")
        else:
            print("Invalid option!")

        print("")


def main():
    temperature_converter()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
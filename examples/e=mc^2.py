"""
File: E=MC2.py
--------------------
This program continually reads in mass from the user 
and then outputs the equivalent energy.

Concepts showcased:
Typecasting, computation and interactive programming
"""


SPEED_OF_LIGHT = 299792458


def mass_energy_relation():
    """
    Function to convert input 'Mass' into 'Energy' using the famous Einstein's relation
    """
    while True:
        # Read the mass as input from user, type is float
        mass = float(input("Enter kilos of mass: "))

        # Calculate energy
        energy = mass * SPEED_OF_LIGHT * SPEED_OF_LIGHT

        # Display work to user
        print("e = m * c ^ 2....")
        print("m = " + str(mass) + " kg")
        print("c = " + str(SPEED_OF_LIGHT) + " m/s")
        print("e = " + str(energy) + " joules")
        print("")


def main():
    mass_energy_relation()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

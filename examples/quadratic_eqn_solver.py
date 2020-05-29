"""
File: Quadratic_Eqn_Solver.py
--------------------
This program prompts the user for the 3 coefficients
of a quadratic equation and outputs the roots.

Concepts showcased:
Use of math library, control flow, String Manipulation
"""

from math import sqrt


def quadratic_solver():
    """
    Function to get coefficients of a quadratic equation and calculate and print out its roots
    """

    # Introductory message
    print("Welcome to Quadratic Equation Solver!")
    print("This program solves equations of the form Ax^2 + Bx + C = 0.")

    while True:
        # Reading polynomial coefficients from user; type-cast to float
        a = float(input("Enter the coefficient A: "))
        b = float(input("Enter the coefficient B: "))
        c = float(input("Enter the coefficient C: "))

        # Compute and print out the roots
        print("The roots of " + str(a) + " x^2 + " + str(b) + " x + " + str(c) + " = 0 are:")
        re = -b/(2*a)
        if b**2 >= 4*a*c:
            im = sqrt(b**2 - 4*a*c)/(2*a)
            x1 = re + im
            x2 = re - im
            print("x1 = " + str(x1))
            print("x2 = " + str(x2))
        else:
            im = sqrt(4*a*c - b**2)/(2*a)
            x1 = str(re) + " + i" + str(im)
            x2 = str(re) + " - i" + str(im)
            print("x1 = " + str(x1))
            print("x2 = " + str(x2))

        print("")


def main():
    quadratic_solver()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()


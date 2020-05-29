"""
File: Leap_Year.py
--------------------
This program continually reads a year from the user
and tells whether a given year is a leap year or not.

Concepts showcased:
Arithmetic and Logical Operators, Precedence
"""


def check_leap_year():
    """
    Function to ask user for an year input and determine whether or not it is a leap year
    """
    while True:
        # Taking user input for year and converting to int
        year_input = int(input("Please input a year: "))

        # Checking the condition for Leap year
        leap_check = ((year_input % 4 == 0) and (year_input % 100 != 0)) or (year_input % 400 == 0)

        # Manipulating a string based on computation
        leap = " NOT"
        if leap_check:
            leap = ""
        leap_result = ' is' + str(leap) + ' a leap'

        # Printing output of the check
        print("The given year " + str(year_input) + str(leap_result) + " year")
        print('--------------------')


def main():
    check_leap_year()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

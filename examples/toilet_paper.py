"""
File: Toilet_Paper.py
--------------------
This program reads in the amount of rolls users have
and the amount of toilet visit per day and
outputs the number of days will their supply
of toilet paper last for.

Concepts showcased:
Arithmetic operations, String Manipulation
"""


SHEETS_PER_ROLE = 160
SHEETS_PER_TOILET_VISIT = 6


def toilet_paper_check():
    # Program keeps running until 'Ctrl + C' is encountered or User presses Enter directly
    while True:
        # Read no.of roles and usage from user
        paper_rolls = float(input("Enter the amount of rolls you have: "))
        toilet_visits = float(input("Enter the number of toilet visits per day: "))

        # Calculate how long the supply will last
        days_lasting = (SHEETS_PER_ROLE * paper_rolls) // (SHEETS_PER_TOILET_VISIT * toilet_visits)

        # Display result to user
        print("How long = " + str(SHEETS_PER_ROLE) + " sheets per roll * number of rolls / (" + str(SHEETS_PER_TOILET_VISIT) + " sheets per toilet visit * toilet visit per day)...")
        print("Number of rolls = " + str(paper_rolls) + " rolls")
        print("Toilet visits = " + str(toilet_visits) + " per day")
        print("You will last " + str(days_lasting) + " day(s)!")
        print("")


def main():
    toilet_paper_check()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

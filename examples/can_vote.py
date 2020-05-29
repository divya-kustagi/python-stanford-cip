"""
File: Can_Vote.py
--------------------
This program takes a person's age as input
and determines if a person can vote or not,
that is, if he is older than 18 years old or not.

Concepts showcased:
Conditional checks and control flow
"""


AGE_LIMIT = 18  # Constant that defines minimum Age required for Voting


def main():
    voting_check()


def voting_check():
    """
    Function to check if a user is eligible to vote based on Age input
    """
    user_age = float(input("Enter your age: "))
    if age_check(user_age, AGE_LIMIT):
        print("You're old enough to vote!")
    else:
        print("Sorry, you can't vote yet!")


def age_check(age, threshold):
    """
     Function that returns 'True' if Age >= Threshold
    """
    return age >= threshold


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

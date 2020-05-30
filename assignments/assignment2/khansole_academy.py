"""
File: khansole_academy.py
-------------------------
This is a program that helps other people learn!
It randomly generates simple addition problems for the user, reads in the answer from the user, and then
checks to see if they got it right or wrong, until the user appears to have mastered the material.
"""

import random

MIN_CORRECT = 3
NUM_MIN = 10
NUM_MAX = 99

def main():
    learning_addition()

def learning_addition():
    crt_count = 0
    while True:
        num1 = random.randint(NUM_MIN, NUM_MAX)
        num2 = random.randint(NUM_MIN, NUM_MAX)
        sum_of_numbers = num1 + num2

        print("What is " + str(num1) + " + " + str(num2) + "?")
        user_ans = int(input("Your answer:"))

        if user_ans == sum_of_numbers:
            crt_count += 1
            print("Correct! You've gotten " + str(crt_count) + " correct in a row.")
            if crt_count == MIN_CORRECT:
                print("Congratulations! You mastered addition.")
                break
        else:
            print("Incorrect. The expected answer is " + str(sum_of_numbers))
            crt_count = 0

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

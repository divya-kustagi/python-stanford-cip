"""
File: hailstones.py
-------------------
This program reads in a number from the user and then
displays the Hailstone sequence for that number.

The problem can be expressed as follows:
* Pick some positive integer and call it n.
* If n is even, divide it by two.
* If n is odd, multiply it by three and add one.
* Continue this process until n is equal to one.
"""


def main():
    hailstones()


def hailstones():
    iterations = 0
    num_input = int(input("Enter a number: "))
    while num_input != 1:
        iterations += 1
        if num_input % 2 == 0:
            next_num = int(num_input / 2)
            print(str(num_input) + " is even, so I  take half: " + str(next_num))
            num_input = int(next_num)
        else:
            next_num = 3*num_input + 1
            print(str(num_input) + " is odd, so I  make 3n + 1: " + str(next_num))
            num_input = int(next_num)
    print("The process took " + str(iterations) + " steps to reach 1")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

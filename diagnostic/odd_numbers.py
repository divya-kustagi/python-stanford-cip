"""
odd_numbers.py

Program to print the first 100 Odd Numbers:
Takes a parameter n to print first n ODD numbers.
"""


def print_odd_numbers(n):
    for i in range(2 * n):
        if (i + 1) % 2 != 0:
            print(i + 1)


def main():
    n = 100
    print_odd_numbers(n)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

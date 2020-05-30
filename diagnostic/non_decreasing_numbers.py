"""
non_decreasing_numbers.py

Program that asks the user to enter a
sequence of "non-decreasing" numbers one at a time.
"""


def main():
    non_decreasing_numbers()


def non_decreasing_numbers():
    print("Enter a sequence of non-decreasing numbers.")
    seq_length = 1

    num_input = float(input("Enter num: "))
    next_num_input = float(input("Enter num: "))

    while (next_num_input - num_input) >= 0:
        num_input = next_num_input
        next_num_input = float(input("Enter num: "))
        seq_length += 1

    print("Thanks for playing!")
    print("Sequence length: " + str(seq_length))


if __name__ == "__main__":
    main()
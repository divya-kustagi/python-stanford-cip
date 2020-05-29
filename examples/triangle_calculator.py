"""
File: Triangle_Calculator.py
--------------------
This program allows the reader to choose between two options:
1. Starting with the length of all three sides
2. Starting with the length of two sides and the angle between them

It then calculates and output the following information:
1. Length of all sides
2. Perimeter
3. Area

Concepts showcased:
Functions and Decomposition, Use of Math library
"""


import math


def triangle_print_info(a, b, c, peri, area):
    # Print out the sides, perimeter and area for a triangle by taking them an inputs
    print("---")
    print("Information about your triangle:...")
    print("Side 1: " + str(a))
    print("Side 2: " + str(b))
    print("Side 3: " + str(c))
    print("Perimeter :" + str(peri))
    print("Area :" + str(area))
    print("---")


def triangle_calculator_sides():
    # If we know all three sides
    side_a = float(input("Length of side 1: "))
    side_b = float(input("Length of side 2: "))
    side_c = float(input("Length of side 3: "))

    # Calculate perimeter and area
    perimeter = side_a + side_b + side_c
    semi_perimeter = perimeter / 2

    # Heron's formula to find Area
    area = math.sqrt(semi_perimeter*(semi_perimeter-side_a)*(semi_perimeter-side_b)*(semi_perimeter-side_c))

    # Call the function to print out triangle info
    triangle_print_info(side_a, side_b, side_c, perimeter, area)


def triangle_calculator_sides_angle():
    side_a = float(input("Length of side 1: "))
    side_b = float(input("Length of side 2: "))

    angle_c = float(input("Angle between them in degrees: "))
    angle_rad_c = angle_c * math.pi / 180

    # Law of Cosines to find third side
    side_c = math.sqrt((side_a ** 2) + (side_b ** 2) - 2*side_a*side_b*math.cos(angle_rad_c))

    # Calculate perimeter and area
    perimeter = side_a + side_b + side_c
    area = 0.5 * side_a * side_b * math.sin(angle_rad_c)

    # Call the function to print out triangle info
    triangle_print_info(side_a, side_b, side_c, perimeter, area)


def triangle_calculator():
    # Introductory explanation and taking user choice
    print("Welcome to the Triangle Calculator!")
    print("What information do you have about your triangle so far?")
    print("(1) Length of all three sides")
    print("(2) Length of two sides and the angle between them")
   
    user_choice = int(input("Please choose 1 or 2: "))

    # Calling different functions based on user choice
    if user_choice == 1:
        triangle_calculator_sides()
    elif user_choice == 2:
        triangle_calculator_sides_angle()
    
    
def main():
    triangle_calculator()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()


"""
ramp_climbing_karel.py
A program that makes Karel-the robot draw a diagonal line across the world, with a slope of 'slope_y/slope_x'
"""

from karel.stanfordkarel import *


def main():
    draw_diagonal()


def draw_diagonal():
    """
    Function for Karel to draw diagonal line
    of slope 1/2 across any world
    y/x = 1/2
    """
    slope_x = 2
    slope_y = 1
    while left_is_clear() and front_is_clear():
        draw_line(slope_x, slope_y)


def draw_line(x, y):
    """
    Karel climbs one step
    Pre-condition : Karel is facing East in the position of a point/beeper.
    Post-condition : Karel has climbed a step(on line with slope 1/2) and is still facing East, in position of next point/beeper.
    """
    put_beeper()
    for i in range(x):
        if front_is_clear():
            move()
    turn_left()
    for i in range(y):
        if front_is_clear():
            move()
    turn_right()


# There is no need to edit code beyond this point

def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
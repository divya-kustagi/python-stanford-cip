from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""

def main():
    paint_job()


def paint_job():
    for i in range(3):
        paint_building()
    turn_left()


"""
Precondition: Karel is standing at the start of first wall on its left
Postcondition: Karel finishes painting, is standing at the start of next building, with wall on left again
"""
def paint_building():
    for i in range(2):
        paint_wall()
        turn_left()
        move()
    paint_wall()
    turn_right()


"""
Precondition: Karel is standing at the start of first wall on its left
Postcondition: Karel finishes painting one wall, is standing one corner outside of the wall just painted (in same direction it traversed to paint)
"""
def paint_wall():
    while left_is_blocked():
        put_beeper()
        move()

def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

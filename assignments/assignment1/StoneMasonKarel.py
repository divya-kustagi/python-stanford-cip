from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    mason_job()

def mason_job():
    while front_is_clear():
        turn_left()
        build_column()
        turn_left()
        for i in range(4):
            move()
    turn_left()
    build_column()


"""
Precondition: Karel is standing facing up, at the base of a column
Postcondition: Karel finishes fixing the column, is standing facing up, at the base of a column
"""
def build_column():
    while front_is_clear():
        repair_corner()
        move()
    repair_corner()
    turn_around()
    move_to_wall()

def repair_corner():
    if no_beepers_present():
        put_beeper()

def turn_around():
    for i in range(2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

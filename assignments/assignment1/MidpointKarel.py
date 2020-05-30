from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    draw_diagonal()
    walk_to_end()
    move_to_centre()
    while not_facing_south():
        turn_left()
    move_to_wall()
    put_beeper()
    pick_all_beepers()

def draw_diagonal():
    put_beeper()
    while front_is_clear():
        move_one_step()
        put_beeper()

def walk_to_end():
    turn_right()
    move_to_wall()
    turn_around()

def move_to_centre():
    while no_beepers_present():
        if no_beepers_present():
            move()
            turn_left()
        if no_beepers_present():
            move()
            turn_right()

#    while no_beepers_present():
#       move_one_step()

def move_one_step():
    move()
    turn_left()
    move()
    turn_right()

def pick_all_beepers():
    turn_right()
    move_to_wall()
    turn_around()
    remove_diagonal()
    walk_to_end()
    turn_left()
    while no_beepers_present():
        move()

def remove_diagonal():
    pick_beeper()
    while front_is_clear():
        move_one_step()
        pick_beeper()

def turn_around():
    for i in range(2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

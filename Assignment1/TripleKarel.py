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
    # Pre-condition: Three building with white walls
    # Post-condition: Three buildings with painted walls

    for i in range(3):
        paint_building()
        turn_right()
    turn_left()


# Pre-condition: Karel is facing certain point
# Post-condition: Karel will turn three times anticlockwise the initial point

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Pre-condition: One of the buildings has white walls
# Post-condition: One of the buildings gets all its walls painted

def paint_building():
    for i in range(2):
        paint_wall()
        turn_left()
        move()
    paint_wall()


# Pre-condition: A wall is white
# Post-condition: The wall is painted

def paint_wall():
    while left_is_blocked():
        put_beeper()
        move()

# There is no need to edit code beyond this point


if __name__ == "__main__":
    run_karel_program()

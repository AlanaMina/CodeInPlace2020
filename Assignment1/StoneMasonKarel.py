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
    # Pre-condition: there are missing parts of walls
    # Post-condition: all walls are fixed

    while front_is_clear():
        build_wall()
        for i in range(4):
            move()
    build_wall()


# Pre-condition: Karel is located ate the top of the fixed wall
# Post-condition: Karel is located at the base of the fixed wall

def go_back():
    turn_around()
    while front_is_clear():
        move()
    turn_left()


# Pre-condition: there are missing parts the wall where Karel is
# Post-condition: All the parts of this wall are fixed

def build_wall():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if no_beepers_present():
        put_beeper()
        go_back()
    else:
        go_back()


# Pre-condition: Karel is facing certain point
# Post-condition: Karel will turn two times anticlockwise the initial point

def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

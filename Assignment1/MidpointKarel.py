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
    if front_is_clear():
        put_beeper()  # 1
        move()
        if front_is_blocked():
            turn_around()
            move()
        else:
            more_than_two()
    else:
        put_beeper()  # 1


# Pre-condition: Only one beeper is at place, but there is space for more than 2
# Post-condition: All beepers are in place at bottom line
def more_than_two():
    while front_is_clear():
        move()
    put_beeper()  # 2
    turn_around()
    new_beeper()
    move()
    complete_line()
    erase()


# Pre-condition: All bottom line has beepers
# Post-condition: Only middle line beeper remains
def erase():
    while front_is_clear():
        move()
        pick_beeper()  # -1
    turn_around()
    while no_beepers_present():
        move()
    while front_is_clear():
        move()
        pick_beeper()  # -2
    turn_around()
    while no_beepers_present():
        move()


# Pre-condition: The first 3 beepers are in place
# Post-condition: All the bottom line has its beepers
def complete_line():
    while no_beepers_present():
        turn_around()
        move()
        turn_around()
        new_beeper()
        move()
    turn_around()
    move()
    turn_around()


# Pre-condition: There are X beepers at place
# Post-condition: There are X+1 beepers at place
def new_beeper():
    for i in range(2):
        move()
    if beepers_present():
        turn_around()
        while beepers_present():
            move()
        put_beeper()
    else:
        while no_beepers_present():
            move()
        turn_around()
        move()
        put_beeper()  # +1


# Pre-condition: Karel is facing certain point
# Post-condition: Karel will turn two times anticlockwise the initial point
def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()

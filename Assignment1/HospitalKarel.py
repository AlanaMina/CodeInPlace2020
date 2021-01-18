from karel.stanfordkarel import *

"""
File: HospitalKarel.py
-----------------------
This file is for optional extension programs. 
"""


def main():
    for i in range(2):
        find_hospital()
        build_hospital()
        move()
    find_hospital()
    build_hospital()
    go_back()
    go_back()


def go_back():
    while front_is_clear():
        move()
    turn_around()


def find_hospital():
    while no_beepers_present():
        move()
    turn_left()


def build_hospital():
    for i in range(2):
        move()
        put_beeper()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

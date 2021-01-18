"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

# pre: The screen is blank
# post: The program returns a countdown from 10 until Liftoff!


def main():
    for i in range(11):
        num = 10
        count = num - i
        if count == 0:
            print("Liftoff!")
        else:
            print(count)
        num += 1


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
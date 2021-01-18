"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

NUM_RANDOM = 10
MIN_RANDOM = 0
MAX_RANDOM = 100

# pre: The screen is blank
# post: The program returns 10 random numbers between 0 and 100


def main():
    for i in range(NUM_RANDOM):
        num = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(num)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

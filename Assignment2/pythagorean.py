"""
File: pythagorean.py
--------------------
Add your comments here.
"""

import math


def main():
    print("Enter values to compute the Pythagorean theorem.")
    num1 = float(input("a: "))
    num2 = float(input("b: "))
    c = math.sqrt((num1**2) + (num2**2))
    print("c: " + str(c))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

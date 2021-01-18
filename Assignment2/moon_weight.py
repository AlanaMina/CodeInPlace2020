"""
File: moon_weight.py
--------------------
Add your comments here.
"""


def main():
    weight_earth = int(input("Enter a weight on earth: "))
    weight_moon = 0.165 * weight_earth
    print("Equivalent weight on moon: " + str(weight_moon))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

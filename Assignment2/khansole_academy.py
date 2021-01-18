"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


# You'll be able to solve four types of operations. If you get three in a row you'll master the exercise.
def main():

    adding()
    # select()


# pre: Ask the user what kind of operation wants to learn or if he/she wants to continue with another one
# post: Questions will begin or the program will finish if the user doesn't want to go on
def select():
    answer = "y"
    while answer == "y":
        problem_type = input("What kind of operation do you want to learn today?"
                             "\nPress \'a\' for adding, \'s\' for subtraction, "
                             "\'m\' for multiplication and \'d\' for division: ")
        if problem_type == "a":
            adding()
        elif problem_type == "s":
            subtraction()
        elif problem_type == "m":
            multiplication()
        elif problem_type == "d":
            division()
        answer = input("Do you want to continue with another operation? y/n >>> ")
    print("Thank you for learning with Khansole Academy")


# pre: The program will ask for adding operations
# post: the user answer three in a row and it will achieve this level
def adding():
    count = 0
    while count < 3:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        print("What is " + str(num1) + " + " + str(num2) + "?")
        ans = int(input(""))
        sum = num1 + num2

        if ans == sum:
            if count == 2:
                break
            else:
                count += 1
                print("Correct! You\'ve gotten " + str(count) + " correct in a row. Your answer: " + str(ans))
        else:
            print("Incorrect. The expected answer is: " + str(sum) + ". Your answer: " + str(ans))
            count = 0
    print("Correct! You've gotten 3 correct in a row. \nCongratulations! You mastered addition.")


# pre: The program will ask for subtraction operations
# post: the user answer three in a row and it will achieve this level
def subtraction():
    count = 0
    while count < 3:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        ans = int(input("What is " + str(num1) + " - " + str(num2) + "= "))
        sub = num1 - num2

        if ans == sub:
            if count == 2:
                break
            else:
                count += 1
                print("Your answer: " + str(ans) + "\nCorrect! You've gotten " + str(count) + " correct in a row.")
        else:
            print("Your answer: " + "\nIncorrect. The expected answer is: " + str(sub) + ".")
            count = 0
    print("Correct! You've gotten 3 correct in a row. \nCongratulations! You mastered subtraction.")


# pre: The program will ask for multiplication operations
# post: the user answer three in a row and it will achieve this level
def multiplication():
    count = 0
    while count < 3:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        ans = int(input("What is " + str(num1) + " * " + str(num2) + "= "))
        mul = num1 * num2

        if ans == mul:
            if count == 2:
                break
            else:
                count += 1
                print("Your answer: " + str(ans) + "\nCorrect! You've gotten " + str(count) + " correct in a row.")
        else:
            print("Your answer: " + "\nIncorrect. The expected answer is: " + str(mul) + ".")
            count = 0
    print("Correct! You've gotten 3 correct in a row. \nCongratulations! You mastered multiplication.")


# pre: The program will ask for dividing operations
# post: the user answer three in a row and it will achieve this level
def division():
    count = 0
    while count < 3:
        num1 = random.randint(0, 99)
        num2 = random.randint(0, 99)
        ans = int(input("Please enter an integer value. What is " + str(num1) + " / " + str(num2) + "= "))
        div = num1 // num2

        if ans == div:
            if count == 2:
                break
            else:
                count += 1
                print("Your answer: " + str(ans) + "\nCorrect! You've gotten " + str(count) + " correct in a row.")
        else:
            print("Your answer: " + "\nIncorrect. The expected answer is: " + str(div) + ".")
            count = 0
    print("Correct! You've gotten 3 correct in a row. \nCongratulations! You mastered division.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

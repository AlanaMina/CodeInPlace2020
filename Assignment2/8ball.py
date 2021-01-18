"""
File: 8ball.py
--------------------
Add your comments here.
"""
import random


def main():
    quest = input("Ask a question: ")
    while quest != "":
        answer = random.randint(1, 20)
        if answer == 1:
            print("As I see it, yes.")
        elif answer == 2:
            print("Ask again later.")
        elif answer == 3:
            print("Better not tell you now.")
        elif answer == 4:
            print("Cannot predict now.")
        elif answer == 5:
            print("Concentrate and ask again.")
        elif answer == 6:
            print("Don’t count on it.")
        elif answer == 7:
            print("It is certain.")
        elif answer == 8:
            print("It is decidedly so.")
        elif answer == 9:
            print("Most likely.")
        elif answer == 10:
            print("My reply is no.")
        elif answer == 11:
            print("My sources say no.")
        elif answer == 12:
            print("Outlook not so good.")
        elif answer == 13:
            print("Outlook good.")
        elif answer == 14:
            print("Reply hazy, try again.")
        elif answer == 15:
            print("Signs point to yes.")
        elif answer == 16:
            print("Very doubtful.")
        elif answer == 17:
            print("Without a doubt.")
        elif answer == 18:
            print("Yes.")
        elif answer == 19:
            print("Yes – definitely.")
        elif answer == 20:
            print("You may rely on it")
        quest = input("Ask a question: ")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

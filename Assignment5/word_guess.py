"""
File: word_guess.py
-------------------
Fill in this comment.
"""

import random

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    nro = INITIAL_GUESSES
    guess = ""
    aux = []
    for i in range(len(secret_word)):
        guess += "-"
    for i in range(len(secret_word)):
        aux.append("-")

    while ("-" in guess) and (nro > 0):
        print("The word now looks like this: " + str(guess))
        print("You have " + str(nro) + " guesses left")
        letter = input("Type a single letter here, then press enter: ")
        if len(letter) != 1:
            print("Guess should only be a single character.")
        else:
            letter = letter.upper()
            if letter in secret_word:
                print("That guess is correct")
                res = []
                for idx, val in enumerate(secret_word):
                    if val in letter:
                        res.append(idx)
                for j in range(len(guess)):
                    aux[j] = guess[j]
                if len(res) > 1:
                    for m in range(len(res)):
                        aux[res[m]] = str(letter)
                else:
                    i = secret_word.index(letter)
                    aux[i] = str(letter)
                guess = ""
                for n in range(len(aux)):
                    guess += aux[n]
            else:
                print("There are no " + str(letter) + "'s in the word")
                nro -= 1
    if nro == 0:
        print("Sorry, you lost. The secret word was: " + str(secret_word))
    elif "-" not in guess:
        print("Congratulations, the word is: " + str(secret_word))


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    aux = []
    with open(LEXICON_FILE) as file:
        for line in file:
            line = line.strip()
            aux.append(line)
    index = random.randrange(122000)
    return str(aux[index])


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()

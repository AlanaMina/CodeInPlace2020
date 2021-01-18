"""
File: nimmAI.py
-------------------------
Add your comments here.
"""


def main():
    stones = 20
    player = int(input("Do you want to be player 1 or 2?: "))
    print("There are " + str(stones) + " stones left")
    while player != 0:
        if player == 1:
            player2()
        elif player == 2:
            player1()
        else:
            break
        player = int(input("Do you want to be player 1 or 2? (3 to quit): "))


def player1():
    stones = 20
    count = 1
    while stones > 0:
        if count % 2 != 0:
            if stones == 20:
                take = 1
                print("Player 1 took 1 stone")
            else:
                if take == 1:
                    take = 2
                    print("Player 1 took 2 stones")
                elif take == 2:
                    take = 1
                    print("Player 1 took 1 stone")
        else:
            take = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while take < 1 or take > 2:
                take = int(input("Please enter 1 or 2: "))
        stones -= take
        if stones <= 1:
            break
        print("\nThere are " + str(stones) + " stones left")
        stones = int(stones)
        count += 1
    if count % 2 != 0:
        player = 1
    else:
        player = 2
    print("\nPlayer " + str(player) + " wins!")


def player2():
    stones = 20
    count = 1
    while stones > 0:
        if count % 2 == 0:
            if stones == 20:
                take = 1
                print("Player 2 took 1 stone")
            elif stones > 4:
                if take == 1:
                    take = 2
                    print("Player 2 took 2 stones")
                elif take == 2:
                    take = 1
                    print("Player 2 took 1 stone")
            elif stones == 4:
                take = 1
                print("Player 2 took 1 stone")
            elif stones == 3:
                take = 2
                print("Player 2 took 2 stones")
            elif stones == 2:
                take = 1
                print("Player 2 took 1 stone")
        else:
            take = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while take < 1 or take > 2:
                take = int(input("Please enter 1 or 2: "))
        stones -= take
        if stones <= 1:
            break
        print("\nThere are " + str(stones) + " stones left")
        stones = int(stones)
        count += 1
    if count % 2 != 0:
        player = 1
    else:
        player = 2
    print("\nPlayer " + str(player) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

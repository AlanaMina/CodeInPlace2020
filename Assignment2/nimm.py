"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    
    stones = 20
    print("There are " + str(stones) + " stones left")
    count = 1

    while stones > 0:
        if count % 2 != 0:
            take = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while take < 1 or take > 2:
                take = int(input("Please enter 1 or 2: "))
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
        player = 2
    else:
        player = 1
    print("\nPlayer " + str(player) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

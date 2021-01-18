"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill1.txt'


def main():
    """
    Add your code (remember to delete the "pass" below)
    """
    dict = {}
    name = ""
    num = ""
    with open(INPUT_FILE) as file:
        for line in file:
            line = line.strip()
            ini = line.index('[')
            end = line.index(']')
            for i in range(ini + 1, end):
                name += line[i]
            for j in range(end + 3, len(line)):
                num += line[j]

            if name not in dict:
                dict[name] = num
            else:
                add = str(int(num) + int(dict[name]))
                dict[name] = add
            name = ""
            num = ""
    for name in dict:
        print(name, "-> $", dict[name])


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

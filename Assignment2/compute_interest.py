"""
File: compute_interest.py
-------------------------
Add your comments here.
"""


def main():
    cash = float(input("Initial balance: "))
    start_year = int(input("Start year: "))
    start_month = int(input("Start month: "))
    end_year = int(input("End year: "))
    end_month = int(input("End month: "))

    count_year = end_year - start_year
    count_month = end_month - start_month
    if count_year < 0:
        print("Starting date needs to be before the ending date.")
    elif (count_year == 0) and (count_month < 0):
        print("Starting date needs to be before the ending date.")
    else:
        interest = int(input("Interest rate (0 to quit): "))
        while interest != 0:
            current_money = cash
            interest_rate = interest / 100
            period = 13 - start_month + count_year * 12 - (12 - end_month)
            current_month = start_month
            current_year = start_year
            for i in range(period):
                if current_month == 12:
                    current_year += 1
                    current_month = 1
                print("Year " + str(current_year) + ", month " + str(current_month) + " balance: " + str(current_money))
                current_month += 1
                current_money += current_money * interest_rate
            interest = int(input("Interest rate (0 to quit): "))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

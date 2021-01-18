# Data comes from Johns Hopkins University. Thanks to them for making this public!
# https://github.com/CSSEGISandData/COVID-19
# You can find data beyond cumulative cases there!

'''
Test your code by analysing total confirmed cases over time
Each line in the file represents one day. The first value is confirmed cases on Jan 22nd.
The number of confirmed cases is "cumulative" meaning that it is the total number
of cases up until the current day. It will never go down! 
'''

ITALY_PATH = 'italy.txt'

# This directory has files for all countries if you want to explore further
DATA_DIR = 'confirmed'

def main():
    file = open(ITALY_PATH)
    list = []
    for line in file:
        list.append(int(line.strip()))

    print(list)

    # Count the number of non-zero values in the file (this is days since first case)
    count = 0
    for i in range(len(list)):
        if list[i] != 0:
            count += 1

    print("Days since first case: " + str(count))

    # Create a list which stores how many new cases there were each day(new cases on a given day are:
    # total cases on that day - total cases on the previous day)
    new_cases_per_day = []
    total_per_day = 0
    total_previous_day = 0
    for i in range(len(list)):
        if i == 0:
            total_previous_day = 0
        else:
            total_previous_day = list[i-1]
        total_per_day = list[i]
        new_cases = total_per_day - total_previous_day
        new_cases_per_day.append(new_cases)

    print(new_cases_per_day)


if __name__ == '__main__':
    main()

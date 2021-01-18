"""
File: data_analysis.py
----------------------
This program read in data on cumulative infections of a disease
in different locations, and computes the number of infections
per day at each location.
"""


def load_data(filename):
    """
    The function takes in the name of a datafile (string), which
    contains data on locations and their seven day cumulative number
    of infections.  The function returns a dictionary in which the
    keys are the locations in the data file, and the value associated
    with each key is a list of the (integer) values presenting the
    cumulative number of infections at that location.
    >>> load_data('disease1.txt')
    {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    """
    dict = {}
    values_list = []
    with open(filename) as file:
        for sentence in file:
            # sentence = "".join(sentence.strip())
            sentence = sentence.strip()
            sentence = sentence.replace('  ', '')
            sentence = sentence.replace(' ,', ',')
            sentence = sentence.replace(', ', ',')
            word_list = sentence.split(',')
            name = word_list[0]
            word_list.remove(name)
            for i in range(len(word_list)):
                value = int(word_list[i])
                values_list.append(value)
            dict[name] = values_list
            values_list = []
        return dict


def daily_cases(cumulative):
    """
    The function takes in a dictionary of the type produced by the load_data
    function (i.e., keys are locations and values are lists of seven values
    representing cumulative infection numbers).  The function returns a
    dictionary in which the keys are the same locations in the dictionary
    passed in, but the value associated with each key is a list of the
    seven values (integers) presenting the number of new infections each
    day at that location.
    >>> daily_cases({'Test': [1, 2, 3, 4, 4, 4, 4]})
    {'Test': [1, 1, 1, 1, 0, 0, 0]}
    >>> daily_cases({'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]})
    {'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5]}
    """
    key_list = list(cumulative.keys())
    daily_list = []
    cumulative_dict = {}
    for i in range(len(key_list)):
        cases = cumulative[key_list[i]]
        daily_list.append(cases[0])
        for j in range(1, len(cases)):
            prev = cases[j - 1]
            today = cases[j]
            daily = today - prev
            daily_list.append(daily)
        cumulative_dict[key_list[i]] = daily_list
        daily_list = []
    return cumulative_dict


def main():
    filename = 'disease1.txt'

    data = load_data(filename)
    print("Loaded datafile " + filename + ":")
    print(data)

    print("Daily infections: ")
    print(daily_cases(data))


if __name__ == '__main__':
    main()

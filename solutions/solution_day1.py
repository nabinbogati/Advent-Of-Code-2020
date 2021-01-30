"""
    --- Part One ---
    For example, suppose your expense report contained the following:

    1721
    979
    366
    299
    675
    1456

    In this list, the two entries that sum to 2020 are 1721 and 299.
    Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
"""
DATA = []

def read_file(filename):
    """ reads each line from given file add adds to list """
    with open(filename, 'r') as file:
        for number in file.readlines():
            DATA.append(int(number))

"""
    --- Part Two ---

    The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they 
    had left over from a past vacation.
    They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
"""


def calculate_two_sum():
    """ returns multiplication of two numbers that adds up to 2020 from given list """
    for value in DATA:
        if 2020-value in DATA:
            result = value*(2020-value)
            break

    return result

def calculate_three_sum():
    """ returns multiplication of three numbers that adds up to 2020 from given list """
    for first in DATA:
        for second in DATA:
            if 2020-(first+second) in DATA:
                result = first*second*(2020-(first+second))
                break

    return result


def main():
    """ main function from where program execution begains """
    filename = 'input_day1.txt'
    read_file(filename)
    three_sum = calculate_two_sum()
    two_sum = calculate_three_sum()

    print(three_sum, two_sum)


if __name__ == "__main__":
    main()

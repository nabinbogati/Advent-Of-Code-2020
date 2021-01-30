"""
    You start on the open square (.) in the top-left corner and need to reach the bottom
    (below the bottom-most row on your map).

    The toboggan can only follow a few specific slopes
    (you opted for a cheaper model that prefers rational numbers);
    start by counting all the trees you would encounter for the slope right 3, down 1:

    From your starting position at the top-left, check the position that is right 3 and down 1.
    Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

"""

FOREST_MAP = []

def read_file(filename):
    with open(filename, 'r') as file:
        for line in file.readlines():
            FOREST_MAP.append(line.strip())


def find_path():
    """ first half puzzle solution."""
    count = 0
    result = []

    for index in range(0, len(FOREST_MAP)):
        length = len(FOREST_MAP[index])
        count += 3

        if count > len(FOREST_MAP[index]) - 1:
            count = count - (length)

        if (index + 1) < len(FOREST_MAP):
            result.append(FOREST_MAP[index+1][count])

    return result


def find_path_generic(right, down):
    """ Second half puzzle solution 
        Finding out solutions for all slopes given
    """
    count = 0
    result = []

    for index in range(0, len(FOREST_MAP), down):
        length = len(FOREST_MAP[index])
        count += right

        if count > len(FOREST_MAP[index]) - 1:
            count = count % length

        if (index + down) < len(FOREST_MAP):
            result.append(FOREST_MAP[index+down][count])

    return result.count('#')



def main():
    input_slopes = [
        {'right': 1, 'down': 1},
        {'right': 3, 'down': 1},
        {'right': 5, 'down': 1},
        {'right': 7, 'down': 1},
        {'right': 1, 'down': 2}
    ]
    filename = 'input_day3.txt'
    count = 1

    read_file(filename)
    for slope in input_slopes:
        count *= find_path_generic(slope['right'], slope['down'])

    print(count)

if __name__ == "__main__":
    main()
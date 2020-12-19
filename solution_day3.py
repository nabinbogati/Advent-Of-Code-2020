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


def main():
    filename = 'input_day3.txt'
    read_file(filename)

    result = find_path()

    print(result.count('#'))


if __name__ == "__main__":
    main()
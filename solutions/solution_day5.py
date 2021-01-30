"""
The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
"""

DATA_MAP = []

def read_file(filename):
    with open(filename, 'r') as file:
        for data in file.readlines():
            data = data.strip()
            DATA_MAP.append({'row': data[:7], 'col': data[7:]})


def process_row(row):
    row_index = list(range(0, 128))

    for char in row:
        l = len(row_index) // 2

        if char == 'F':
            row_index = row_index[:l]
        else:
            row_index = row_index[l:]
    
    return row_index[0]

def process_col(col):
    col_index = list(range(0, 8))

    for char in col:
        l = len(col_index) // 2

        if char == 'L':
            col_index = col_index[:l]
        else:
            col_index = col_index[l:]
    
    return col_index[0]


def calculate_seat_id(row, col):
    seat_id = row*8 + col
    
    return seat_id


def find_my_seat(seat_ids):
    for value in seat_ids:
        if value + 1 not in seat_ids:
            return value+1


def main():
    filename = 'input_day5.txt'
    highest_seat_id = 0
    seat_ids = []
    read_file(filename)

    for space in DATA_MAP:
        row = process_row(space['row'])
        col = process_col(space['col'])

        seat_id = calculate_seat_id(row, col)

        seat_ids.append(seat_id)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    seat_ids = sorted(seat_ids)
    my_seat_id = find_my_seat(seat_ids)

    print(my_seat_id)


if __name__ == "__main__":
    main()
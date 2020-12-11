import enum
import copy
import common


class SeatType(str, enum.Enum):
    FLOOR: str    = '.'
    EMPTY: str    = 'L'
    OCCUPIED: str = '#'

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


def do_round(seats: common.Matrix):
    return_matrix: common.Matrix = copy.deepcopy(seats)

    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            adjacent_seats_occupied: int = 0
            adjacent_seats_empty: int = 0

            for x in range(max(0, i - 1), min(len(seats), i + 2)):
                for y in range(max(0, j - 1), min(len(row), j + 2)):
                    # skip the current seat
                    if (i, j) == (x, y):
                        continue

                    if seats[x][y] == SeatType.OCCUPIED:
                        adjacent_seats_occupied += 1

            if seat == SeatType.EMPTY and adjacent_seats_occupied == 0:
                return_matrix[i][j] = str(SeatType.OCCUPIED)

            if seat == SeatType.OCCUPIED and adjacent_seats_occupied >= 4:
                return_matrix[i][j] = str(SeatType.EMPTY)

    return return_matrix


if __name__ == '__main__':
    f = 'day11-test.txt'
    seat_matrix = common.read_matrix(f, str)
    common.print_matrix(seat_matrix)

    for turn in range(0, 4):
        print('------')
        seat_matrix = do_round(seat_matrix)
        common.print_matrix(seat_matrix)
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


def count_occupied_seats(r: int, c: int, seats: common.Matrix):
    count: int = 0
    relative_points = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i, j in relative_points:
        x = r+i
        y = c+j

        while 0 <= x < len(seats) and 0 <= y < len(seats[0]):
            if seats[x][y] == SeatType.OCCUPIED:
                count += 1
                break
            elif seats[x][y] == SeatType.EMPTY:
                break

            x += i
            y += j

    return count


def do_round_v2(seats: common.Matrix):
    return_matrix: common.Matrix = copy.deepcopy(seats)

    # r: row
    # c: column
    for r, row in enumerate(seats):
        for c, seat in enumerate(row):
            if seats[r][c] == SeatType.FLOOR:
                continue

            adjacent_seats_occupied: int = count_occupied_seats(r, c, seats)

            if seat == SeatType.EMPTY and adjacent_seats_occupied == 0:
                return_matrix[r][c] = str(SeatType.OCCUPIED)

            if seat == SeatType.OCCUPIED and adjacent_seats_occupied >= 5:
                return_matrix[r][c] = str(SeatType.EMPTY)

    return return_matrix


def part1(f: str) -> int:
    seat_matrix = common.read_matrix(f, str)
    count: int = 0

    while True:
        previous_matrix = copy.deepcopy(seat_matrix)
        seat_matrix = do_round(seat_matrix)

        if common.matrix_equal(previous_matrix, seat_matrix):
            break

        count += 1

    print(f'Rounds: {count}')
    ret: int = common.count_in_matrix(seat_matrix, SeatType.OCCUPIED)

    return ret


def part2(f: str) -> int:
    seat_matrix = common.read_matrix(f, str)
    count: int  = 0

    # common.print_matrix(seat_matrix)
    while True:
        previous_matrix = copy.deepcopy(seat_matrix)
        seat_matrix     = do_round_v2(seat_matrix)

        # print('----------')
        # common.print_matrix(seat_matrix)


        if common.matrix_equal(previous_matrix, seat_matrix):
            break

        count += 1

    print(f'Rounds: {count}')
    ret: int = common.count_in_matrix(seat_matrix, SeatType.OCCUPIED)

    return ret


if __name__ == '__main__':
    input_file = 'day11.txt'

    answer1 = part1(input_file)
    print(f'Answer 1: {answer1}')

    answer2 = part2(input_file)
    print(f'Answer 2: {answer2}')

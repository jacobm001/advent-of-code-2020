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


def matrix_walk(a_start: int, b_start: int, a_stop: int, b_stop: int \
                , a_increment: int = 0, b_increment: int = 0):

    while abs(a_start) - abs(a_stop) and abs(b_start) - abs(b_stop):
        yield a_start, b_start

        a_start += a_increment
        b_start += b_increment


def do_round_v2(seats: common.Matrix):
    return_matrix: common.Matrix = copy.deepcopy(seats)

    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            # if seats[i][j] == SeatType.FLOOR:
            #     continue

            adjacent_seats_occupied: int = 0

            # check up
            for x in range(min(i-1, 0), -1, -1):
                if (x, j) == (i, j): continue

                if seats[x][j] == SeatType.OCCUPIED:
                    adjacent_seats_occupied += 1
                    break
                if seats[x][j] == SeatType.EMPTY:
                    break

            # check down
            for x in range(min(i+1, len(seats)), len(seats), 1):
                if (x, j) == (i, j): continue

                if seats[x][j] == SeatType.OCCUPIED:
                    adjacent_seats_occupied += 1
                    break
                if seats[x][j] == SeatType.EMPTY:
                    break


            # check left
            for y in range(min(j-1, 0), -1, -1):
                if (i, y) == (i, j): continue

                if seats[i][y] == SeatType.OCCUPIED:
                    adjacent_seats_occupied += 1
                    break
                if seats[i][y] == SeatType.EMPTY:
                    break

            # check right
            for y in range(min(j+1, len(row)), len(row), 1):
                if (i, y) == (i, j): continue

                if seats[i][y] == SeatType.OCCUPIED:
                    adjacent_seats_occupied += 1
                    break
                if seats[i][y] == SeatType.EMPTY:
                    break

            # check up-left
            for x, y in matrix_walk(min(i-1, 0), min(j-1, 0), -1, -1, -1, -1):
                if (x, y) == (i, j): continue

                if seats[x][y] == SeatType.OCCUPIED:
                    adjacent_seats_occupied += 1
                    break
                if seats[x][y] == SeatType.EMPTY:
                    break

            # check up-right
            for x, y in matrix_walk(min(i-1, 0), min(j+1, len(row)), -1, len(row), -1, 1):
                if (x, y) == (i, j): continue

                if seats[x][y] == SeatType.OCCUPIED:
                    adjacent_seats_occupied += 1
                    break
                if seats[x][y] == SeatType.EMPTY:
                    break

            # check down-left
            for x, y in matrix_walk(i, j, len(seats), -1, 1, -1):
                if (x, y) == (i, j): continue

                if seats[x][y] == SeatType.OCCUPIED:
                    adjacent_seats_occupied += 1
                    break
                if seats[x][y] == SeatType.EMPTY:
                    break

            # check down-right
            for x, y in matrix_walk(i, j, len(seats), len(row), 1, 1):
                if (x, y) == (i, j): continue

                if seats[x][y] == SeatType.OCCUPIED:
                    adjacent_seats_occupied += 1
                    break
                if seats[x][y] == SeatType.EMPTY:
                    break

            if seat == SeatType.EMPTY and adjacent_seats_occupied == 0:
                return_matrix[i][j] = str(SeatType.OCCUPIED)

            if seat == SeatType.OCCUPIED and adjacent_seats_occupied >= 5:
                return_matrix[i][j] = str(SeatType.EMPTY)

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

    common.print_matrix(seat_matrix)
    while True:
        previous_matrix = copy.deepcopy(seat_matrix)
        seat_matrix     = do_round_v2(seat_matrix)

        print('----------')
        common.print_matrix(seat_matrix)


        if common.matrix_equal(previous_matrix, seat_matrix):
            break

        count += 1

    print(f'Rounds: {count}')
    ret: int = common.count_in_matrix(seat_matrix, SeatType.OCCUPIED)

    return ret


if __name__ == '__main__':
    input_file = 'day11-test.txt'

    answer1 = part1(input_file)
    print(f'Answer 1: {answer1}')

    answer2 = part2(input_file)
    print(f'Answer 2: {answer2}')

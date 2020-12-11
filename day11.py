import enum
import copy
import common


class seat_type(str, enum.Enum):
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
            adjacent_seats: int = 0

            # check left
            if j != 0 and row[j-1] == seat_type.OCCUPIED:
                adjacent_seats += 1
            # check right
            if j+1 < len(row) and row[j+1] == seat_type.OCCUPIED:
                adjacent_seats += 1
            # check up
            if i != 0 and seats[i-1][j] == seat_type.OCCUPIED:
                adjacent_seats += 1
            # check down
            if i+1 < len(seats) and seats[i+1][j] == seat_type.OCCUPIED:
                adjacent_seats += 1

            #
            if seat == seat_type.EMPTY and adjacent_seats == 0:
                return_matrix[i][j] = str(seat_type.OCCUPIED)
            if seat == seat_type.OCCUPIED and adjacent_seats >= 4:
                return_matrix[i][j] = str(seat_type.EMPTY)

    return return_matrix


if __name__ == '__main__':
    f = 'day11-test.txt'
    seat_matrix = common.read_matrix(f, str)
    common.print_matrix(seat_matrix)

    print('------')
    seat_matrix = do_round(seat_matrix)
    common.print_matrix(seat_matrix)

    print('------')
    seat_matrix = do_round(seat_matrix)
    common.print_matrix(seat_matrix)
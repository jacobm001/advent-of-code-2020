from common import read_matrix
from common import Matrix


class Toboggan:
    matrix: Matrix
    matrix_width: int
    matrix_height: int
    start_pos_x: int = 0
    start_pos_y: int = 0
    cur_pos_x: int
    cur_pos_y: int
    collisions: list

    def __init__(self, input_matrix: Matrix):
        self.matrix        = input_matrix
        self.matrix_width  = len(input_matrix[0])
        self.matrix_height = len(input_matrix)
        self.cur_pos_x     = 0
        self.cur_pos_y     = 0
        self.collisions    = []

    def increment_position(self, x: int, y: int):
        self.cur_pos_x += x
        self.cur_pos_y += y

    def check_position_value(self):
        # There's no need to actually copy the matrix over in memory
        # applying a mod operator here will simulate the matrix extension
        x = self.cur_pos_x % self.matrix_width
        return self.matrix[self.cur_pos_y][x]

    def run(self, slope_x: int, slope_y: int):
        while self.cur_pos_y < self.matrix_height-1:
            self.increment_position(slope_x, slope_y)
            if self.check_position_value() == '#':
                self.collisions.append((self.cur_pos_x, self.cur_pos_y))

    def count_collisions(self) -> int:
        return len(self.collisions)


if __name__ == "__main__":
    input_file = 'day03.txt'
    matrix     = read_matrix(input_file, str)

    # Part 1
    t = Toboggan(matrix)
    t.run(3, 1)

    print(f'Answer 1: {t.count_collisions()}')
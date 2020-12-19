from typing import Tuple, Dict, List
from collections import defaultdict
import common

Matrix     = List[List[str]]
Coordinate = Tuple[int, int, int]
ACTIVE     = '#'
INACTIVE   = '.'
NEWCOOR    = 'N'


def cube_neighbors() -> Coordinate:
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == j == k == 0:
                    continue

                yield i, j, k


class ConwayCube:
    coordinates: Dict

    def __init__(self, starting_input: Matrix):
        self.coordinates: defaultdict = defaultdict(lambda: '?')
        self.parse_input(starting_input)

    def parse_input(self, starting_input: Matrix):
        z = 0
        for x, line in enumerate(starting_input):
            for y, point in enumerate(line):
                self.coordinates[(x, y, z)] = point

    def count_type(self, coordinate_type: str) -> int:
        count: int = 0
        for state in self.coordinates.values():
            if state == coordinate_type:
                count += 1

        return count

    def check_neighbors(self, coordinate) -> int:
        count: int = 0
        for relative_pos in cube_neighbors():
            relative_coordinate = tuple(sum(x) for x in zip(coordinate, relative_pos))
            relative_state      = self.coordinates[relative_coordinate]

            if relative_state == ACTIVE:
                count += 1

        return count

    def do_round(self):
        # overriding the iterator here to try and not have the defaultdict not change the size during run
        for coordinate, state in tuple(self.coordinates.items()):
            active_neighbors: int = self.check_neighbors(coordinate)

            if state == ACTIVE and 2 <= active_neighbors <= 3:
                # cube remains active
                continue
            elif state == INACTIVE and active_neighbors == 2:
                self.coordinates[coordinate] = ACTIVE

        # handle the new NEWCOOR pieces
        for coordinate, state in tuple(self.coordinates.items()):
            if state != NEWCOOR:
                continue

            active_neighbors: int = self.check_neighbors(coordinate)
            if active_neighbors == 2:
                self.coordinates[coordinate] = ACTIVE
            else:
                self.coordinates[coordinate] = INACTIVE


if __name__ == '__main__':
    puzzle_input = common.read_matrix('day17-test.txt', str)
    cube = ConwayCube(puzzle_input)

    for i in range(0, 7):
        cube.do_round()

    print('Active:   ', cube.count_type(ACTIVE))
    print('Inactive: ', cube.count_type(INACTIVE))
    print('New:      ', cube.count_type(NEWCOOR))
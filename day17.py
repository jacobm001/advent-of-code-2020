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
        self.coordinates = defaultdict(lambda: NEWCOOR)
        self.parse_input(starting_input)

    def parse_input(self, starting_input: Matrix):
        z = 0
        for x, line in enumerate(starting_input):
            for y, point in enumerate(line):
                self.coordinates[(x, y, z)] = point

    def count_active(self):
        count = 0
        for point in self.coordinates.values():
            if point == ACTIVE:
                count += 1

    def do_round(self):
        new_dict: defaultdict   = self.coordinates.copy()
        new_coords: List[Tuple] = []
        active_neighbors: int   = 0

        for coordinate in self.coordinates.keys():
            for relative_pos in cube_neighbors():
                new_coord = tuple(sum(x) for x in zip(coordinate, relative_pos))
                value     = self.coordinates[new_coord]

                if value == NEWCOOR:
                    new_coords.append(new_coord)
                elif value == ACTIVE:
                    active_neighbors += 1


if __name__ == '__main__':
    puzzle_input = common.read_matrix('day17.txt', str)
    cube = ConwayCube(puzzle_input)
    cube.do_round()
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
        self.coordinates = {}
        self.parse_input(starting_input)

    def parse_input(self, starting_input: Matrix):
        z = 0
        for x, line in enumerate(starting_input):
            for y, point in enumerate(line):
                self.coordinates[(x, y, z)] = point

    def count_active(self) -> int:
        count = 0
        for point in self.coordinates.values():
            if point == ACTIVE:
                count += 1

        return count

    def do_round(self):
        new_dict: Dict          = self.coordinates.copy()
        new_coords: List[Tuple] = []

        for coordinate, state in self.coordinates.items():
            active_neighbors: int = 0

            for relative_pos in cube_neighbors():
                new_coord = tuple(sum(x) for x in zip(coordinate, relative_pos))
                # new_state = self.coordinates[new_coord]
                if new_coord not in self.coordinates:
                    new_state = NEWCOOR
                else:
                    new_state = self.coordinates[new_coord]

                if new_state == NEWCOOR:
                    new_coords.append(new_coord)
                elif new_state == ACTIVE:
                    active_neighbors += 1

            if state == ACTIVE and 2 <= active_neighbors <= 3:
                new_dict[coordinate] = ACTIVE
            else:
                new_dict[coordinate] = INACTIVE

            if state == INACTIVE and active_neighbors == 3:
                new_dict[coordinate] = ACTIVE

        for coordinate in new_coords:
            active_neighbors: int = 0

            for relative_pos in cube_neighbors():
                new_coord = tuple(sum(x) for x in zip(coordinate, relative_pos))
                if new_coord not in self.coordinates:
                    new_state = NEWCOOR
                else:
                    new_state = self.coordinates[new_coord]

                # We don't care about going further into the unknowns
                if new_state == NEWCOOR:
                    continue
                elif new_state == ACTIVE:
                    active_neighbors += 1

            if state == INACTIVE and active_neighbors == 3:
                new_dict[coordinate] = ACTIVE
                
        self.coordinates = new_dict.copy()


if __name__ == '__main__':
    puzzle_input = common.read_matrix('day17-test.txt', str)
    cube = ConwayCube(puzzle_input)

    for i in range(0, 2):
        cube.do_round()

    print(cube.count_active())
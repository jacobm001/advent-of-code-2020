import enum


class CompassPoints(enum.Enum):
    NORTH: int = 0
    SOUTH: int = 180
    EAST: int = 90
    WEST: int = 270


class Boat:
    heading: int
    pos_north: int
    pos_east: int

    def __init__(self, start_heading: int = 90):
        self.heading = start_heading
        self.pos_north = 0
        self.pos_east = 0

    def move(self, instruction: str):
        direction: str = instruction[:1]
        distance: int = int(instruction[1:])

        if direction == 'N':
            self.pos_north += distance
        elif direction == 'S':
            self.pos_north -= distance
        elif direction == 'E':
            self.pos_east += distance
        elif direction == 'W':
            self.pos_east -= distance
        elif direction == 'F':
            self.move_forward(distance)
        elif direction in ('L', 'R'):
            self.turn(direction, distance)
        else:
            raise ValueError(f'{direction} is not a valid direction')

    def move_forward(self, distance: int):
        if self.heading == CompassPoints.NORTH.value:
            self.pos_north += distance
        elif self.heading == CompassPoints.SOUTH.value:
            self.pos_north -= distance
        elif self.heading == CompassPoints.EAST.value:
            self.pos_east += distance
        elif self.heading == CompassPoints.WEST.value:
            self.pos_east -= distance

    def turn(self, direction: str, degrees: int):
        if direction == 'L':
            self.heading -= degrees
        elif direction == 'R':
            self.heading += degrees
        else:
            raise ValueError("Invalid direction, %s", direction)

        if self.heading >= 360:
            self.heading -= 360
        elif self.heading < 0:
            self.heading += 360

        return

    def manhattan_distance(self) -> int:
        return abs(self.pos_north) + abs(self.pos_east)
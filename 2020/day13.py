import common
from typing import List, Any
from itertools import count


def part1(earliest_departure: int, bus_times: List[int]) -> int:
    start: int = earliest_departure

    answer: int = None
    while answer is None:
        for i, bus in enumerate(bus_times):
            if start % bus == 0:
                wait: int = start - earliest_departure
                bus_id: int = bus_times[i]
                answer: int = wait * bus_id
                break

        start += 1

    return answer


# My previous solution took so long it'd effectively never return. I came up with this based
# on some hints I came across online.
def part2(buses_id_time) -> int:
    start: int = 0
    step: int = 1
    for bus, offset in buses_id_time:
        for i in count(start, step):
            if (i + offset) % bus == 0:
                start, step = i, step * bus
                break

    return start


if __name__ == '__main__':
    earliest: int
    buses_raw: List[Any]
    buses: List[int]

    with open('inputs/day13.txt', 'r') as f:
        earliest  = int(f.readline().strip())
        buses_raw = f.readline().strip().split(',')

    # I hate the next two lines... But here we are because they work
    buses  = list(map(int, list(filter(lambda x: x.isnumeric(), buses_raw))))
    buses2 = [(int(bus), index) for index, bus in enumerate(buses_raw) if bus != 'x']

    answer1   = part1(earliest, buses)
    answer2   = part2(buses2)

    print(f'Answer 1: {answer1}')
    print(f'Answer 2: {answer2}')

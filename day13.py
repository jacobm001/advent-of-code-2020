import common
from typing import List, Any


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


def part2(bus_times: List[str]) -> int:
    answer: int = None
    first_bus: int = int(bus_times[0])

    start: int = 100000000000000
    while answer is None:
        if start % first_bus == 0:
            found: bool = True
            for i in range(1, len(bus_times)):
                if not (bus_times[i] == 'x' or (start+i) % int(bus_times[i]) == 0):
                    found = False
                    break

            if found == True:
                answer = start

        start += 1

    return answer


if __name__ == '__main__':
    earliest: int
    buses_raw: List[Any]
    buses: List[int]

    with open('inputs/day13.txt', 'r') as f:
        earliest  = int(f.readline().strip())
        buses_raw = f.readline().strip().split(',')

    buses     = list(map(int, list(filter(lambda x: x.isnumeric(), buses_raw))))
    answer1   = part1(earliest, buses)
    answer2   = part2(buses_raw)

    print(f'Answer 1: {answer1}')
    print(f'Answer 2: {answer2}')

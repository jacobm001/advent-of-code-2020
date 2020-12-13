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


if __name__ == '__main__':
    earliest: int
    buses_raw: List[Any]
    buses: List[int]

    with open('inputs/day13.txt', 'r') as f:
        earliest  = int(f.readline().strip())
        buses_raw = f.readline().strip().split(',')

    buses_raw = list(filter(lambda x: x.isnumeric(), buses_raw))
    buses     = list(map(int, buses_raw))
    answer1   = part1(earliest, buses)
    print(f'Answer 1: {answer1}')

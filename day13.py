import common
from typing import List, Any

if __name__ == '__main__':
    earliest: int
    buses_raw: List[Any]
    buses: List[int]

    with open('inputs/day13.txt', 'r') as f:
        earliest  = int(f.readline().strip())
        buses_raw = f.readline().strip().split(',')

    buses_raw = list(filter(lambda x: x.isnumeric(), buses_raw))
    buses     = list(map(int, buses_raw))

    start: int = earliest

    answer1: int = None
    while answer1 is None:
        for i, bus in enumerate(buses):
            if start % bus == 0:
                wait: int    = start - earliest
                bus_id: int  = buses[i]
                answer1: int = wait * bus_id
                break

        start += 1

    print(f'Answer 1: {answer1}')

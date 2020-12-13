import common
from typing import List, Any

if __name__ == '__main__':
    earliest: int
    buses_raw: List[Any]
    buses: List[int]

    with open('inputs/day13-test.txt', 'r') as f:
        earliest  = int(f.readline())
        buses_raw = f.readline().strip().split(',')

    buses_raw = list(filter(lambda x: x.isnumeric(), buses_raw))
    buses     = list(map(int, buses_raw))

    rounds: int = 1
    answer1: int = None
    while True:
        round_times: List = list(map(lambda x: (x * rounds)-1, buses))
        min_time: int     = min(round_times)

        if earliest <= min_time:
            pos: int    = round_times.index(min_time)
            bus_id: int = buses[pos]
            wait: int   = min_time - earliest

            answer1: int = wait * bus_id
            break

        rounds += 1

    print(f'Answer 1: {answer1}')

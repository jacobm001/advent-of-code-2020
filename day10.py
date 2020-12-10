from typing import List
import collections
import common


def prep_list(il: List[int]):
    # sort values
    il.sort()

    # Add in our device's maximum rating
    device_max = il[-1] + 3
    il.append(device_max)

    # Add the leading 0 for the seat
    il = [0] + il

    return il


def get_differences(il: List[int]) -> collections.Counter:
    differences: List[int] = []

    for i in range(1, len(il)):
        diff = il[i] - il[i-1]
        differences.append(diff)

    return collections.Counter(differences)


def part1(il) -> int:
    il = prep_list(il)
    difference_count = get_differences(il)

    return difference_count[1] * difference_count[3]


if __name__ == '__main__':
    f = 'day10.txt'
    input_list: List[int] = common.read_list(f)

    answer1: int = part1(input_list)
    print(f'Answer 1: {answer1}')
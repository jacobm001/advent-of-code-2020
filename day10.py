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


def count_branches(il: List[int], position: int = 0):
    count = 1
    start = position + 1
    end   = len(il) - start
    for i in range(start, end+1):
        if il[i] - il[position] <= 3:
            count += count_branches(il, i+1)

    return count


def part1(il) -> int:
    il = prep_list(il)
    difference_count = get_differences(il)

    return difference_count[1] * difference_count[3]


def part2(il) -> int:
    il = prep_list(il)
    return count_branches(input_list) + 1


if __name__ == '__main__':
    f = 'day10.txt'
    input_list: List[int] = common.read_list(f)

    answer1: int = part1(input_list)
    print(f'Answer 1: {answer1}')

    answer2: int = part2(input_list)
    print(f'Answer 2: {answer2}')
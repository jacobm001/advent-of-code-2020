from itertools import combinations
from common import IntList
from common import read_list


def product(arr: IntList):
    ret = arr[0]

    for x in arr[1:]:
        ret *= x

    return ret


def find_values(arr: IntList, expected_value: int, group_size: int = 2):
    for group in combinations(arr, group_size):
        if sum(group) == expected_value:
            return product(group)


if __name__ == "__main__":
    input_file = 'day01.txt'
    input_array = read_list(input_file)

    # Puzzle 1
    res1 = find_values(input_array, 2020)
    print(f'Puzzle1 Answer: {res1}')

    # Puzzle 2
    res2 = find_values(input_array, 2020, 3)
    print(f'Puzzle2 Answer: {res2}')


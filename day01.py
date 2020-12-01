from itertools import combinations


def product(arr: list):
    ret = arr[0]

    for x in arr[1:]:
        ret *= x

    return ret


def find_values(arr: list, expected_value: int, group_size: int = 2):
    for group in combinations(arr, 2):
        if sum(group) == expected_value:
            return product(group)

if __name__ == "__main__":
    v = find_values([1721,979,366,299,675,1456], 2020)
    print(v)
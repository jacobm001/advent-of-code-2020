""" Handles converting puzzle input to useable data structures"""

from typing import List
IntList = List[int]


def read_list(f: str, type_func = int):
    path = f'inputs/{f}'
    with open(path, 'r') as f:
        raw_arr = f.readlines()

    arr = list(map(type_func, raw_arr))
    return arr

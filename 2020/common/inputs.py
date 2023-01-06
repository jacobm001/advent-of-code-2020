""" Handles converting puzzle input to useable data structures"""

from typing import Any, List
IntList = List[int]
Matrix  = List[Any]


def read_list(f: str, type_func = int):
    path = f'inputs/{f}'
    with open(path, 'r') as f:
        raw_arr = f.readlines()

    arr = list(map(type_func, raw_arr))
    return arr


def read_blocks(f: str, type_func = str) -> List[Any]:
    path = f'inputs/{f}'
    with open(path, 'r') as f:
        raw_str = f.read()

    arr = raw_str.split('\n\n')
    arr = list(map(type_func, arr))
    return arr


def read_matrix(f: str, type_func = int) -> Matrix:
    path = f'inputs/{f}'
    with open(path, 'r') as f:
        matrix: Matrix = f.read().splitlines()

    for i, line in enumerate(matrix):
        # convert the line to a list of the input type
        matrix[i] = list(map(type_func, list(line)))

    return matrix

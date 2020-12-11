from typing import Any

from .inputs import *
from .testing import *
from .tree import *


def product(arr: IntList):
    ret = arr[0]

    for x in arr[1:]:
        ret *= x

    return ret


def print_matrix(matrix: Matrix):
    for row in matrix:
        print(row)


def matrix_equal(matrix_a: Matrix, matrix_b: Matrix) -> bool:
    for x in range(0, len(matrix_a)):
        for y in range(0, len(matrix_a[0])):
            if matrix_a[x][y] != matrix_b[x][y]:
                return False

    return True


def count_in_matrix(matrix: Matrix, value: Any) -> int:
    count: int = 0

    for row in matrix:
        for seat in row:
            if seat == value:
                count += 1

    return count

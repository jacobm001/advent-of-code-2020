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

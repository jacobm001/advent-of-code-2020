from .inputs import *
from .testing import *


def product(arr: IntList):
    ret = arr[0]

    for x in arr[1:]:
        ret *= x

    return ret

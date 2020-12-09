import itertools
import common
from typing import List, Set


class XMAS:
    code: List[int]
    preamble_length: int

    def __init__(self, input_numbers: List[int], preamble_length: int = 25):
        self.code            = input_numbers
        self.preamble_length = preamble_length

    def find_first_invalid_entry(self) -> int:
        start: int = self.preamble_length
        stop: int  = len(self.code)

        for i in range(start, stop):
            possible_multiplicands = self.code[i-self.preamble_length:i]
            possible_combos = itertools.combinations(possible_multiplicands, 2)

            f = list(filter(lambda x: sum(x) == self.code[i], possible_combos))
            if not f:
                return self.code[i]



if __name__ == '__main__':
    f    = 'day09.txt'
    xmas = XMAS(common.read_list(f, int), 25)

    answer1 = xmas.find_first_invalid_entry()
    print(f'Answer 1: {answer1}')

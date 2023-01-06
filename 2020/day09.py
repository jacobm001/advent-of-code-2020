import itertools
import common
from typing import List


class XMAS:
    code: List[int]
    preamble_length: int

    def __init__(self, input_numbers: List[int], preamble_length: int = 25):
        self.code            = input_numbers
        self.preamble_length = preamble_length

    @property
    def find_first_invalid_entry(self) -> int:
        start: int = self.preamble_length
        stop: int  = len(self.code)

        for i in range(start, stop):
            possible_multiplicands = self.code[i - self.preamble_length:i]
            possible_combos = itertools.combinations(possible_multiplicands, 2)

            if list(filter(lambda x: sum(x) == self.code[i], possible_combos)):
                continue

            return self.code[i]

    def find_encryption_weakness(self, invalid_entry) -> int:
        """ Uses a nested for loop to try and find the sublist that totals the submitted invalid entry """

        stop: int  = self.code.index(invalid_entry)

        for i in range(0, stop):
            total: int = self.code[i]

            for j in range(i+1, stop):
                total += self.code[j]

                if total == invalid_entry:
                    values = self.code[i:j]
                    return min(values) + max(values)


if __name__ == '__main__':
    f    = 'day09.txt'
    xmas = XMAS(common.read_list(f, int), 25)

    answer1 = xmas.find_first_invalid_entry
    print(f'Answer 1: {answer1}')

    answer2 = xmas.find_encryption_weakness(answer1)
    print(f'Answer 2: {answer2}')

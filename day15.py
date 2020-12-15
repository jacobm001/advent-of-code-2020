import timeit
from typing import List, Optional, Dict


class MemoryGame:
    numbers: Dict[int, int]
    starting_numbers: List[int]

    def __init__(self, starting_numbers: List[int]):
        self.starting_numbers = starting_numbers
        self.numbers = {}

    def play_until(self, play_until: int) -> int:
        nth_number: int = 0

        for number in self.starting_numbers:
            self.numbers[number] = [nth_number]
            nth_number += 1

        last_number: int = self.starting_numbers[-1]
        new_number: bool = True
        while nth_number < play_until:
            if new_number:
                last_number = 0
                self.numbers[last_number].append(nth_number)
                new_number = False
            else:
                last_number = self.numbers[last_number][-1] - self.numbers[last_number][-2]
                if last_number not in self.numbers:
                    self.numbers[last_number] = [nth_number]
                    new_number = True
                else:
                    self.numbers[last_number].append(nth_number)
                    new_number = False

            nth_number += 1


        return last_number


if __name__ == '__main__':
    puzzle_input = [1, 0, 16, 5, 17, 4]

    # Part 1
    game1 = MemoryGame(puzzle_input)
    start_time   = timeit.default_timer()
    answer1: int = game1.play_until(2020)
    end_time     = timeit.default_timer() - start_time
    print(f'Answer 1: {answer1}')
    print(f'\t Answer 1 completed in {end_time} seconds.')

    # Part 21
    game2        = MemoryGame(puzzle_input)
    start_time   = timeit.default_timer()
    answer2: int = game2.play_until(30000000)
    end_time     = timeit.default_timer() - end_time
    print(f'Answer 2: {answer2}')
    print(f'\t Answer 2 completed in {end_time} seconds.')

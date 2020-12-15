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
    # puzzle_input = [0, 3, 6]
    game1 = MemoryGame(puzzle_input)

    answer1: int = game1.play_until(2020)
    print(f'Answer 1: {answer1}')

    game2 = MemoryGame(puzzle_input)
    answer2: int = game2.play_until(30000000)
    print(f'Answer 2: {answer2}')

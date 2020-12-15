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
        while nth_number < 2020:
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
    game = MemoryGame(puzzle_input)

    answer1: int = game.play_until(2020)

    print(f'Answer 1: {answer1}')
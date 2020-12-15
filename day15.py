from typing import List, Optional


class MemoryGame:
    numbers: List[int]

    def __init__(self, starting_numbers: List[int]):
        self.numbers = starting_numbers

    def _rindex(self, value: int) -> Optional[int]:
        try:
            self.numbers.reverse()
            i = self.numbers.index(value, 1)
            self.numbers.reverse()
            return len(self.numbers) - i - 1
        except ValueError:
            return None

    def round(self):
        while len(self.numbers) < 2020:
            last_spoken = self.numbers[-1]
            last_index  = self._rindex(last_spoken)
            if not last_index:
                self.numbers.append(0)
            else:
                new_number: int = len(self.numbers) - last_index
                self.numbers.append(new_number)


if __name__ == '__main__':
    # puzzle_input = [1, 0, 16, 5, 17, 4]
    puzzle_input = [0, 3, 6]
    game = MemoryGame(puzzle_input)
    game.round()

    print(game.numbers[-1])
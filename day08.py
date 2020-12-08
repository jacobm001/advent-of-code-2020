import re
from typing import List
import common


INSTRUCTION_PATTERN = re.compile(r"^([a-z]{3}) ([+\-0-9]+)$")


def parse_instruction(instruction: str) -> (str, int):
    match = re.match(INSTRUCTION_PATTERN, instruction)
    cmd   = match.group(1)
    arg   = int(match.group(2))

    return cmd, arg


class BootCode:
    instructions: List[str]
    seen_positions: List[int]
    accumulator: int
    cur_position: int

    def __init__(self, input_instructions: List[str]):
        self.accumulator    = 0
        self.cur_position   = 0
        self.seen_positions = []

        self.cmd_translate = {
            'acc': self.accumulate
            , 'jmp': self.jump
            , 'nop': self.noop
        }

        self.instructions = input_instructions

    def accumulate(self, value):
        self.accumulator += value
        self.cur_position += 1

    def jump(self, value):
        self.cur_position += value

    def noop(self, value):
        self.cur_position += 1

    def process(self):
        instruction = self.instructions[self.cur_position]
        cmd, arg = parse_instruction(instruction)

        self.seen_positions.append(self.cur_position)
        self.cmd_translate[cmd](arg)

    def process_first_loop(self):
        while self.cur_position not in self.seen_positions:
            self.process()

            if self.cur_position in self.seen_positions:
                break

        return self.accumulator


if __name__ == '__main__':
    f          = 'day08.txt'
    input_list = common.read_list(f, str)
    bc         = BootCode(input_list)

    answer1 = bc.process_first_loop()

    print(f'Answer 1: {answer1}')


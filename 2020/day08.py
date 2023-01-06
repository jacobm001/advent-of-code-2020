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
        self.accumulator       = 0
        self.cur_position      = 0
        self.seen_positions    = []

        self.cmd_translate = {
            'acc': self.accumulate
            , 'jmp': self.jump
            , 'nop': self.noop
        }

        self.instructions          = input_instructions
        self.original_instructions = input_instructions

    def accumulate(self, value) -> None:
        self.accumulator += value
        self.cur_position += 1

    def jump(self, value) -> None:
        self.cur_position += value

    def noop(self, value) -> None:
        self.cur_position += 1

    def process(self, try_swap: bool = False) -> None:
        instruction = self.instructions[self.cur_position]
        cmd, arg    = parse_instruction(instruction)

        self.seen_positions.append(self.cur_position)
        self.cmd_translate[cmd](arg)

    def check_for_exit(self) -> bool:
        if self.cur_position >= len(self.instructions) - 1:
            return True
        else:
            return False

    def reset(self):
        self.accumulator    = 0
        self.cur_position   = 0
        self.seen_positions = []

    def process_first_loop(self) -> bool:
        while True:
            self.process()

            if self.cur_position in self.seen_positions:
                return False

            if self.check_for_exit():
                return True


if __name__ == '__main__':
    f          = 'day08.txt'
    input_list = common.read_list(f, str)
    bc         = BootCode(input_list)

    bc.process_first_loop()
    answer1 = bc.accumulator
    print(f'Answer 1: {answer1}')

    changeable_spaces = []
    for i, line in enumerate(input_list):
        if line[:3] in ['nop', 'jmp']:
            changeable_spaces.append(i)

    for space in changeable_spaces:
        instructions = input_list.copy()
        if instructions[space][:3] == 'nop':
            cmd = 'jmp'
        else:
            cmd = 'nop'

        instructions[space] = cmd + instructions[space][3:]
        bc2 = BootCode(instructions)
        if bc2.process_first_loop():
            answer2 = bc2.accumulator
            print(f'Answer 2: {answer2}')

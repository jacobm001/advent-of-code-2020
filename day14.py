import common
import re
from typing import List, Dict
import itertools

Mask   = List[str]
Memory = Dict[int, str]


MASK_PATTERN = re.compile(r'^mask = ([X01]{36})$')
MEM_PATTERN  = re.compile(r'^mem\[([0-9]+)\] = ([0-9]+)$')


class ComputerSystem:
    mask: Mask
    mem: Memory

    def __init__(self):
        self.mask = ['X'] * 36
        self.mem  = {}

    def set_mask(self, new_mask: Mask):
        self.mask = new_mask

    def apply_mask(self, binary_rep: List[str]) -> str:
        return_value = ['0'] * 36
        for i in range(len(binary_rep)-1, -1, -1):
            if self.mask[i] != 'X':
                return_value[i] = self.mask[i]
            else:
                return_value[i] = binary_rep[i]

        return return_value

    def set_memory(self, address: int, value: int):
        binary_rep        = '{0:036b}'.format(value)
        binary_rep        = list(binary_rep)
        masked_value      = self.apply_mask(binary_rep)
        self.mem[address] = masked_value

    def apply_memory_mask(self, binary_rep: List[str]) -> str:
        return_value = ['0'] * 36
        for i in range(len(binary_rep)-1, -1, -1):
            if self.mask[i] == '0':
                return_value[i] = binary_rep[i]
            elif self.mask[i] == '1':
                return_value[i] = '1'
            else:
                return_value[i] = 'X'

        return return_value

    def _get_memory_combinations(self, applied_mask: List[str]) -> List[int]:
        indices = [i for i, x in enumerate(applied_mask) if x == 'X']
        combos  = list(itertools.product('01', repeat=len(indices)))

        new_list: List[int] = []
        for combo in combos:
            new_mask = applied_mask.copy()
            for i, index in enumerate(indices):
                new_mask[index] = combo[i]

            s = ''.join(new_mask)
            new_list.append(int(s, 2))

        return new_list

    def memory_decoder(self, key: int, value: int):
        mem_binary_rep = '{0:036b}'.format(key)
        applied_mask   = self.apply_memory_mask(list(mem_binary_rep))

        for address in self._get_memory_combinations(applied_mask):
            self.mem[address] = value


    def get_memory_sum(self) -> int:
        # iterate through the memory dictionary values
        # 1. for each value, join the List[str] to a single string
        # 2. convert that 36bit binary string to an integer.
        # 3. return the sum()
        return sum(list(map(lambda x: int(''.join(x), 2), self.mem.values())))


def part1(instructions: List[str]) -> int:
    cs: ComputerSystem = ComputerSystem()

    for instruction in instructions:
        if instruction[0:3] == 'mas':
            match = re.match(MASK_PATTERN, instruction)
            if match:
                cs.set_mask(match.group(1))

        elif instruction[0:3] == 'mem':
            match = re.match(MEM_PATTERN, instruction)
            if match:
                cs.set_memory(int(match.group(1)), int(match.group(2)))

    return cs.get_memory_sum()


def part2(instructions: List[str]) -> int:
    cs: ComputerSystem = ComputerSystem()

    for instruction in instructions:
        if instruction[0:3] == 'mas':
            match = re.match(MASK_PATTERN, instruction)
            if match:
                cs.set_mask(match.group(1).strip())

        elif instruction[0:3] == 'mem':
            match = re.match(MEM_PATTERN, instruction)
            if match:
                cs.memory_decoder(int(match.group(1)), int(match.group(2)))

    return sum(cs.mem.values())


if __name__ == '__main__':
    instructions: List[str] = common.read_list('day14.txt', str)

    answer1 = part1(instructions)
    print(f'Answer 1: {answer1}')

    answer2 = part2(instructions)
    print(f'Answer 2: {answer2}')

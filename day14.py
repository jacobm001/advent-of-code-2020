import common
from typing import List, Dict
Mask   = List[str]
Memory = Dict[int, str]


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

    def set_memory(self, key: int, value: int):
        binary_rep    = '{0:036b}'.format(value)
        binary_rep    = list(binary_rep)
        masked_value  = self.apply_mask(binary_rep)
        self.mem[key] = masked_value

    def get_memory_sum(self) -> int:
        # iterate through the memory dictionary values
        # 1. for each value, join the List[str] to a single string
        # 2. convert that 36bit binary string to an integer.
        # 3. return the sum()
        return sum(list(map(lambda x: int(''.join(x), 2), self.mem.values())))


if __name__ == '__main__':
    cs = ComputerSystem()
    cs.set_mask(list('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))
    cs.set_memory(8, 11)
    cs.set_memory(7, 101)
    cs.set_memory(8, 0)

    answer1 = cs.get_memory_sum()
    print(f'Answer 1: {answer1}')

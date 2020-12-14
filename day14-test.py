import unittest
import re
import day14


class MyTestCase(unittest.TestCase):
    def test_part1_example(self):
        cs = day14.ComputerSystem()
        cs.set_mask(list('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))
        cs.set_memory(8, 11)
        cs.set_memory(7, 101)
        cs.set_memory(8, 0)

        self.assertEqual(165, cs.get_memory_sum())

    def test_regex_mask(self):
        instruction: str = 'mask = X100110110X011000101000101XX11001X11'
        match: re.Match  = re.match(day14.MASK_PATTERN, instruction)

        self.assertEqual('X100110110X011000101000101XX11001X11', match.group(1))

    def test_regex_mem(self):
        instruction: str = 'mem[5201] = 1838761'
        match: re.Match  = re.match(day14.MEM_PATTERN, instruction)

        self.assertEqual('5201', match.group(1))
        self.assertEqual('1838761', match.group(2))

    def test_memory_masking(self):
        instruction0: str = 'mask = 000000000000000000000000000000X1001X'
        instruction1: str = 'mem[42] = 100'

        cs = day14.ComputerSystem()
        cs.set_mask(list('000000000000000000000000000000X1001X'))
        cs.memory_decoder(42, 100)

        self.assertEqual(100, cs.mem[26])


if __name__ == '__main__':
    unittest.main()

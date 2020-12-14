import unittest
import day14


class MyTestCase(unittest.TestCase):
    def test_part1_example(self):
        cs = day14.ComputerSystem()
        cs.set_mask(list('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))
        cs.set_memory(8, 11)
        cs.set_memory(7, 101)
        cs.set_memory(8, 0)

        self.assertEqual(165, cs.get_memory_sum())


if __name__ == '__main__':
    unittest.main()

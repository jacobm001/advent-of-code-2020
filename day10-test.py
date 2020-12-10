import unittest
from typing import List
import common
import day10


class MyTestCase(unittest.TestCase):
    def test_prep_list(self):
        input_list = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        expected_list = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
        answer = day10.prep_list(input_list)

        self.assertListEqual(expected_list, answer)

    def test_get_differences(self):
        input_list = [1, 3, 4, 5]
        expected = {2: 1, 1: 2}
        answer = day10.get_differences(input_list)

        self.assertDictEqual(expected, answer)

    def test_second_example(self):
        f = 'day10-test2.txt'
        input_list: List[int] = common.read_list(f)
        answer: int = day10.part1(input_list)

        self.assertEqual(220, answer)

    def test_first_ex_part2(self):
        f = 'day10-test1.txt'
        input_list: List[int] = common.read_list(f)

        answer: int = day10.part2(input_list)
        self.assertEqual(8, answer)

    def test_second_ex_part2(self):
        f = 'day10-test2.txt'
        input_list: List[int] = common.read_list(f)

        answer: int = day10.part2(input_list)
        self.assertEqual(19208, answer)


if __name__ == '__main__':
    unittest.main()

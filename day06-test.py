import unittest
from typing import List
import common
import day06


class MyTestCase(unittest.TestCase):
    def test_unique_entries(self):
        f = 'day06-sample2.txt'
        groups: List[day06.SurveyGroup] = common.read_blocks(f, day06.SurveyGroup)
        self.assertEqual(groups[0].count_unique_entries(), 3)
        self.assertEqual(groups[1].count_unique_entries(), 3)
        self.assertEqual(groups[2].count_unique_entries(), 3)
        self.assertEqual(groups[3].count_unique_entries(), 1)
        self.assertEqual(groups[4].count_unique_entries(), 1)

    def test_yes_summary(self):
        f = 'day06-sample2.txt'
        groups: List[day06.SurveyGroup] = common.read_blocks(f, day06.SurveyGroup)
        count = day06.get_yes_summary(groups)
        self.assertEqual(count, 11)


if __name__ == '__main__':
    unittest.main()

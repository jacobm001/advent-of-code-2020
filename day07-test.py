import unittest
import common
import day07


class MyTestCase(unittest.TestCase):
    def test_example(self):
        f = 'day07-test.txt'
        raw_list = common.read_list(f, str)

        sg = day07.SuitcaseCatalog(raw_list)
        answer1 = sg.count_contains('shiny gold')

        self.assertEqual(answer1, 4)


if __name__ == '__main__':
    unittest.main()

import unittest
import common
import day07


class MyTestCase(unittest.TestCase):
    def test_example(self):
        f = 'day07-test.txt'
        raw_list = common.read_list(f, str)

        sg = day07.SuitcaseCatalog(raw_list)
        answer1 = sg.count_contains('shiny gold')

        self.assertEqual(4, answer1)

    def test_count_descendents(self):
        f = 'day07-test3.txt'
        raw_list = common.read_list(f, str)

        sg = day07.SuitcaseCatalog(raw_list)
        answer2 = sg.count_descendants('shiny gold')

        self.assertEqual(126, answer2)



if __name__ == '__main__':
    unittest.main()

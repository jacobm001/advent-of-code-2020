import unittest
import common
import day09

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        f = 'day09-test.txt'
        self.test_input = common.read_list(f)

    def test_find_first_invalid_entry(self):
        test = common.TestValue(None, 127)
        xmas = day09.XMAS(self.test_input, 5)
        ret  = xmas.find_first_invalid_entry

        self.assertEqual(test.expected_output, ret)

    def test_find_encryption_weakness(self):
        test = common.TestValue(127, 62)
        xmas = day09.XMAS(self.test_input, 5)

        weakness = xmas.find_encryption_weakness(test.input_value)
        self.assertEqual(test.expected_output, weakness)


if __name__ == '__main__':
    unittest.main()

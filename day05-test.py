import unittest
from common import TestValue
import day05


class MyTestCase(unittest.TestCase):
    def test_assigned_seat(self):
        tests = [
            TestValue('FBFBBFFRLR', (44, 5))
            , TestValue('BFFFBBFRRR', (70, 7))
            , TestValue('FFFBBBFRRR', (14, 7))
            , TestValue('BBFFBBFRLL', (102, 4))
        ]
        for test in tests:
            t = day05.TicketParser(test.input_value)
            self.assertEqual(t.get_seat(), test.expected_output)

    def test_seat_id(self):
        tests = [
            TestValue('FBFBBFFRLR', 357)
            , TestValue('BFFFBBFRRR', 567)
            , TestValue('FFFBBBFRRR', 119)
            , TestValue('BBFFBBFRLL', 820)
        ]
        for test in tests:
            t = day05.TicketParser(test.input_value)
            self.assertEqual(t.seat_id, test.expected_output)


if __name__ == '__main__':
    unittest.main()

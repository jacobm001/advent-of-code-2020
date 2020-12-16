import unittest
import day16


class MyTestCase(unittest.TestCase):
    def test_parse_my_ticket(self):
        with open('inputs/day16-test-my-ticket.txt', 'r') as f:
            raw_input = f.read().split('\n')

        res      = day16.parse_my_ticket(raw_input)
        expected = [127, 109, 139, 113]
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()

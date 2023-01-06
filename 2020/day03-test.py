import unittest
from common import read_matrix
from day03 import Toboggan


class MyTestCase(unittest.TestCase):
    def test_toboggan_run(self):
        input_file = 'day03-test.txt'
        matrix     = read_matrix(input_file, str)

        t = Toboggan(matrix)
        t.run(3, 1)

        self.assertEqual(len(t.collisions), 7)


if __name__ == '__main__':
    unittest.main()

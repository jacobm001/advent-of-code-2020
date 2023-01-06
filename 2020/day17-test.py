import unittest
import day17


class MyTestCase(unittest.TestCase):
    def test_cube_neighbors(self):
        neighbors = list(day17.cube_neighbors())
        self.assertEqual(26, len(neighbors))


if __name__ == '__main__':
    unittest.main()

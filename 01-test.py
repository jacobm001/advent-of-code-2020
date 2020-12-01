import unittest
import day01


class TestDay01(unittest.TestCase):
    def test_product(self):
        res = day01.product([1,2,3,4])
        self.assertEqual(res, 24)


    def test_product_zero(self):
        res = day01.product([0,100,123])
        self.assertEqual(res, 0)


    def test_find_values(self):
        """ Values here provided code """
        arr = [1721, 979, 366, 299, 675, 1456]
        res = day01.find_values(arr, 2020)
        self.assertEqual(res, 514579)


if __name__ == '__main__':
    unittest.main()

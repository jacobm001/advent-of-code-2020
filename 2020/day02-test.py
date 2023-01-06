import unittest
import day02
from common import TestValue


class MyTestCase(unittest.TestCase):
    def test_PasswordAuthenticator_init(self):
        tests = [
            TestValue('1-3 a: abcde', [1, 3, 'a', 'abcde'])
            , TestValue('1-3 b: cdefg', [1, 3, 'b', 'cdefg'])
            , TestValue('2-9 c: ccccccccc', [2, 9, 'c', 'ccccccccc'])
        ]

        for test in tests:
            with self.subTest(test=test):
                pa = day02.PasswordAuthenticator(test.input_value)
                res = [
                    pa.minimum
                    , pa.maximum
                    , pa.character
                    , pa.password
                ]
                self.assertListEqual(res, test.expected_output)

    def test_validation_1(self):
        tests = [
            TestValue('1-3 a: abcde', True)
            , TestValue('1-3 b: cdefg', False)
            , TestValue('2-9 c: ccccccccc', True)
        ]

        for test in tests:
            with self.subTest(test=test):
                pa = day02.PasswordAuthenticator(test.input_value)
                self.assertEqual(pa.validate_password_1(), test.expected_output)

    def test_validation_2(self):
        tests = [
            TestValue('1-3 a: abcde', True)
            , TestValue('1-3 b: cdefg', False)
            , TestValue('2-9 c: ccccccccc', False)
        ]

        for test in tests:
            with self.subTest(test=test):
                pa = day02.PasswordAuthenticator(test.input_value)
                self.assertEqual(pa.validate_password_2(), test.expected_output)


if __name__ == '__main__':
    unittest.main()

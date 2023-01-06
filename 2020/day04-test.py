import unittest
import day04


class MyTestCase(unittest.TestCase):
    def test_read_passport_file(self):
        passport = day04.read_passport_file('day04-test.txt')[0]

        self.assertEqual(passport.passport_fields['byr'], '1937')
        self.assertEqual(passport.passport_fields['iyr'], '2017')
        self.assertEqual(passport.passport_fields['eyr'], '2020')
        self.assertEqual(passport.passport_fields['hgt'], '183cm')
        self.assertEqual(passport.passport_fields['hcl'], '#fffffd')
        self.assertEqual(passport.passport_fields['ecl'], 'gry')
        self.assertEqual(passport.passport_fields['pid'], '860033327')
        self.assertEqual(passport.passport_fields['cid'], '147')

    def test_invalid_passport_file(self):
        passports   = day04.read_passport_file('day04-test-invalid-passports.txt')
        count: int  = 0

        for passport in passports:
            if passport.validate_passport(validate_fields=True):
                count += 1

        self.assertEqual(count, 0)

    def test_valid_passport_file(self):
        passports   = day04.read_passport_file('day04-test-valid-passports.txt')
        count: int  = 0

        for passport in passports:
            if passport.validate_passport(validate_fields=True):
                count += 1

        self.assertEqual(count, 4)

    def test_birth_year(self):
        self.assertTrue(day04.Passport.validate_birth_year('2002'))
        self.assertFalse(day04.Passport.validate_birth_year('2003'))

    def test_height(self):
        self.assertTrue(day04.Passport.validate_height('60in'))
        self.assertTrue(day04.Passport.validate_height('190cm'))
        self.assertFalse(day04.Passport.validate_height('190in'))
        self.assertFalse(day04.Passport.validate_height('190'))

    def test_hair_color(self):
        self.assertTrue(day04.Passport.validate_hair_color('#123abc'))
        self.assertFalse(day04.Passport.validate_hair_color('123abz'))
        self.assertFalse(day04.Passport.validate_hair_color('123abc'))

    def test_eye_color(self):
        self.assertTrue(day04.Passport.validate_eye_color('brn'))
        self.assertFalse(day04.Passport.validate_eye_color('wat'))

    def test_pid(self):
        self.assertTrue(day04.Passport.validate_pid('000000001'))
        self.assertFalse(day04.Passport.validate_pid('0123456789'))


if __name__ == '__main__':
    unittest.main()

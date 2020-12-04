import abc
import re

PASSPORT_REQUIRED_FIELDS = [
    'byr'   # (Birth Year)
    , 'iyr' # (Issue Year)
    , 'eyr' # (Expiration Year)
    , 'hgt' # (Height)
    , 'hcl' # (Hair Color)
    , 'ecl' # (Eye Color)
    , 'pid' # (Passport ID)
]
PASSPORT_OPTIONAL_FIELDS = [
    'cid' # (Country ID)
]

VALID_YEAR_PATTERN       = re.compile('[0-9]{4}')
VALID_HEIGHT_PATTERN     = re.compile('[0-9]{2,3}(cm|in)')
VALID_HAIR_COLOR_PATTERN = re.compile('#[0-9a-f]{6}')
VALID_PID_PATTERN        = re.compile('^[0-9]{9}$')
VALID_EYE_COLORS         = [
    'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
]



class Passport:
    passport_fields: dict

    def __init__(self, raw_str):
        raw_str  = raw_str.replace('\n', ' ')
        raw_keys = raw_str.split(' ')
        self.passport_fields = {}

        for entry in raw_keys:
            entry = entry.split(':')
            self.passport_fields[entry[0]] = entry[1]

    def has_required_fields(self) -> bool:
        for field in PASSPORT_REQUIRED_FIELDS:
            if field not in self.passport_fields:
                return False

        return True

    @staticmethod
    def validate_birth_year(byr: str) -> bool:
        if not re.match(VALID_YEAR_PATTERN, byr):
            return False

        if 1920 <= int(byr) <= 2002:
            return True

        return False

    @staticmethod
    def validate_issue_year(iyr: str) -> bool:
        if not re.match(VALID_YEAR_PATTERN, iyr):
            return False

        if 2010 <= int(iyr) <= 2020:
            return True

        return False

    @staticmethod
    def validate_expiration(eyr: str) -> bool:
        if not re.match(VALID_YEAR_PATTERN, eyr):
            return False

        if 2020 <= int(eyr) <= 2030:
            return True

        return False

    @staticmethod
    def validate_height(hgt: str) -> bool:
        if not re.match(VALID_HEIGHT_PATTERN, hgt):
            return False

        num_value = int(hgt[:-2])
        unit      = hgt[-2:]

        if unit == 'cm' and 150 <= num_value <= 193:
            return True
        elif unit == 'in' and 59 <= num_value <= 76:
            return True
        else:
            return False

    @staticmethod
    def validate_hair_color(hcl: str) -> bool:
        if re.match(VALID_HAIR_COLOR_PATTERN, hcl):
            return True
        else:
            return False

    @staticmethod
    def validate_eye_color(ecl: str) -> bool:
        if ecl in VALID_EYE_COLORS:
            return True
        else:
            return False

    @staticmethod
    def validate_pid(pid: str) -> bool:
        if re.match(VALID_PID_PATTERN, pid):
            return True
        return False

    def validate_passport(self, validate_fields: bool = False) -> bool:
        if not self.has_required_fields():
            return False

        if validate_fields:
            if not self.validate_birth_year(self.passport_fields['byr']):
                return False
            if not self.validate_issue_year(self.passport_fields['iyr']):
                return False
            if not self.validate_expiration(self.passport_fields['eyr']):
                return False
            if not self.validate_height(self.passport_fields['hgt']):
                return False
            if not self.validate_hair_color(self.passport_fields['hcl']):
                return False
            if not self.validate_eye_color(self.passport_fields['ecl']):
                return False
            if not self.validate_pid(self.passport_fields['pid']):
                return False

        return True


def read_passport_file(input_file):
    f_path = f'inputs/{input_file}'
    with open(f_path, 'r') as f:
        passports_raw_batch = f.read()

    ret = []
    passports_raw = passports_raw_batch.split('\n\n')
    for entry in passports_raw:
        ret.append(Passport(entry))

    return ret


if __name__ == '__main__':
    passports = read_passport_file('day04.txt')

    count_ans_1: int = 0
    count_ans_2: int = 0
    for passport in passports:
        if passport.validate_passport():
            count_ans_1 += 1
        if passport.validate_passport(validate_fields = True):
            count_ans_2 += 1

    print(f'Answer 1: {count_ans_1}')
    # 176 too high
    # 175 is the correct answer. Can't figure out why
    print(f'Answer 2: {count_ans_2}')

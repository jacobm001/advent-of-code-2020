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


class Passport:
    passport_fields: dict

    def __init__(self, raw_str):
        raw_str  = raw_str.replace('\n', '')
        raw_keys = raw_str.split(' ')
        self.passport_fields = {}

        for entry in raw_keys:
            entry = entry.split(':')
            self.passport_fields[entry[0]] = entry[1]

    def validate_passport(self):
        for field in PASSPORT_REQUIRED_FIELDS:
            if field not in self.passport_fields:
                return False

        return True


def read_passport_file(input_file):
    f_path = f'inputs/{input_file}'
    with open(f_path, 'r') as f:
        passports_raw_batch = f.read()

    passports = []
    passports_raw = passports.split('\n\n')
    for entry in passports_raw:
        passports.append(Passport(entry))


if __name__ == '__main__':
    # read_passport_file('day04.txt')
    p = Passport('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm')
    print(p.validate_passport())
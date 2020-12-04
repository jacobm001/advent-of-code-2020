

class Passport:
    passport_fields: dict

    def __init__(self, raw_str):
        raw_str  = raw_str.replace('\n', '')
        raw_keys = raw_str.split(' ')

        for entry in raw_keys:
            entry = entry.split(':')




def read_passport_file(input_file):
    f_path = f'inputs/{input_file}'
    with open(f_path, 'r') as f:
        passports_raw_batch = f.read()

    passports = []
    passports_raw = passports.split('\n\n')
    for p in passports:


if __name__ == '__main__':
    read_passport_file('day04.txt')
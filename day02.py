import re
from common import read_list

PASSWORD_PATTERN = re.compile('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')


class PasswordAuthenticator:
    minimum: int   = 0
    maximum: int   = 0
    character: str = ""
    password: str  = ""

    def __init__(self, input_line: str):
        match = re.match(PASSWORD_PATTERN, input_line)
        if match:
            self.minimum   = int(match.group(1))
            self.maximum   = int(match.group(2))
            self.character = match.group(3)
            self.password  = match.group(4)

    def validate_password_1(self) -> bool:
        """
        Returns true if the number of occurrences of the specified
        character is between the designated min and max.
        """
        count: int = self.password.count(self.character)

        if self.minimum <= count <= self.maximum:
            return True
        else:
            return False

    def validate_password_2(self) -> bool:
        """
        Returns true if the specified character is at either the min
        or max position
        """
        count: int = 0
        if self.password[self.minimum-1] == self.character:
            count += 1

        if self.password[self.maximum-1] == self.character:
            count += 1

        if count == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    input_file  = 'day02.txt'
    input_array = read_list(input_file, PasswordAuthenticator)

    valid_count_1 = 0
    valid_count_2 = 0
    for password in input_array:
        if password.validate_password_1():
            valid_count_1 += 1

        if password.validate_password_2():
            valid_count_2 += 1

    print(f'Answer 1: {valid_count_1} valid passwords')
    print(f'Answer 2: {valid_count_2} valid passwords')

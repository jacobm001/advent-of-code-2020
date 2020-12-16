from typing import List, Tuple
import re
import common


FIELD_PATTERN = re.compile(r'^([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$')


Ticket  = List[int]
Tickets = List[Ticket]


class Field:
    name: str
    ranges: List[Tuple]

    def __init__(self, name: str, ranges: List[Tuple]):
        self.name   = name
        self.ranges = ranges

    def number_in_range(self, number: int) -> bool:
        for r in self.ranges:
            if r[0] <= number <= r[1]:
                return True

        return False


def parse_fields(field_input: List[str]) -> List[Field]:
    ret_fields = []

    for line in field_input.split('\n'):
        match = re.match(FIELD_PATTERN, line)
        if match:
            field_name: str  = match.group(1)
            ranges: List     = [
                (int(match.group(2)), int(match.group(3))), (int(match.group(4)), int(match.group(5)))
            ]
            new_field: Field = Field(field_name, ranges)

            ret_fields.append(new_field)

    return ret_fields


if __name__ == '__main__':
    # block 1: fields
    # block 2: my ticket
    # block 3: nearby tickets
    with open('inputs/day16.txt', 'r') as f:
        raw_input = f.read().split('\n\n')

    fields: List[Field] = parse_fields(raw_input[0])
    print(fields)



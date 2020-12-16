from typing import List, Tuple
import re
from itertools import permutations

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

    def __repr__(self):
        return f'Field: {self.name}'

    def number_in_range(self, number: int) -> bool:
        for r in self.ranges:
            if r[0] <= number <= r[1]:
                return True

        return False


def parse_fields(field_input: str) -> List[Field]:
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


def parse_my_ticket(my_ticket_input: str) -> Ticket:
    my_ticket_input = my_ticket_input.split('\n')
    return [int(t) for t in my_ticket_input[1].split(',')]


def parse_nearby_tickets(nearby_ticket_input: str) -> Tickets:
    nearby_ticket_input = nearby_ticket_input.split('\n')
    ret: Tickets = []

    for line in nearby_ticket_input[1:]:
        if line == "":
            continue

        ret.append([int(t) for t in line.split(',')])

    return ret


if __name__ == '__main__':
    # block 1: fields
    # block 2: my ticket
    # block 3: nearby tickets
    with open('inputs/day16-test.txt', 'r') as f:
        raw_input = f.read().split('\n\n')

    fields: List[Field]     = parse_fields(raw_input[0])
    my_ticket: Ticket       = parse_my_ticket(raw_input[1])
    nearby_tickets: Tickets = parse_nearby_tickets(raw_input[2])

    invalid_fields: List[int] = []
    # part 1
    for ticket in nearby_tickets:
        for entry in ticket:
            valid_field = False
            for field in fields:
                if field.number_in_range(entry):
                    valid_field = True

            if valid_field is False:
                invalid_fields.append(entry)

    answer1 = sum(invalid_fields)
    print(f'Answer1: {answer1}')

    # part 2
    # example should return
    #   row, class, seat
    num_fields: int = len(fields)
    for perm in permutations(fields):
        valid_perm: bool = True
        for i in range(len(nearby_tickets)):
            for j in range(num_fields):
                if perm[j].number_in_range(nearby_tickets[i][j]):
                    continue
                else:
                    valid_perm = False
                    break

            if not valid_perm:
                break

        if valid_perm:
            print(perm)

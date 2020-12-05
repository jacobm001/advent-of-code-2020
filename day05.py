import math
import re
import common

NUM_ROWS: int = 128
NUM_COLS: int = 8

TICKET_PATTERN: re.Pattern = re.compile('^([FB]+)([LR]+)$')


class TicketParser():
    seat_code: str
    seat_id: int
    assigned_row: int
    assigned_col: int

    def __init__(self, seat_str: str):
        self.seat_code = seat_str

        match = re.match(TICKET_PATTERN, seat_str)
        self.find_row(match.group(1))
        self.find_col(match.group(2))
        self.calc_seat_id()

    def find_row(self, row_code):
        min_row: int = 0
        max_row: int = NUM_ROWS - 1

        for i, letter in enumerate(row_code):
            if i == len(row_code) - 1:
                if letter == 'F':
                    self.assigned_row = min_row
                elif letter == 'B':
                    self.assigned_row = max_row

                return

            if letter == 'F':
                max_row = math.floor((max_row + min_row) / 2)
            elif letter == 'B':
                min_row = math.ceil((max_row + min_row) / 2)

    def find_col(self, col_code):
        min_col: int = 0
        max_col: int = NUM_COLS - 1

        for i, letter in enumerate(col_code):
            if i == len(col_code) - 1:
                if letter == 'L':
                    self.assigned_col = min_col
                elif letter == 'R':
                    self.assigned_col = max_col

                return

            if letter == 'L':
                max_col = math.floor((max_col + min_col) / 2)
            elif letter == 'R':
                min_col = math.ceil((max_col + min_col) / 2)

    def get_seat(self) -> tuple:
        return self.assigned_row, self.assigned_col

    def calc_seat_id(self):
        self.seat_id = self.assigned_row * 8 + self.assigned_col


if __name__ == "__main__":
    input_file   = 'day05.txt'
    ticket_codes = common.read_list(input_file, str)

    seat_ids = []
    for ticket_code in ticket_codes:
        t = TicketParser(ticket_code)
        seat_ids.append(t.seat_id)

    max_seat_id = max(seat_ids)
    print(f'Answer 1: {max_seat_id}')

    seat_ids.sort()
    my_seat_id: int = None
    for i, seat_id in enumerate(seat_ids):
        difference = seat_ids[i+1] - seat_id
        if difference > 1:
            my_seat_id = (seat_id + seat_ids[i+1]) // 2
            break

    print(f'Answer 2: {my_seat_id}')

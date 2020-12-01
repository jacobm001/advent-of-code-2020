""" Handles converting puzzle input to useable data structures"""


def file_to_int_array(f: str):
    path = f'inputs/{f}'
    with open(path, 'r') as f:
        raw_arr = f.readlines()

    arr = list(map(int, raw_arr))
    return arr

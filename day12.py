import common

if __name__ == '__main__':
    f = 'day12.txt'
    moves = common.read_list(f, str)
    ship = common.Boat()

    for move in moves:
        ship.move(move)

    answer1: int = ship.manhattan_distance()
    print(f'Answer 1: {answer1}')

    ship2 = common.WaywardBoat()

    for move in moves:
        ship2.move(move)

    answer2: int = ship2.manhattan_distance()
    print(f'Answer2: {answer2}')


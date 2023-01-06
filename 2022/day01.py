

def get_input() -> list[list[int]]:
    inputa: str
    with open('day01-inputa.txt', 'r') as f:
        inputa = f.read()

    # outer list-comprehension only results in a list[list[str]]
    # inner list-comprehension converts the innermost strings to ints
    ret: list[list[int]] = [[int(y) for y in x.split('\n')] for x in inputa.split('\n\n')]

    return ret


if __name__ == '__main__':
    elves = get_input()

    most_calories = max([sum(x) for x in elves])
    print('Answer 1: ', most_calories)

    elves_totaled: list[int] = [sum(x) for x in elves]
    top3_elves = sorted(elves_totaled, reverse=True)[0:3]
    print('Answer 2: ', sum(top3_elves))

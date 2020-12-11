from typing import List, Tuple
import collections
import common
from functools import lru_cache


def prep_list(il: List[int]):
    # sort values
    il.sort()

    # Add in our device's maximum rating
    device_max = il[-1] + 3
    il.append(device_max)

    # Add the leading 0 for the seat
    il = [0] + il

    return il


def get_differences(il: List[int]) -> collections.Counter:
    differences: List[int] = []

    for i in range(1, len(il)):
        diff = il[i] - il[i-1]
        differences.append(diff)

    return collections.Counter(differences)


# Now that I've discovered the miracle known as "memoization", I've altered my original solution to accept
# a tuple instead of a list. This allows the @lru_cache to cache the results in the provided dictionary.
#
# This function works by counting the branch endpoints. If the jolt variation is increased.
@lru_cache(None)
def count_branches(il: Tuple[int], count: int = 0):
    if len(il) == 1:
        return 1

    end = min(len(il), 4)
    for i in range(1, end):
        if il[i] - il[0] <= 3:
            count += count_branches(il[i:])

    return count


# When my above solution failed I figured the splicing was a bad idea
# and that it was clearly responsible for the slow down and my memory consumption.
#
# This is attempt two, which is an implementation of a tree. I figured this would be more efficient
# and that it might return in time. I was wrong. While this too produces the correct result, and is much faster
# than my previous solution, the result is that it uses all my RAM faster.
def part2_tree(il: List[int]):
    t = common.Tree()
    for i, entry in enumerate(il):
        for j in range(i + 1, len(il)):
            if il[j] - il[i] <= 3:
                t.add_node(il[i], il[j])
            else:
                break

    return t.count_ends()


# This is the result of me looking it up. I'm not even sorry.
# Update: As I've fixed my original implementation, this code is no longer needed, but I'm keeping it
#         here as it's cool.
# Source: https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfbo61q
#
# Explanation preserved here
# Logic: count all possible input paths into an adapter / node, start from wall,
# propagate the count up till the end of chain.
#
# - start from wall adapter (root node) with input count 1
# - add this count to the next 1, 2 or 3 adapters / nodes
# - add their input counts to next adapters / nodes
# - repeat this for all adapters (in sorted order)
# - you'll end up with input count for your device adapter
def count(il: List[int]) -> int:
    counter = collections.Counter({0: 1})
    for entry in il:
        counter[entry + 1] += counter[entry]
        counter[entry + 2] += counter[entry]
        counter[entry + 3] += counter[entry]

    return counter[max(il)]


def part1(il) -> int:
    difference_count = get_differences(il)
    return difference_count[1] * difference_count[3]


def part2(il) -> int:
    return count_branches(tuple(il))


if __name__ == '__main__':
    f = 'day10.txt'
    input_list: List[int] = common.read_list(f)
    input_list = prep_list(input_list)

    answer1: int = part1(input_list)
    print(f'Answer 1: {answer1}')

    answer2: int = part2(input_list)
    print(f'Answer 2: {answer2}')

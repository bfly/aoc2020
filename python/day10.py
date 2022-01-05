import collections
from functools import lru_cache


@lru_cache
def n_for_streak(n):
    assert n >= 2
    if n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4
    else:
        return n_for_streak(n - 1) + n_for_streak(n - 2) + n_for_streak(n - 3)


def part1(_numbers, ):
    n = 0
    counts = collections.Counter({3: 1})
    for number in sorted(_numbers):
        counts[number - n] += 1
        n = number
    return counts[1] * counts[3]


def part2(_numbers):
    prev, combos, streak = 0, 1, 1

    for n in _numbers:
        if n == prev + 1:
            streak += 1
        elif streak > 1:
            combos *= n_for_streak(streak)
            streak = 1
        prev = n

    if streak > 1:
        combos *= n_for_streak(streak)

    return combos


def main(_fn):
    with open('../day10/' + _fn) as fi:
        lines = fi.read()
    numbers = [int(line) for line in lines.splitlines()]

    print()
    print(f'Part 1: The 1-jolt differences times the 3-jolt differences is {part1(numbers)}.')
    print(f'Part 2: The number of distinct arrangements is {part2(sorted(numbers))}.')


if __name__ == '__main__':
    f = input('Press ENTER for test, m for medium, s to submit: ')
    if f == 's':
        fn = 'inputdata.txt'
    elif f == 'm':
        fn = 'mediumdata.txt'
    else:
        fn = 'smalldata.txt'
    main(fn)

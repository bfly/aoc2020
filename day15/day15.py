import collections
import re
from typing import NamedTuple, Tuple, Generator, Dict, List


def part1(_lines):
    prev_seen: Dict[int, List[int]] = collections.defaultdict(list)
    numbers = [int(n) for n in _lines.strip().split(',')]
    n = 0

    for turn in range(2020):
        if turn < len(numbers):
            n = numbers[turn]
        elif len(prev_seen[n]) == 1:
            n = 0
        else:
            n = prev_seen[n][-1] - prev_seen[n][-2]

        prev_seen[n].append(turn)

    return n


def part2(_lines):
    seen2: Dict[int, int] = {}
    seen1: Dict[int, int] = {}
    numbers = [int(n) for n in _lines.strip().split(',')]
    n = 0

    for turn in range(30_000_000):
        if turn < len(numbers):
            n = numbers[turn]
        elif n not in seen2:
            n = 0
        else:
            n = seen1[n] - seen2[n]

        if n in seen1:
            seen2[n] = seen1[n]
        seen1[n] = turn

    return n


def main(_fn):
    with open(_fn) as fi:
        lines = fi.read()
    print()

    print(f'Part 1: {part1(lines)}.')
    print(f'Part 2: {part2(lines)}.')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'

    main(fn)

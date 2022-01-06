from collections import Counter
from typing import Set, Tuple

test = True


DIV = 20201227


def get_loop_size(target: int) -> int:
    n = 1
    i = 0
    while n != target:
        n *= 7
        n %= 20201227
        i += 1
    return i


def transform(subject: int, loop: int) -> int:
    n = 1
    for _ in range(loop):
        n *= subject
        n %= 20201227
    return n


def part1(_lines):
    lines = _lines.strip().splitlines()
    card = int(lines[0])
    door = int(lines[1])
    return transform(card, get_loop_size(door))


def main(_fn):
    with open('../day25/' + _fn) as fi:
        lines = fi.read()

    print(f'Part 1: {part1(lines)}.')
    print()
    # print(f'Part 2: {part2(lines)}.')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'
    if f == 's':
        test = False

    main(fn)

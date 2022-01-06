from collections import Counter
from typing import Set, Tuple

test = True


DIRECTIONS = [
    (2, 0),
    (-2, 0),
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2)
]


def part1(_lines):
    black_tiles: Set[Tuple[int, int]] = set()

    for line in _lines.strip().splitlines():
        x = y = i = 0
        while i < len(line):
            if line.startswith('e', i):
                x += 2
                i += 1
            elif line.startswith('w', i):
                x += -2
                i += 1
            elif line.startswith('ne', i):
                x += 1
                y += 2
                i += 2
            elif line.startswith('nw', i):
                x += -1
                y += 2
                i += 2
            elif line.startswith('se', i):
                x += 1
                y += -2
                i += 2
            elif line.startswith('sw', i):
                x += -1
                y += -2
                i += 2
            else:
                raise AssertionError(line[i:])

        black_tiles ^= {(x, y)}

    return len(black_tiles)


def part2(_lines):
    black_tiles: Set[Tuple[int, int]] = set()

    for line in _lines.strip().splitlines():
        x = y = i = 0
        while i < len(line):
            if line.startswith('e', i):
                x += 2
                i += 1
            elif line.startswith('w', i):
                x += -2
                i += 1
            elif line.startswith('ne', i):
                x += 1
                y += 2
                i += 2
            elif line.startswith('nw', i):
                x += -1
                y += 2
                i += 2
            elif line.startswith('se', i):
                x += 1
                y += -2
                i += 2
            elif line.startswith('sw', i):
                x += -1
                y += -2
                i += 2
            else:
                raise AssertionError(line[i:])

        black_tiles ^= {(x, y)}

    for _ in range(100):
        counts: Counter[Tuple[int, int]] = Counter()
        for x, y in black_tiles:
            for dx, dy in DIRECTIONS:
                counts[(x + dx, y + dy)] += 1

        to_discard = set()
        for x, y in black_tiles:
            if counts[(x, y)] == 0 or counts[(x, y)] > 2:
                to_discard.add((x, y))

        to_add = set()
        for (x, y), count in counts.items():
            if count == 2 and (x, y) not in black_tiles:
                to_add.add((x, y))

        black_tiles -= to_discard
        black_tiles |= to_add

    return len(black_tiles)


def main(_fn):
    with open('../day24/' + _fn) as fi:
        lines = fi.read()

    print(f'Part 1: {part1(lines)}.')
    print()
    print(f'Part 2: {part2(lines)}.')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'
    if f == 's':
        test = False

    main(fn)

from collections import Counter
from typing import Tuple


def part1(_lines):
    space = {}
    for y, line in enumerate(_lines.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                space[(0, y, x)] = c

    for _ in range(6):
        marked: Counter[Tuple[int, int, int]] = Counter()

        for (z, y, x), c in space.items():
            for z_i in (-1, 0, 1):
                for y_i in (-1, 0, 1):
                    for x_i in (-1, 0, 1):
                        if z_i == y_i == x_i == 0:
                            continue
                        marked[(z + z_i, y + y_i, x + x_i)] += 1

        new_space = {}
        for k, v in marked.items():
            if v == 3:
                new_space[k] = '#'

        for k in space:
            if marked[k] in {2, 3}:
                new_space[k] = '#'

        space = new_space

    return len(space)


def part2(_lines):
    space = {}
    for y, line in enumerate(_lines.splitlines()):
        for x, c in enumerate(line):
            if c == '#':
                space[(0, 0, y, x)] = c

    for _ in range(6):
        marked: Counter[Tuple[int, int, int, int]] = Counter()

        for (w, z, y, x), c in space.items():
            for w_i in (-1, 0, 1):
                for z_i in (-1, 0, 1):
                    for y_i in (-1, 0, 1):
                        for x_i in (-1, 0, 1):
                            if w_i == z_i == y_i == x_i == 0:
                                continue
                            marked[(w + w_i, z + z_i, y + y_i, x + x_i)] += 1

        new_space = {}
        for k, v in marked.items():
            if v == 3:
                new_space[k] = '#'

        for k in space:
            if marked[k] in {2, 3}:
                new_space[k] = '#'

        space = new_space

    return len(space)


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

import collections
from typing import Optional, Tuple, Generator, Counter


def _index(lines: Tuple[str, ...], y: int, x: int) -> str:
    if y < 0 or y >= len(lines) or \
       x < 0 or x >= len(lines[0]):
        return ' '
    return lines[y][x]


def _adjacent(lines: Tuple[str, ...], y: int, x: int) -> Tuple[str, ...]:
    def _inner() -> Generator[str, None, None]:
        for y_i in range(y - 1, y + 2):
            for x_i in range(x - 1, x + 2):
                if (y_i, x_i) != (y, x):
                    yield _index(lines, y_i, x_i)

    return tuple(_inner())


def part1(_lines, ):
    lines = tuple(_lines.splitlines())

    prev: Optional[Tuple[str, ...]] = None
    while lines != prev:
        prev = lines

        new_lines = []
        for y, line in enumerate(lines):
            line_c = []
            for x, c in enumerate(line):
                if c == 'L':
                    if _adjacent(lines, y, x).count('#') == 0:
                        line_c.append('#')
                    else:
                        line_c.append('L')
                elif c == '#':
                    if _adjacent(lines, y, x).count('#') >= 4:
                        line_c.append('L')
                    else:
                        line_c.append('#')
                else:
                    line_c.append(c)

            new_lines.append(''.join(line_c))

        lines = tuple(new_lines)

    return sum(line.count('#') for line in lines)


def part2(_lines):
    lines = tuple(_lines.splitlines())

    prev: Optional[Tuple[str, ...]] = None
    while lines != prev:
        prev = lines

        dct: Counter[Tuple[int, int]] = collections.Counter()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    for d_y, d_x in (
                            (0, 1),
                            (0, -1),
                            (1, 0),
                            (-1, 0),
                            (1, 1),
                            (-1, -1),
                            (1, -1),
                            (-1, 1),
                    ):
                        y_i, x_i = y + d_y, x + d_x
                        c = _index(lines, y_i, x_i)
                        while c not in 'L# ':
                            y_i, x_i = y_i + d_y, x_i + d_x
                            c = _index(lines, y_i, x_i)
                        if c != ' ':
                            dct[(y_i, x_i)] += 1

        new_lines = []
        for y, line in enumerate(lines):
            line_c = []
            for x, c in enumerate(line):
                if c == 'L':
                    if dct[(y, x)] == 0:
                        line_c.append('#')
                    else:
                        line_c.append('L')
                elif c == '#':
                    if dct[(y, x)] >= 5:
                        line_c.append('L')
                    else:
                        line_c.append('#')
                else:
                    line_c.append(c)

            new_lines.append(''.join(line_c))

        lines = tuple(new_lines)

    return sum(line.count('#') for line in lines)


def main(_fn):
    with open(_fn) as fi:
        lines = fi.read()

    print()
    print(f'Part 1: There are {part1(lines)} unoccupied seats.')
    print(f'Part 2: There are {part2(lines)} unoccupied seats.')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'

    main(fn)

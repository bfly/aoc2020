import collections
import re
from typing import NamedTuple, Tuple, Generator, Dict, List


class Mask(NamedTuple):
    ones_mask: int
    x_masks: Tuple[Tuple[int, int], ...]

    def targets(self, number: int) -> Generator[int, None, None]:
        number = number | self.ones_mask
        for x_mask_or, x_mask_and in self.x_masks:
            yield (number | x_mask_or) & x_mask_and


def parse_mask(_lines: str) -> Mask:
    one_mask = int(_lines.replace('X', '0'), 2)
    xs = [match.start() for match in re.finditer('X', _lines)]
    x_masks = []
    for i in range(1 << len(xs)):
        number_or, number_and = 0, -1
        for j in range(len(xs)):
            bit = (i & (1 << j)) >> j
            if bit:
                number_or |= 1 << (len(_lines) - 1 - xs[j])
            else:
                number_and &= ~(1 << (len(_lines) - 1 - xs[j]))
        x_masks.append((number_or, number_and))
    return Mask(one_mask, tuple(x_masks))


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

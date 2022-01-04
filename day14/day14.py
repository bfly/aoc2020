import collections
import re
from typing import NamedTuple, Tuple, Generator

MEM_RE = re.compile(r'^mem\[(\d+)] = (\d+)$')

INPUT_V2 = '''\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''


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


def part1(_lines, ):
    memory = collections.defaultdict(int)
    mask_or, mask_and = 0, -1

    for line in _lines.splitlines():
        if line.startswith('mask'):
            _, _, mask_s = line.partition(' = ')
            mask_or = int(mask_s.replace('X', '0'), 2)
            mask_and = int(mask_s.replace('X', '1'), 2)
        else:
            match = MEM_RE.match(line)
            assert match
            target, number = int(match[1]), int(match[2])
            masked = (number | mask_or) & mask_and
            memory[target] = masked

    return sum(memory.values())


def part2(_lines):
    memory = collections.defaultdict(int)
    mask = Mask(-1, ())
    for line in _lines.splitlines():
        if line.startswith('mask'):
            _, _, mask_s = line.partition(' = ')
            mask = parse_mask(mask_s)
        else:
            match = MEM_RE.match(line)
            assert match
            target, number = int(match[1]), int(match[2])

            for target in mask.targets(target):
                memory[target] = number

    return sum(memory.values())


def main(_fn):
    with open(_fn) as fi:
        lines = fi.read()
    print()

    print(f'Part 1: {part1(lines)}.')
    if _fn == 'smalldata.txt':
        lines = INPUT_V2
    print(f'Part 2: {part2(lines)}.')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'

    main(fn)

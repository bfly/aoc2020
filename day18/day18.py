import re
from re import Match

ans1 = [71, 51, 26, 437, 12240, 13632]
res1 = []
ans2 = [231, 51, 46, 1445, 669060, 23340]
res2 = []
test = True

ADD_RE = re.compile(r'(\d+) \+ (\d+)')
PAREN_RE = re.compile(r'\(([^()]+)\)')


def replace_add(match: Match[str]) -> str:
    return str(int(match[1]) + int(match[2]))


def compute_part_replace2(match: Match[str]) -> str:
    return str(compute_part2(match[1]))


def compute_part2(_lines: str) -> int:
    while ADD_RE.search(_lines):
        _lines = ADD_RE.sub(replace_add, _lines)

    parts = _lines.split()
    n = int(parts[0])

    i = 1
    while i < len(parts):
        op = parts[i]
        val = int(parts[i + 1])

        if op == '+':
            n += val
        elif op == '*':
            n *= val
        else:
            raise AssertionError(n, op, val)

        i += 2
    return n


def compute_part_replace1(match: Match[str]) -> str:
    return str(compute_part1(match[1]))


def compute_part1(_lines: str) -> int:
    parts = _lines.split()
    n = int(parts[0])

    i = 1
    while i < len(parts):
        op = parts[i]
        val = int(parts[i + 1])

        if op == '+':
            n += val
        elif op == '*':
            n *= val
        else:
            raise AssertionError(n, op, val)

        i += 2
    return n


def part1(_lines):
    total = 0

    for line in _lines.splitlines():
        print(f'{line} -> ', end='')
        while PAREN_RE.search(line):
            line = PAREN_RE.sub(compute_part_replace1, line)

        res = compute_part1(line)
        res1.append(res)
        print(f'{res}')
        total += res

    return total


def part2(_lines):
    total = 0

    for line in _lines.splitlines():
        print(f'{line} -> ', end='')
        while PAREN_RE.search(line):
            line = PAREN_RE.sub(compute_part_replace2, line)

        res = compute_part2(line)
        res2.append(res)
        print(f'{res}')
        total += res

    return total


def main(_fn):
    with open(_fn) as fi:
        lines = fi.read()

    print(f'Part 1: {part1(lines)}.')
    if test:
        for i, res in enumerate(res1):
            if res != ans1[i]:
                print(f'{i + 1}: {res} not = {ans1[i]}')
    print()
    print(f'Part 2: {part2(lines)}.')
    if test:
        for i, res in enumerate(res2):
            if res != ans2[i]:
                print(f'{i + 1}: {res} not = {ans2[i]}')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'
    if f == 's':
        test = False

    main(fn)

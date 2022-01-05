import re

test = True


def part1(_lines):
    rules, lines = _lines.split('\n\n')

    rules_s = {}
    for line in rules.splitlines():
        k, _, v = line.partition(': ')
        rules_s[k] = v

    def _get_re(s: str) -> str:
        if s == '|':
            return s

        rule_s = rules_s[s]
        if rule_s.startswith('"'):
            return rule_s.strip('"')
        else:
            return f'({"".join(_get_re(part) for part in rule_s.split())})'

    ret = re.compile(_get_re('0'))

    return sum(bool(ret.fullmatch(line)) for line in lines.splitlines())


def part2(_lines):
    rules, lines = _lines.split('\n\n')

    rules_s = {}
    for line in rules.splitlines():
        k, _, v = line.partition(': ')
        rules_s[k] = v

    def _get_re(s: str) -> str:
        if s == '|':
            return s

        rule_s = rules_s[s]
        if rule_s.startswith('"'):
            return rule_s.strip('"')
        else:
            return f'({"".join(_get_re(part) for part in rule_s.split())})'

    re_42 = re.compile(_get_re('42'))
    re_31 = re.compile(_get_re('31'))

    count = 0
    for line in lines.splitlines():
        pos = 0

        count_42 = 0
        while match := re_42.match(line, pos):
            count_42 += 1
            pos = match.end()

        count_31 = 0
        while match := re_31.match(line, pos):
            count_31 += 1
            pos = match.end()

        if 0 < count_31 < count_42 and pos == len(line):
            count += 1

    return count


def main(_fn):
    with open('../day19/' + _fn) as fi:
        lines = fi.read()

    print(f'Part 1: {part1(lines)}.')
    print()
    if not test:
        print(f'Part 2: {part2(lines)}.')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'
    if f == 's':
        test = False

    main(fn)

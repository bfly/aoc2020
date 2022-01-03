BINARY = 2


def part1(_lines):
    counts = 0
    for line in _lines.split('\n\n'):
        counts += len(set(line) - {' ', '\n'})
    return counts


def part2(_lines):
    counts = 0
    for group in _lines.split('\n\n'):
        lines = group.splitlines()
        all_counted = set(lines[0])
        for other in lines[1:]:
            all_counted &= set(other)
        counts += len(all_counted)
    return counts


def main(_fn):
    with open(_fn) as fi:
        lines = fi.read()

    print(f'Part 1: Sum of yes answers is {part1(lines)}.')
    print(f'Part 2: Sum of yes answers is {part2(lines)}.')


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    print()
    main(fn)

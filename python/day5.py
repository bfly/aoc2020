BINARY = 2


def part1(_lines):
    maximum = 0
    for line in _lines:
        line = line.replace('F', '0').replace('B', '1')
        line = line.replace('R', '1').replace('L', '0')
        maximum = max(maximum, int(line, BINARY))
    return maximum


def part2(_lines):
    possible = set(range(1024))
    for line in _lines:
        line = line.replace('F', '0').replace('B', '1')
        line = line.replace('R', '1').replace('L', '0')
        possible.discard(int(line, BINARY))

    for candidate in possible:
        if candidate - 1 not in possible and candidate + 1 not in possible:
            return candidate
    else:
        return -1


def main(_fn):
    with open('../day5/' + _fn) as fi:
        lines = fi.read().splitlines()

    print(f'Part 1: Maximum value is {part1(lines)}')
    print(f'Part 2: Your seat id is {part2(lines)}.')


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    print()
    main(fn)

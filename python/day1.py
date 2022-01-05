def part1(_lines):
    ans = 0
    compls = set()

    for x in _lines:
        x = int(x)
        y = 2020 - x

        if x in compls:
            ans = x * y
            break

        compls.add(y)
    return ans


def part2(_lines):
    ans = 0
    for i, x in enumerate(_lines):
        x = int(x)
        compls = set()
        yz = 2020 - x

        for y in _lines[i + 1:]:
            y = int(y)
            z = yz - y

            if y in compls:
                ans = x * y * z
                break

            compls.add(z)
    return ans


def main(_fn):
    with open('../day1/' + _fn) as fi:
        lines = fi.read().splitlines()

    print(f'Part 1: {part1(lines)}')  # answer of part one

    print(f'Part 2: {part2(lines)}')  # answer of part two


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    print()
    main(fn)

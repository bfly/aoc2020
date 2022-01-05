def downslope(_lines, _right, _down):
    height = len(_lines)
    width = len(_lines[0])
    count = 0
    y = 0
    for x in range(0, height, _down):
        if _lines[x][y % width] == '#':
            count += 1
        y += _right
    return count


def part1(_lines):
    right, down = 3, 1
    trees = downslope(_lines, right, down)
    print(f'Part 1: {right=}, {down=}, {trees=}')
    print()


def part2(_lines):
    slope = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    product = 1
    for right, down in slope:
        trees = downslope(_lines, right, down)
        print(f'\t\t{right=}, {down=}, {trees=}')
        product *= trees

    print(f'Part 2: {product=}')


def main(_fn):
    with open('../day3/' + _fn) as fi:
        lines = fi.read().splitlines()
    part1(lines)
    part2(lines)


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    print()
    main(fn)

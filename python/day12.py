DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def part1(_lines, ):
    x, y, direction = 0, 0, (0, 1)

    for line in _lines.splitlines():
        d, n = line[0], int(line[1:])

        if d == 'N':
            y -= n
        elif d == 'S':
            y += n
        elif d == 'E':
            x += n
        elif d == 'W':
            x -= n
        elif d == 'L':
            rotations = n // 90
            ind = DIRECTIONS.index(direction)
            direction = DIRECTIONS[(ind - rotations) % 4]
        elif d == 'R':
            rotations = n // 90
            ind = DIRECTIONS.index(direction)
            direction = DIRECTIONS[(ind + rotations) % 4]
        elif d == 'F':
            y += n * direction[0]
            x += n * direction[1]
        else:
            raise NotImplementedError

    return abs(x) + abs(y)


def part2(_lines):
    s_y, s_x, w_y, w_x = 0, 0, 1, 10

    for line in _lines.splitlines():
        d, n = line[0], int(line[1:])

        if d == 'N':
            w_y += n
        elif d == 'S':
            w_y -= n
        elif d == 'E':
            w_x += n
        elif d == 'W':
            w_x -= n
        elif d == 'L':
            for i in range(n // 90):
                w_y, w_x = w_x, w_y
                w_x *= -1
        elif d == 'R':
            for i in range(n // 90):
                w_y, w_x = w_x, w_y
                w_y *= -1
        elif d == 'F':
            s_y += w_y * n
            s_x += w_x * n
        else:
            raise NotImplementedError

    return abs(s_x) + abs(s_y)


def main(_fn):
    with open('../day12/' + _fn) as fi:
        lines = fi.read()

    print()
    print(f'Part 1: The Manhattan distance is {part1(lines)}.')
    print(f'Part 2: The Manhattan distance is {part2(lines)}.')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'

    main(fn)

from sympy.ntheory.modular import crt

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def part1(_lines, ):
    lines = _lines.splitlines()
    start_time = int(lines[0])

    busses = [int(s) for s in lines[1].split(',') if s != 'x']

    minimum = busses[0] * (start_time // busses[0] + 1)
    bus_id = busses[0]
    for bus in busses[1:]:
        n = start_time // bus
        depart_time = bus * (n + 1)
        if depart_time < minimum:
            minimum = depart_time
            bus_id = bus
    return bus_id * (minimum - start_time)


def part2(_lines):
    lines = _lines.splitlines()
    parsed = [
        (int(s), i)
        for i, s in enumerate(lines[1].split(','))
        if s != 'x'
    ]
    buses = [pt[0] for pt in parsed]
    mods = [-1 * pt[1] for pt in parsed]

    return crt(buses, mods)[0]


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

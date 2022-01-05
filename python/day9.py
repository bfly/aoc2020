import itertools


def part1(_numbers, n):
    seen = []
    for i, number in enumerate(_numbers):
        if i >= n:
            prev_25 = seen[-n:]
            for x, y in itertools.combinations(prev_25, 2):
                if x + y == number:
                    break
            else:
                return number
        seen.append(number)

    raise NotImplementedError('unreachable')


def part2(numbers, n=25):
    target = part1(numbers, n=n)

    start, end = 0, 0
    current = numbers[0]

    while True:
        if current < target:
            end += 1
            current += numbers[end]
        elif current > target:
            current -= numbers[start]
            start += 1
        else:
            r = numbers[start:end + 1]
            return min(r) + max(r)


def main(_fn, _n):
    with open('../day9/' + _fn) as fi:
        lines = fi.read()
    numbers = [int(line) for line in lines.splitlines()]

    print()
    print(f'Part 1: The value is {part1(numbers, n=_n)}.')
    print(f'Part 2: The value is {part2(numbers, n=_n)}.')


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    preamble = 25 if fn == 'inputdata.txt' else 5
    main(fn, preamble)

from typing import List, Tuple

FLIP = {'nop': 'jmp', 'jmp': 'nop'}


def run(code: List[Tuple[str, int]], flip: int) -> int:
    visited = set()
    n = 0
    pc = 0
    while pc not in visited and pc < len(code):
        visited.add(pc)
        opc, value = code[pc]

        if pc == flip:
            opc = FLIP[opc]

        if opc == 'acc':
            n += value
            pc += 1
        elif opc == 'jmp':
            pc += value
        elif opc == 'nop':
            pc += 1
        else:
            raise NotImplementedError(opc)

    if pc == len(code):
        return n
    else:
        raise RuntimeError(visited)


def part1(_lines):
    code = []
    for line in _lines.splitlines():
        opc, n_s = line.split()
        n = int(n_s)
        code.append((opc, n))

    visited = set()
    n = 0
    pc = 0
    while pc not in visited:
        visited.add(pc)
        opc, value = code[pc]
        if opc == 'acc':
            n += value
            pc += 1
        elif opc == 'jmp':
            pc += value
        elif opc == 'nop':
            pc += 1
        else:
            raise NotImplementedError(opc)

    return n


def part2(_lines):
    code = []
    for line in _lines.splitlines():
        opc, n_s = line.split()
        n = int(n_s)
        code.append((opc, n))

    try:
        run(code, -1)
    except RuntimeError as e:
        visited, = e.args
    else:
        raise AssertionError('unreachable')

    for i in visited:
        if code[i][0] in {'nop', 'jmp'}:
            try:
                return run(code, i)
            except RuntimeError:
                pass

    raise NotImplementedError('wat')


def main(_fn):
    with open(_fn) as fi:
        lines = fi.read()

    print(f'Part 1: The value in the accumulator is {part1(lines)}.')
    print(f'Part 2: The value in the accumulator after the program terminates is {part2(lines)}.')


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    print()
    main(fn)

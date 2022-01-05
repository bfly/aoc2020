import re

FIELD_RE = re.compile(r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)$')


def part1(_lines):
    x = _lines.split('\n\n')
    print(x)
    # fields, my_ticket, nearby = _lines.split('\n\n')

    field_ranges = {}
    for line in fields.splitlines():
        m = FIELD_RE.match(line)
        assert m
        field_ranges[m[1]] = (int(m[2]), int(m[3]), int(m[4]), int(m[5]))

    invalid = 0
    for line in nearby.splitlines()[1:]:
        for n_s in line.split(','):
            n = int(n_s)
            for b1, e1, b2, e2 in field_ranges.values():
                if b1 <= n <= e1 or b2 <= n <= e2:
                    break
            else:
                invalid += n

    return invalid


def part2(_lines):
    fields, my_ticket, nearby = _lines.split('\n\n')

    field_ranges = {}
    for line in fields.splitlines():
        m = FIELD_RE.match(line)
        assert m
        field_ranges[m[1]] = (int(m[2]), int(m[3]), int(m[4]), int(m[5]))

    my_ticket_n = [int(n_s) for n_s in my_ticket.splitlines()[1].split(',')]

    valid_tickets = []
    for line in nearby.splitlines()[1:]:
        ticket = [int(n_s) for n_s in line.split(',')]
        for n in ticket:
            for b1, e1, b2, e2 in field_ranges.values():
                if b1 <= n <= e1 or b2 <= n <= e2:
                    break
            else:
                break
        else:
            valid_tickets.append(ticket)

    possible_at_position = {
        pos: {
            k for k, (b1, e1, b2, e2) in field_ranges.items()
            if all(
                b1 <= ticket[pos] <= e1 or b2 <= ticket[pos] <= e2
                for ticket in valid_tickets
            )
        }
        for pos in range(len(valid_tickets[0]))
    }

    positions = {}
    while possible_at_position:
        for k, v in tuple(possible_at_position.items()):
            if len(v) == 1:
                key, = v
                positions[key] = k
                possible_at_position.pop(k)
                for _v in possible_at_position.values():
                    _v.discard(key)

    ret = 1
    for key, pos in positions.items():
        if key.startswith('departure '):
            ret *= my_ticket_n[pos]

    return ret


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

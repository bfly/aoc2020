import collections
import re

BINARY = 2
PATTERN = re.compile('^([^ ]+ [^ ]+) bags contain (.*)$')
BAG_RE = re.compile(r'(\d+) ([^ ]+ [^ ]+)')


def part1(_lines):
    parents = collections.defaultdict(list)
    for line in _lines.splitlines():
        match = PATTERN.match(line)
        assert match
        k = match[1]
        targets = [(int(n), tp) for n, tp in BAG_RE.findall(match[2])]
        for _, color in targets:
            parents[color].append(k)

    total_colors = set()
    todo = parents['shiny gold']
    while todo:
        color = todo.pop()
        if color not in total_colors:
            total_colors.add(color)
            todo.extend(parents[color])

    return len(total_colors)


def part2(_lines):
    colors = {}
    for line in _lines.splitlines():
        match = PATTERN.match(line)
        assert match
        k = match[1]
        targets = [(int(n), tp) for n, tp in BAG_RE.findall(match[2])]
        colors[k] = targets

    total_bags = 0
    todo = [(1, 'shiny gold')]
    while todo:
        n, color = todo.pop()
        total_bags += n
        for n_i, color_i in colors[color]:
            todo.append((n * n_i, color_i))

    total_bags -= 1
    return total_bags


def main(_fn):
    with open('../day7/' + _fn) as fi:
        lines = fi.read()

    print(f'Part 1: The number of bag colors that eventually contain at least one shiny gold bag is {part1(lines)}.')
    print(f'Part 2: A shiny gold bag must contain {part2(lines)} other bags.')


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    print()
    main(fn)

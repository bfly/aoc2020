import collections

test = True


class Node:
    def __init__(self, n: int) -> None:
        self.n = n
        self.next_node = self

    def __repr__(self) -> str:
        numbers = [self.n]
        next_node = self.next_node
        while next_node is not self:
            numbers.append(next_node.n)
            next_node = next_node.next_node
        return f'{type(self).__name__}({numbers!r})'

    def append(self, n: int):
        new_node = type(self)(n)
        new_node.next_node = self.next_node
        self.next_node = new_node
        return self.next_node

    def pop3(self):
        ret = self.next_node
        self.next_node = self.next_node.next_node.next_node.next_node
        return ret

    def push3(self, node3) -> None:
        node3.next_node.next_node.next_node = self.next_node
        self.next_node = node3


def part1(_lines):
    cups = collections.deque(int(n) for n in list(_lines.strip()))
    maximum = max(cups)

    for _ in range(100):
        current = cups[0]
        cups.rotate(-1)
        taken = [cups.popleft() for _ in range(3)]

        current_label = (current - 1)
        if current_label == 0:
            current_label = maximum
        while current_label in taken:
            current_label = (current_label - 1)
            if current_label == 0:
                current_label = maximum

        idx = cups.index(current_label)
        cups.rotate(-1 * idx - 1)
        cups.extend(taken)
        cups.rotate(idx + 3 + 1)

    cups.rotate(-cups.index(1))
    cups.popleft()
    return int(''.join(str(n) for n in cups))


def part2(_lines):
    numbers = [int(n) for n in list(_lines.strip())]

    nodes = {}
    nodes[numbers[0]] = current = Node(numbers[0])
    appender = current
    for number in numbers[1:]:
        nodes[number] = appender = appender.append(number)

    N = 1_000_000

    for i in range(len(numbers) + 1, N + 1):
        nodes[i] = appender = appender.append(i)

    for i in range(N * 10):
        taken = current.pop3()
        taken_n = {taken.n, taken.next_node.n, taken.next_node.next_node.n}

        current_label = (current.n - 1)
        if current_label == 0:
            current_label = N
        while current_label in taken_n:
            current_label = (current_label - 1)
            if current_label == 0:
                current_label = N

        nodes[current_label].push3(taken)

        current = current.next_node

    return nodes[1].next_node.n * nodes[1].next_node.next_node.n


def main(_fn):
    with open('../day23/' + _fn) as fi:
        lines = fi.read()

    print(f'Part 1: {part1(lines)}.')
    print()
    print(f'Part 2: {part2(lines)}.')


if __name__ == '__main__':
    f = input('Press ENTER for test, s to submit: ')
    fn = 'inputdata.txt' if f == 's' else 'smalldata.txt'
    if f == 's':
        test = False

    main(fn)

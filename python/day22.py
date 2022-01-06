import collections
import itertools
from typing import Deque, Tuple

test = True


def play_game(
        player1: Deque[int],
        player2: Deque[int],
) -> Tuple[bool, Deque[int]]:
    seen = set()

    while True:
        if player1 and not player2:
            return True, player1
        elif player2 and not player1:
            return False, player2

        gamestate = (tuple(player1), tuple(player2))
        if gamestate in seen:
            return True, player1

        c1, c2 = player1.popleft(), player2.popleft()
        if c1 <= len(player1) and c2 <= len(player2):
            sub_p1 = collections.deque(itertools.islice(player1, c1))
            sub_p2 = collections.deque(itertools.islice(player2, c2))
            player1_won, _ = play_game(sub_p1, sub_p2)
            if player1_won:
                player1.extend((c1, c2))
            else:
                player2.extend((c2, c1))
        elif c1 > c2:
            player1.extend((c1, c2))
        else:
            player2.extend((c2, c1))

        seen.add(gamestate)


def part1(_lines):
    player1_s, player2_s = _lines.strip().split('\n\n')

    player1: Deque[int] = collections.deque()
    for line in player1_s.splitlines()[1:]:
        player1.append(int(line))
    player2: Deque[int] = collections.deque()
    for line in player2_s.splitlines()[1:]:
        player2.append(int(line))

    while player1 and player2:
        n1, n2 = player1.popleft(), player2.popleft()
        if n1 > n2:
            player1.extend((n1, n2))
        else:
            player2.extend((n2, n1))

    total = 0
    if player1:
        for i, el in enumerate(reversed(player1), 1):
            total += i * el
    else:
        for i, el in enumerate(reversed(player2), 1):
            total += i * el

    return total


def part2(_lines):
    player1_s, player2_s = _lines.strip().split('\n\n')

    player1: Deque[int] = collections.deque()
    for line in player1_s.splitlines()[1:]:
        player1.append(int(line))
    player2: Deque[int] = collections.deque()
    for line in player2_s.splitlines()[1:]:
        player2.append(int(line))

    _, result = play_game(player1, player2)

    total = 0
    for i, el in enumerate(reversed(result), 1):
        total += i * el

    return total


def main(_fn):
    with open('../day22/' + _fn) as fi:
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

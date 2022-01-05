import collections
import functools
import math
import re
from typing import NamedTuple, FrozenSet, Generator

test = True
DARGON_RE0 = re.compile('(?=                  # )'.replace(' ', '.'))
DARGON_RE1 = re.compile('#    ##    ##    ###'.replace(' ', '.'))
DARGON_RE2 = re.compile(' #  #  #  #  #  #   '.replace(' ', '.'))


class Edges(NamedTuple):
    top: str
    right: str
    bottom: str
    left: str


class Tile1(NamedTuple):
    tile_id: int
    edges: FrozenSet[str]
    back_edges: FrozenSet[str]


class Tile2:
    def __init__(self, tile_id: int, lines: tuple[str, ...]) -> None:
        self.tile_id = tile_id
        self.lines = lines

    @functools.cached_property
    def edges(self) -> Edges:
        return Edges(
            self.lines[0],
            ''.join(line[-1] for line in self.lines),
            self.lines[-1],
            ''.join(line[0] for line in self.lines),
        )

    @functools.cached_property
    def back_edges(self) -> tuple[str, ...]:
        return tuple(edge[::-1] for edge in self.edges)

    @functools.cached_property
    def inner_parts(self) -> tuple[str, ...]:
        return tuple(line[1:-1] for line in self.lines[1:-1])

    def rotate(self):
        line_len = len(self.lines[0])
        lines = tuple(
            ''.join(self.lines[line_len - 1 - j][i] for j in range(line_len))
            for i in range(line_len)
        )
        return type(self)(self.tile_id, lines)

    def flip(self):
        lines = tuple(line[::-1] for line in self.lines)
        return type(self)(self.tile_id, lines)

    def possible(self) -> Generator[Tile1, None, None]:
        tile = self
        yield tile
        for i in range(3):
            tile = tile.rotate()
            yield tile
        tile = tile.flip()
        yield tile
        for i in range(3):
            tile = tile.rotate()
            yield tile

    def __repr__(self) -> str:
        lines_r = '\n        '.join(repr(line) for line in self.lines)
        return (
            f'{type(self).__name__}(\n'
            f'    tile_id={self.tile_id},\n'
            f'    lines=(\n'
            f'        {lines_r}\n'
            f'    ),\n'
            f')'
        )


def _first_corner(tiles: dict[int, Tile2]) -> Tile2:
    for i, tile in enumerate(tiles.values()):
        matched_edges = set()
        for j, other in enumerate(tiles.values()):
            if i == j:
                continue
            for e_i, edge in enumerate(tile.edges):
                for other_edge in other.edges:
                    if edge == other_edge:
                        matched_edges.add(e_i)
                for other_edge in other.back_edges:
                    if edge == other_edge:
                        matched_edges.add(e_i)
        if len(matched_edges) == 2:
            while matched_edges != {1, 2}:
                tile = tile.rotate()
                matched_edges = {(e_i + 1) % 4 for e_i in matched_edges}
            return tile

    raise AssertionError('unreachable')


def part1(_lines):
    tiles = []
    for tile_s in _lines.strip().split('\n\n'):
        lines = tile_s.splitlines()
        tileid = int(lines[0].split()[1][:-1])
        edges_f = frozenset((
            lines[1],
            ''.join(line[-1] for line in lines[1:]),
            lines[-1][::-1],
            ''.join(line[0] for line in lines[1:])[::-1],
        ))
        back_edges_f = frozenset(edge[::-1] for edge in edges_f)
        tiles.append(Tile1(tileid, edges_f, back_edges_f))

    corners = []
    for i, tile in enumerate(tiles):
        edges = set(tile.edges)
        for j, other in enumerate(tiles):
            if i == j:
                continue
            for edge in tuple(edges):
                if edge in other.edges | other.back_edges:
                    edges.discard(edge)
        if len(edges) == 2:
            corners.append(tile.tile_id)

    n = 1
    for corner in corners:
        n *= corner
    return n


def part2(_lines):
    tiles = {}
    for tile_s in _lines.strip().split('\n\n'):
        lines = tile_s.splitlines()
        tile_id = int(lines[0].split()[1][:-1])
        tiles[tile_id] = Tile2(tile_id, tuple(lines[1:]))

    by_connections = collections.defaultdict(set)
    connections = collections.defaultdict(set)
    for i, tile in enumerate(tiles.values()):
        n = 0
        for j, other in enumerate(tiles.values()):
            if i == j:
                continue
            for edge in tile.edges:
                for other_edge in other.edges:
                    if edge == other_edge:
                        n += 1
                        connections[tile.tile_id].add(other.tile_id)
                for other_edge in other.back_edges:
                    if edge == other_edge:
                        n += 1
                        connections[tile.tile_id].add(other.tile_id)

        by_connections[n].add(tile.tile_id)

    corner = _first_corner(tiles)
    prev_bottom = corner.edges.top
    # assumption: the puzzle is a square
    size = int(math.sqrt(len(tiles)))

    rows = []
    for i in range(size):
        row = []
        if i == 0 or i == size - 1:
            target_size = 2  # looking for a corner
        else:
            target_size = 3

        # find first piece
        for tile_id in by_connections[target_size]:
            tile = tiles[tile_id]
            if prev_bottom in tile.edges or prev_bottom in tile.back_edges:
                for tile in tile.possible():
                    if tile.edges.top == prev_bottom:
                        break
                else:
                    raise AssertionError('unreachable: no find first orient')
                row.append(tile)
                by_connections[target_size].discard(tile_id)
                break
        else:
            raise AssertionError('unreachable: no find first piece')

        # append rest of pieces
        for i2 in range(1, size):
            if i2 != size - 1:
                inner_target_size = target_size + 1
            else:
                inner_target_size = target_size

            target_edge = row[-1].edges.right
            for tile_id in by_connections[inner_target_size]:
                tile = tiles[tile_id]
                if target_edge in tile.edges or target_edge in tile.back_edges:
                    for tile in tile.possible():
                        if tile.edges.left == target_edge:
                            break
                    else:
                        raise AssertionError('unreachable: no find orient')
                    row.append(tile)
                    by_connections[inner_target_size].discard(tile_id)
                    break
            else:
                raise AssertionError('unreachable: no find next piece')

        rows.append(row)
        prev_bottom = row[0].edges.bottom

    tile_height = len(rows[0][0].inner_parts)

    grid = Tile2(
        -1,
        tuple(
            ''.join(tile.inner_parts[i] for tile in row)
            for row in rows
            for i in range(tile_height)
        )
    )

    for grid in grid.possible():
        count = 0
        for i, line in enumerate(grid.lines[:-2]):
            for match in DARGON_RE0.finditer(line):
                if (
                        DARGON_RE1.match(grid.lines[i + 1], match.start()) and
                        DARGON_RE2.match(grid.lines[i + 2], match.start())
                ):
                    count += 1

        if count > 0:
            octothorpes = sum(c == '#' for line in grid.lines for c in line)
            return octothorpes - 15 * count

    raise AssertionError('unreachable')


def main(_fn):
    with open('../day20/' + _fn) as fi:
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

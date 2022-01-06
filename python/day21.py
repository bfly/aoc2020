from typing import NamedTuple, FrozenSet, Dict, Set

test = True


class Recipe(NamedTuple):
    ingredients: FrozenSet[str]
    allergens: FrozenSet[str]


def part1(_lines):
    recipes = []
    for line in _lines.strip().splitlines():
        begin, _, rest = line.partition('(contains ')

        begin = begin.strip()
        ingredients = frozenset(begin.split())

        rest = rest.strip(')')
        allergens = frozenset(rest.split(', '))
        recipes.append(Recipe(ingredients, allergens))

    by_allergen: Dict[str, Set[str]] = {}
    for recipe in recipes:
        for allergen in recipe.allergens:
            by_allergen.setdefault(allergen, set(recipe.ingredients))
            by_allergen[allergen] &= recipe.ingredients

    assigned = {}
    while by_allergen:
        for k, v in tuple(by_allergen.items()):
            if len(v) == 1:
                val, = v
                assigned[k] = val
                for _v in by_allergen.values():
                    _v.discard(val)
                del by_allergen[k]

    total = 0
    known = set(assigned.values())
    for recipe in recipes:
        total += len(recipe.ingredients - known)
    return total


def part2(_lines):
    recipes = []
    for line in _lines.strip().splitlines():
        begin, _, rest = line.partition('(contains ')

        begin = begin.strip()
        ingredients = frozenset(begin.split())

        rest = rest.strip(')')
        allergens = frozenset(rest.split(', '))
        recipes.append(Recipe(ingredients, allergens))

    by_allergen: Dict[str, Set[str]] = {}
    for recipe in recipes:
        for allergen in recipe.allergens:
            by_allergen.setdefault(allergen, set(recipe.ingredients))
            by_allergen[allergen] &= recipe.ingredients

    assigned = {}
    while by_allergen:
        for k, v in tuple(by_allergen.items()):
            if len(v) == 1:
                val, = v
                assigned[k] = val
                for _v in by_allergen.values():
                    _v.discard(val)
                del by_allergen[k]

    items = sorted(assigned.items())
    return ','.join(val for _, val in items)


def main(_fn):
    with open('../day21/' + _fn) as fi:
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

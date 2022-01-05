import re


def validate(_policies):
    valid1, valid2 = 0, 0

    for m1, m2, char, password in _policies:
        m1, m2 = int(m1), int(m2)

        if m1 <= password.count(char) <= m2:
            valid1 += 1

        if (password[m1 - 1] == char) != (password[m2 - 1] == char):
            valid2 += 1

    return valid1, valid2


def main(_fn):
    with open('../day2/' + _fn) as fi:
        lines = fi.read()

    policies = re.findall(r'(\d+)-(\d+) (\w): (\w+)', lines)
    valid1, valid2 = validate(policies)
    print(f'Part 1: {valid1} valid')  # answer of part one
    print(f'Part 2: {valid2} valid')  # answer of part two


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    print()
    main(fn)

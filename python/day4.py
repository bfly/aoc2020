from box import Box
from string import digits

VALID_ECL = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


# ---------- PART-1 ----------
def part1(_lines):
    passports = []
    passport = Box({})
    for line in _lines:
        if len(line) > 0:
            for field in line.split():
                key, value = field.split(':')
                passport[key] = value
            continue

        if all(attr in passport for attr in REQUIRED_FIELDS):
            passports.append(passport)
        passport = Box({})

    if all(attr in passport for attr in REQUIRED_FIELDS):
        passports.append(passport)

    return passports


# ---------- PART-2 ----------
def part2(_passports):
    valid_count = 0
    for passport in _passports:
        # check byr, iyr and eyr
        if not 1920 <= int(passport.byr) <= 2002:
            continue
        if not 2010 <= int(passport.iyr) <= 2020:
            continue
        if not 2020 <= int(passport.eyr) <= 2030:
            continue

        # check hgt
        if 'cm' in passport.hgt:
            if not 150 <= int(passport.hgt[:-2]) <= 193:
                continue
        elif 'in' in passport.hgt:
            if not 59 <= int(passport.hgt[:-2]) <= 76:
                continue
        else:
            continue

        # check hcl
        if not passport.hcl.startswith('#'):
            continue
        if not all(c in digits + 'abcdef' for c in passport.hcl[1:]):
            continue

        # check ecl
        if passport.ecl not in VALID_ECL:
            continue

        # check pid
        if len(passport.pid) != 9:
            continue
        if not all(c in digits for c in passport.pid):
            continue
        valid_count += 1
    return valid_count


def main(_fn):
    with open('../day4/' + _fn) as fi:
        lines = fi.read().splitlines()

    passports = part1(lines)
    print(f'{len(passports)} passports with required fields')  # answer of part one

    count = part2(passports)
    print(f'{count} passports with validated fields')  # answer of part two


if __name__ == '__main__':
    fn = 'inputdata.txt' if input('Press ENTER for test, s to submit: ') == 's' else 'smalldata.txt'
    print()
    main(fn)

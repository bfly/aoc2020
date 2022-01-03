# Problem 4 - passport validation

import re

with open('inputdata.txt', 'r') as fd:
    content = fd.read()
    lines = content.split("\n\n")
    input = [line.replace("\n", " ") for line in lines]

# Part 1
ValidTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
ValidPassports = 0
for pp in input:
    if all(x in pp for x in ValidTerms):
        ValidPassports += 1

print("Part 1: The amount of valid passports is: " + str(ValidPassports))

# Part 2
ValidPassports = 0
for pp in input:
    if (re.search(r"byr:19[2-9]\d|byr:200[0-2]", pp) and
            re.search(r"eyr:202\d|eyr:2030", pp) and
            re.search(r"iyr:201\d|iyr:2020", pp) and
            re.search(r"hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in", pp) and
            re.search(r"hcl:#[a-z0-9]{6}", pp) and
            re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", pp) and
            re.search(r"pid:\d{9}\b", pp)):
        ValidPassports += 1

print("Part 2: The amount of valid passports is: " + str(ValidPassports))

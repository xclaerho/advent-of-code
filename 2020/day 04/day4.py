import re

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
allowed_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def parse_passports(lines):
    passports = []
    passport = dict()
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            fields = line.split(' ')
            for field in fields:
                k,v = field.split(':')
                passport[k] = v
        else:
            passports.append(passport)
            passport = dict()
    # final line may not be a newline, empty passports get filtered out anyway
    passports.append(passport)
    return passports

def has_required_fields(passport):
    return set(passport).issuperset(set(required_fields))

def check_fields(p):
    if not len(p['byr']) == 4 or not 1920 <= int(p['byr']) <= 2002:
        return False
    if not len(p['iyr']) == 4 or not 2010 <= int(p['iyr']) <= 2020:
        return False
    if not len(p['eyr']) == 4 or not 2020 <= int(p['eyr']) <= 2030:
        return False
    if not p['ecl'] in allowed_ecl:
        return False
    if not ((p['hgt'][-2:] == "in" and 59 <= int(p['hgt'][:-2]) <= 76) or (p['hgt'][-2:] == "cm" and 150 <= int(p['hgt'][:-2]) <= 193)):
        return False
    if not re.match(r"^[0-9]{9}$", p['pid']):
        return False
    if not re.match(r"^#[0-9a-f]{6}$", p['hcl']):
        return False
    return True


file = open("input.txt", 'r')
lines = file.readlines()
passports = parse_passports(lines)
part1 = sum([1 for passport in passports if has_required_fields(passport)])
part2 = sum([1 for passport in passports if has_required_fields(passport) and check_fields(passport)])
print(part1)
print(part2)
        
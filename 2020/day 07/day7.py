# {'type': [{'type': xxx, 'num': yyy},...]}
rules = dict()

for rule in open('input.txt').readlines():
    bagtype, inside = rule.split('s contain ')
    bags = inside[:-2].split(',')
    r= []
    for bag in bags:
        if 'no' in bag:
            break
        if '1' in bag:
            r.append({'type': bag.strip()[2:], 'num': bag.strip()[0]})
        else:
            r.append({'type': bag.strip()[2:-1], 'num': bag.strip()[0]})
    rules[bagtype] = r


def can_contain(rules, motherbag, goal):
    if motherbag == goal:
        return True
    if len(rules[motherbag]) == 0:
        return False
    else:
        return True in [can_contain(rules, bag['type'], goal) for bag in rules[motherbag]]


def count_contain(rules, goal):
    options = 0
    for bag in [bag for bag in rules.keys() if bag != goal]:
        options += 1 if can_contain(rules, bag, 'shiny gold bag') else 0
    return options


print(count_contain(rules, 'shiny gold bag'))


def count_inside(rules, bagtype):
    if len(rules[bagtype]) == 0:
        return 0
    return sum([int(bag['num'])+int(bag['num'])*count_inside(rules, bag['type']) for bag in rules[bagtype]])


print(count_inside(rules, 'shiny gold bag'))

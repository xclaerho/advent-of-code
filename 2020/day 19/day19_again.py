from copy import deepcopy

def check_match(text, pattern, rules) -> bool:
    """aabba, [8, 11], dict of int to list or char -> Boolean """
    # if there are more numbers than characters it will never be possible to match
    if len(text) < len(pattern):
        return False
    # remove front a's and b's if possible
    while len(pattern) > 0 and rules.get(pattern[0]) in ['a', 'b']:
        if text[0] == rules.get(pattern[0]):
            text = text[1:]
            pattern = pattern[1:]
        else:
            return False
    # if no more rules and text => exact match
    if len(pattern) == 0:
        return len(text) == 0
    # replace first number by subrule and check (do this for each subrule)
    for sub in rules.get(pattern[0]):
        s = deepcopy(sub) # deepcopy otherwise rules dictionary is getting updated.......
        s.extend(pattern[1:])
        match = check_match(text, s, rules)
        if match:
            return True
    return False

def check_match_with_loops(text, pattern, rules) -> bool:
    """aabba, [8, 11], dict of int to list or char -> Boolean """
    # if there are more numbers than characters it will never be possible to match
    if len(text) < len(pattern):
        return False
    # remove front a's and b's if possible
    while len(pattern) > 0 and rules.get(pattern[0]) in ['a', 'b']:
        if text[0] == rules.get(pattern[0]):
            text = text[1:]
            pattern = pattern[1:]
        else:
            return False
        
    # if no more rules and text => exact match
    if len(pattern) == 0:
        return len(text) == 0

    # special ones: try combo's until there are more numbers than characters get too long
    if pattern[0] == 8:
        i = 1
        while i + len(pattern[1:]) <= len(text):
            prepend = [42]*i
            prepend.extend(pattern[1:])
            match = check_match_with_loops(text, prepend, rules)
            if match:
                return True
            i += 1
        return False
    if pattern[0] == 11:
        i = 1
        while 2*i + len(pattern[1:]) <= len(text):
            prepend = [42]*i
            prepend.extend([31]*i)
            prepend.extend(pattern[1:])
            match = check_match_with_loops(text, prepend, rules)
            if match:
                return True
            i += 1
        return False
    
    # replace first number by subrule and check (do this for each subrule)
    for sub in rules.get(pattern[0]):
        s = deepcopy(sub) # deepcopy otherwise rules dictionary is getting updated.......
        s.extend(pattern[1:])
        match = check_match_with_loops(text, s, rules)
        if match:
            return True
    return False

matches1 = matches2 = 0

rules = dict()
messages = []
for line in open('input.txt').read().split('\n'):
    if ':' in line:
        number, expr = line.split(':')
        if 'a' in expr:
            rules[int(number)] = 'a'
        elif 'b' in expr:
            rules[int(number)] = 'b'
        else:
            rules[int(number)] = [[int(x) for x in sub.strip().split(' ')] for sub in expr.strip().split('|')]
    elif len(line) > 0:
        m = line
        if check_match(m, [0], rules):
            matches1 += 1
        if check_match_with_loops(m, [0], rules):
            matches2 += 1
print(matches1, matches2)
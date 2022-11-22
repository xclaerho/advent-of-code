import re
import itertools

def form_patterns(number, rules):
    pattern = rules.get(number)
    if pattern == 'a' or pattern == 'b':
        return [pattern]
    subpatterns = pattern.split('|')
    test = []
    for subp in subpatterns:
        permutations = list(itertools.product(*[form_patterns(x, rules) for x in subp.strip().split(' ')]))
        options = [''.join(x) for x in permutations]
        test.extend(options)
    return test

rules = dict()
messages = []
for line in open('input.txt').read().split('\n'):
    if ':' in line:
        number, expr = line.split(':')
        rules[number] = expr.strip().replace('"', '')
    elif len(line) > 0:
        messages.append(line)
    
rule = set(form_patterns('0', rules))
print("found rule")
matches = 0
for m in messages:
    if m in rule:
        matches += 1
        print(m)
print(matches)
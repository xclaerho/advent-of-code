import re

def solve(line, method):
    braced = re.findall(r'\([\d+| |+|*]+\)', line)
    while len(braced) > 0:
        solved = [method(expr[1:-1]) for expr in braced]
        for i, expr in enumerate(braced):
            line = line.replace(expr, str(solved[i]), 1)
        braced = re.findall(r'\([\d+| |+|*]+\)', line)
    return method(line)

def solve_left_right(line):
    pattern = r"\d+ [\+|\*] \d+"
    while re.search(pattern, line):
        match = re.findall(pattern, line)[0]
        line = line.replace(match, str(eval(match)), 1)
    return int(line)

def solve_ordered(line):
    order = ['+', '*']
    for op in order:
        pattern = "\\d+ \\" + op + " \\d+"
        while re.search(pattern, line):
            match = re.findall(pattern, line)[0]
            line = line.replace(match, str(eval(match)), 1)
    return int(line)
from day18 import solve, solve_left_right, solve_ordered

lines = open('input.txt').read().split('\n')
part1 = part2 = 0
for line in lines:
    part1 += solve(line, solve_left_right)
    part2 += solve(line, solve_ordered)
print(part1, part2)
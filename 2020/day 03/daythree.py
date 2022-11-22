file = open("input.txt", 'r')

lines = file.readlines()

steps = [(1,1), (3,1),(5,1), (7,1),(1,2)]
prod = 1

for step in steps:
    x = y = trees = 0
    x_step, y_step = step
    while y < len(lines)-1:
        y+=y_step
        x+=x_step
        if lines[y][x % (len(lines[0])-1)] == '#':
            trees += 1

    prod *= trees
print(prod)
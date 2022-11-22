from copy import deepcopy


def count_all_occupied(rows):
    count = 0
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] == '#':
                count += 1
    return count


def count_occupied_neighbors(rows, x, y):
    occupied = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (i == x and j == y) and (i >= 0 and j >= 0) and (i < len(rows) and j < len(rows[0])) and rows[i][j] == "#":
                occupied += 1
    return occupied


def count_occupied_in_sight(rows, x, y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i == 0 and j == 0):
                count += check_direction(rows,x,y,(i,j))
    return count


def check_direction(rows, x, y, direction):
    x += direction[0]
    y += direction[1]
    while 0 <= x < len(rows) and 0 <= y < len(rows[0]):
        if rows[x][y] == '#':
            return 1
        if rows[x][y] == 'L':
            return 0
        x += direction[0]
        y += direction[1]
    return 0


def move(rows):
    new_rows = []
    changed = 0
    for i in range(len(rows)):
        new_row = ''
        for j in range(len(rows[0])):
            position = rows[i][j]
            neighbors = count_occupied_neighbors(rows, i, j)
            if position == 'L' and neighbors == 0:
                new_row += '#'
            elif position == '#' and neighbors >= 4:
                new_row += 'L'
            else:
                new_row += position
        new_rows.append(new_row)
    return new_rows


def iterate(rows):
    nr = move(rows)
    while nr != rows:
        rows = deepcopy(nr)
        nr = move(nr)
    return count_all_occupied(nr)


def move2(rows):
    new_rows = []
    changed = 0
    for i in range(len(rows)):
        new_row = ''
        for j in range(len(rows[0])):
            position = rows[i][j]
            neighbors = count_occupied_in_sight(rows, i, j)
            if position == 'L' and neighbors == 0:
                new_row += '#'
            elif position == '#' and neighbors >= 5:
                new_row += 'L'
            else:
                new_row += position
        new_rows.append(new_row)
    return new_rows


def iterate2(rows):
    nr = move2(rows)
    while nr != rows:
        rows = deepcopy(nr)
        nr = move2(nr)
    return count_all_occupied(nr)


rows = open('input.txt').read().split('\n')

print(iterate(rows))
print(iterate2(rows))

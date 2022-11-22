def count_active(field, x, y, z):
    active = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if not (i==x and j==y and k==z):
                    if field.get((i,j,k), '.') == '#':
                        active += 1
    return active

def move(field, dimensions):
    new_field = dict()
    new_dimensions = [d+2 for d in dimensions]
    for i in range(0, new_dimensions[0]):
        for j in range(0, new_dimensions[1]):
            for k in range(0, new_dimensions[2]):
                active = count_active(field,i-1,j-1,k-1)
                if field.get((i-1,j-1,k-1), '.') == '#' and 2 <= active <= 3:
                    new_field[(i,j,k)] = '#'
                elif field.get((i-1,j-1,k-1), '.') == '.' and active == 3:
                    new_field[(i,j,k)] = '#'

    return new_field, new_dimensions

def number_active(field):
    return sum([1 if cube == '#' else 0 for cube in field.values()])

initial_field = open('input.txt').read().split('\n')
field = dict()
for i, line in enumerate(initial_field):
    for j, char in enumerate(line):
        field[(i,j,0)] = char

dimensions = [8,8,1]
for i in range(6):
    field, dimensions = move(field, dimensions)
print(number_active(field))
#######
def count_active2(field, x, y, z, w):
    active = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if not (i==x and j==y and k==z and l==w):
                        if field.get((i,j,k,l), '.') == '#':
                            active += 1
    return active

def move2(field, dimensions):
    new_field = dict()
    new_dimensions = [d+2 for d in dimensions]
    for i in range(0, new_dimensions[0]):
        for j in range(0, new_dimensions[1]):
            for k in range(0, new_dimensions[2]):
                for l in range(0, new_dimensions[3]):
                    active = count_active2(field,i-1,j-1,k-1, l-1)
                    if field.get((i-1,j-1,k-1,l-1), '.') == '#' and 2 <= active <= 3:
                        new_field[(i,j,k,l)] = '#'
                    elif field.get((i-1,j-1,k-1,l-1), '.') == '.' and active == 3:
                        new_field[(i,j,k,l)] = '#'
    return new_field, new_dimensions

field = dict()
for i, line in enumerate(initial_field):
    for j, char in enumerate(line):
        field[(i,j,0,0)] = char

dimensions = [8,8,1,1]
for i in range(6):
    field, dimensions = move2(field, dimensions)
print(number_active(field))

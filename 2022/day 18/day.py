input = open('input.txt').read().splitlines()
cubes = [tuple(map(int, i.split(','))) for i in input]

def get_neighbours(cube):
    for side in range(len(cube)):
        for d in [-1,1]:
            neighbour = [c for c in cube]
            neighbour[side] += d
            yield tuple(neighbour)

def get_sides(cubes):
    sides = dict()

    for cube in cubes:
        for neighbour in get_neighbours(cube):
            sides[neighbour] = sides.get(neighbour, 0) + 1

    for cube in cubes:
        sides.pop(cube, None)

    return sides

sides = get_sides(cubes)
print(sum(sides.values()))

def is_inside_and_fill(point, cubes, max_size):
    fill = set()
    queue = [point]
    while len(queue) > 0 and len(fill)+len(queue) < max_size:
        current = queue.pop(0)
        fill.add(current)
        for neighbour in get_neighbours(current):
            if neighbour in cubes or neighbour in fill or neighbour in queue:
                continue
            queue.append(neighbour)
    if len(queue) == 0:
        return True, fill
    return False, fill | set(queue)

cubes = set(cubes)
for side, value in sides.items():
    if value > 0:
        inside, fill = is_inside_and_fill(side, cubes, 8000)
        if inside:
            cubes |= fill
        else: # do not have to check cubes in fill anymore, they are outside
            for cube in fill:
                if cube in sides.keys():
                    sides[cube] = 0

sides = get_sides(cubes)
print(sum(sides.values()))
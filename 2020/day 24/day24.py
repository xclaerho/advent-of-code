def tile_coords(steps):
    x = y = 0
    while len(steps) > 0:
        if steps[:2] == 'ne':
            x += 0.5
            y += 1
            steps = steps[2:]
        elif steps[:2] == 'nw':
            x -= 0.5
            y += 1
            steps = steps[2:]
        elif steps[:2] == 'se':
            x += 0.5
            y -= 1
            steps = steps[2:]
        elif steps[:2] == 'sw':
            x -= 0.5
            y -= 1
            steps = steps[2:]
        elif steps[0] == 'e':
            x += 1
            steps = steps[1:]
        elif steps[0] == 'w':
            x -= 1
            steps = steps[1:]
    return x, y

flipped = set()

for line in open('input.txt').read().split('\n'):
    x, y = tile_coords(line)
    if (x,y) in flipped:
        flipped.remove((x,y))
    else:
        flipped.add((x,y))

print("part 1:", len(flipped))

neighbors = [(-1,0), (1,0), (0.5, 1), (0.5, -1), (-0.5, 1), (-0.5, -1)]

def check_adjacent(tile, neighbors, flipped):
    count = 0
    for n in neighbors:
        if (tile[0]+n[0],tile[1]+n[1]) in flipped:
            count += 1
    return count

def next_day(today, neighbors):
    tomorrow = set()
    for tile in today:
        adjacent = check_adjacent(tile, neighbors, today)
        if 1 <= adjacent <= 2:
            tomorrow.add(tile)
        # check neighboring white tiles
        for n in neighbors:
            neighbor = (tile[0]+n[0],tile[1]+n[1])
            if not neighbor in flipped:
                adjacent = check_adjacent(neighbor, neighbors, today)
                if adjacent == 2:
                    tomorrow.add(neighbor)
    return tomorrow

for _ in range(100):
    flipped = next_day(flipped, neighbors)

print("part 2:", len(flipped))
        
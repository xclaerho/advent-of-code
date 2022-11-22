from collections import defaultdict

class Tile:
    def __init__(self, id, top, bottom, left, right):
        self.id = id
        self.edges = [top, bottom, left, right]

def find_corners(tiles):
    corners = []
    sides = defaultdict(list)
    for t in tiles:
        for e in t.edges:
            if e in sides.keys():
                sides[e].append(t.id)
            else:
                sides[e[::-1]].append(t.id)
    edges = defaultdict(int)
    for s in sides:
        if len(sides[s]) == 1:
            tile_id = sides[s][0]
            edges[tile_id] += 1
            if edges[tile_id] == 2:
                corners.append(tile_id)
    return corners

tiles = []

for tile in open('input.txt').read().split('\n\n'):
    lines = tile.split('\n')
    tile_id = int(lines[0][-5:-1])
    lines = lines[1:]
    top = lines[0]
    bottom = lines[-1]
    left = ''.join([l[0] for l in lines if len(l) > 0])
    right = ''.join([l[-1] for l in lines if len(l) > 0])
    tiles.append(Tile(tile_id, top, bottom, left, right))

from functools import reduce

p1 = reduce(lambda x, y: x*y, find_corners(tiles))
print(p1)
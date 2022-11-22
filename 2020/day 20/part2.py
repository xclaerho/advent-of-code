"""
* no edge is present more than 2 times
* to check all orientations: check all rotations, flip (either horizontally or vertically) and check all rotations again
"""
from collections import defaultdict
from math import sqrt
from copy import deepcopy

class Tile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile
        # [top, right, bottom, left] (also for neighbors)
        self.set_edges()
        self.neighbors = [None, None, None, None]
    
    def set_edges(self):
        tile = self.tile
        self.edges = [tile[0], ''.join([l[-1] for l in tile if len(l)>0]), tile[-1], ''.join([l[0] for l in tile if len(l)>0])]

    def set_neighbor(self, edge, neighbor_id):
        for i, e in enumerate(self.edges):
            if e == edge or e == edge[::-1]:
                self.neighbors[i] = neighbor_id
                return

    def flip(self):
        """Flips tile vertically"""
        self.tile.reverse()
        self.set_edges()
        temp = self.neighbors[0]
        self.neighbors[0] = self.neighbors[2]
        self.neighbors[2] = temp

    def rotate(self):
        """Rotates tile 90° right"""
        self.tile = list(map(''.join, zip(*reversed(self.tile)))) # credits stackoverflow
        self.neighbors = [self.neighbors[i] for i in range(-1,3)]
        self.set_edges()

    def orient(self, left, top):
        """Orient tile so that left and top neighbor id match"""
        if self.neighbors[3] == left and self.neighbors[0] == top:
            return
        for _ in range(4):
            self.rotate()
            if self.neighbors[3] == left and self.neighbors[0] == top:
                return
        self.flip()
        for _ in range(4):
            self.rotate()
            if self.neighbors[3] == left and self.neighbors[0] == top:
                return
    
    def trim(self):
        """Removes edges from tile"""
        self.tile = self.tile[1:-1]
        self.tile = [''.join(l[1:-1]) for l in self.tile]

    def __str__(self):
        return f'{self.id}: top={self.neighbors[0]}, right={self.neighbors[1]}, bottom={self.neighbors[2]}, left={self.neighbors[3]}'

def set_neighbors(tiles) -> None:
    """Add ids of neighbors in correct place (relative to how tile is currently oriented) to tiles"""
    sides = defaultdict(list) # edge -> list of tile ids
    for t in tiles.values():
        for e in t.edges:
            if e in sides.keys():
                sides[e].append(t.id)
            else:
                sides[e[::-1]].append(t.id)
    for s in sides.keys():
        for i in sides[s]:
            for j in sides[s]:
                if not i == j:
                    tiles[i].set_neighbor(s, j)
                    tiles[j].set_neighbor(s, i)

def form_image(tiles) -> list:
    side_length = int(sqrt(len(tiles)))
    # find a corner
    curr = -1
    for t in tiles.values():
        if t.neighbors.count(None) == 2:
            curr = t.id
            break
    # puzzle id's of tiles together in a valid way
    image = []
    x = y = 0
    for y in range(side_length):
        line = []
        for x in range(side_length):
            # orient tile so that top and left neighbor are correct
            left = None
            if x > 0:
                left = line[x-1]
            top = None
            if y > 0:
                top = image[y-1][x]
            tiles[curr].orient(left, top)
            # add tile to image
            line.append(curr)
            # continue with right neighbor
            curr = tiles[curr].neighbors[1]
        image.append(line)
        # continue with bottom neighbor of first tile in line
        curr = tiles[image[y][0]].neighbors[2]
    # form full resolution image
    full_res_image = []
    for y, line in enumerate(image):
        full_res_line = []
        for x, id in enumerate(line):
            tile = tiles[id]
            tile.trim()
            if x == 0:
                full_res_line = deepcopy(tile.tile)
            else:
                for i, l in enumerate(tile.tile):
                    full_res_line[i] += l
        full_res_image.extend(full_res_line)
    return full_res_image

def is_monster(monster, image, x, y) -> (bool, set):
    monster_coords = set()
    for j, line in enumerate(monster):
        for i, char in enumerate(line):
            if char == '#':
                if not image[y+j][x+i] == '#':
                    return False, set()
                else:
                    monster_coords.add((y+j, x+i))
    return True, monster_coords

def monster_count_and_coords(image) -> (int, int):
    monster = ['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']
    monster_count = 0
    monster_coords = set()
    for y in range(len(image)-len(monster)):
        for x in range(len(image[0])-len(monster[0])):
            spotted, coords = is_monster(monster, image, x, y)
            if spotted:
                monster_count += 1
                monster_coords = monster_coords.union(coords)
    return monster_count, monster_coords

def sea_roughness(image, monster_coords) -> int:
    roughness = 0
    for y in range(len(image)):
        for x in range(len(image[0])):
            if not (y,x) in monster_coords:
                if image[y][x] == "#":
                    roughness += 1
    return roughness

def part2(image) -> int:
    monsters, coords = monster_count_and_coords(image.tile)
    if monsters > 0:
        return sea_roughness(image.tile, coords)
    for _ in range(3):
        image.rotate()
        monsters, coords = monster_count_and_coords(image.tile)
        if monsters > 0:
            return sea_roughness(image.tile, coords)
    image.flip()
    for _ in range(3):
        image.rotate()
        monsters, coords = monster_count_and_coords(image.tile)
        if monsters > 0:
            return sea_roughness(image.tile, coords)
    return monsters

tiles = dict()

for tile in open('input.txt').read().split('\n\n'):
    lines = tile.split('\n')
    id = int(lines[0][-5:-1])
    tile = [l for l in lines[1:] if len(l)>0]
    tiles[id] = Tile(id, tile)


set_neighbors(tiles)
image = form_image(tiles)
image_tile = Tile(0, image)
roughness = part2(image_tile)
print(roughness)

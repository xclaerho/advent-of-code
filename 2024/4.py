grid = open('input.txt').readlines()

directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

xmases = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
      if char != 'X':
        continue
      for dx, dy in directions:
        coords = [(x+dx*i, y+dy*i) for i in range(4)]
        if all(0 <= x < len(line) and 0 <= y < len(grid) for x,y in coords):
          word = ''.join(grid[y][x] for x, y in coords)
          if word == 'XMAS':
            xmases += 1

print(xmases)

xmases = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
      if char != 'A':
        continue
      coords = [[(x-1,y+1),(x,y),(x+1,y-1)],[(x-1,y-1),(x,y),(x+1,y+1)]]
      if not all(0 <= x < len(line) and 0 <= y < len(grid) for c in coords for x,y in c):
        continue
      word_1 = ''.join(grid[y][x] for x, y in coords[0])
      word_2 = ''.join(grid[y][x] for x, y in coords[1])
      if word_1 in ('MAS','SAM') and word_2 in ('MAS','SAM'):
        xmases += 1

print(xmases)



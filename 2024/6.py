area = [l.strip() for l in open('input.txt').readlines()]

directions = [(0,1),(1,0),(0,-1),(-1,0)] # R, D, L, U

def find_guard(area):
  directions = ['>','v','<','^']
  for y, l in enumerate(area):
    for x, direction in enumerate(l):
      if direction in directions:
        return y,x,directions.index(direction)

y,x,direction = find_guard(area)

positions = set()

while 0<=y<len(area) and 0<=x<len(area[0]):
  positions.add((y,x))
  ny,nx = y+directions[direction][0], x+directions[direction][1]
  if not (0<=ny<len(area) and 0<=nx<len(area[0])):
    break
  while area[ny][nx]=='#':
    direction = (direction+1)%4
    ny,nx = y+directions[direction][0], x+directions[direction][1]
  y,x = ny,nx

print(len(positions))

# p2
iy,ix,_ = find_guard(area)
p2 = 0

# try all positions for a block
for by in range(len(area)):
  for bx in range(len(area[0])):
    # not in initial position
    if by == iy and bx == ix:
      continue

    y,x,direction = find_guard(area)
    positions = set() # also keep direction now
    while 0<=y<len(area) and 0<=x<len(area[0]):
      if (y,x,direction) in positions:
        p2 += 1
        break
      positions.add((y,x,direction))
      ny,nx = y+directions[direction][0], x+directions[direction][1]
      if not (0<=ny<len(area) and 0<=nx<len(area[0])):
        break
      while area[ny][nx]=='#' or (ny,nx) == (by,bx):
        direction = (direction+1)%4
        ny,nx = y+directions[direction][0], x+directions[direction][1]
      y,x = ny,nx

print(p2)

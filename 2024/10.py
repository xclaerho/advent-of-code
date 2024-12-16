input = open('input.txt').read().splitlines()
input = [list(map(int,line)) for line in input]

def trail_ends(y, x, input):
  if input[y][x] == 9:
    yield (y,x)
  else:
    for dy,dx in [(-1,0),(1,0),(0,1),(0,-1)]:
      if 0 <= y+dy < len(input) and 0 <= x+dx < len(input[0]) and input[y+dy][x+dx] == input[y][x]+1:
        yield from trail_ends(y+dy, x+dx, input)

score, rating = 0, 0

for y, line in enumerate(input):
  for x, num in enumerate(line):
    if num == 0:
      ends = []
      for end in trail_ends(y, x, input):
        ends.append(end)
      score += len(set(ends))
      rating += len(ends)

print(score, rating)

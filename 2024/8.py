from collections import defaultdict

city = [l.strip() for l in open('input.txt').readlines()]

locations = defaultdict(list)
for y, l in enumerate(city):
  for x, c in enumerate(l):
    if c != '.':
      locations[c].append((y,x))

# part 1
antinodes = set()
for positions in locations.values():
  # find all antinodes and check if in city area
  for i, p1 in enumerate(positions):
    for p2 in positions[i+1:]:
      dy,dx = p2[0]-p1[0], p2[1]-p1[1]

      ay,ax = p1[0]-dy, p1[1]-dx
      if 0 <= ay < len(city) and 0 <= ax < len(city[0]):
        antinodes.add((ay,ax))

      ay,ax = p2[0]+dy, p2[1]+dx
      if 0 <= ay < len(city) and 0 <= ax < len(city[0]):
        antinodes.add((ay,ax))

print(len(antinodes))

# part 2
antinodes = set()
for positions in locations.values():
  # find all antinodes and check if in city area
  for i, p1 in enumerate(positions):
    for p2 in positions[i+1:]:
      antinodes.add(p1)
      antinodes.add(p2)
      dy,dx = p2[0]-p1[0], p2[1]-p1[1]

      ay,ax = p1[0]-dy, p1[1]-dx
      while 0 <= ay < len(city) and 0 <= ax < len(city[0]):
        antinodes.add((ay,ax))
        ay,ax = ay-dy, ax-dx

      ay,ax = p2[0]+dy, p2[1]+dx
      while 0 <= ay <len(city) and 0 <= ax < len(city[0]):
        antinodes.add((ay,ax))
        ay,ax = ay+dy, ax+dx

print(len(antinodes))

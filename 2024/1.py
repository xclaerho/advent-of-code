a,b = zip(*[line.split() for line in open('input').readlines()])
a = sorted(int(x) for x in a)
b = sorted(int(x) for x in b)

dist = sum([abs(x-y) for x,y in zip(a,b)])
print(dist)

counts = {x: b.count(x) for x in b}
similarity = sum([x*counts.get(x, 0) for x in a])
print(similarity)

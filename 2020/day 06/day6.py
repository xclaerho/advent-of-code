import collections
p1 = p2 = 0
for group in open('input.txt').read().split('\n\n'):
    a_count = collections.Counter(group.replace('\n', ''))
    p1 += len(set(a_count))
    p2 += sum([1 for v in a_count.values() if v == len(group.splitlines())])
print(p1, p2)
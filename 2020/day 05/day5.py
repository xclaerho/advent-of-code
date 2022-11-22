ids = set()
for seat in open('input.txt').read().splitlines():
    ids.add(int(''.join(['1'  if char == 'B' or char == 'R' else '0' for char in seat]), 2))
print(max(ids), set(range(min(ids), max(ids))) - ids)
from collections import defaultdict

stone_numbers = defaultdict(int)
for stone in open('input.txt').readlines()[0].split():
  stone_numbers[int(stone)] += 1

def blink(stone):
  if stone == 0:
    return [1]
  if len(str(stone)) % 2 == 1:
    return [stone*2024]
  stone = str(stone)
  return [int(stone[:len(stone)//2]), int(stone[len(stone)//2:])]

for _ in range(75):
  new_stone_numbers = defaultdict(int)
  for stone, number in stone_numbers.items():
    next_stones = blink(stone)
    for s in next_stones:
      new_stone_numbers[s] += number
  stone_numbers = new_stone_numbers

print(sum(stone_numbers.values()))

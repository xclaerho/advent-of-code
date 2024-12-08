import re

lines = open('input').readlines()

result = 0
for line in lines:
  matches = re.findall(r'mul\(\d+,\d+\)', line)
  matches = [map(int,match[4:-1].split(',')) for match in matches]
  result += sum(a*b for a,b in matches)

print(result)

enabled, result = True, 0
for line in lines:
  matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
  for match in matches:
    if match == 'do()':
      enabled = True
    elif match == 'don\'t()':
      enabled = False
    elif enabled:
      a,b = map(int,match[4:-1].split(','))
      result += a*b

print(result)

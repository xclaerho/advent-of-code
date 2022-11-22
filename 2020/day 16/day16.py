import re

## part 1, check for each number if it is not in valid range
fields = dict()
ticket = []
tickets = []

f = open('input.txt').read().split('\n')
for i in range(len(f)):
    field = re.match('(.+): (\d+)-(\d+) or (\d+)-(\d+)', f[i])
    if field:
        vals = field.groups()
        fields[vals[0]] = [(int(vals[1]), int(vals[2])), (int(vals[3]), int(vals[4]))]
    elif 'your' in f[i]:
        ticket = [int(x) for x in f[i+1].split(',')]
    elif ',' in f[i]:
        tickets.append([int(x) for x in f[i].split(',')])

s = 0
valid_tickets = []
for t in tickets:
    ticket_valid = True
    for num in t:
        valid = False
        for r in fields.values():
            if r[0][0] <= num <= r[0][1] or r[1][0] <= num <= r[1][1]:
                valid = True
        if not valid:
            s += num
            ticket_valid = False
    if ticket_valid:
        valid_tickets.append(t)

print(s)

## part 2
tickets = valid_tickets
possibilities = []

for i in range(len(ticket)):
    possibilities.append(list(fields.keys()))

for t in tickets:
    for i in range(len(t)):
        num = t[i]
        to_remove = []
        for p in possibilities[i]:
            r = fields.get(p)
            if not r[0][0] <= num <= r[0][1] and not r[1][0] <= num <= r[1][1]:
               to_remove.append(p)
        for p in to_remove:
            if len(to_remove) == len(possibilities[i]):
                print('bad filtering')
            possibilities[i].remove(p)

unique = set()
while sum([len(p) for p in possibilities]) != len(ticket):
    for field in possibilities:
        if len(field) == 1:
            unique.add(field[0])
        else:
            for p in field:
                if p in unique:
                    field.remove(p)

fields = [p[0] for p in possibilities]
part2 = 1
for i in range(len(fields)):
    if 'departure' in fields[i]:
        part2 *= ticket[i]

print(part2)
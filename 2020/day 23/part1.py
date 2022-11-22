def move(cups, cursor):
    current = cups[cursor]
    lifted = []
    for i in range(1,4):
        if cursor + i >= len(cups):
            lifted.append(cups[(cursor+i)%len(cups)])
        else:
            lifted.append(cups[cursor+i])
    rest = [x for x in cups if not x in lifted]
    # find destination
    destination = current-1
    while not destination in rest:
        if destination < min(rest):
            destination = max(rest)
        else:
            destination -= 1
    destination = rest.index(destination)
    # put lifted cups in correct place
    cups = rest[:destination+1] + lifted + rest[destination+1:]
    # move cursor
    cursor = (cups.index(current)+1)%len(cups)
    return cups, cursor

cups = [int(x) for x in "123487596"]
cursor = 0
for i in range(100):
    cups, cursor = move(cups, cursor)

cups = cups[cups.index(1)+1:] + cups[:cups.index(1)]

print(''.join([str(x) for x in cups]))
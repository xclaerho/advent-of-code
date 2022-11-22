import time

class Cup:
    def __init__(self, val):
        self.next = None
        self.val = val
    
    def set_next(self, cup):
        self.next = cup
    
    def __str__(self):
        return f'{self.val}'

def move(cup, cups):
    # remove next three
    removed_numbers = []
    three_begin = cup.next
    three_end = cup
    for _ in range(3):
        three_end = three_end.next
        removed_numbers.append(three_end.val)
    cup.set_next(three_end.next)
    # find destination
    goal = cup.val-1
    if goal == 0:
        goal = 1000000
    while goal in removed_numbers:
        goal -= 1
        if goal == 0:
            goal = 1000000
    destination = cups[goal]
    # insert
    three_end.set_next(destination.next)
    destination.set_next(three_begin)
    # move one cup
    return cup.next

cups = dict()

numbers = [int(x) for x in "123487596"]
numbers.extend(list(range(10,1000001)))

c = Cup(numbers[0])
start = c
for number in numbers[1:]:
    cups[c.val] = c
    n = Cup(number)
    c.set_next(n)
    c = n
cups[c.val] = c
c.set_next(start)

start_time = time.time()

for _ in range(10000000):
    start = move(start, cups)

print(time.time() - start_time)

while start.val != 1:
    start = start.next

print(start.next.val*start.next.next.val)
starting = [5,2,8,16,18,0,1]
spoken = dict()
last = 5

for turn, num in enumerate(starting):
    if turn == 0:
        last = num
        continue
    spoken[last] = turn
    last = num

for turn in range(len(starting),30000000):
    if turn == 2020 or turn == 30000000:
        print(last)
    if spoken.get(last, -1) > 0:
        new_last = turn - spoken.get(last)
        spoken[last] = turn
        last = new_last
    else:
        spoken[last] = turn
        last = 0
print(last)    



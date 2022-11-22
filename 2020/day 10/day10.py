adapters = [int(a) for a in open('input.txt').read().split('\n')]
adapters = sorted(adapters)
adapters.insert(0,0)
adapters.append(max(adapters)+3)

def d1d3(adapters):
    diff1 = diff3 = 0
    for i in range(len(adapters)-1):
        diff = adapters[i+1] - adapters[i]
        if diff == 1:
            diff1+=1
        elif diff == 3:
            diff3+=1
    return diff1* diff3

print(d1d3(adapters))


def arrangements(adapters, memo):
    if memo.get(adapters[0]) is not None:
        return memo[adapters[0]], memo
    total = 0
    i = 1
    while i < len(adapters) and adapters[i] - adapters[0] <= 3:
        num, memo = arrangements(adapters[i:], memo)
        total += num
        i += 1
    memo[adapters[0]] = total
    return total, memo

memo = dict()
memo[max(adapters)] = 1


print(arrangements(adapters, memo)[0])


#### try automatic memoization
from functools import cache

@cache
def automemo(adapters):
    if len(adapters) == 1:
        return 1
    total = 0
    i = 1
    while i < len(adapters) and adapters[i] - adapters[0] <= 3:
        total += automemo(adapters[i:])
        i += 1
    return total

print(automemo(tuple(adapters)))
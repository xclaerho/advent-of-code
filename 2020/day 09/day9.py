numbers = open('input.txt').read().split('\n')
numbers = list(map(lambda x: int(x), numbers))

def first_error(preamble_length, numbers):
    preamble = numbers[:preamble_length]
    sums = []
    for i,num in enumerate(preamble):
        sums.extend([num + numbers[j] for j in range(i+1, i+preamble_length)])
    for num in numbers[preamble_length:]:
        if num not in sums:
            return num
        preamble = preamble[1:]
        sums = sums[(preamble_length-1):]
        sums.extend([i + num for i in preamble])
        preamble.append(num)

e = first_error(25, numbers)
print(e)

def weakness(error, numbers):
    running_sums = [[numbers[0]]]
    for i in range(1, len(numbers)):
        for s in running_sums:
            s.append(numbers[i])
        running_sums.append([numbers[i]])
        running_sums = [x for x in running_sums if sum(x) <= error]
        for x in running_sums:
            if sum(x) == error:
                return min(x)+max(x)

print(weakness(e,numbers))
input = []
with open('input.txt') as fv:
    for number in fv:
        input.append(int(number))

def day_one(input, num_numbers):
    indices = [0]*num_numbers
    indices[-1] = -1
    for i in range(len(indices)-1):
        indices[i] = i

    input.sort()
    found = False

    while not found:
        s = sum([input[i] for i in indices])
        if s == 2020:
            found = True
            nums = [input[i] for i in indices]
            prod = 1
            for num in nums:
                prod *= num
            return prod
        elif s > 2020:
            indices[-1] -= 1
            for i in range(len(indices)-1):
                indices[i] = i
        else:
            for i in range(len(indices) -1):
                if indices[i]+1 != indices[i+1]:
                    indices[i] += 1
                    break

print(day_one(input, 2))
print(day_one(input, 3))
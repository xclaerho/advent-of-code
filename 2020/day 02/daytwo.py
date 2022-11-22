import re

input = []
with open('input.txt') as fv:
    for line in fv:
        splitted = re.split(': |-| ', line)
        input.append([int(splitted[0]), int(splitted[1]), splitted[2], splitted[3].strip()])

def count_valid(input):
    valid = 0
    for password in input:
        count = password[3].count(password[2])
        if count >= password[0] and count <= password[1]:
            valid +=1
    return valid

def count_valid2(input):
    valid = 0
    for password in input:
        ind1 = password[0]-1
        ind2 = password[1]-1
        char = password[2]
        word = password[3]
        if word[ind1] == char and not word[ind2] == char:
            valid+=1
        elif not word[ind1] == char and word[ind2] == char:
            valid +=1
    return valid

print(count_valid(input))
print(count_valid2(input))

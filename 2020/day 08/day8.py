
instructions = open('test.txt').read().split('\n')

def acc_before_loop(instructions, curr, acc, seen):
    while curr != len(instructions)-1:
        if curr in seen:
            return True, acc
        seen.add(curr)
        instruction, number = instructions[curr].split(' ')
        number = int(number)
        if instruction == 'nop':
            curr += 1
        elif instruction == 'acc':
            acc += number
            curr += 1
        else:
            curr += number
    return False, acc

print(acc_before_loop(instructions, 0, 0, set()))

def acc_if_finish(instructions):
    for i, instruction in enumerate(instructions):
        if instruction[:3] == 'nop':
            instructions[i] = instructions[i].replace('nop', 'jmp')
            loop, acc = acc_before_loop(instructions, 0, 0, set())
            if not loop:
                return acc
            instructions[i] = instructions[i].replace('jmp','nop')
        if instruction[:3] == 'jmp':
            instructions[i] = instructions[i].replace('jmp','nop')
            loop, acc = acc_before_loop(instructions, 0, 0, set())
            if not loop:
                return acc
            instructions[i] = instructions[i].replace('nop', 'jmp')
    return False

print(acc_if_finish(instructions))
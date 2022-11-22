mask = 0
memory = dict()

input = open('input.txt').read().split('\n')

for line in input:
    instr, val = line.split('=')
    instr = instr.strip()
    val = val.strip()
    if 'mask' in instr:
        mask = val
    else:
        value = format(int(val), '036b')
        masked = ''.join([i if i!='X' else j for i,j in zip(mask, value)])
        memory[instr] = int(masked, base=2)

print(sum(memory.values()))
#####

def mask_addresses(addr, mask):
    addresses = ['']
    for i,j in zip(addr, mask):
        a = []
        if j == '0':
            for r in addresses:
                a.append(r + i)
        elif j == '1':
            for r in addresses:
                a.append(r + j)
        else:
            for r in addresses:
                a.append(r + '1')
                a.append(r + '0')
        addresses = a
    return addresses

mask = 0
memory = dict()

for line in input:
    instr, val = line.split('=')
    instr = instr.strip()
    val = val.strip()
    if 'mask' in instr:
        mask = val
    else:
        og_addr = format(int(instr.split('[')[1][:-1]), '036b')
        addresses = mask_addresses(og_addr, mask)
        for addr in addresses:
            memory[addr] = int(val)

print(sum(memory.values()))
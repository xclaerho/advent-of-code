pk_1 = 6270530
pk_2 = 14540258

def transform(start, subject_number, loop_size):
    val = start
    for _ in range(loop_size):
        val *= subject_number
        val %= 20201227
    return val

start = 1
loop_size_1 = 0
while start != pk_1:
    start = transform(start, 7, 1)
    loop_size_1 += 1

ek = transform(1, pk_2, loop_size_1)
print(ek)
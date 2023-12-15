def snafu_to_decimal(num):
    decimal = 0
    snafu_map = {'1': 1, '2': 2, '0': 0, '-': -1, '=': -2}
    for i, digit in enumerate(reversed(num)):
        decimal += 5**i * snafu_map[digit]
    return decimal

def decimal_to_snafu(num):
    # first to quinary
    quinary = ''
    while num > 4:
        remainder = num%5
        num = num//5
        quinary = str(remainder) + quinary
    quinary = str(num) + quinary
    # change quinary representation
    snafu = ''
    decimal_map = {1:'1',2:'2',0:'0',-2:'=',-1:'-'}
    carry = 0
    for digit in reversed(quinary):
        num = int(digit) + carry
        if num < -2:
            carry = -1
            snafu = decimal_map[num+5] + snafu
        elif num > 2:
            carry = 1
            snafu = decimal_map[num-5] + snafu
        else:
            snafu = decimal_map[num] + snafu
            carry = 0
    if carry != 0:
        snafu = decimal_map[carry] + snafu
    return snafu

with open('in.txt') as f:
    input = f.read().splitlines()

    sum = sum(snafu_to_decimal(num) for num in input)
    print(sum)
    sum_snafu = decimal_to_snafu(sum)
    print(sum_snafu)

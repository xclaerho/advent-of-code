input = open('input.txt').read().split('\n')
earliest = int(input[0])
busses = input[1].split(',')

wait = 100000000
busid = 0

for bus in busses:
    if bus != 'x':
        bus = int(bus)
        arrival = bus - (earliest % bus)
        if arrival < wait:
            wait = arrival
            busid = bus

print(busid*wait)

## part 2
def solve(a,b,m,n):
    gcd, r, s  = euclid_extended(m,n)
    return (a*s*n+b*r*m)%(m*n), m*n
    
def euclid_extended(m,n):
    if m == 0:
        return n, 0, 1
    gcd, x1, y1 = euclid_extended(n%m, m)
    x = y1 - (n//m) * x1
    y = x1
    return gcd, x, y

a = None
m = None
for i, bus in enumerate(busses):
    if a == None and bus != 'x':
        a = -i
        m = int(bus)
        continue
    if bus != 'x':
        n = int(bus)
        b = -i
        a, m = solve(a,b,m,n)
# check
for i, bus in enumerate(busses):
    if bus != 'x':
        bus = int(bus)
        if a % bus != -i % bus:
            print("problem", i, bus)

print(a)


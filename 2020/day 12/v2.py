import numpy as np

def rotate(waypoint, degrees):
    times = int(degrees/90) % 4
    for i in range(times):
        waypoint = np.array([-waypoint[1],waypoint[0]])
    return waypoint

def distance(point):
    return sum([abs(x) for x in point])

f = {
    'F': lambda point, waypoint, times: (point+waypoint*times, waypoint),
    'N': lambda point, waypoint, times: (point+np.array([0,1]) * times, waypoint),
    'S': lambda point, waypoint, times: (point+np.array([0,-1]) * times, waypoint),
    'W': lambda point, waypoint, times: (point+np.array([-1,0]) * times, waypoint),
    'E': lambda point, waypoint, times: (point+np.array([1,0]) * times, waypoint),
    'R': lambda point, waypoint, degrees: (point, rotate(waypoint, -degrees)),
    'L': lambda point, waypoint, degrees: (point, rotate(waypoint, degrees)),
}

instructions = open('input.txt').read().split('\n')

ship = np.array([0,0])
waypoint= np.array([1,0])
for i in instructions:
    num = int(i[1:])
    ship, waypoint = f[i[0]](ship, waypoint, num)
print(distance(ship))

ship = np.array([0,0])
waypoint= np.array([10,1])
for i in instructions:
    num = int(i[1:])
    if i[0] in ['N', 'S', 'W', 'E']:
        waypoint, ship = f[i[0]](waypoint, ship, num)
    else:
        ship, waypoint = f[i[0]](ship, waypoint, num)
print(distance(ship))
instructions = open('input.txt').read().split('\n')


# [0,0,0,0], 'N', 'F', 3
def move1(moved, facing, instruction, number):
    directions = ['N', 'E', 'S', 'W']
    if instruction == 'R':
        m = number/90
        new_d = int((directions.index(facing)+m)%len(directions))
        return moved, directions[new_d]
    if instruction == 'L':
        m = -number/90
        new_d = int((directions.index(facing)+m)%len(directions))
        return moved, directions[new_d]
    if instruction == 'F':
        moved[directions.index(facing)] += number
        return moved, facing
    moved[directions.index(instruction)] += number
    return moved, facing

begin = [0,0,0,0]
facing = 'E'

for i in instructions:
    begin, facing = move1(begin, facing, i[0], int(i[1:]))

manha_dist = abs(begin[0]-begin[2])+abs(begin[1]-begin[3])
print(manha_dist)

## part 2


def manhattan_distance(point):
    return sum([abs(x) for x in point])

def move(point, direction, distance):
    if direction == 'N':
        point[1] += distance
    elif direction == 'S':
        point[1] -= distance
    elif direction == 'E':
        point[0] += distance
    else:
        point[0] -= distance
    return point

def rotate_ship(facing, direction, degrees):
    directions = ['N', 'E', 'S', 'W']
    diff = degrees/90
    if instruction == 'R':
        facing = int((directions.index(facing)+diff)%len(directions))
        return directions[facing]
    else:
        facing = int((directions.index(facing)-diff)%len(directions))
        return directions[facing]

def rotate_waypoint(waypoint, direction, degrees):
    times = int(degrees/90)
    for i in range(times):
        if direction == 'R':
            waypoint = [waypoint[1],-waypoint[0]]
        else:
            waypoint = [-waypoint[1],waypoint[0]]
    return waypoint

def move_ship_to_waypoint(ship, waypoint):
    return [ship[0]+waypoint[0], ship[1]+waypoint[1]]


ship = [0,0]
waypoint = [10,1]

for i in instructions:
    if i[0] == 'R' or i[0] == 'L':
        waypoint = rotate_waypoint(waypoint, i[0], int(i[1:]))
    elif i[0] == 'F':
        for i in range(int(i[1:])):
            ship = move_ship_to_waypoint(ship, waypoint)
    else:
        waypoint = move(waypoint, i[0], int(i[1:]))

print(manhattan_distance(ship))
import copy
def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()

def is_adjacent(h, t):
    dx = [1,1,1,-1,-1,-1,0,0]
    dy = [1,-1,0,1,-1,0,1,-1]
    #start at h
    if h == t:
        return True
    for i in range(len(dx)):
        temp = (h[0]+dx[i], h[1]+dy[i])
        if temp == t:
            return True
    return False

def get_move_direction(h, t):
    dir = [0,0]
    if h[0] > t[0]:
        dir[0] = 1
    if h[1] > t[1]:
        dir[1] = 1
    if h[0] < t[0]:
        dir[0] = -1
    if h[1] < t[1]:
        dir[1] = -1
    return dir

def move(knots, dir, steps, tail_visits):
    for i in range(steps):
        # comparison_knots = copy.deepcopy(knots)
        for idx in range(len(knots)):
            if idx == len(knots)-1:
                continue
            if idx == 0:
                knots[idx] = (knots[idx][0] + dir[0], knots[idx][1] + dir[1])
            if is_adjacent(knots[idx], knots[idx+1]):
                continue
            movement = get_move_direction(knots[idx], knots[idx+1])
            knots[idx+1] = (knots[idx+1][0] + movement[0], knots[idx+1][1] + movement[1])
        tail_visits.add(knots[-1])
    return knots

def part1():
    d = get_test_data()
    tail_visits = set()
    knots = [(0, 0)] * 2
    for line in d:
        line = line.strip().split(' ')
        if line[0] == 'R':
            knots = move(knots, [1,0], int(line[1]), tail_visits)
        if line[0] == 'L':
            knots = move(knots, [-1,0], int(line[1]), tail_visits)
        if line[0] == 'D':
            knots = move(knots, [0,-1], int(line[1]), tail_visits)
        if line[0] == 'U':
            knots = move(knots, [0,1], int(line[1]), tail_visits)
    print(len(tail_visits))


def part2():
    d = get_data()
    tail_visits = set()
    knots = [(0, 0)] * 10
    for line in d:
        line = line.strip().split(' ')
        if line[0] == 'R':
            knots = move(knots, [1,0], int(line[1]), tail_visits)
        if line[0] == 'L':
            knots = move(knots, [-1,0], int(line[1]), tail_visits)
        if line[0] == 'D':
            knots = move(knots, [0,-1], int(line[1]), tail_visits)
        if line[0] == 'U':
            knots = move(knots, [0,1], int(line[1]), tail_visits)
    print(len(tail_visits))


if __name__ == '__main__':
    part2()
    
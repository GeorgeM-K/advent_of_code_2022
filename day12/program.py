from collections import deque
def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()


def build_matrix(d):
    m = []
    row = []
    for line in d:
        line = line.strip()
        row = []
        for c in line:
            row.append(c)
        m.append(row)
    return m

def in_bounds(pos, m):
    if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(m) and pos[1] < len(m[0]):
        return True
    return False

def part1():
    d = get_data()
    m = build_matrix(d)
    q = deque()
    seen = set()
    for i in range(len(m)):
        a = False
        for j in range(len(m[0])):
            if m[i][j] == 'S':
                q.append((i,j))
                a = True
                break
        if a:
            break

    dist = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while len(q) > 0:
        l = len(q)
        for _ in range(l):
            x, y= q.popleft()
            if (x,y) in seen:
                continue
            seen.add((x,y))
            if m[x][y] == 'E':
                print(dist)
                return
            for i in range(len(dx)):
                new_pos = (x+dx[i], y + dy[i])
                if in_bounds(new_pos, m):
                    x2, y2 = new_pos
                    new_char = m[x2][y2] if m[x2][y2] != 'E' else 'z'
                    old_char = m[x][y] if m[x][y] != 'S' else 'a'
                    if ord(new_char) - (ord(old_char)) <= 1:
                        q.append(new_pos)
        dist+=1
            
                    
            


def part2():
    d = get_data()
    m = build_matrix(d)
    
    starts = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 'S' or m[i][j] == 'a':
                starts.append((i,j))

    min_dist = 1000000000
    for pos in starts:
        q = deque()
        seen = set()
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        q.append(pos)
        dist = 0
        stop = False
        while len(q) > 0:
            l = len(q)
            if stop:
                break
            for _ in range(l):
                x, y= q.popleft()
                if (x,y) in seen:
                    continue
                seen.add((x,y))
                if m[x][y] == 'E':
                    min_dist = min(min_dist, dist)
                    stop = True
                    break
                for i in range(len(dx)):
                    new_pos = (x+dx[i], y + dy[i])
                    if in_bounds(new_pos, m):
                        x2, y2 = new_pos
                        new_char = m[x2][y2] if m[x2][y2] != 'E' else 'z'
                        old_char = m[x][y] if m[x][y] != 'S' else 'a'
                        if ord(new_char) - (ord(old_char)) <= 1:
                            q.append(new_pos)
            dist+=1
    print(min_dist)


if __name__ == '__main__':
    part2()
    
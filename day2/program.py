def get_data():
    return open('data.txt', 'r').readlines()

#rock: 1
# paper: 2
# scissors: 3 


def get_points(mm, tm):
    base_points = 0
    if mm == 'X':
        base_points = 0
    elif mm == 'Y':
        base_points = 3
    elif mm == 'Z':
        base_points = 6
    
    if mm == 'X' and tm == 'A':
        base_points += 3
    elif mm == 'X' and tm == 'B':
        base_points += 1
    elif mm == 'X' and tm == 'C':
        base_points += 2
    elif mm == 'Y' and tm == 'A':
        base_points += 1
    elif mm == 'Y' and tm == 'B':
        base_points += 2
    elif mm == 'Y' and tm == 'C':
        base_points += 3
    elif mm == 'Z' and tm == 'A':
        base_points += 2
    elif mm == 'Z' and tm == 'B':
        base_points += 3
    elif mm == 'Z' and tm == 'C':
        base_points += 1
    return base_points

def part1():
    d = get_data()
    s = 0
    for line in d:
        tm, mm = line.strip().split(' ')
        s += get_points(mm, tm)
    print(s)


if __name__ == '__main__':
    part1()
def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()


def part1():
    d = get_test_data()
    s = 0
    cycle =1
    x = 1
    important_cycles = [20, 60, 100, 140, 180, 220]
    for line in d:
        instruction = line.strip().split(' ')
        if instruction[0] == 'noop':
            cycle += 1
            if cycle in important_cycles:
                s += (x * cycle)
        else:
            for i in range(2):
                if i == 1:
                    x += int(instruction[1])
                cycle+=1
                if cycle in important_cycles:
                    s += (x * cycle)
    print(s)            

def get_sprite_pos(x):
    return [x-1, x, x+1]

def update_crt(cur_row, crt, x):
    cur_update = len(cur_row)
    if cur_update in get_sprite_pos(x):
        cur_row.append('#')
    else:
        cur_row.append('.')
    if len(cur_row) == 40:
        crt.append(cur_row)
        cur_row = []
    return cur_row, crt
def part2():
    d = get_data()
    s = 0
    cycle =1
    x = 1
    crt = []
    cur_row = []
    important_cycles = [20, 60, 100, 140, 180, 220]
    for line in d:
        instruction = line.strip().split(' ')
        if instruction[0] == 'noop':
            cur_row, crt = update_crt(cur_row,crt,x)
            cycle += 1
            if cycle in important_cycles:
                s += (x * cycle)
        else:
            for i in range(2):
                cur_row, crt = update_crt(cur_row,crt,x)
                if i == 1:
                    x += int(instruction[1])
                cycle+=1
                if cycle in important_cycles:
                    s += (x * cycle)
    for row in crt:
        print(''.join(row))    


if __name__ == '__main__':
    part2()
    
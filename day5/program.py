def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()


def get_stacks_and_moves(data):
    stack_info = []
    moves = []
    done_stack = False
    for line in data:
        if len(line) == 1:
            done_stack = True
            continue
        if not done_stack:
            stack_info.append(line)
        else:
            moves.append(line.strip())

    stack_idxs = []
    i = 0
    for c in stack_info[-1]:
        if c.isdigit():
            stack_idxs.append(i)
        i+=1
    stacks = []
    for i in range(len(stack_idxs)):
        stacks.append([])

    for data_idx in range(len(stack_info)-2, -1, -1):
        info = stack_info[data_idx]
        index = 0
        for i in stack_idxs:
            if info[i].isalpha():
                stacks[index].append(info[i])
            index+=1
    return stacks, moves



def part1():
    d = get_data()
    stacks, moves = get_stacks_and_moves(d)
    for move in moves:
        directions = move.split(' ')
        amount, start, end = int(directions[1]), int(directions[3]), int(directions[5])
        start-=1
        end-=1
        while amount > 0:
            stacks[end].append(stacks[start].pop())
            amount -=1
    
    tbr = ''
    for stack in stacks:
        tbr+=stack[-1]
    print(tbr)


def part2():
    d = get_data()
    stacks, moves = get_stacks_and_moves(d)
    for move in moves:
        directions = move.split(' ')
        amount, start, end = int(directions[1]), int(directions[3]), int(directions[5])
        start-=1
        end-=1
        temp = []
        while amount > 0:
            temp.append(stacks[start].pop())
            amount -=1
        while(len(temp) > 0):
            stacks[end].append(temp.pop())
    
    tbr = ''
    for stack in stacks:
        tbr+=stack[-1]
    print(tbr)


if __name__ == '__main__':
    part2()
import itertools
from functools import cmp_to_key
def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()


def compare(left, right):
    lesser = 0
    for l, r in itertools.zip_longest(left, right):
        if type(l) == list and type(r) == list:
            lesser = compare(l, r)
        elif type(l) == list and type(r) == int:
            lesser = compare(l, [r])
        elif type(l) == int and type(r) == list:
            lesser = compare([l], r)
        elif type(l) == int and type(r) == int:
            if l < r:
                lesser = -1
            if l == r:
                lesser = 0
            if l > r:
                lesser = 1
        elif l is None and r is not None:
            lesser = -1
            return -1
        elif l is not None and r is None:
            lesser = 1
            return 1
        if lesser in (-1, 1):
            return lesser
    return lesser


def part1():
    d = get_data()            
    left =None
    right = None
    right_idxs = []
    cur_idx = 1
    for line in d:
        line = line.strip()
        
        if len(line) < 1:
            cur_idx += 1
            left, right = None, None
        elif left is not None:
            right = eval(line)
            lesser = compare(left, right)
            if lesser == -1:
                print("correct", left, right)
                right_idxs.append(cur_idx)
        else:
            left = eval(line)
    print(sum(right_idxs))

def part2():
    d = get_data()
    left =None
    right = None
    right_idxs = []
    packets = []
    cur_idx = 1
    for line in d:
        line = line.strip()
        
        if len(line) < 1:
            cur_idx += 1
            left, right = None, None
        elif left is not None:
            right = eval(line)
            packets.append(left)
            packets.append(right)
        else:
            left = eval(line)
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare))
    locations = []
    for idx, packet in enumerate(packets):
        if packet in ([[2]], [[6]]):
            locations.append(idx+1)
    print(locations[0] * locations[1])



if __name__ == '__main__':
    part2()
    # l = []
    # r = [1,1,5,1,1]
    # print(compare(l, r))
    
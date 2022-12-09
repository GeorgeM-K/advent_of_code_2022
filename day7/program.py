from collections import deque
def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.contents = []
        self.parent = parent

sum = 0

def iterate_directory(directory, threshold, dir_sizes=None):
    global sum
    dir_sum = 0
    for item in directory.contents:
        if type(item) is Directory:
            dir_sum += iterate_directory(item, threshold, dir_sizes=dir_sizes)
        else:
            dir_sum += int(item)
    if dir_sum < threshold:
        sum+=dir_sum
    if type(dir_sizes) == list:
        dir_sizes.append(dir_sum)
    return dir_sum


def part1():
    d = get_data()
    root = Directory('/', None)
    cur_dir = root
    for line in d:
        line = line.strip()
        if len(line) < 1:
            continue
        if line.startswith('$'):
            line = line.split(' ')
            if line[1] == 'ls':
                continue
            if line[1] == 'cd':
                if line[2] == '/':
                    cur_dir = root
                elif line[2] == '..':
                    cur_dir = cur_dir.parent
                else:
                    for item in cur_dir.contents:
                        if type(item) == Directory and item.name == line[2]:
                            cur_dir = item
                            break
        else:
            line = line.split(' ')
            if line[0] == 'dir':
                cur_dir.contents.append(Directory(line[1], cur_dir))
            else:
                cur_dir.contents.append(line[0])
            
    iterate_directory(root, 100000)
    global sum
    print(sum)

def part2():
    d = get_data()
    root = Directory('/', None)
    cur_dir = root
    for line in d:
        line = line.strip()
        if len(line) < 1:
            continue
        if line.startswith('$'):
            line = line.split(' ')
            if line[1] == 'ls':
                continue
            if line[1] == 'cd':
                if line[2] == '/':
                    cur_dir = root
                elif line[2] == '..':
                    cur_dir = cur_dir.parent
                else:
                    for item in cur_dir.contents:
                        if type(item) == Directory and item.name == line[2]:
                            cur_dir = item
                            break
        else:
            line = line.split(' ')
            if line[0] == 'dir':
                cur_dir.contents.append(Directory(line[1], cur_dir))
            else:
                cur_dir.contents.append(line[0])
    dir_sizes = []
    iterate_directory(root, 100000, dir_sizes=dir_sizes)
    dir_sizes.sort()
    used_space = dir_sizes[-1]
    total_space = 70000000
    avail = total_space-used_space
    needed = 30000000 - avail
    for size in dir_sizes:
        if size >= needed:
            print(size)
            break


if __name__ == '__main__':
    part2()
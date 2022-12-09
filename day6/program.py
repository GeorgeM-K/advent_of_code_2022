from collections import deque
def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()


def part1():
    d = get_test_data()
    s = d[0]
    window = deque()
    for i in range(len(s)):
        window.append(s[i])
        if len(window) == 4:
            if len(set(window)) == 4:
                return i+1
            else:
                window.popleft()



def part2():
    d = get_data()
    s = d[0]
    window = deque()
    for i in range(len(s)):
        window.append(s[i])
        if len(window) == 14:
            if len(set(window)) == 14:
                return i+1
            else:
                window.popleft()


if __name__ == '__main__':
    print(part2())
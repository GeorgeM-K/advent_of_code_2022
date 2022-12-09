def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()

def get_priority(c):
    priority = ord(c)
    if priority >= 97:
        priority = priority -97 + 1
    elif priority >= 65:
        priority = priority -65 + 27
    return priority

def part1():
    d = get_data()
    s = 0
    for bag in d:
        bag = bag.strip()
        common = set()
        c1 = bag[:int(len(bag)/2)]
        c2 = bag[int(len(bag)/2):]
        
        for c in c1:
            if c in c2:
                common.add(c)
        for c in common:
            s+=get_priority(c)
    print(s)

def part2():
    d = get_data()
    s = 0
    count_group = 0
    identifiers = []
    grouped_rucksacks = []
    for bag in d:
        bag = bag.strip()
        grouped_rucksacks.append(bag)
        count_group +=1
        if count_group == 3:
            for c in grouped_rucksacks[0]:
                if c in grouped_rucksacks[1] and c in grouped_rucksacks[2]:
                    identifiers.append(c)
                    break
            grouped_rucksacks.clear()
            count_group = 0
    for badge in identifiers:
        s += get_priority(badge)
    print(s)

if __name__ == '__main__':
    part2()
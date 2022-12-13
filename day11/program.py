import math
from typing import List
def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()

class Monkey:
    def __init__(self):
        self.items = []
        self.op_a = None
        self.op_b = None
        self.action = None
        self.rule = ""
        self.tru = 0
        self.fal = 0
        self.count = 0

def parse_input(d) -> List[Monkey]:
    monkeys = []
    cur_monkey = None
    for line in d:
        line = line.strip()
        if len(line) < 1:
            monkeys.append(cur_monkey)
        elif line.startswith("Monkey"):
            cur_monkey = Monkey()
        elif line.startswith("Starting"):
            s = line.split(":")[1].strip().split(", ")
            items = [int(item) for item in s]
            cur_monkey.items = items
        elif line.startswith("Operation"):
            s = line.split("Operation: new = ")[1].split(" ")
            cur_monkey.op_a = s[0]
            cur_monkey.op_b = s[2]
            cur_monkey.action = s[1]
        elif line.startswith("Test"):
            cur_monkey.rule = int(line.split(" ")[-1])
        elif line.startswith("If true"):
            cur_monkey.tru = int(line.strip().split(" ")[-1])
        else:
            cur_monkey.fal = int(line.strip().split(" ")[-1])
    monkeys.append(cur_monkey)
    return monkeys
            
        
def update_worry_level(base_level, op_a, op_b, operation, p2=False, divs = None):
    if op_a == 'old':
        op_a = base_level
    else:
        op_a = int(op_a)
    if op_b == 'old':
        op_b = base_level
    else:
        op_b = int(op_b)

    if p2 and divs:
        if operation == '*':
            return (op_a * op_b) % divs
        else:
            return (op_a + op_b) % divs
    
    if operation == '*':
        return math.floor((op_a * op_b)/3)
    else:
        return math.floor((op_a + op_b)/3)
    
    

def check_worry(level: int, rule: int) -> bool:
    return level % rule == 0

def part1():
    d = get_test_data()
    monkeys = parse_input(d)
    for i in range(20):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                monkey.count += 1
                item = monkey.items.pop()
                item = update_worry_level(item, monkey.op_a, monkey.op_b, monkey.action)
                if check_worry(item, monkey.rule):
                    monkeys[monkey.tru].items.append(item)
                else:
                    monkeys[monkey.fal].items.append(item)
    monkeys.sort(key = lambda x: x.count, reverse = True)

    print(monkeys[0].count * monkeys[1].count)



def part2():
    d = get_data()
    monkeys = parse_input(d)
    divs = 1
    for monkey in monkeys:
        divs *= monkey.rule
    for i in range(10000):
        for monkey in monkeys:
            while(len(monkey.items) > 0):
                monkey.count += 1
                item = monkey.items.pop()
                item = update_worry_level(item, monkey.op_a, monkey.op_b, monkey.action, p2=True, divs = divs)
                if check_worry(item, monkey.rule):
                    monkeys[monkey.tru].items.append(item)
                else:
                    monkeys[monkey.fal].items.append(item)
    monkeys.sort(key = lambda x: x.count, reverse = True)

    print(monkeys[0].count * monkeys[1].count)


if __name__ == '__main__':
    part2()
    
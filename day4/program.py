def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()

def part1():
    d = get_data()

    complete_cover = 0

    for pair in d:
        p1, p2 = pair.strip().split(',')
        min1, max1 = int(p1.split('-')[0]), int(p1.split('-')[1])
        min2, max2 = int(p2.split('-')[0]), int(p2.split('-')[1])

        if min1 <= min2 and max1 >= max2:
            complete_cover+=1
        elif min2 <= min1 and max2 >= max1:
            complete_cover +=1

    print(complete_cover)

def part2():
    d = get_data()

    overlap = 0

    for pair in d:
        p1, p2 = pair.strip().split(',')
        min1, max1 = int(p1.split('-')[0]), int(p1.split('-')[1])
        min2, max2 = int(p2.split('-')[0]), int(p2.split('-')[1])

        #complete overlap
        if min1 <= min2 and max1 >= max2:
            overlap+=1
        elif min2 <= min1 and max2 >= max1:
            overlap +=1

        #partial overlap
        elif min1 <= min2 and max1 >= min2:
            overlap+=1
        elif max1 >= max2 and min1 <= max2:
            overlap+=1
        elif min2 <= min1 and max2 >= min1:
            overlap+=1
        elif max2 >= max1 and min2 <= max1:
            overlap+=1
        
    print(overlap)
if __name__ == '__main__':
    part2()
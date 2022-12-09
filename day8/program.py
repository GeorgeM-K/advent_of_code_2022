def get_data():
    return open('data.txt', 'r').readlines()

def get_test_data():
    return open('test_data.txt', 'r').readlines()

def on_edge(matrix, i, j):
    return i == 0 or j == 0 or i == len(matrix)-1 or j == len(matrix[0])-1

def in_bounds(matrix, i, j):
    return i>= 0 and j>=0 and i < len(matrix) and j < len(matrix[0]) 

def generate_matrix_and_seen(data):
    matrix, seen = [], []
    for line in data:
        cur = []
        s = []
        for c in line.strip():
            cur.append(int(c))
            s.append(False)
        matrix.append(cur)
        seen.append(s)
    return matrix, seen


def part1():
    d = get_data()
    matrix, seen = generate_matrix_and_seen(d)
    visible = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if on_edge(matrix, i, j):
                visible+=1
                continue
            for z in range(len(dx)):
                cur_x = i + dx[z]
                cur_y = j + dy[z]
                is_visible = matrix[i][j] > matrix[cur_x][cur_y]
                while True:
                    if matrix[i][j] <= matrix[cur_x][cur_y]:
                        is_visible = False
                        break
                    if not is_visible:
                        break
                    if on_edge(matrix, cur_x, cur_y):
                        break
                    cur_x += dx[z]
                    cur_y += dy[z]
                if is_visible:
                    visible += 1
                    break
    print(visible)





def part2():
    d = get_data()
    matrix, seen = generate_matrix_and_seen(d)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    best_score = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            cur_score = []
            for z in range(len(dx)):
                cur_x = i + dx[z]
                cur_y = j + dy[z]
                trees_seen = 1
                if not in_bounds(matrix, cur_x, cur_y):
                    cur_score.append(0)
                    continue
                is_visible = matrix[i][j] > matrix[cur_x][cur_y]
                while True:
                    if matrix[i][j] <= matrix[cur_x][cur_y]:
                        is_visible = False
                        break
                    if not is_visible:
                        break
                    if on_edge(matrix, cur_x, cur_y):
                        break
                    cur_x += dx[z]
                    cur_y += dy[z]
                    trees_seen += 1
                cur_score.append(trees_seen)
            score = 1
            for s in cur_score:
                score *= s
            best_score = max(score, best_score)
    print(best_score)



if __name__ == '__main__':
    part2()
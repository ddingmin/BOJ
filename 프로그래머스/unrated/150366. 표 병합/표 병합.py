# cells에 key값(index)을 적어 관리
cells = [[0] * 51 for _ in range(51)]
index = 1
# 1부터 키값 할당
for i in range(1, 51):
    for j in range(1, 51):
        cells[i][j] = index
        index += 1
store = {}
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def change(r, c, value):
    store[cells[r][c]] = value

def get_target(key):
    targets = []
    for i in range(1, 51):
        for j in range(1, 51):
            if cells[i][j] == key: targets.append([i, j])
    return targets

def update(command):
    # print("update")
    # "UPDATE r c value" 형태
    if len(command) == 4:
        ud, r, c, value = command
        r, c = int(r), int(c)
        change(r, c, value)
    # "UPDATE value1 value2" 형태
    if len(command) == 3:
        ud, find_value, change_value = command
        for i in range(1, 51):
            for j in range(1, 51):
                if cells[i][j] in store and store[cells[i][j]] == find_value:
                    change(i, j, change_value)

def merge(command):
    # print("merge")
    # "MERGE r1 c1 r2 c2" 형태
    mg, r1, c1, r2, c2 = command
    r1, r2, c1, c2 = int(r1), int(r2), int(c1), int(c2)
    # 같은 좌표의 경우 무시
    if r1 == r2 and c1 == c2: return
    # 첫번째 값이 존재하면 첫번째 값으로 머지
    if cells[r1][c1] in store:
        # 두번째 키값을 가지는 좌표를 구하기
        targets = get_target(cells[r2][c2])
        for x, y in targets:
            cells[x][y] = cells[r1][c1]
    # 첫번째 값이 없다면 두번째 값으로 머지
    elif cells[r2][c2] in store:
        # 첫번째 키값을 가지는 좌표를 구하기
        targets = get_target(cells[r1][c1])
        for x, y in targets:
            cells[x][y] = cells[r2][c2]
    else:
        # 두번째 키값을 가지는 좌표를 구하기
        targets = get_target(cells[r2][c2])
        for x, y in targets:
            cells[x][y] = cells[r1][c1]
        

def ummerge(command):
    # print("unmerge")
    global index
    # "UNMERGE r c" 형태
    um, r, c = command
    r, c = int(r), int(c)
    # 완전 탐색하며 r,c와 같은 키값을 같는 값들을 찾아 키값을 새로 할당
    for i in range(1, 51):
        for j in range(1, 51):
            if i == r and j == c: continue
            if cells[i][j] == cells[r][c]:
                cells[i][j] = index
                index += 1

def print_cell(command):
    # print("print")
    pt, r, c = command
    r, c = int(r), int(c)
    
    if cells[r][c] in store:
        return store[cells[r][c]]
    else:
        return "EMPTY"
                
def solution(commands):
    answer = []
    for command in commands:
        command = command.split()
        if command[0] == "UPDATE": update(command)
        elif command[0] == "MERGE": merge(command)
        elif command[0] == "UNMERGE": ummerge(command)
        elif command[0] == "PRINT": 
            answer.append(print_cell(command))

    return answer
import sys
input = sys.stdin.readline
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
see = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            see += 1
        if 1 <= maps[i][j] <= 5:
            cctvs.append([maps[i][j], [i, j]])

answer = see
def dfs(cctvs_dir, depth):
    global answer
    # 방향을 다 정함
    if depth == len(cctvs):
        # 감시범위 만들기
        new_map = [[0] * m for _ in range(n)]
        for start, i, j in cctvs_dir:
            make_range(new_map, i, j, start)
        answer = min(answer, get_space(new_map))
        return
    
    x, y = cctvs[depth][1]
    if cctvs[depth][0] == 5:
        cctvs_dir.append([0, x, y])
        dfs(cctvs_dir, depth + 1)
        cctvs_dir.pop()
    elif cctvs[depth][0] == 2:
        for d in range(2):
            cctvs_dir.append([d, x, y])
            dfs(cctvs_dir, depth + 1)
            cctvs_dir.pop()
    else:
        for d in range(4):
            cctvs_dir.append([d, x, y])
            dfs(cctvs_dir, depth + 1)
            cctvs_dir.pop()
            

def make_line(new_map, i, j, d):
    dist = 1
    while 1:
        x, y = i + dx[d] * dist, j + dy[d] * dist
        if not(0 <= x < n and 0 <= y < m): break
        if maps[x][y] != 6:
            if maps[x][y] == 0:
                new_map[x][y] = 9
            dist += 1
        else:
            break

def make_range(new_map, i, j, start):
    if maps[i][j] == 1:
        make_line(new_map, i, j, start)
    elif maps[i][j] == 2:
        make_line(new_map, i, j, start)
        make_line(new_map, i, j, (start + 2) % 4)
    elif maps[i][j] == 3:
        make_line(new_map, i, j, start)
        make_line(new_map, i, j, (start + 1) % 4)
    elif maps[i][j] == 4:
        make_line(new_map, i, j, start)
        make_line(new_map, i, j, (start + 1) % 4)
        make_line(new_map, i, j, (start + 2) % 4)
    elif maps[i][j] == 5:
        make_line(new_map, i, j, start)
        make_line(new_map, i, j, (start + 1) % 4)
        make_line(new_map, i, j, (start + 2) % 4)
        make_line(new_map, i, j, (start + 3) % 4)
        
        


def get_space(new_map):
    count = 0
    for i in range(n):
        for j in range(m):
            if new_map[i][j] == 9:
                count += 1
    # for k in new_map:
    #     print(*k)
    # print()
    # print(see, count)
    
    return see - count
    
dfs([], 0)
print(answer)
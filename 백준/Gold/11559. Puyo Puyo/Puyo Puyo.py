import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maps = [list(input().strip()) for _ in range(12)]

def find_pop_blocks():
    visit = [[0] * 6 for _ in range(12)]
    pop_blocks = []
    for i in range(12):
        for j in range(6):
            if maps[i][j] == '.': continue
            if visit[i][j] == 1: continue
            tmp = [[i, j]]
            q = deque()
            q.append([i, j])
            visit[i][j] = 1
            while q:
                i, j = q.popleft()
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if not(0 <= x < 12 and 0 <= y < 6): continue
                    if visit[x][y] == 1: continue
                    if maps[i][j] == maps[x][y]:
                        tmp.append([x, y])
                        q.append([x, y])
                        visit[x][y] = 1
            if len(tmp) >= 4:
                pop_blocks += tmp
    # 터질 블록이 있다면
    if len(pop_blocks):
        for i, j in pop_blocks:
            maps[i][j] = '.'
        return 1
    else:
        return 0

def drop_blocks():
    for j in range(6):
        blocks = deque()
        for i in range(11, -1, -1):
            if maps[i][j] == '.': continue
            blocks.append(maps[i][j])
        for i in range(11, -1, -1):
            if blocks:
                maps[i][j] = blocks.popleft()
            else:
                maps[i][j] = '.'

# 게임 시작
count = 0
while 1:
    tmp = find_pop_blocks()
    if not tmp: break
    count += tmp
    drop_blocks()
print(count)
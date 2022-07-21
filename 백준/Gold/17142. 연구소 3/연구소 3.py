# BOJ 17141
from collections import deque

n, virusNum = map(int, input().split())

arr = []
start = []
wall = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# Input
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 2: start.append((i, j))
        if arr[i][j] == 1: wall.append((i, j))

# 방문 노드 초기화 함수
def mkvisit():
    visit = [[0] * n for _ in range(n)]
    for i, j in wall:
        visit[i][j] = 1
    return visit

setXY = []

def selectXY(out, l):
    if len(out) == virusNum:
        setXY.append(out.copy())
        return
    else:
        for k in range(l, len(start)):
            i, j = start[k]
            out.append((i, j))
            selectXY(out, k + 1)
            out.pop()

def bfs(startList):
    q = deque()
    visit = mkvisit()

    for i, j in startList:
        q.append((i, j, 1))
        visit[i][j] = 1

    while q:
        i, j, second = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < n): continue
            if visit[x][y] >= 1 or arr[x][y] == 1: continue
            if arr[x][y] == 2 and visit[x][y] == 0:
                q.append((x, y, second + 1))
                visit[x][y] = -1
            if visit[x][y] == 0:
                visit[x][y] = second + 1
                q.append((x, y, second + 1))

    ans = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0: return -1
            else: ans = max(ans, visit[i][j])
    return ans - 1

selectXY([], 0)

ans = 3000
flag = False
for k in setXY:
    t = bfs(k)
    if t != -1: ans = min(ans, t)

if ans == 3000: ans = -1
print(ans)
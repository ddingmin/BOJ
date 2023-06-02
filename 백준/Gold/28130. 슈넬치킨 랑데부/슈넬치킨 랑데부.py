import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    
n, m = map(int, input().split())

maps = []
A = None
B = None
for i in range(n):
    maps.append(list(input().strip()))
    for j in range(m):
        if maps[i][j] == 'A':
            A = [i, j]
        elif maps[i][j] == 'B':
            B = [i, j]

visit = [[-1] * m for _ in range(n)]


# B 먼저 돌려서 시간 계산
q = deque()
q.append(A)
visit[A[0]][A[1]] = 0

while q:
    i, j = q.popleft()
    for dir in range(4):
        x, y = i + dx[dir], j + dy[dir]
        if not(0 <= x < n and 0 <= y < m): continue
        if visit[x][y] > -1 or maps[x][y] == 'G': continue
        visit[x][y] = visit[i][j] + 1
        q.append([x, y])

i, j = B
# 방향 세팅
if (i == 0 and j != m - 1):
    dir = 0
elif (i != n - 1 and j == m - 1):
    dir = 1
elif (i == n - 1 and j != 0):
    dir = 2
else:
    dir = 3

move = 0
for _ in range(n * m):
    x, y = i + dx[dir], j + dy[dir]
    if not(0 <= x < n and 0 <= y < m):
        dir = (dir + 1) % 4
        x, y = i + dx[dir], j + dy[dir]
    i, j = x, y
    move += 1
    if visit[x][y] == -1: continue
    if visit[x][y] <= move and visit[x][y] % 2 == move % 2:
        print(move)
        exit(0)
print(-1)

# BOJ 2589
from collections import deque

n, m = map(int, input().split())
arr = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    arr.append(list(input()))

def bfs(i, j):
    q = deque()
    q.append((i, j, 1))
    visit[i][j] = 1
    temp = 0
    while q:
        i, j, time = q.popleft()
        for k in range(4):
            x, y = dx[k] + i, dy[k] + j
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y] >= 1: continue
            if arr[x][y] == 'L':
                visit[x][y] = time + 1
                q.append((x, y, time + 1))
                temp = max(temp, time)
    return temp

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visit = [[0] * m for _ in range(n)]
            ans = max(bfs(i, j), ans)
print(ans)
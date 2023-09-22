import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# input
n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visit = [[0] * m for _ in range(n)]
for _ in range(k):
    sy, sx, ey, ex = map(int, input().split())
    for i in range(sx, ex):
        for j in range(sy, ey):
            arr[i][j] = 1


def bfs(i, j):
    size = 1
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not (0 <= x < n and 0 <= y < m): continue
            if visit[x][y] or arr[x][y] == 1: continue
            visit[x][y] = 1
            size += 1
            q.append([x, y])
    return size


ans = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visit[i][j] == 0:
            ans.append(bfs(i, j))

print(len(ans))
print(*sorted(ans))

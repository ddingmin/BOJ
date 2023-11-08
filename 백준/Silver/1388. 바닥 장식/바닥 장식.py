import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visit = [[0] * m for _ in range(n)]


def bfs(i, j, shape):
    q = deque()
    q.append([i, j])
    visit[i][j] = 1

    if shape == '-':
        dx, dy = [0, 0], [-1, 1]
    else:
        dx, dy = [-1, 1], [0, 0]

    while q:
        i, j = q.popleft()
        for k in range(2):
            x, y = i + dx[k], j + dy[k]
            if not (0 <= x < n and 0 <= y < m): continue
            if visit[x][y] == 0 and arr[i][j] == arr[x][y]:
                visit[x][y] = 1
                q.append([x, y])


ans = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            ans += 1
            bfs(i, j, arr[i][j])

print(ans)

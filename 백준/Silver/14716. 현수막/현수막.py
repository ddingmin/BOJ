import sys
from collections import deque

input = sys.stdin.readline


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visit[i][j] = 1
    while q:
        i, j = q.popleft()
        for dir in range(8):
            x, y = i + dx[dir], j + dy[dir]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y]: continue
            if arr[x][y] == 1:
                visit[x][y] = 1
                q.append([x, y])
    return 1

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visit[i][j] == 0:
            ans += bfs(i, j)
print(ans)
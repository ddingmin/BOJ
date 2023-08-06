import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
h, w, sx, sy, fx, fy = map(int, input().split())
sx -= 1
sy -= 1
fx -= 1
fy -= 1

def can_go(i, j):
    for ii in range(h):
        if arr[i + ii][j] == 1: return False
    for ii in range(h):
        if arr[i + ii][j + w - 1] == 1: return False
    for jj in range(w):
        if arr[i][j + jj] == 1: return False
    for jj in range(w):
        if arr[i + h - 1][j + jj] == 1: return False
    return True


ans = 0
q = deque()
q.append([sx, sy])
visit = [[0] * m for _ in range(n)]
visit[sx][sy] = 1

while q:
    for _ in range(len(q)):
        i, j = q.popleft()
        if i == fx and j == fy:
            print(ans)
            exit()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not (0 <= x < n and 0 <= y < m): continue
            if not (0 <= x + h - 1 < n and 0 <= y + w - 1 < m): continue
            if visit[x][y] == 0 and can_go(x, y):
                q.append([x, y])
                visit[x][y] = 1
    ans += 1


print(-1)

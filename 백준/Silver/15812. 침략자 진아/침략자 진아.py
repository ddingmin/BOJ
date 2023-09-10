import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# input
n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

village = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            village += 1

# solve
def find(i, j, ii, jj, village):
    if village == 0:
        return 0
    visit = [[0] * m for _ in range(n)]
    visit[i][j] = 1
    visit[ii][jj] = 1
    q = deque()
    q.append([i, j])
    q.append([ii, jj])

    day = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < n and 0 <= y < m): continue
                if visit[x][y] == 0:
                    visit[x][y] = 1
                    q.append([x, y])
                    if arr[x][y] == 1:
                        village -= 1
        day += 1
        if village == 0:
            return day
    return day

ans = float('inf')

pmlst = [i for i in range(0, 20)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            continue
        for ii in range(n):
            for jj in range(m):
                if i == ii and j == jj: continue
                if arr[ii][jj] == 1: continue
                ans = min(ans, find(i, j, ii, jj, village))

print(ans)
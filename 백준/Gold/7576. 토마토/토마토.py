from collections import deque

m, n = map(int,input().split())
arr = []
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0 ,0], [0, 0, -1, 1]
tomato = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 1: tomato.append((i, j))

def solve():
    q = deque()
    for i, j in tomato:
        q.append((i, j))
        visit[i][j] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y] == 0 and arr[x][y] != -1:
                if arr[x][y] == 0:
                    arr[x][y] = arr[i][j] + 1
                    visit[x][y] = 1
                    q.append((x, y))
                elif arr[i][j] + 1 <= arr[x][y]:
                    arr[x][y] = arr[i][j] + 1
                    visit[x][y] = 1
                    q.append((x, y))

solve()

flag = False

ans = 0
for k in arr:
    for l in k:
        if l == 0: flag = True
        else: ans = max(ans, l)

if flag: print(-1)
else: print(ans - 1)

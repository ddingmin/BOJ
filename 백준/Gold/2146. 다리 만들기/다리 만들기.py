from collections import deque
n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

level = 2

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            q = deque()
            q.append((i, j))
            arr[i][j] = level

            while q:
                i, j = q.popleft()
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if not(0 <= x < n and 0 <= y < n): continue
                    if arr[x][y] == 1:
                        arr[x][y] = level
                        q.append((x, y))
            level += 1

def find_dist(i, j):
    now = arr[i][j]
    q = deque()
    q.append((i, j, 0))
    visit = [[0] * n for _ in range(n)]
    visit[i][j] = 1
    while q:
        i, j, d = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < n): continue
            if visit[x][y] == 1: continue
            if arr[x][y] > 0:
                if arr[x][y] != now:
                    return d
            if arr[x][y] == 0:
                visit[x][y] = 1
                q.append((x, y, d + 1))
    return float('inf')

ans = float('inf')
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            ans = min(ans, find_dist(i, j))
print(ans)

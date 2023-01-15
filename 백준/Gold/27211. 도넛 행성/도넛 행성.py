from collections import deque
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# 범위를 넘어간 경우 좌표 최적화
def over(x, y):
    if x == -1:
        x = n - 1
    if x == n:
        x = 0
    if y == -1:
        y = m - 1
    if y == m:
        y = 0
    return x, y

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visit[sx][sy] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            x, y = over(x, y)
            # print(x, y)
            if arr[x][y] == 0 and visit[x][y] == 0:
                visit[x][y] = 1
                q.append([x, y])

ans = 0
visit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visit[i][j] == 0:
            bfs(i, j)
            ans += 1
print(ans)
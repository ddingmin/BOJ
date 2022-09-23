from collections import deque

input = __import__('sys').stdin.readline

m, n = map(int, input().split())
arr = []
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(n):
    arr.append(list(input().strip()))

def bfs(color, i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    power = 1
    while q:
        i, j = q.popleft()
        for dir in range(4):
            x, y = i + dx[dir], j + dy[dir]
            if not (0 <= x < n and 0 <= y < m): continue
            if visit[x][y] == 0 and arr[x][y] == color:
                q.append((x, y))
                visit[x][y] = 1
                power += 1
    return power * power

black = 0
white = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            if arr[i][j] == 'B': black += bfs(arr[i][j], i, j)
            elif arr[i][j] == 'W': white += bfs(arr[i][j], i, j)

print(white, black)
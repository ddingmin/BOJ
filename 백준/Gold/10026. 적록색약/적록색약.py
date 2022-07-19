from collections import deque

n = int(input())

visit = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
arr = []
for i in range(n):
    arr.append(list(input()))

def bfs(x, y):
    if visit[x][y] == 1: return 0
    q = deque()
    c = arr[x][y]
    q.append((x, y, c))
    visit[x][y] = 1
    while q:
        i, j, c = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < n): continue
            if visit[x][y] == 1: continue
            if arr[x][y] == c:
                visit[x][y] = 1
                q.append((x, y, c))
    return 1

def bfs2(x, y):
    if visit[x][y] == 1: return 0
    q = deque()
    c = arr[x][y]
    if c == 'R' or c == 'G': c = "RG"
    q.append((x, y, c))
    visit[x][y] = 1
    while q:
        i, j, c = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < n): continue
            if visit[x][y] == 1: continue
            if c == "RG":
                if arr[x][y] == 'R' or arr[x][y] == 'G':
                    visit[x][y] = 1
                    q.append((x, y, c))

            elif arr[x][y] == c:
                visit[x][y] = 1
                q.append((x, y, c))

    return 1


ans1, ans2 = 0, 0
for i in range(n):
    for j in range(n):
        ans1 += bfs(i, j)
visit = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans2 += bfs2(i, j)

print(ans1, ans2)


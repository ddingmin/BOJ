from collections import deque
#input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))
visit = [[-1]* m for _ in range(n)]
# visit 배열이 거리를 가지도록 함.
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

ans = 1

def bfs(i, j):
    global ans
    if visit[i][j] > 0 or arr[i][j] == 0: return
    visit[i][j] = 1
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            print(visit[x][y])
            return
        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            if not(0 <= tx < n and 0 <= ty < m): continue
            if visit[tx][ty] > 0 or arr[tx][ty] == 0: continue
            visit[tx][ty] = visit[x][y] + 1
            q.append((tx, ty))
bfs(0, 0)
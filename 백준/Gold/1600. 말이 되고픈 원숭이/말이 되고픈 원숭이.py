from collections import deque

# input
input = __import__('sys').stdin.readline
h = int(input())
m, n = map(int, input().split())
arr = []
visit = [[[0 for _ in range(31)] for _ in range(m)] for _ in range(n)]
hx, hy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs(i, j):
    q = deque()
    q.append((i, j, 0, 0))
    visit[i][j][0] = 1
    while q:
        i, j, cnt, move = q.popleft()
        if i == n - 1 and j == m - 1: return move
        if cnt < h:
            for k in range(8):
                x, y = i + hx[k], j + hy[k]
                if not(0 <= x < n and 0 <= y < m): continue
                if visit[x][y][cnt + 1]: continue
                if arr[x][y] == 0:
                    visit[x][y][cnt + 1] = 1
                    q.append((x, y, cnt + 1, move + 1))
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y][cnt]: continue
            if arr[x][y] == 0:
                visit[x][y][cnt] = 1
                q.append((x, y, cnt, move + 1))
    return -1
print(bfs(0, 0))
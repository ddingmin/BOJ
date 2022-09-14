from collections import deque

# input
input = __import__('sys').stdin.readline
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs(i, j):
    visit = [[0] * m for _ in range(n)]
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    while q:
        i, j = q.popleft()
        for dir in range(8):
            x, y = i + dx[dir], j + dy[dir]
            if not(0 <= x < n and 0 <= y < m): continue
            elif arr[x][y] == 1: # 안전거리 체크
                return visit[i][j]
            elif arr[x][y] == 0 and visit[x][y] == 0:
                q.append((x, y))
                visit[x][y] = visit[i][j] + 1

def solve():
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: 
                ans = max(ans, bfs(i, j))
    return ans

print(solve())
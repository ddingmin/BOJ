from collections import deque

# input
input = __import__('sys').stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs(i, j):
    sx, sy = i, j
    visit = [[0] * m for _ in range(n)]
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    length = 1
    psw = 2
    while q:
        i, j = q.popleft()
        for dir in range(4):
            x, y = i + dx[dir], j + dy[dir]
            if not(0 <= x < n and 0 <= y < m): continue
            if arr[x][y] and visit[x][y] == 0:
                visit[x][y] = visit[i][j] + 1
                q.append((x, y))

                if length < visit[x][y]:
                    length = visit[x][y]
                    psw = arr[sx][sy] + arr[x][y]
                elif length == visit[x][y]:
                    psw = max(psw, arr[sx][sy] + arr[x][y])
    return length, psw



def solve():
    l, p = 0, 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0: 
                length, psw = bfs(i, j)
                #print(length, psw)
                if length > l:
                    l = length
                    p = psw
                elif length == l:
                    p = max(p, psw)
    return p

print(solve())
from collections import deque
input = __import__('sys').stdin.readline

dir = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs():
    global ans
    ans += 1
    while q:
        temp = q.popleft()
        visit[temp[0]][temp[1]]
        for d in dir:
            dx, dy = temp[0] + d[0], temp[1] + d[1]
            if 0 <= dx < n and 0 <= dy < m and not visit[dx][dy]:
                visit[dx][dy] = True
                if arr[dx][dy] == 1:
                    q.append((dx, dy))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    ans = 0
    q = deque()
    for _ in range(k):
        a, b = map(int,input().split())
        arr[b][a] = 1
    visit = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            q.append((i, j))
            if not visit[i][j] and arr[i][j] == 1:
                bfs()
            else:
                q.popleft()
    print(ans)
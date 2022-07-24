from collections import deque
t = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for cnt in range(t):
    m, n = map(int, input().split())
    arr = []
    fire = []
    for i in range(n):
        arr.append(list(input()))
        for j in range(m):
            if arr[i][j] == '*': fire.append((i, j))
            elif arr[i][j] == '@': start = (i, j)
    visit = [[0] * m for _ in range(n)]
    def bfs(start, fire):
        i, j = start
        q = deque()
        q.append((i, j, 0))
        visit[i][j] = 1
        firetime = 0
        while q:
            i, j ,time = q.popleft()
            if time > firetime:
                fireq = deque()
                for fx, fy in fire:
                    fireq.append((fx, fy))
                fire = []
                while fireq:
                    fi, fj = fireq.popleft()
                    for k in range(4):
                        fx, fy = fi + dx[k], fj + dy[k]
                        if not (0 <= fx < n and 0 <= fy < m): continue
                        if arr[fx][fy] == '.':
                            arr[fx][fy] = '*'
                            fire.append((fx, fy))
                firetime += 1
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < n and 0 <= y < m): return time + 1
                if arr[x][y] == '#' or arr[x][y] == '*': continue
                if visit[x][y] == 1: continue
                flag = True
                for k in range(4):
                    tx, ty = x + dx[k], y + dy[k]
                    if not (0 <= tx < n and 0 <= ty < m): continue
                    if arr[tx][ty] == '*': flag = False
                if flag and arr[x][y] == '.':
                    q.append((x, y, time + 1))
                    visit[x][y] = 1
            # for k in arr:
            #     print(*k)
            # print()
        return 'IMPOSSIBLE'
    print(bfs(start, fire))

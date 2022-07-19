n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input()))
visit = [[0] * m for _ in range(n)]

def dir(d):
    if d == 'D':
        return (1, 0)
    elif d == 'U':
        return (-1, 0)
    elif d == 'R':
        return (0, 1)
    elif d == 'L':
        return (0, -1)

def dfs(x, y, area):
    global areaNum
    area.append((x, y))
    visit[x][y] = -1
    dx, dy = dir(arr[x][y])
    x, y = x + dx, y + dy

    if visit[x][y] == 0:
        dfs(x, y, area)

    elif visit[x][y] == -1:
        areaNum += 1
        for i, j in area:
            visit[i][j] = areaNum
        return
    elif visit[x][y] >= 1:
        for i, j in area:
            visit[i][j] = visit[x][y]

areaNum = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            dfs(i, j, [])


print(areaNum)
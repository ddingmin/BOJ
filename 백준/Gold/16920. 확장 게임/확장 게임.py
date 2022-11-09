from collections import deque
input = __import__('sys').stdin.readline

n, m, p = map(int, input().split())
playerDist = list(map(int, input().split()))
playerCastleCount = [0] * (p)
playerXY = [deque() for _ in range(p)]
dx, dy = [-1, 1, 0, 0], [0, 0,-1 ,1]
arr = []
wallCount = 0
for i in range(n):
    arr.append(list(input()))
    for j in range(m):
        if arr[i][j] == '.': wallCount += 1
        elif arr[i][j] == '#': continue
        else:
            arr[i][j] = int(arr[i][j]) - 1
            playerCastleCount[int(arr[i][j])] += 1
            playerXY[int(arr[i][j])].append((i, j))

def bfs(dist, player):
    global wallCount
    visit = [[0] * m for _ in range(n)]
    q = deque()
    for i, j in playerXY[player]:
        q.append((i, j, 0))
        visit[i][j] = 1
    change = []
    while q:
        for _ in range(len(q)):
            i, j, c = q.popleft()

            if c == dist:
                change = list(set(change))
                wallCount -= len(change)
                playerCastleCount[player] += len(change)
                for x, y in change:
                    arr[x][y] = str(player)
                playerXY[player] = change
                return 0
            for dir in range(4):
                x, y = i + dx[dir], j + dy[dir]
                if not (0 <= x < n and 0 <= y < m): continue
                if visit[x][y] == 0 and arr[x][y] == '.':
                    visit[x][y] = 1
                    q.append((x, y, c + 1))
                    change.append((x, y))
    change = list(set(change))
    wallCount -= len(change)
    playerCastleCount[player] += len(change)
    for x, y in change:
        arr[x][y] = str(player)
    playerXY[player] = change
    return 0

startWall = wallCount
flag = True

while flag:
    for playeridx in range(p):
        bfs(playerDist[playeridx], playeridx)
    if startWall == wallCount: 
        flag = False
    startWall = wallCount
print(*playerCastleCount)
from collections import deque
input = __import__('sys').stdin.readline

n, m = map(int, input().split())

arr = []
makeWall = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# makeWall
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0: makeWall.append((i,j))

setWall = []
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs():
    global ansTemp
    while q:
        temp = q.popleft()
        visit[temp[0]][temp[1]] = True
        for d in dir:
            dx, dy = temp[0] + d[0], temp[1] + d[1]
            if 0 <= dx < n and 0 <= dy < m and not visit[dx][dy] and arr[dx][dy] == 0:
                ansTemp -= 1
                visit[dx][dy] = True
                q.append((dx, dy))

ans = 0
for i in range(len(makeWall)):
    setWall.append(makeWall[i])
    for j in range(i + 1, len(makeWall)):
        setWall.append(makeWall[j])
        for k in range(j + 1, len(makeWall)):
            setWall.append(makeWall[k])
            # 여기다가 bfs
            for wall in setWall:
                arr[wall[0]][wall[1]] = 1
            visit = [[False] * m for _ in range(n)]
            q = deque()
            ansTemp = len(makeWall) - 3
            for x in range(n):
                for y in range(m):
                    if arr[x][y] == 2 and not visit[x][y]:
                        q.append((x,y))
                        bfs()
            ans = max(ans, ansTemp)
                        
            
            #끝나고 초기화
            for wall in setWall:
                arr[wall[0]][wall[1]] = 0
            setWall.pop()
        setWall.pop()
    setWall.pop()

print(ans)
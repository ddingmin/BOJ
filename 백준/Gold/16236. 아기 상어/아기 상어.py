from collections import deque
input = __import__('sys').stdin.readline

n = int(input())
arr = []
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j in range(n):
        if arr[i][j] == 9: 
            sx, sy = i, j
            arr[i][j] = 0

def bfs(sx, sy):
    visit = [[0] * n for _ in range(n)]
    q = deque()
    level = 2
    exp = 0
    q.append((sx, sy, 0))
    visit[sx][sy] = 1
    ans = 0
    
    while 1:
    # x, y, dist
        canEat = []
        while q:
            i, j, move = q.popleft()
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < n and 0 <= y < n): continue
                if visit[x][y]: continue
                if arr[x][y] <= level:
                    # 0 또는 자신과 같은 크기라면 그냥 이동
                    if arr[x][y] == 0 or arr[x][y] == level:
                        visit[x][y] = 1
                        q.append((x, y, move + 1))
                    # 물고기 라면 canEat 배열에 넣고 이동
                    else:
                        canEat.append((x, y, move + 1))
                        visit[x][y] = 1
                        q.append((x, y, move + 1))
        # canEat 에서 먹을 물고기 선택 후 다시 bfs
        # canEat이 비어 있다면 더이상 먹을 고기가 없으므로 return
        if canEat:
            # 거리가 가장 가깝고, 가장 위에, 왼쪽에 존재하는 좌표
            canEat = sorted(canEat, key = lambda x: [x[2], x[0], x[1]])
            x, y, move = canEat[0]
            
            # 다시 BFS 큐 초기화, 경험치 += 1, 먹은 위치 0만들기, visit 배열 초기화, ans 값 갱신
            q = deque()
            exp += 1
            arr[x][y] = 0
            visit = [[0] * n for _ in range(n)]
            visit[x][y] = 1
            q.append((x, y, move))
            ans = move
            # 아기 상어가 자신만큼 먹을 경우 (크기 + 1)
            if exp == level:
                exp = 0
                level += 1
        else: return ans
        
print(bfs(sx, sy))
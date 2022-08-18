from collections import deque

# input
input = __import__('sys').stdin.readline
n = int(input())
arr = []
rog = []
endpoint = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cx, cy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    arr.append(list(input().strip()))
    for j in range(n):
        # 통나무와 도착지점 좌표 저장
        if arr[i][j] == 'E': 
            endpoint.append((i, j))
            arr[i][j] = '0'
        if arr[i][j] == 'B': 
            rog.append((i, j))
            arr[i][j] = '0'


# 통나무 방향 알기 / 가로는 0, 세로는 1
if rog[0][0] == rog[1][0]: rogDir = 0
else: rogDir = 1
# 종료 지점 방향
if endpoint[0][0] == endpoint[1][0]: endDir = 0
else: endDir = 1

# 방향에 따른 방문 노드도 필요함
visit = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]

def bfs(i, j):
    q = deque()
    q.append((i, j, rogDir, 0))
    visit[i][j][rogDir] = 1
    while q:
        i, j, r, move = q.popleft()
        # 통나무의 최종 방향과, 가운대 좌표가 일치하면 성공
        if i == endpoint[1][0] and j == endpoint[1][1] and r == endDir: 
            return move
        
        # 통나무의 방향이 세로 일 때
        if r:
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= y < n and 0 <= x - 1 < n and 0 <= x + 1 < n): continue
                if visit[x][y][r]: continue
                if arr[x][y] == '0' and arr[x - 1][y] == '0' and arr[x + 1][y] == '0':
                    visit[x][y][r] = 1
                    q.append((x, y, r, move + 1))
        # 가로일 떄
        else:
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < n and 0 <= y - 1 < n and 0 <= y + 1 < n): continue
                if visit[x][y][r]: 
                    continue
                if arr[x][y] == '0' and arr[x][y - 1] == '0' and arr[x][y + 1] == '0':
                    visit[x][y][r] = 1
                    q.append((x, y, r, move + 1))
            
        # 도는 경우
        flag = True
        for k in range(8):
            x, y = i + cx[k], j + cy[k]
            if not(0 <= x < n and 0 <= y < n): 
                flag = False
                break
            if arr[x][y] != '0': flag = False
        if flag:
            if r == 1 and visit[i][j][0] == 0:
                visit[i][j][0] = 1
                q.append((i, j, 0, move + 1))
            elif r == 0 and visit[i][j][1] == 0:
                visit[i][j][1] = 1
                q.append((i, j, 1, move + 1))
        # print((i, j), r)

    return 0
print(bfs(rog[1][0], rog[1][1]))
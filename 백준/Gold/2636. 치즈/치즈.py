from collections import deque

# input
input = __import__('sys').stdin.readline
n, m = map(int, input().split())
arr = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cheese = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 1:
            cheese += 1
airMap = [[0] * m for _ in range(n)]


# 뚫린 공기의 map을 갱신해주는 함수
# 공기가 통하는 좌표는 1
def findAir():
    global airMap
    q = deque()
    q.append((0, 0))
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    airMap[0][0] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y] == 0 and arr[x][y] == 0:
                visit[x][y] = 1
                airMap[x][y] = 1
                q.append((x, y))

def findMelts():
    cheese = 0
    melts = []
    
    # 녹일 치즈의 좌표를 저장
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: continue
            cheese += 1
            isMelts = 0
            
            # 상하좌우에 공기가 닿아 있으면 녹일 예정
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if airMap[x][y] == 1: isMelts = 1
            if isMelts: melts.append((i, j))
    
    # 치즈 녹이기
    for x, y in melts:
        arr[x][y] = 0
        
    # 남은 치즈의 수 반환
    return cheese - len(melts)
        
    
        
findAir() 
ans = 0
temp = 0    # 치즈가 다 녹기 전 치즈의 개수
while 1:
    if cheese == 0:
        print(ans)
        print(temp)
        break
    findAir()
    temp = cheese
    cheese = findMelts()
    ans += 1

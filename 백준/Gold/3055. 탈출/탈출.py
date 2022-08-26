from collections import deque

# input
input = __import__('sys').stdin.readline
n, m = map(int, input().split())
arr = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    arr.append(list(input().strip()))
    for j in range(m):
        if arr[i][j] == 'S':
            start = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'D':
            end = (i, j)
            arr[i][j] = '.'
        

def solve():
    global end
    ex, ey = end
    
    ans = 0
    q = deque()
    visit = [[0] * m for _ in range(n)]
    i, j = start
    q.append((i, j))
    visit[i][j] = 1
    while q:
        # 한 턴 동안 고슴도치의 다음 위치 탐색
        for _ in range(len(q)):  
            i, j = q.popleft()
            
            
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < n and 0 <= y < m): continue
                if visit[x][y] == 0 and arr[x][y] == '.':
                    # 도착 지점인지
                    if x == ex and y == ey:
                        return ans + 1
                    # 다음 물이 차면 잠기는지 체크
                    flag = 1
                    for kk in range(4):
                        cx, cy = x + dx[kk], y + dy[kk]
                        if not(0 <= cx < n and 0 <= cy < m): continue
                        if arr[cx][cy] == '*': flag = 0
                    
                    if flag:
                        q.append((x, y))
                        visit[x][y] = 1
        
        water = []
        # 물 번지기
        for i in range(n):
            for j in range(m):
                if arr[i][j] == '*':
                    for k in range(4):
                        x, y = i + dx[k], j + dy[k]
                        if not(0 <= x < n and 0 <= y < m): continue
                        # 도착지점은 물 번지지 않도록 예외처리
                        if x == ex and y == ey: continue
                        if arr[x][y] == '.': water.append((x, y))
        
        for x, y in water:
            arr[x][y] = '*'
        
        ans += 1
        
    return "KAKTUS"

print(solve())
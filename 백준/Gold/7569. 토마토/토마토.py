from collections import deque

# input
input = __import__('sys').stdin.readline
arr = []
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
m, n, h = map(int, input().split())
tomato = deque()
cnt = 0
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
    arr.append(temp)
    
for i in range(h):
    for j in range(n):
        for t in range(m):
            if arr[i][j][t] == 1:
                tomato.append((i, j, t))
            if arr[i][j][t] == 0:
                cnt += 1

def solve():
    global tomato
    global cnt
    visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    for i, j, t in tomato:
        visit[i][j][t] = 1
        
    ans = 0
    if cnt == 0: return 0
    
    while tomato:
        for _ in range(len(tomato)):
            i, j, t = tomato.popleft()
            
            
            for k in range(6):
                z, x, y = i + dz[k], j + dx[k], t + dy[k]
                if not(0 <= z < h and 0 <= x < n and 0 <= y < m): continue
                if visit[z][x][y] == 0 and arr[z][x][y] == 0:
                    visit[z][x][y] = 1
                    arr[z][x][y] = 1
                    tomato.append((z, x, y))
                    cnt -= 1
    
        ans += 1
        if cnt == 0: return ans
        
    return -1
    
print(solve())
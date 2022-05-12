from collections import deque
input = __import__('sys').stdin.readline
dx, dy = [-1,0,1,-1,1,-1,0,1], [-1,-1,-1,0,0,1,1,1]

def bfs():
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == 1 and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    q.append((nx,ny))

while 1:
    w, h = map(int, input().split())
    if w == h == 0: break

    arr = []
    for _ in range(h):
        arr.append(list(map(int,input().split())))
    
    check = [[0]*w for _ in range(h)]

    q = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and check[i][j] == 0:
                cnt += 1
                check[i][j] = 1
                q.append((i,j))
                bfs()
    print(cnt)
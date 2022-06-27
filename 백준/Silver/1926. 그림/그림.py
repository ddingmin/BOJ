from collections import deque
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visit = [[0]* m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


pic_num = 0
pic_size = 0

def bfs(i, j):
    global pic_num, pic_size

    if visit[i][j] or arr[i][j] == 0: return
    visit[i][j] = 1
    q = deque()
    q.append((i, j))
    pic_num += 1
    temp_size = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            if not(0 <= tx < n and 0 <= ty < m): continue
            if visit[tx][ty] or arr[tx][ty] == 0: continue
            visit[tx][ty] = 1
            q.append((tx, ty))
            temp_size += 1
    pic_size = max(pic_size, temp_size)

for i in range(n):
    for j in range(m):
        bfs(i, j)
        
print(pic_num)
print(pic_size)
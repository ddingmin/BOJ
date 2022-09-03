from collections import deque

# input
input = __import__('sys').stdin.readline
n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
light = [[[] for _ in range(n)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    x -= 1
    y -= 1
    a -= 1
    b -= 1

    light[x][y].append((a, b))

def solve():
    visit = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visit[0][0] = 1
    arr[0][0] = 1
    # 시작 지점 스위치 켜주기
    for a, b in light[0][0]:
        arr[a][b] = 1
    
    while q:
        i, j = q.popleft()
        for dir in range(4):
            x, y = i + dx[dir], j + dy[dir]
            if not(0 <= x < n and 0 <= y < n): continue
            if visit[x][y] == 0 and arr[x][y] == 1:
                visit[x][y] = 1
                q.append((x, y))
                for a, b in light[x][y]:
                    arr[a][b] = 1
                    
                    # 스위치 켜진 방으로 진입할 수 있다면 큐에 넣어주기
                    for dir in range(4):
                        aa, bb = a + dx[dir], b + dy[dir]
                        if not(0 <= aa < n and 0 <= bb < n): continue
                        if arr[aa][bb] == 1 and visit[aa][bb] == 1:
                            q.append((aa, bb))
    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1: ans += 1
    
    return ans      

print(solve())
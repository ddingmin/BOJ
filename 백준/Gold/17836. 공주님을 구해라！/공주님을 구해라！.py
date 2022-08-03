from collections import deque
input = __import__('sys').stdin.readline

n, m, t = map(int, input().split())
arr = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visit = [[0] * m for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs(x, y):
    # 기본 세팅
    isGram = False  # 칼을 들고 있는지
    q = deque()
    q.append((x, y, 0)) # 좌표, 이동 시간
    visit[x][y] = 1
    time = []   #   칼을 찾았을 때, 칼없이 갔을 때
    
    while q:
        i, j, dist = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y] == 1: continue
            if x == n - 1 and y == m - 1:       # 공주를 만나면 time배열 반환
                time.append(dist + 1)
                return time
            if arr[x][y] == 2 and isGram == False:  # 칼을 만난적 없고, 칼을 만났을 때
                # 최초 칼을 만났을 때가 최소거리임.
                isGram = True
                visit[x][y] = 1
                q.append((x, y, dist + 1))
                d = n - x + m - y - 2   # 현재 위치부터 n, m까지 맨해튼 거리가 최소거리
                time.append(dist + 1 + d)   # 현재까지 걸린 시간 + d가 최소시간
            elif arr[x][y] == 0:
                visit[x][y] = 1
                q.append((x, y, dist + 1))
    return time

ans = bfs(0, 0)
if not(ans): print('Fail')
else:
    ans = min(ans)
    if ans <= t: print(ans)
    else: print('Fail')

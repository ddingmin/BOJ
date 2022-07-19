# BOJ 16946
from collections import deque

n, m = map(int, input().split())
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
arr = []

for i in range(n):
    arr.append(list(input()))

# 해당 구역의 크기를 구하는 bfs
def bfs(x, y, visitnum):
    cango = 1
    q = deque()
    q.append((x, y))
    visit[x][y] = visitnum

    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y] >= 1: continue
            if arr[x][y] == '0':
                visit[x][y] = visitnum
                q.append((x, y))
                cango += 1
    return cango % 10

visitnum = 1
size = [0]

# 각 구역의 크기를 미리 구함.
# visit 배열에 각 구역별 번호가 담겨있고,
# size 배열에 해당 구역의 크기가 담겨져 있음.
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0' and visit[i][j] == 0:
            size.append(bfs(i, j, visitnum))
            visitnum += 1

for i in range(n):
    for j in range(m):
        # 벽인 경우 상하좌우 구역의 사이즈를 모두 더하고 부순 벽 + 1을 해주면 답
        # 이때 상하좌우 구역이 같은 구역이 존재할 수 있으므로 해당 경우는 set을 통해 중복제거
        if arr[i][j] == '1':
            ans = []
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if not (0 <= x < n and 0 <= y < m): continue
                ans.append(visit[x][y])
            ans = list(set(ans))
            temp = 0
            for k in ans: temp += size[k]
            print((temp + 1) % 10, end= "")
        else:
            print(0, end="")
    print()

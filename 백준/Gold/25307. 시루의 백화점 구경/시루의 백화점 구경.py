# BOJ 25307
input = __import__('sys').stdin.readline
from collections import deque

n, m, dis = map(int, input().split())
arr = []
visit = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
end = []
cant = []
for i in range(n):
	arr.append(list(map(int, input().split())))
	for j in range(m):
		if arr[i][j] == 4: sx, sy = i, j
		elif arr[i][j] == 2: end.append((i, j))
		elif arr[i][j] == 3: cant.append((i, j))
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
ans = []

# 마네킹으로 갈 수 없는 곳 visit에 지정
def bfsCantGo(x, y):
	q = deque()
	q.append((x, y))
	visit[x][y] = 1
	while q:
		i, j = q.popleft()
		if visit[i][j] == dis + 1: return
		for k in range(4):
			x, y = i + dx[k], j + dy[k]
			if not(0 <= x < n and 0 <= y < m): continue
			if visit[x][y] != 0: continue

			visit[x][y] = visit[i][j] + 1
			q.append((x, y))

for i, j in cant:
	bfsCantGo(i, j)

# for k in visit:
# 	print(*k)

def bfs(x, y):
	q = deque()
	q.append((x, y))
	visit[x][y] = 1
	while q:
		i, j = q.popleft()
		for k in range(4):
			x, y = i + dx[k], j + dy[k]
			
			if not(0 <= x < n and 0 <= y < m): continue
			if arr[x][y] != 1 and visit[x][y] == 0:
				dp[x][y] = dp[i][j] + 1
				visit[x][y] = 1
				q.append((x, y))
				
				if arr[x][y] == 2: 
					ans.append(dp[x][y])
					return

bfs(sx, sy)

if ans: print(min(ans))
else: print(-1)
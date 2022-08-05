from collections import deque
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):	# 영역 탐색
	q = deque()
	q.append((x, y))
	visit[x][y] = 1
	while q:
		i, j = q.popleft()
		for k in range(4):
			x, y = i + dx[k], j + dy[k]
			if not(0 <= x < n and 0 <= y < m): continue
			if visit[x][y]: continue
			if arr[x][y]:
				q.append((x, y))
				visit[x][y] = 1

def melting(i, j):	# i, j 좌표 인근에 0의 수
	cnt = 0
	for k in range(4):
		x, y = i + dx[k], j + dy[k]
		if not(0 <= x < n and 0 <= y < m): continue
		if arr[x][y] == 0: cnt += 1
	return (i, j, cnt)	# 좌표와 녹을 양 반환


# 처음부터 2개의 빙산이라면
# BFS로 영역 탐색
cnt = 0
visit = [[0] * m for _ in range(n)]
for i in range(n):
	for j in range(m):
		if arr[i][j] > 0 and visit[i][j] == 0:
			cnt += 1
			bfs(i, j)

if cnt >= 2:	# 영역이 2개 이상이면 출력
	print(0)
	exit(0)
if cnt == 0:	# 영역이 모두 녹아 0개면 0 출력
	print(0)
	exit(0)

days = 0
while 1:

	# 녹이는 양 구하기
	melt = []
	for i in range(n):
		for j in range(m):
			if arr[i][j]: melt.append(melting(i, j))
	# 녹이기
	for x, y, c in melt:
		arr[x][y] -= c
		if arr[x][y] < 0: arr[x][y] = 0
	# BFS로 영역 탐색
	cnt = 0
	visit = [[0] * m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if arr[i][j] > 0 and visit[i][j] == 0:
				cnt += 1
				bfs(i, j)

	days += 1

	if cnt >= 2:	# 영역이 2개 이상이면 출력
		print(days)
		exit(0)
	if cnt == 0:	# 영역이 모두 녹아 0개면 0 출력
		print(0)
		exit(0)
from collections import deque


n, m = map(int, input().split())
arr = []
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for i in range(n):
	arr.append(list(map(int, input())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y, z):
	q = deque()
	# 벽을 부셧는지
	q.append((x, y, z))
	visit[x][y][z] = 1
	while q:
		i, j, isCrash = q.popleft()
		if i == n - 1 and j == m - 1:
			return visit[i][j][isCrash]
		for k in range(4):
			x, y = i + dx[k], j + dy[k]
			if not(0 <= x < n and 0 <= y < m): continue
			if arr[x][y] and isCrash == 0:
				visit[x][y][1] = visit[i][j][0] + 1
				q.append((x, y, 1))
			elif arr[x][y] == 0 and visit[x][y][isCrash] == 0:
				visit[x][y][isCrash] = visit[i][j][isCrash] + 1
				q.append((x, y, isCrash))
	return -1		

print(bfs(0, 0, 0))

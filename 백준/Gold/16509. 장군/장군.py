from collections import deque
input = __import__('sys').stdin.readline

# 16509 장군
arr = [[0] * 9 for _ in range(10)]
visit = [[0] * 9 for _ in range(10)]
dx, dy = [-3, -3, -2, -2, 2, 2, 3, 3], [-2, 2, -3, 3, -3, 3, -2, 2]
r, c = map(int, input().split())
a, b = map(int, input().split())
arr[a][b] = 1

def move(i, j, tp):
	tx = [
		[-1, -2],
		[-1, -2],
		[0, -1],
		[0, -1],
		[0, 1],
		[0, 1],
		[1, 2],
		[1, 2]
	]
	ty = [
		[0, -1],
		[0, 1],
		[-1, -2],
		[1, 2],
		[-1, -2],
		[1, 2],
		[0, -1],
		[0, 1]
	]
	for k in range(2):
		x, y = i + tx[tp][k], j + ty[tp][k]
		if (x == a and y == b): 
			return 0
	return 1

def bfs(i, j):
	q = deque()
	visit[i][j] = 1
	q.append((i, j, 0))

	while q:
		i, j, c = q.popleft()
		for k in range(8):
			x, y = i + dx[k], j + dy[k]
			if not(0 <= x < 10 and 0 <= y < 9): continue
			if not move(i, j, k): continue
			if visit[x][y]: continue
			if x == a and y == b: return c + 1
			visit[x][y] = 1
			q.append((x, y, c + 1))
	return -1

print(bfs(r, c))
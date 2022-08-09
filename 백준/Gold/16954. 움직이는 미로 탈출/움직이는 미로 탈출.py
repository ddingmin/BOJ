from collections import deque
input = __import__('sys').stdin.readline

arr = []
wall = []

# Input
for i in range(8):
	arr.append(list(input().strip()))
	for j in range(8):
		if arr[i][j] == '#': wall.append((i, j))

dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1, 0], [0, 0, -1, 1, -1, 1, -1, 1, 0]

def moveWall(wall): # 벽이 모두 한칸씩 떨어짐
	temp = []
	for i, j in wall:
		arr[i][j] = '.'
	
	for i, j in wall:
		x, y = i + 1, j
		if x >= 8: continue
		temp.append((x, y))
		arr[x][y] = '#'

	return temp

def bfs(x, y, wall):
	visit = [[0] * 8 for _ in range(8)]
	q = deque()
	q.append((x, y))

	while q:
		# 한 사이클이 끝나면 벽이 떨어져야함.
		if not wall:
			return 1
		for _ in range(len(q)):
			i, j = q.popleft()
			if arr[i][j] == '#': continue	# 내 위치에 벽이 내려온 경우
			for k in range(9):
				x, y = i + dx[k], j + dy[k]
				if not(0 <= x < 8 and 0 <= y < 8): continue
				if arr[x][y] == '.' and visit[x][y] == 0:
					if x == 0 and y == 7: return 1	# 목표에 도착한 경우
					q.append((x, y))
					visit[x][y] = 1
					
		# 벽 내려오기
		wall = moveWall(wall)
		visit = [[0] * 8 for _ in range(8)]
		
	return 0

# 초기 위치 7, 0
print(bfs(7, 0, wall))
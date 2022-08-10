# from collections import deque
input = __import__('sys').stdin.readline

# input
arr = []
empty = []
for i in range(9):
	arr.append(list(map(int, input().split())))
	for j in range(9):
		if arr[i][j] == 0: empty.append((i, j))

# 스도구 규칙 확인
def check(x, y, num):
	# 행 확인
	for i in range(9):
		if arr[x][i] == num: return 0

	# 열 확인
	for i in range(9):
		if arr[i][y] == num: return 0
	# 3 * 3 확인
	if 0 <= x < 3 and 0 <= y < 3:
		sx, sy, ex, ey = 0, 0, 3, 3
	elif 0 <= x < 3 and 3 <= y < 6:
		sx, sy, ex, ey = 0, 3, 3, 6
	elif 0 <= x < 3 and 6 <= y < 9:
		sx, sy, ex, ey = 0, 6, 3, 9
	elif 3 <= x < 6 and 0 <= y < 3:
		sx, sy, ex, ey = 3, 0, 6, 3
	elif 3 <= x < 6 and 3 <= y < 6:
		sx, sy, ex, ey = 3, 3, 6, 6
	elif 3 <= x < 6 and 6 <= y < 9:
		sx, sy, ex, ey = 3, 6, 6, 9
	elif 6 <= x < 9 and 0 <= y < 3:
		sx, sy, ex, ey = 6, 0, 9, 3
	elif 6 <= x < 9 and 3 <= y < 6:
		sx, sy, ex, ey = 6, 3, 9, 6
	elif 6 <= x < 9 and 6 <= y < 9:
		sx, sy, ex, ey = 6, 6, 9, 9

	for i in range(sx, ex):
		for j in range(sy, ey):
			if arr[i][j] == num: return 0

	return 1

def dfs(idx):
	global arr
	global empty
	if idx == len(empty):
		for k in arr: 
			print(*k)
		exit(0)

	i, j = empty[idx]
	for num in range(1, 10):
		# 스도쿠 규칙이 옳다면 다음 dfs
		if check(i, j, num): 
			arr[i][j] = num
			dfs(idx + 1)
		arr[i][j] = 0
	
	# for k in arr:
	# 	print(*k)
	# print()
	return -1
print(dfs(0))

n = int(input())
arr = []

for _ in range(n):
	a, b = map(int, input().split())
	arr.append((a, b))

arr = sorted(arr, key = lambda x: (x[0], x[1]))

for i in range(n):
	print(arr[i][0], arr[i][1])
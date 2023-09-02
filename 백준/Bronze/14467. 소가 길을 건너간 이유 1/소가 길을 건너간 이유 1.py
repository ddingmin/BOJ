n = int(input())
cnt = 0
arr = [-1] * 11
for _ in range(n):
	a, b = map(int, input().split())
	if arr[a] == -1:
		arr[a] = b
	elif arr[a] != b:
		arr[a] = b
		cnt += 1
print(cnt)
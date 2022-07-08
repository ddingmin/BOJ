# BOJ 1194

# input
n = int(input())
arr = []
for i in range(n):
	arr.append(list(map(int, input().split())))


dp = [[0] * 3 for _ in range(n)]
# 첫 시작 값 채워주기
for i in range(3):
	dp[0][i] = arr[0][i]

# 값을 채울때는 i-1에 있는 같은 위치를 제외한 두 값 중 최소값을 더해서 채우기
for i in range(1, n):
	for j in range(3):
		dp[i][j] = min(dp[i-1][(j+1) % 3] + arr[i][j], dp[i-1][(j+2) % 3] + arr[i][j])

print(min(dp[-1]))
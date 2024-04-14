n = int(input())
arr = list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
dp[0] = 0

ans = 0

for i in range(n):
    for j in range(1, arr[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n - 1] == float('inf'):
    print(-1)
else:
    print(dp[n - 1])

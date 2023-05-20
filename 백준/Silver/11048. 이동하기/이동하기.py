import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dp[0][0] = maps[0][0]
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + maps[0][j]
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + maps[i][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + maps[i][j]

print(dp[-1][-1])
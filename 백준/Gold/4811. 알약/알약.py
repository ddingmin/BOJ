import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]
for i in range(1, 31):
    dp[i][0] = 1

for i in range(1, 31):
    for j in range(1, i + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while 1:
    n = int(input())
    if n == 0: break
    print(dp[n][n])
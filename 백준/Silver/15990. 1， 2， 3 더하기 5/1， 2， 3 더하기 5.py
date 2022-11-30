dp = [[0] * (100001) for _ in range(4)]
dp[1][1] = 1
dp[1][3] = 1
dp[2][2] = 1
dp[2][3] = 1
dp[3][3] = 1

for i in range(4):
    dp[0][i] = dp[1][i] + dp[2][i] + dp[3][i]

for i in range(4, 100001):
    for j in range(1, 4):
        dp[j][i] = dp[0][i - j] - dp[j][i - j]
    dp[0][i] = (dp[1][i] + dp[2][i] + dp[3][i]) % 1000000009


n = int(input())
for _ in range(n):
    print(dp[0][int(input())])

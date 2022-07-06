n = int(input())
num = [0, 1, 2, 3]
dp = [[0] * 10005 for _ in range(4)]
dp[2][3] = 1
for i in range(10003):
    dp[0][i] = 1
    dp[1][i] = i // 2
    if i > 3: dp[2][i] = dp[3][i - 3]
    dp[3][i] = dp[0][i] + dp[1][i] + dp[2][i]


for i in range(n):

    t = int(input())
    print(dp[3][t])
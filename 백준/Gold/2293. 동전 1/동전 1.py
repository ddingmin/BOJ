n, k = map(int, input().split())
coin = [0] * 200
for i in range(1, n + 1):
    coin[i] = int(input())

#   1   2   3   4   5   6   7   8   9   10
# 1 1   1   1   1   1   1   1   1   1   1
# 2 0   1   1   2   2   3   3   4   4   5
# 5 0   0   0   0   1   1   2   2   3   4
# t 1   2   2   3   4   5   5   6   6   8

dp = [0] * 20000
dp[0] = 1
for i in range(1, n + 1):
    for j in range(coin[i], k + 1):
        dp[j] += dp[j - coin[i]]

print(dp[k])
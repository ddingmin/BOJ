input = __import__('sys').stdin.readline

n = int(input())
stair = [0]
dp = [[0] * 301 for _ in range(4)]
step = [0] * 301
for _ in range(n): stair.append(int(input()))

for i in range(1, n + 1):
    for j in range(1, 4):
        dp[j][i] = stair[i] + dp[j - 1][i - 1]
    dp[0][i] = max(dp[1][i - 1], dp[2][i - 1])

ans = 0
for i in range(1, 3):
    ans = max(ans, dp[i][n])
print(ans)


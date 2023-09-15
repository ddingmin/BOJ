import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# input
n, m = map(int, input().split())
dp = [[0] * 301 for _ in range(301)]
arr = [[0] * 301 for _ in range(301)]

for _ in range(n):
    x, y = map(int, input().split())
    arr[x][y] = m

ans = 0
for i in range(1, 301):
    dp[i][0] = dp[i - 1][0] + max(arr[i][0] - i, 0)
    ans = max(ans, dp[i][0])
for j in range(301):
    dp[0][j] = dp[0][j - 1] + max(arr[0][j] - j, 0)
    ans = max(ans, dp[0][j])

for i in range(1, 301):
    for j in range(1, 301):
        dp[i][j] = max(arr[i][j] - i - j, 0) + max(dp[i - 1][j], dp[i][j - 1])
        ans = max(ans, dp[i][j])

print(ans)
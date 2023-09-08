import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
power = int(input())
dp[0][0] = arr[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + arr[i][0]
for j in range(1, m):
    dp[0][j] = dp[0][j - 1] + arr[0][j]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]

ans = (dp[-1][-1])

if ans > power:
    print("NO")
else:
    print("YES")
    print(ans)
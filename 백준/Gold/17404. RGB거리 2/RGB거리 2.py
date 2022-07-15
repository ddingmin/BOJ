n = int(input())
arr = []
ans = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for k in range(3):
    dp = [[0] * 3 for _ in range(n)]

    for j in range(3):
        if j == k: dp[0][j] = arr[0][k]
        else: dp[0][j] = 1000 * 1000 + 1

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

    ans.append(min(dp[-1][(k+1) % 3], dp[-1][(k+2) % 3]))

print(min(ans))
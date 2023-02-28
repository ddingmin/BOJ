def solve(n):
    # 왼쪽, 오른쪽, 안놓는 경우
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0] = [1, 1, 1]
    for i in range(1, n):
        dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
        dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901

    return sum(dp[n - 1]) % 9901

n = int(input())
print(solve(n))
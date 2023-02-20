def solve(n, cards):
    dp = cards.copy()
    for i in range(n + 1):
        for j in range(i):
            dp[i] = max(dp[i - j] + dp[j], dp[i])
    return dp[n]

n = int(input())
cards = [0] + list(map(int, input().split()))
print(solve(n, cards))
import sys
input = sys.stdin.readline
dp = [0] * 10001

dp[1] = 1
dp[2] = 1
for i in range(3, len(dp)):
    dp[i] = dp[i - 1] + dp[i - 2]

n = int(input())
for i in range(1, n + 1):
    p, q = map(int, input().split())
    print(f"Case #{i}: {dp[p] % q}")

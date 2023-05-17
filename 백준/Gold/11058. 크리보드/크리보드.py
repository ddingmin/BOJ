import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 101

for i in range(1, 101):
    dp[i] = i

for i in range(2, 101):
    next = 2
    while i + next < 101:
        dp[i + next] = max(dp[i] * (next - 1), dp[i + next])
        next += 1
for i in range(2, 101):
    next = 2
    while i + next < 101:
        dp[i + next] = max(dp[i] * (next - 1), dp[i + next])
        next += 1

print(dp[n])
        
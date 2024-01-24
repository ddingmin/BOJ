import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 21
dp[0] = 1
for i in range(1, 20):
    dp[i] = i * dp[i - 1]

if n == 0:
    print("NO")
else:
    for i in range(20, -1, -1):
        if n >= dp[i]:
            n -= dp[i]

    if n == 0:
        print("YES")
    else:
        print("NO")

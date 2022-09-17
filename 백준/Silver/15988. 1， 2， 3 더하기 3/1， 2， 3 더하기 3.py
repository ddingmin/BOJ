# input
input = __import__('sys').stdin.readline

n = int(input())


dp = [0] * (10 ** 6 + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, len(dp)):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for i in range(n):
    k = int(input())
    print(dp[k] % 1000000009)
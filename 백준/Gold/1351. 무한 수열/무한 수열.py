import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())

dp = {}
dp[0] = 1

def bt(num):
    if num in dp:
        return dp[num]
    dp[num] = bt(num // p) + bt(num // q)
    return dp[num]

print(bt(n))
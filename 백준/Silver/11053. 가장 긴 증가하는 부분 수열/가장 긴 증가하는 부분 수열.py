input = __import__('sys').stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 값, 수
dp = [0] * 1_001

for i in arr:
    dp[i] = max(dp[0:i]) + 1

print(max(dp))
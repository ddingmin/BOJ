n = int(input())

dp = [0] * 1_000_001
for num in range(1, 1_000_001):
    temp = num
    for s in str(num):
        temp += int(s)
    if temp <= 1_000_000 and dp[temp] == 0:
        dp[temp] = num

print(dp[n])
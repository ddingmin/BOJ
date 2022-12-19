# BOJ [11727] 2×n 타일링 2
MAX_SIZE = 1001
DIV = 10007
dp = [0] * (MAX_SIZE)
dp[1] = 1
dp[2] = 3
# dp 테이블 채우기
for i in range(3, MAX_SIZE):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % DIV

print(dp[int(input())])

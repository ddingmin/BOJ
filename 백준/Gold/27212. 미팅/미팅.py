input = __import__('sys').stdin.readline

n, m, c = map(int, input().split())
W = []
for _ in range(c):
    W.append(list(map(int, input().split())))

A = list(map(int, input().split()))
B = list(map(int, input().split()))


dp = [[0] * (m) for _ in range(n)]

for i in range(m):
    dp[0][i] = W[A[0] - 1][B[i] - 1]

ans = max(dp[0])
for i in range(1, n):
    for j in range(m):
        # 선택한 경우, 선택 안한경우
        if j:
            selec = max(dp[i - 1][0:j]) + W[A[i] - 1][B[j] - 1]
        else:
            selec = W[A[i] - 1][B[j] - 1]
        noselec = max(dp[i - 1][0:j + 1])
        dp[i][j] = max(selec, noselec)
        ans = max(ans, dp[i][j])
    
print(ans)
import sys

input = sys.stdin.readline
######################### solve ###############################


def solve():
    n, m = map(int, input().split())
    k = int(input())
    cant = {}
    n += 1
    m += 1
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        if a + b > c + d:
            cant[(c, d, a, b)] = True
        else:
            cant[(a, b, c, d)] = True

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(1, n):
        if (i - 1, 0, i, 0) in cant:
            dp[i][0] = 0
            break
        else:
            dp[i][0] = 1

    for j in range(1, m):
        if (0, j - 1, 0, j) in cant:
            dp[0][j] = 0
            break
        else:
            dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            if (i - 1, j, i, j) in cant and (i, j - 1, i, j) in cant:
                dp[i][j] = 0
            elif (i - 1, j, i, j) in cant:
                dp[i][j] = dp[i][j - 1]
            elif (i, j - 1, i, j) in cant:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    # for dpprint in dp:
    #     print(dpprint)
    return dp[n - 1][m - 1]


###############################################################

print(solve())

def solve(n, m, x, y):
    # 무조건 n이 더 큰 수
    count = x + 1
    dp = [0] * (m + 1)
    i, j = x, x % m

    while dp[j] == 0:
        if (i, j) == (x, y): return count
        dp[j] = 1
        count += n
        j = (j + n) % m

    return -1


t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    if n >= m:
        print(solve(n, m, x - 1, y - 1))
    else:
        print(solve(m, n, y - 1, x - 1))

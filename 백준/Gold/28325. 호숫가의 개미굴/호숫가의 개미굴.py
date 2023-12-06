import sys


def solve(n, arr):
    dp = [[0] * n for _ in range(3)]

    ans = 0

    for i in range(n):
        # 큰집 먹고 작은집 안먹기
        dp[0][i] = max(dp[1][i - 1], dp[2][i - 1]) + 1
        # 큰집 안먹고 작은집 먹기
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1]) + arr[i]
        # 큰집 안먹고 작은집 안먹기
        dp[2][i] = max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1])

        ans = max(ans, dp[0][i], dp[1][i], dp[2][i])

    return ans


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

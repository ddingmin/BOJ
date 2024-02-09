import sys

_MAX = 201
_MOD = 1_000_000_000


def solve(n, k):
    dp = [[1] * _MAX for _ in range(_MAX)]

    for i in range(2, _MAX):
        for j in range(1, _MAX):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % _MOD

    return dp[k][n]


def main():
    n, k = map(int, input().split())
    print(solve(n, k))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

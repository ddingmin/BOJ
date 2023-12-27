import sys


def solve(n):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return (dp[n] + dp[n - 1]) * 2 + dp[n] * 2


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

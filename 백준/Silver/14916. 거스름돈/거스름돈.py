import sys


def solve(n):
    dp = [float('inf')] * (max(n, 5) + 1)
    dp[2], dp[4], dp[5] = 1, 2, 1

    for i in range(6, n + 1):
        dp[i] = min(dp[i - 2], dp[i - 5]) + 1

    return -1 if dp[n] == float('inf') else dp[n]


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

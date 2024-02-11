import sys


def solve(n, k, arr):
    _sum = sum(arr[0:k])
    ans = max(-float("inf"), _sum)

    for i in range(k, n):
        _sum += arr[i]
        _sum -= arr[i - k]
        ans = max(_sum, ans)

    return ans


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

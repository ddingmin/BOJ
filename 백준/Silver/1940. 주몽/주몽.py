import sys


def solve(n, m, arr):
    s, e = 0, n - 1

    _sum = arr[s] + arr[e]

    ans = 0
    while s < e:
        if _sum == m:
            ans += 1
        if _sum >= m:
            _sum -= arr[e]
            e -= 1
            _sum += arr[e]
        else:
            _sum -= arr[s]
            s += 1
            _sum += arr[s]

    return ans


def main():
    n = int(input())
    m = int(input())
    arr = list(sorted(map(int, input().split())))
    print(solve(n, m, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

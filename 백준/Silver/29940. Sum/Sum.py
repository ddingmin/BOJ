import sys


def solve(n, k, arr):
    s, e = 0, n - 1
    _sum = arr[s] + arr[e]
    ans = 0
    while s < e:
        if _sum == k:
            ans += 1

        if arr[s] + arr[e] <= k:
            _sum -= arr[s]
            s += 1
            _sum += arr[s]
        else:
            _sum -= arr[e]
            e -= 1
            _sum += arr[e]
    return ans


def main():
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(solve(n, k, sorted(arr)))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

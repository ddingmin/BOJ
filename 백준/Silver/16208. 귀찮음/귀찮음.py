import sys


def solve(n, arr):
    _sum = sum(arr)
    ans = 0
    for i in arr[:-1]:
        _sum -= i
        ans += _sum * i

    return ans


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print(solve(n, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

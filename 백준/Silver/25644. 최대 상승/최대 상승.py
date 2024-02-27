import sys


def solve(n, arr):
    ans, _max = 0, 0
    for i in range(n):
        _max = max(_max, arr[i])
        ans = max(ans, _max - arr[i])
    return ans


def main():
    n = int(input())
    arr = list(map(int, input().split()))[::-1]
    print(solve(n, arr))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()

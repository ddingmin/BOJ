import sys


def solve(n, k, arr):
    return sorted(arr)[k - 1]


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

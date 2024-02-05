import sys


def solve(arr):
    arr = sorted(arr, key=lambda x: [-x[1]])
    for a, b in arr:
        print(a)


def main():
    n = int(input())
    arr = []
    for idx in range(1, n + 1):
        a, b = map(int, input().split())
        arr.append([idx, a ** 2 + b ** 2])
    solve(arr)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

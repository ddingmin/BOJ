import sys


def solve(arr):
    pass


def main():
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append(b - a)
    arr.sort()

    print(max(arr[k - 1], 0))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()

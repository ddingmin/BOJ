import sys


def solve(n, arr):
    a, b = 1, 1

    for i in range(n):
        if i == 0:
            b = arr[i]
            continue
        a += arr[i] * b
        a, b = b, a

    return b - a, b


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = arr[::-1]
    print(" ".join(map(str, solve(n, arr))))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

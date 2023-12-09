import sys

dir = [[-1, -1], [-1, 1], [1, -1], [1, 1]]


def solve(n):
    for i in range(1, n):
        print(("*" * i).rjust(n, " "))
    print("*" * n)
    for i in range(n - 1, -1 , -1):
        print(("*" * i).rjust(n, " "))
    return 0


def main():
    n = int(input())
    solve(n)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

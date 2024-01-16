import sys

FIVE = "++++ "
ONE = "|"


def solve(n):
    return n // 5 * FIVE + n % 5 * ONE


def main():
    t = int(input())
    for _ in range(t):
        print(solve(int(input())))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

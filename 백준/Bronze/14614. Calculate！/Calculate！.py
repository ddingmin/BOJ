import sys

FIVE = "++++ "
ONE = "|"


def solve(n):
    return n // 5 * FIVE + n % 5 * ONE


def main():
    a, b, c = map(int, input().split())

    if c % 2 == 1:
        print(a ^ b)
    else:
        print(a ^ b ^ b)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

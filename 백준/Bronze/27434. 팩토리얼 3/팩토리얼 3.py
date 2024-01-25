import sys
import math


def solve(n):
    return math.factorial(n)


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

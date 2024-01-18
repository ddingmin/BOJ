import sys
import math


def solve(n):
    pass


def main():
    n = int(input())
    print(math.factorial(n) % 10)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

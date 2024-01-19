import sys
import math


def solve(n):
    pass


def main():
    n = int(input())
    while n:
        if n % 42 == 0:
            print("PREMIADO")
        else:
            print("TENTE NOVAMENTE")
        n = int(input())


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

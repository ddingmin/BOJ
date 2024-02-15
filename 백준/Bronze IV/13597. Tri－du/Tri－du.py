import sys


def solve(n, m, visit, adj):
    pass


def main():
    a, b = map(int, input().split())
    if a == b:
        print(a)
    else:
        print(max(a, b))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

import sys


def solve(n, m, visit, adj):
    pass


def main():
    _sum = sum(map(int, input().split()))
    n = int(input())
    if _sum >= n * 2:
        print(_sum - n * 2)
    else:
        print(_sum)

if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

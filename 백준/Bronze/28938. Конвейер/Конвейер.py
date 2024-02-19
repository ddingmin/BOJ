import sys


def solve(n, m, visit, adj):
    pass


def main():
    n = int(input())
    _sum = sum(map(int, input().split()))
    if _sum == 0:
        print("Stay")
    elif _sum > 0:
        print("Right")
    else:
        print("Left")


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

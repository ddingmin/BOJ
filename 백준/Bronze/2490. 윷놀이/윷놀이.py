import sys


def solve(t):
    if t == 0:
        return "D"
    elif t == 3:
        return "A"
    elif t == 2:
        return "B"
    elif t == 1:
        return "C"
    elif t == 4:
        return "E"


def main():
    _sum = sum(map(int, input().split()))
    print(solve(_sum))
    _sum = sum(map(int, input().split()))
    print(solve(_sum))
    _sum = sum(map(int, input().split()))
    print(solve(_sum))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

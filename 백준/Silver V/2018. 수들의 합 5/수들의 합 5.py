import sys


def solve(n):
    _sum = 1
    s, e = 1, 1
    cnt = 0

    while s <= n:
        if _sum == n:
            cnt += 1
        if _sum < n:
            e += 1
            _sum += e
        else:
            _sum -= s
            s += 1

    return cnt


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

import sys


def solve(n, m):
    ans = 0
    for i in range(n, m + 1):
        if len(set(list(str(i)))) == len(list(str(i))):
            ans += 1

    return ans


def main():
    arr = sys.stdin.readlines()
    for line in arr:
        n, m = map(int, line.split())
        print(solve(n, m))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

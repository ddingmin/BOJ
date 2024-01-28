import sys


def solve(a, aa, b, bb):
    arr = [a, aa, b, bb]
    s = set()

    for c in arr:
        for cc in arr:
            s.add(f"{c} {cc}")

    for pp in sorted(s):
        print(pp)


def main():
    a, aa = input().split()
    b, bb = input().split()
    solve(a, aa, b, bb)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

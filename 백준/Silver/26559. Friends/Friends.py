import sys


def solve(arr):
    d = {}
    for name, value in arr:
        d[int(value)] = name

    ans = []

    for k in sorted(d.keys(), reverse=True):
        ans.append(d[k])

    return ", ".join(ans)


def main():
    n = int(input())
    for _ in range(n):
        t = int(input())
        arr = []
        for _ in range(t):
            name, value = input().split()
            arr.append([name, int(value)])

        print(solve(arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

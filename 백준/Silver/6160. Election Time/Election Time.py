import sys


def solve(k, arr):
    arr.sort(key=lambda x: [-x[1]])
    round1 = arr[:k]
    round1.sort(key=lambda x: [-x[2]])
    return round1[0][0]


def main():
    n, k = map(int, input().split())
    arr = []
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        arr.append([i, a, b])
    print(solve(k, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

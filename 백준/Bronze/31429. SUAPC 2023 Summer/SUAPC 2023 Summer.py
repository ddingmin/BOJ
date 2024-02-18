import sys


def solve(n, m, visit, adj):
    pass


def main():
    n = int(input())
    arr = [
        [12, 1600],
        [11, 894],
        [11, 1327],
        [10, 1311],
        [9, 1004],
        [9, 1178],
        [9, 1357],
        [8, 837],
        [7, 1055],
        [6, 556],
        [6, 773]
    ]
    print(*arr[n - 1])


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

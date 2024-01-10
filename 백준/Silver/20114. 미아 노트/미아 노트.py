import sys


def solve(k, n, m, arr):
    ans = ['?'] * k
    for j in range(m * k):
        for i in range(n):
            if arr[i][j] != '?':
                ans[j // m] = arr[i][j]
    return ''.join(map(str, ans))


def main():
    k, n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    print(solve(k, n, m, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()

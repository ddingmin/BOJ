import sys


def solve(n, m, arr):
    cnt = 0
    visit = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 'o': continue
            flag = False
            if 0 <= i - 1 < n and 0 <= i + 1 < n:
                if arr[i - 1][j] == 'v' and arr[i + 1][j] == '^':
                    flag = True
            if 0 <= j - 1 < m and 0 <= j + 1 < m:
                if arr[i][j - 1] == '>' and arr[i][j + 1] == '<':
                    flag = True
            if flag:
                cnt += 1

    return cnt


def main():
    t = int(input())
    for _ in range(t):
        input()
        n, m = map(int, input().split())
        arr = [list(input().strip()) for _ in range(n)]
        print(solve(n, m, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
